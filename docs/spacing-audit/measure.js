/**
 * LUSENA Spacing Audit — Measurement Script
 *
 * Runs inside a single page.evaluate() call to avoid Shopify hot-reload drift.
 * Returns a JSON object with all section gaps, intra-section sibling gaps,
 * resolved spacing tokens, and bug detection metadata.
 *
 * Usage (via playwright-cli):
 *   1. Read this file content
 *   2. Pass to: playwright-cli eval '<file content wrapped in IIFE>'
 *   3. Parse the returned JSON string
 *
 * Measurement approach:
 *   - Uses getBoundingClientRect() for box-edge positions
 *   - Collects getComputedStyle() for margins, padding, display, line-height
 *   - Walks 3 levels deep from each section
 *   - Filters out invisible elements (display:none, zero dimensions)
 *   - Skips <script>, <style>, <template>, <noscript>, <link> tags
 */
(function lusenaSpacingAudit() {
  'use strict';

  // ── Helpers ──────────────────────────────────────────────

  var SKIP_TAGS = { SCRIPT: 1, STYLE: 1, TEMPLATE: 1, NOSCRIPT: 1, LINK: 1, BR: 1, SVG: 1 };

  function isVisible(el) {
    if (SKIP_TAGS[el.tagName]) return false;
    if (el.offsetWidth === 0 && el.offsetHeight === 0) return false;
    var cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') return false;
    return true;
  }

  function shortText(el) {
    var t = (el.textContent || '').trim().replace(/\s+/g, ' ');
    return t.length > 50 ? t.substring(0, 47) + '...' : t;
  }

  function classStr(el) {
    return el.className && typeof el.className === 'string'
      ? el.className.trim()
      : '';
  }

  function pxVal(str) {
    return Math.round(parseFloat(str) || 0);
  }

  /**
   * Extract the translateY value from a CSS transform matrix.
   * matrix(a, b, c, d, tx, ty) → ty
   * Returns 0 if no transform or no Y translation.
   */
  function getTranslateY(el) {
    var cs = getComputedStyle(el);
    var t = cs.transform;
    if (!t || t === 'none') return 0;
    // matrix(1, 0, 0, 1, 0, 14) → extract the 6th value (ty)
    var match = t.match(/matrix\([^,]+,[^,]+,[^,]+,[^,]+,[^,]+,\s*([^)]+)\)/);
    if (match) return parseFloat(match[1]) || 0;
    return 0;
  }

  function getElementInfo(el) {
    var r = el.getBoundingClientRect();
    var cs = getComputedStyle(el);
    return {
      tag: el.tagName,
      classes: classStr(el),
      text: shortText(el),
      rect: {
        top: Math.round(r.top * 10) / 10,
        bottom: Math.round(r.bottom * 10) / 10,
        height: Math.round(r.height * 10) / 10
      },
      marginTop: cs.marginTop,
      marginBottom: cs.marginBottom,
      paddingTop: cs.paddingTop,
      paddingBottom: cs.paddingBottom,
      display: cs.display,
      flexDirection: cs.flexDirection || '',
      gap: cs.gap || '',
      rowGap: cs.rowGap || '',
      lineHeight: cs.lineHeight,
      fontSize: cs.fontSize
    };
  }

  function getVisibleChildren(parent) {
    var kids = [];
    for (var i = 0; i < parent.children.length; i++) {
      if (isVisible(parent.children[i])) {
        kids.push(parent.children[i]);
      }
    }
    return kids;
  }

  // ── Measure gaps between adjacent visible siblings ──────

  function measureSiblingGaps(parent, depth, maxDepth) {
    var children = getVisibleChildren(parent);
    if (children.length === 0) return null;

    var parentInfo = getElementInfo(parent);
    var gaps = [];

    for (var i = 0; i < children.length - 1; i++) {
      var a = children[i];
      var b = children[i + 1];
      var aRect = a.getBoundingClientRect();
      var bRect = b.getBoundingClientRect();
      var aCs = getComputedStyle(a);
      var bCs = getComputedStyle(b);

      // Skip absolutely/fixed positioned elements (they overlap intentionally)
      var aPos = aCs.position;
      var bPos = bCs.position;
      var hasAbsolute = (aPos === 'absolute' || aPos === 'fixed' || bPos === 'absolute' || bPos === 'fixed');

      // Only measure vertical gaps (skip horizontal siblings in flex-row/grid-row)
      var isVertical = true;
      if (parentInfo.display.indexOf('flex') !== -1 && parentInfo.flexDirection === 'row') {
        isVertical = false;
      }
      if (parentInfo.display === 'grid') {
        // Grid can be both — check if B is below A
        isVertical = bRect.top >= aRect.bottom - 2; // 2px tolerance for alignment
      }
      // Skip absolute/fixed pairs — overlaps are intentional
      if (hasAbsolute) {
        isVertical = false;
      }

      if (isVertical) {
        // Compensate for scroll-trigger translateY offsets
        var aTy = getTranslateY(a);
        var bTy = getTranslateY(b);
        var aBottomTrue = aRect.bottom - aTy;
        var bTopTrue = bRect.top - bTy;
        var rawGap = Math.round((bRect.top - aRect.bottom) * 10) / 10;
        var trueGap = Math.round((bTopTrue - aBottomTrue) * 10) / 10;

        gaps.push({
          childA: {
            tag: a.tagName,
            classes: classStr(a),
            text: shortText(a),
            bottom: Math.round(aRect.bottom * 10) / 10,
            marginBottom: aCs.marginBottom,
            lineHeight: aCs.lineHeight,
            fontSize: aCs.fontSize,
            translateY: aTy
          },
          childB: {
            tag: b.tagName,
            classes: classStr(b),
            text: shortText(b),
            top: Math.round(bRect.top * 10) / 10,
            marginTop: bCs.marginTop,
            lineHeight: bCs.lineHeight,
            fontSize: bCs.fontSize,
            translateY: bTy
          },
          gapPx: trueGap,
          rawGapPx: rawGap,
          transformCompensated: (aTy !== 0 || bTy !== 0)
        });
      }
    }

    // Recurse into children (up to maxDepth)
    var childContainers = [];
    if (depth < maxDepth) {
      for (var j = 0; j < children.length; j++) {
        var childResult = measureSiblingGaps(children[j], depth + 1, maxDepth);
        if (childResult && childResult.gaps.length > 0) {
          childContainers.push(childResult);
        }
      }
    }

    return {
      selector: parentInfo.tag + '.' + parentInfo.classes.split(' ')[0],
      classes: parentInfo.classes,
      display: parentInfo.display,
      flexDirection: parentInfo.flexDirection,
      gap: parentInfo.gap,
      rowGap: parentInfo.rowGap,
      paddingTop: parentInfo.paddingTop,
      paddingBottom: parentInfo.paddingBottom,
      rect: parentInfo.rect,
      gaps: gaps,
      children: childContainers
    };
  }

  // ── Resolve spacing tokens ─────────────────────────────

  function resolveTokens() {
    var rootStyle = getComputedStyle(document.documentElement);
    var tokenNames = [
      '--lusena-space-05', '--lusena-space-1', '--lusena-space-2',
      '--lusena-space-3', '--lusena-space-4', '--lusena-space-5',
      '--lusena-space-6', '--lusena-space-8', '--lusena-space-10',
      '--lusena-space-12', '--lusena-space-16', '--lusena-space-24'
    ];
    var tokens = {};
    for (var i = 0; i < tokenNames.length; i++) {
      var raw = rootStyle.getPropertyValue(tokenNames[i]).trim();
      // Convert rem to px (1rem = 10px in this theme due to 62.5% font-size)
      if (raw.indexOf('rem') !== -1) {
        tokens[tokenNames[i]] = Math.round(parseFloat(raw) * 10);
      } else if (raw.indexOf('px') !== -1) {
        tokens[tokenNames[i]] = Math.round(parseFloat(raw));
      } else {
        tokens[tokenNames[i]] = raw;
      }
    }
    return tokens;
  }

  // ── Section-level measurements ─────────────────────────

  function measureSections() {
    var mainEl = document.querySelector('main') || document.getElementById('MainContent');
    if (!mainEl) return { error: 'No <main> or #MainContent found' };

    var shopifySections = mainEl.querySelectorAll(':scope > .shopify-section, :scope > section.shopify-section');
    var sections = [];
    var sectionGaps = [];

    for (var i = 0; i < shopifySections.length; i++) {
      var wrapper = shopifySections[i];
      // Find the inner section element (the lusena-* one)
      var inner = wrapper.querySelector(':scope > section') || wrapper.querySelector(':scope > div');
      if (!inner || !isVisible(inner)) continue;

      var wrapperRect = wrapper.getBoundingClientRect();
      var innerRect = inner.getBoundingClientRect();
      var innerCs = getComputedStyle(inner);

      var sectionData = {
        id: wrapper.id || 'section-' + i,
        classes: classStr(inner),
        rect: {
          top: Math.round(wrapperRect.top * 10) / 10,
          bottom: Math.round(wrapperRect.bottom * 10) / 10,
          height: Math.round(wrapperRect.height * 10) / 10
        },
        innerRect: {
          top: Math.round(innerRect.top * 10) / 10,
          bottom: Math.round(innerRect.bottom * 10) / 10,
          height: Math.round(innerRect.height * 10) / 10
        },
        paddingTop: innerCs.paddingTop,
        paddingBottom: innerCs.paddingBottom,
        marginTop: innerCs.marginTop,
        marginBottom: innerCs.marginBottom,
        containers: []
      };

      // Measure inside this section (5 levels deep from the inner section)
      // Depth 5 is needed for PDP buybox: section > container > grid > buy-box > children
      var result = measureSiblingGaps(inner, 0, 5);
      if (result) {
        sectionData.containers.push(result);
      }

      sections.push(sectionData);
    }

    // Measure gaps between adjacent sections
    for (var j = 0; j < sections.length - 1; j++) {
      sectionGaps.push({
        sectionA: sections[j].id,
        sectionB: sections[j + 1].id,
        gapPx: Math.round((sections[j + 1].rect.top - sections[j].rect.bottom) * 10) / 10,
        sectionAPaddingBottom: sections[j].paddingBottom,
        sectionBPaddingTop: sections[j + 1].paddingTop
      });
    }

    return {
      sections: sections,
      sectionGaps: sectionGaps
    };
  }

  // ── Bug detection ──────────────────────────────────────

  function detectBugs(sectionData) {
    var bugs = [];

    function walkContainers(container, sectionId) {
      // Check each gap
      for (var i = 0; i < container.gaps.length; i++) {
        var gap = container.gaps[i];
        var a = gap.childA;
        var b = gap.childB;

        // Bug 1: <p> with default margins inside flex/grid
        var isFlexOrGrid = container.display.indexOf('flex') !== -1 || container.display === 'grid';
        if (isFlexOrGrid) {
          if (a.tag === 'P' && pxVal(a.marginBottom) > 8) {
            bugs.push({
              type: 'unreset-p-margin',
              severity: 'error',
              section: sectionId,
              element: 'P.' + a.classes.split(' ')[0],
              detail: '<p> inside ' + container.display + ' container has marginBottom: ' + a.marginBottom + '. Add margin: 0.',
              text: a.text
            });
          }
          if (b.tag === 'P' && pxVal(b.marginTop) > 8) {
            bugs.push({
              type: 'unreset-p-margin',
              severity: 'error',
              section: sectionId,
              element: 'P.' + b.classes.split(' ')[0],
              detail: '<p> inside ' + container.display + ' container has marginTop: ' + b.marginTop + '. Add margin: 0.',
              text: b.text
            });
          }
        }

        // Bug 2: Gap doesn't match any LUSENA token
        var gapPx = Math.abs(gap.gapPx);
        if (gapPx > 2) { // skip near-zero gaps
          var tokenValues = [4, 8, 16, 24, 32, 40, 48, 64, 80, 96, 128, 192];
          var matchesToken = false;
          var nearest = 0;
          var nearestDiff = 999;
          for (var t = 0; t < tokenValues.length; t++) {
            var diff = Math.abs(gapPx - tokenValues[t]);
            if (diff <= 2) { matchesToken = true; break; }
            if (diff < nearestDiff) { nearestDiff = diff; nearest = tokenValues[t]; }
          }
          if (!matchesToken && gapPx > 0) {
            bugs.push({
              type: 'off-grid-spacing',
              severity: 'warning',
              section: sectionId,
              detail: 'Gap of ' + gap.gapPx + 'px between [' + a.tag + '.' + a.classes.split(' ')[0] + '] and [' + b.tag + '.' + b.classes.split(' ')[0] + '] does not match any LUSENA token. Nearest: ' + nearest + 'px (diff: ' + nearestDiff + 'px).',
              gapPx: gap.gapPx,
              nearestToken: nearest
            });
          }
        }

        // Bug 3: Negative gap (overlap)
        if (gap.gapPx < -2) {
          bugs.push({
            type: 'element-overlap',
            severity: 'info',
            section: sectionId,
            detail: 'Elements overlap by ' + Math.abs(gap.gapPx) + 'px: [' + a.tag + '.' + a.classes.split(' ')[0] + '] and [' + b.tag + '.' + b.classes.split(' ')[0] + '].',
            gapPx: gap.gapPx
          });
        }

        // Bug 4: <h1>-<h6> with unreset margins inside flex/grid
        if (isFlexOrGrid) {
          var headingTags = { H1: 1, H2: 1, H3: 1, H4: 1, H5: 1, H6: 1 };
          if (headingTags[a.tag] && pxVal(a.marginBottom) > 4) {
            bugs.push({
              type: 'unreset-heading-margin',
              severity: 'error',
              section: sectionId,
              element: a.tag + '.' + a.classes.split(' ')[0],
              detail: '<' + a.tag.toLowerCase() + '> inside ' + container.display + ' container has marginBottom: ' + a.marginBottom + '. Add margin: 0.',
              text: a.text
            });
          }
          if (headingTags[b.tag] && pxVal(b.marginTop) > 4) {
            bugs.push({
              type: 'unreset-heading-margin',
              severity: 'error',
              section: sectionId,
              element: b.tag + '.' + b.classes.split(' ')[0],
              detail: '<' + b.tag.toLowerCase() + '> inside ' + container.display + ' container has marginTop: ' + b.marginTop + '. Add margin: 0.',
              text: b.text
            });
          }
        }

        // Bug 5: Double margin in non-collapsing context (flex/grid)
        // Both siblings contribute margin → additive spacing, usually unintended
        if (isFlexOrGrid) {
          var mbA = pxVal(a.marginBottom);
          var mtB = pxVal(b.marginTop);
          if (mbA > 4 && mtB > 4) {
            bugs.push({
              type: 'double-margin',
              severity: 'warning',
              section: sectionId,
              detail: 'Double margin in ' + container.display + ' context: [' + a.tag + '.' + a.classes.split(' ')[0] + '] marginBottom: ' + a.marginBottom + ' + [' + b.tag + '.' + b.classes.split(' ')[0] + '] marginTop: ' + b.marginTop + '. These add up (no collapse). Use gap or single-side margin.',
              gapPx: gap.gapPx,
              marginBottom: a.marginBottom,
              marginTop: b.marginTop
            });
          }
        }

        // Bug 6: Very large gap (>150px) — likely a layout bug or invisible spacer
        if (gap.gapPx > 150) {
          bugs.push({
            type: 'excessive-gap',
            severity: 'warning',
            section: sectionId,
            detail: 'Gap of ' + gap.gapPx + 'px between [' + a.tag + '.' + a.classes.split(' ')[0] + '] and [' + b.tag + '.' + b.classes.split(' ')[0] + '] is unusually large. Check for invisible spacers or layout issues.',
            gapPx: gap.gapPx
          });
        }
      }

      // Recurse into child containers
      if (container.children) {
        for (var c = 0; c < container.children.length; c++) {
          walkContainers(container.children[c], sectionId);
        }
      }
    }

    // Walk all sections
    for (var s = 0; s < sectionData.sections.length; s++) {
      var section = sectionData.sections[s];
      for (var k = 0; k < section.containers.length; k++) {
        walkContainers(section.containers[k], section.id);
      }
    }

    // Bug 7: Section padding not matching any LUSENA tier
    // Expected tiers: 0 (hero/trust), 48 (hero with padding), 64 (standard), 96 (spacious)
    var tierValues = [0, 48, 64, 96];
    var tierTolerance = 2;
    for (var st = 0; st < sectionData.sections.length; st++) {
      var sec = sectionData.sections[st];
      var ptVal = pxVal(sec.paddingTop);
      var pbVal = pxVal(sec.paddingBottom);

      function matchesTier(val) {
        for (var tv = 0; tv < tierValues.length; tv++) {
          if (Math.abs(val - tierValues[tv]) <= tierTolerance) return true;
        }
        return false;
      }

      if (ptVal > 0 && !matchesTier(ptVal)) {
        bugs.push({
          type: 'off-tier-padding',
          severity: 'info',
          section: sec.id,
          detail: 'Section padding-top: ' + sec.paddingTop + ' (' + ptVal + 'px) does not match any LUSENA tier (0, 64, 96). Classes: ' + sec.classes.split(' ').slice(0, 3).join(' '),
          paddingTop: sec.paddingTop
        });
      }
      if (pbVal > 0 && !matchesTier(pbVal)) {
        bugs.push({
          type: 'off-tier-padding',
          severity: 'info',
          section: sec.id,
          detail: 'Section padding-bottom: ' + sec.paddingBottom + ' (' + pbVal + 'px) does not match any LUSENA tier (0, 64, 96). Classes: ' + sec.classes.split(' ').slice(0, 3).join(' '),
          paddingBottom: sec.paddingBottom
        });
      }
    }

    return bugs;
  }

  // ── Main ───────────────────────────────────────────────

  var tokens = resolveTokens();
  var sectionData = measureSections();
  var bugs = detectBugs(sectionData);

  var output = {
    url: window.location.pathname,
    viewport: { width: window.innerWidth, height: window.innerHeight },
    timestamp: new Date().toISOString(),
    tokens: tokens,
    sectionGaps: sectionData.sectionGaps,
    sections: sectionData.sections,
    bugs: bugs,
    summary: {
      totalSections: sectionData.sections.length,
      totalSectionGaps: sectionData.sectionGaps.length,
      totalBugs: bugs.length,
      bugsByType: bugs.reduce(function(acc, b) { acc[b.type] = (acc[b.type] || 0) + 1; return acc; }, {})
    }
  };

  // When used with page.evaluate(), return the string directly.
  // When injected as a script tag, store on window for retrieval.
  if (typeof window !== 'undefined') {
    window.__lusenaSpacingAudit = output;
  }
  return JSON.stringify(output);
})()
