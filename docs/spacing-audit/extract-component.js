/**
 * LUSENA Spacing Audit — Component Gap Extractor
 *
 * Measures gaps between direct visible children of a specific CSS selector.
 * Set window.__componentSelector before injecting, or defaults to '.lusena-pdp-buy-box'.
 * Result stored on window.__componentResult.
 *
 * Usage:
 *   playwright-cli eval "window.__componentSelector = '.lusena-pdp-buy-box'"
 *   -- then inject this script via addScriptTag --
 *   playwright-cli run-code "async (page) => {
 *     await page.addScriptTag({ path: 'docs/spacing-audit/extract-component.js' });
 *     await page.waitForTimeout(300);
 *     return await page.evaluate(() => window.__componentResult);
 *   }"
 */
(function() {
  var selector = window.__componentSelector || '.lusena-pdp-buy-box';
  var el = document.querySelector(selector);
  if (!el) {
    window.__componentResult = 'NOT FOUND: ' + selector;
    return;
  }

  var SKIP = { SCRIPT: 1, STYLE: 1, TEMPLATE: 1, NOSCRIPT: 1, LINK: 1, BR: 1, SVG: 1 };
  var results = [];
  var children = Array.from(el.children).filter(function(c) {
    if (SKIP[c.tagName]) return false;
    var cs = getComputedStyle(c);
    return cs.display !== 'none' && c.offsetHeight > 0;
  });

  for (var i = 0; i < children.length - 1; i++) {
    var a = children[i], b = children[i + 1];
    var aR = a.getBoundingClientRect();
    var bR = b.getBoundingClientRect();
    results.push({
      a: (a.className || '').split(' ').slice(0, 2).join(' ') || a.tagName,
      a_t: (a.textContent || '').trim().replace(/\s+/g, ' ').substring(0, 60),
      b: (b.className || '').split(' ').slice(0, 2).join(' ') || b.tagName,
      b_t: (b.textContent || '').trim().replace(/\s+/g, ' ').substring(0, 60),
      gap: Math.round(bR.top - aR.bottom),
      a_mb: getComputedStyle(a).marginBottom,
      b_mt: getComputedStyle(b).marginTop
    });
  }

  var cs = getComputedStyle(el);
  window.__componentResult = JSON.stringify({
    selector: selector,
    display: cs.display,
    gap: cs.gap,
    flexDirection: cs.flexDirection,
    totalChildren: children.length,
    gaps: results
  });
})();
