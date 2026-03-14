/**
 * LUSENA Spacing Audit — Comparison Engine
 *
 * Compares measurement data (window.__lusenaSpacingAudit) against a spec
 * (window.__lusenaSpacingSpec) and produces a structured report.
 *
 * Usage:
 *   1. Run measure.js first (populates window.__lusenaSpacingAudit)
 *   2. Inject the spec JSON into window.__lusenaSpacingSpec
 *   3. Run this script (populates window.__lusenaSpacingReport)
 *
 * The report contains PASS/FAIL for each check with actual vs expected values.
 */
(function lusenaSpacingCompare() {
  'use strict';

  var audit = window.__lusenaSpacingAudit;
  var spec = window.__lusenaSpacingSpec;

  if (!audit) return JSON.stringify({ error: 'No audit data. Run measure.js first.' });
  if (!spec) return JSON.stringify({ error: 'No spec data. Inject spec into window.__lusenaSpacingSpec.' });

  var defaultTolerance = spec.tolerancePx || 4;
  var checks = [];
  var pass = 0;
  var fail = 0;
  var skip = 0;

  // ── Helpers ──────────────────────────────────────────────

  function check(category, label, actual, expected, tolerance, note) {
    var tol = (tolerance !== undefined && tolerance !== null) ? tolerance : defaultTolerance;
    var actualNum = parseFloat(actual) || 0;
    var delta = Math.abs(actualNum - expected);
    var passed = delta <= tol;

    var entry = {
      category: category,
      label: label,
      expected: expected,
      actual: actualNum,
      delta: Math.round(delta * 10) / 10,
      tolerance: tol,
      status: passed ? 'PASS' : 'FAIL',
      note: note || ''
    };

    checks.push(entry);
    if (passed) pass++; else fail++;
    return passed;
  }

  /**
   * Find a section in audit data by short ID (e.g., "hero", "trust").
   * Section IDs in audit look like: shopify-section-template--{num}__{shortId}
   */
  function findSectionById(shortId) {
    for (var i = 0; i < audit.sections.length; i++) {
      var s = audit.sections[i];
      if (s.id.indexOf('__' + shortId) !== -1) return s;
      // Also try exact match for non-template IDs
      if (s.id === shortId) return s;
    }
    return null;
  }

  /**
   * Find a section in audit data by matching class.
   */
  function findSectionByClass(matchClass) {
    for (var i = 0; i < audit.sections.length; i++) {
      var s = audit.sections[i];
      if (s.classes.indexOf(matchClass) !== -1) return s;
    }
    return null;
  }

  /**
   * Flatten all gaps from a container tree into a flat list with depth info.
   */
  function flattenGaps(container, depth) {
    var out = [];
    if (!container) return out;

    for (var i = 0; i < container.gaps.length; i++) {
      var g = container.gaps[i];
      out.push({
        depth: depth,
        childAClass: g.childA.classes.split(' ')[0],
        childBClass: g.childB.classes.split(' ')[0],
        childAClasses: g.childA.classes,
        childBClasses: g.childB.classes,
        gapPx: g.gapPx,
        transformCompensated: g.transformCompensated
      });
    }

    if (container.children) {
      for (var j = 0; j < container.children.length; j++) {
        out = out.concat(flattenGaps(container.children[j], depth + 1));
      }
    }

    return out;
  }

  /**
   * Match spec container children rules against measured gaps.
   * Returns matched pairs of {specRule, measuredGap}.
   */
  function matchChildRules(specChildren, measuredGaps, targetDepth) {
    var matches = [];
    var usedGaps = {};

    for (var r = 0; r < specChildren.length; r++) {
      var rule = specChildren[r];
      var matchClass = rule.matchClass;

      if (rule.expectedGapToNext === undefined) {
        // No gap check needed, but still try to find the element for child matching
        continue;
      }

      // Find the first unused gap where childA starts with matchClass
      var found = false;
      for (var g = 0; g < measuredGaps.length; g++) {
        if (usedGaps[g]) continue;
        if (measuredGaps[g].depth !== targetDepth) continue;

        var aMatch = measuredGaps[g].childAClass === matchClass ||
                     measuredGaps[g].childAClasses.indexOf(matchClass) !== -1;

        if (aMatch) {
          matches.push({ rule: rule, gap: measuredGaps[g] });
          usedGaps[g] = true;
          found = true;

          // If repeat, consume all consecutive gaps with same childA class
          if (rule.repeat) {
            for (var rg = g + 1; rg < measuredGaps.length; rg++) {
              if (usedGaps[rg]) continue;
              if (measuredGaps[rg].depth !== targetDepth) continue;
              var raMatch = measuredGaps[rg].childAClass === matchClass ||
                            measuredGaps[rg].childAClasses.indexOf(matchClass) !== -1;
              if (raMatch) {
                matches.push({ rule: rule, gap: measuredGaps[rg] });
                usedGaps[rg] = true;
              } else {
                break;
              }
            }
          }
          break;
        }
      }

      if (!found) {
        checks.push({
          category: 'gap',
          label: matchClass + ' → next',
          expected: rule.expectedGapToNext,
          actual: null,
          delta: null,
          tolerance: rule.tolerancePx || defaultTolerance,
          status: 'SKIP',
          note: 'Element not found in measurements'
        });
        skip++;
      }
    }

    return matches;
  }

  // ── 1. Section gap checks ─────────────────────────────

  if (spec.sectionGaps) {
    for (var sg = 0; sg < spec.sectionGaps.length; sg++) {
      var sgSpec = spec.sectionGaps[sg];
      var sA = sgSpec.between[0];
      var sB = sgSpec.between[1];

      // Find matching audit section gap
      var found = false;
      for (var ag = 0; ag < audit.sectionGaps.length; ag++) {
        var aGap = audit.sectionGaps[ag];
        if (aGap.sectionA.indexOf('__' + sA) !== -1 && aGap.sectionB.indexOf('__' + sB) !== -1) {
          check(
            'section-gap',
            sA + ' → ' + sB,
            aGap.gapPx,
            sgSpec.expectedGapPx,
            null,
            ''
          );
          found = true;
          break;
        }
      }

      if (!found) {
        checks.push({
          category: 'section-gap',
          label: sA + ' → ' + sB,
          expected: sgSpec.expectedGapPx,
          actual: null,
          delta: null,
          tolerance: defaultTolerance,
          status: 'SKIP',
          note: 'Section pair not found'
        });
        skip++;
      }
    }
  }

  // ── 2. Section padding checks ─────────────────────────

  if (spec.sections) {
    for (var sKey in spec.sections) {
      if (!spec.sections.hasOwnProperty(sKey)) continue;
      var sSpec = spec.sections[sKey];
      var section = findSectionByClass(sSpec.matchClass);

      if (!section) {
        if (sSpec.expectedPaddingTop !== undefined) {
          checks.push({ category: 'padding', label: sKey + ' padding-top', expected: sSpec.expectedPaddingTop, actual: null, delta: null, tolerance: defaultTolerance, status: 'SKIP', note: 'Section not found: ' + sSpec.matchClass });
          skip++;
        }
        if (sSpec.expectedPaddingBottom !== undefined) {
          checks.push({ category: 'padding', label: sKey + ' padding-bottom', expected: sSpec.expectedPaddingBottom, actual: null, delta: null, tolerance: defaultTolerance, status: 'SKIP', note: 'Section not found: ' + sSpec.matchClass });
          skip++;
        }
        continue;
      }

      // Padding top
      if (sSpec.expectedPaddingTop !== undefined) {
        check(
          'padding',
          sKey + ' padding-top',
          section.paddingTop,
          sSpec.expectedPaddingTop,
          null,
          ''
        );
      }

      // Padding bottom
      if (sSpec.expectedPaddingBottom !== undefined) {
        check(
          'padding',
          sKey + ' padding-bottom',
          section.paddingBottom,
          sSpec.expectedPaddingBottom,
          null,
          ''
        );
      }

      // ── 3. Container gap checks ───────────────────────

      if (sSpec.containers && section.containers && section.containers[0]) {
        // Flatten all gaps from the section's container tree
        var allGaps = flattenGaps(section.containers[0], 0);

        for (var containerSel in sSpec.containers) {
          if (!sSpec.containers.hasOwnProperty(containerSel)) continue;
          var childRules = sSpec.containers[containerSel];

          // Depth 0 = direct children of the section's first container child
          // (section > lusena-container > children)
          // The measurement tree: section.containers[0] is the section itself,
          // its children[0] is typically .lusena-container
          var depth1Gaps = allGaps.filter(function(g) { return g.depth === 1; });
          var matches = matchChildRules(childRules, allGaps, 1);

          for (var m = 0; m < matches.length; m++) {
            var rule = matches[m].rule;
            var gap = matches[m].gap;
            check(
              'gap',
              sKey + ' > ' + rule.matchClass + ' → next',
              gap.gapPx,
              rule.expectedGapToNext,
              rule.tolerancePx,
              rule.note || ''
            );
          }

          // Check nested children (depth 2)
          for (var cr = 0; cr < childRules.length; cr++) {
            if (!childRules[cr].children) continue;
            var nestedRules = childRules[cr].children;
            var depth2Gaps = allGaps.filter(function(g) { return g.depth === 2; });
            var nestedMatches = matchChildRules(nestedRules, allGaps, 2);

            for (var nm = 0; nm < nestedMatches.length; nm++) {
              var nRule = nestedMatches[nm].rule;
              var nGap = nestedMatches[nm].gap;
              check(
                'gap',
                sKey + ' > ' + childRules[cr].matchClass + ' > ' + nRule.matchClass + ' → next',
                nGap.gapPx,
                nRule.expectedGapToNext,
                nRule.tolerancePx,
                nRule.note || ''
              );
            }
          }
        }
      }
    }
  }

  // ── Build report ───────────────────────────────────────

  var report = {
    page: spec.page,
    url: spec.url,
    viewport: audit.viewport,
    timestamp: audit.timestamp,
    tolerance: defaultTolerance,
    summary: {
      total: checks.length,
      pass: pass,
      fail: fail,
      skip: skip
    },
    checks: checks,
    bugs: audit.bugs
  };

  window.__lusenaSpacingReport = report;
  return JSON.stringify(report);
})()
