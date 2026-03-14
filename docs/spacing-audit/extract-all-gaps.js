/**
 * LUSENA Spacing Audit — Gap Extractor
 *
 * Flattens all measured gaps from all sections into a single array.
 * Must be injected AFTER measure.js. Result stored on window.__gapResult.
 *
 * Usage:
 *   playwright-cli run-code "async (page) => {
 *     await page.addScriptTag({ path: 'docs/spacing-audit/extract-all-gaps.js' });
 *     await page.waitForTimeout(300);
 *     return await page.evaluate(() => window.__gapResult);
 *   }"
 */
(function() {
  var d = window.__lusenaSpacingAudit;
  if (!d) { window.__gapResult = 'NO DATA — inject measure.js first'; return; }

  function flatten(container, prefix, result) {
    if (!container) return;
    var label = prefix || container.classes.split(' ')[0];
    for (var i = 0; i < container.gaps.length; i++) {
      var g = container.gaps[i];
      result.push({
        parent: label,
        pDisp: container.display,
        pGap: container.gap,
        a: g.childA.tag + '.' + g.childA.classes.split(' ')[0],
        a_t: g.childA.text.substring(0, 40),
        b: g.childB.tag + '.' + g.childB.classes.split(' ')[0],
        b_t: g.childB.text.substring(0, 40),
        gap: g.gapPx,
        a_mb: g.childA.marginBottom,
        b_mt: g.childB.marginTop
      });
    }
    if (container.children) {
      for (var j = 0; j < container.children.length; j++) {
        flatten(
          container.children[j],
          label + ' > ' + container.children[j].classes.split(' ')[0],
          result
        );
      }
    }
  }

  var all = [];
  for (var s = 0; s < d.sections.length; s++) {
    var sec = d.sections[s];
    for (var k = 0; k < sec.containers.length; k++) {
      flatten(sec.containers[k], sec.classes.split(' ')[0], all);
    }
  }
  window.__gapResult = JSON.stringify(all);
})();
