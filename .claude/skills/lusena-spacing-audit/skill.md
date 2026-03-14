---
name: lusena-spacing-audit
description: "Automated spacing measurement and validation for any LUSENA page. Measures distances between ALL visible content elements, compares against a JSON spec, reports pass/fail with actual vs expected values, and auto-detects common CSS bugs. Use when verifying spacing after changes, auditing a page's spacing health, or debugging layout issues. Keywords: spacing audit, measure, validate, pixel, gap, padding, spec, pass, fail, bug detection."
user_invocable: true
---

# LUSENA Spacing Audit

## Purpose

Automatically measure every visible spacing value on a LUSENA page and either:
1. **Validate against a spec** — compare measured values against expected values from a JSON spec file, reporting PASS/FAIL for each check
2. **Discover bugs** — auto-detect common CSS spacing issues (unreset margins, off-grid values, overlaps, double margins)
3. **Baseline a page** — capture raw measurements for creating a new spec

## When to use

- After making CSS/spacing changes — verify nothing regressed
- Before shipping a page — full spacing health check
- When debugging a layout issue — get exact pixel measurements
- When creating a spec for a new page — capture the current state as baseline

## CRITICAL: Use playwright-cli via Bash, NOT Playwright MCP tools

**Always** run browser commands through `playwright-cli` using the Bash tool. **Never** use Playwright MCP browser tools directly (`browser_navigate`, `browser_snapshot`, `browser_evaluate`, etc.) — they bypass the project workflow defined in CLAUDE.md.

### MANDATORY: Use a named session (`-s=audit`)

**Multiple Claude Code instances may run concurrently**, each with its own browser. Without a named session, all instances share the `default` browser and will navigate each other's pages — causing wrong-page measurements and wasted time.

**Every `playwright-cli` command in this skill MUST include `-s=audit`.**

```bash
# CORRECT — isolated session via Bash tool:
playwright-cli -s=audit open http://127.0.0.1:9292/products/example
playwright-cli -s=audit resize 1440 900
playwright-cli -s=audit eval "document.title"
playwright-cli -s=audit run-code "async (page) => { ... }"

# WRONG — no session flag (collides with other instances):
# playwright-cli open http://...
# playwright-cli -s=audit eval "..."

# WRONG — never call MCP tools directly:
# mcp__playwright__browser_navigate
# mcp__playwright__browser_evaluate
```

## Quote escaping: use .js files for complex code

`playwright-cli eval` and `playwright-cli run-code` take inline JS as a string argument. Complex JS with nested quotes, template literals, or multi-line logic **will break** due to shell escaping.

**Rule of thumb:**
- **Simple expressions** (< 1 line, no nested quotes) → `playwright-cli -s=audit eval "..."`
- **Multi-step code** (addScriptTag + evaluate) → `playwright-cli -s=audit run-code "async (page) => { ... }"`
- **Complex extraction logic** → write a `.js` file in `docs/spacing-audit/`, inject via `addScriptTag`

The repo includes permanent helper scripts for common extractions — see Files section below. Use those instead of writing inline JS.

## Files

| File | Purpose |
|---|---|
| `docs/spacing-audit/measure.js` | Browser-side measurement IIFE — walks DOM 5 levels deep, measures gaps, detects bugs |
| `docs/spacing-audit/extract-all-gaps.js` | Flattens all measured gaps from all sections into a single array on `window.__gapResult` |
| `docs/spacing-audit/extract-component.js` | Measures gaps inside any CSS selector (set `window.__componentSelector` first). Result on `window.__componentResult` |
| `docs/spacing-audit/compare.js` | Comparison engine — reads measurement + spec, produces PASS/FAIL report |
| `docs/spacing-audit/inject-spec.js` | Spec injector template (currently embeds homepage-desktop spec) |
| `docs/spacing-audit/specs/*.json` | Per-page per-viewport spec files |
| `docs/spacing-audit/spec-schema.md` | Documentation of the spec JSON format |

## Workflow

### Standard one-liner: scroll + inject + verify

This pattern handles scroll-trigger animations and measurement in a single command:

```bash
playwright-cli -s=audit run-code "async (page) => { await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight)); await page.waitForTimeout(1500); await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(500); await page.addScriptTag({ path: 'docs/spacing-audit/measure.js' }); await page.waitForTimeout(500); return await page.evaluate(() => window.__lusenaSpacingAudit ? JSON.stringify(window.__lusenaSpacingAudit.summary) : 'NO DATA'); }"
```

### Mode A: Full validation (spec exists)

Use when a spec file exists for the page/viewport being tested.

#### Step 1: Navigate and resize

```bash
playwright-cli -s=audit open http://127.0.0.1:9292/{page-path}
playwright-cli -s=audit resize {width} {height}
```

Wait for page to fully load. If scroll-trigger animations are present, scroll to bottom and back to top to trigger them, or wait 2 seconds.

#### Step 2: Inject measurement script

```bash
playwright-cli -s=audit run-code "async (page) => { await page.addScriptTag({ path: 'docs/spacing-audit/measure.js' }); }"
```

Verify it worked:
```bash
playwright-cli -s=audit eval "window.__lusenaSpacingAudit ? window.__lusenaSpacingAudit.summary.totalSections + ' sections' : 'NO DATA'"
```

#### Step 3: Inject spec

The spec must be set on `window.__lusenaSpacingSpec`. Two approaches:

**Option A — Use inject-spec.js** (if it contains the right spec):
```bash
playwright-cli -s=audit run-code "async (page) => { await page.addScriptTag({ path: 'docs/spacing-audit/inject-spec.js' }); }"
```

**Option B — Build a new injector** (for a different page/viewport):
1. Read the spec JSON file with the Read tool
2. Create a new `inject-spec.js` file (or a page-specific variant like `inject-spec-pdp-desktop.js`) that assigns the JSON to `window.__lusenaSpacingSpec`
3. Inject via `addScriptTag`

Verify:
```bash
playwright-cli -s=audit eval "window.__lusenaSpacingSpec ? window.__lusenaSpacingSpec.page : 'NO SPEC'"
```

#### Step 4: Run comparison

```bash
playwright-cli -s=audit run-code "async (page) => { await page.addScriptTag({ path: 'docs/spacing-audit/compare.js' }); }"
```

#### Step 5: Read results

Summary:
```bash
playwright-cli -s=audit eval "JSON.stringify(window.__lusenaSpacingReport.summary)"
```

Full check details (if failures exist):
```bash
playwright-cli -s=audit eval "JSON.stringify(window.__lusenaSpacingReport.checks.filter(function(c){return c.status !== 'PASS'}))"
```

All checks:
```bash
playwright-cli -s=audit eval "JSON.stringify(window.__lusenaSpacingReport.checks)"
```

Bug list:
```bash
playwright-cli -s=audit eval "JSON.stringify(window.__lusenaSpacingReport.bugs)"
```

#### Step 6: Report to user

Format results as a table:

```
## Spacing Audit: {page} @ {width}x{height}

**Summary: {pass}/{total} PASS, {fail} FAIL, {skip} SKIP**

| Status | Category | Check | Expected | Actual | Delta |
|--------|----------|-------|----------|--------|-------|
| PASS   | padding  | hero padding-top | 0 | 0 | 0 |
| FAIL   | gap      | faq > heading → next | 32 | 48 | 16 |
...

### Bugs detected
| Type | Severity | Section | Detail |
...
```

### Mode B: Bug scan only (no spec)

Use when no spec exists — just measure and detect CSS issues.

#### Steps 1-2: Same as Mode A

Navigate, resize, inject `measure.js`.

#### Step 3: Read bug report and all gaps

```bash
playwright-cli -s=audit eval "JSON.stringify(window.__lusenaSpacingAudit.summary)"
playwright-cli -s=audit eval "JSON.stringify(window.__lusenaSpacingAudit.bugs)"
```

For the full gap map (all intra-section spacing):
```bash
playwright-cli -s=audit run-code "async (page) => { await page.addScriptTag({ path: 'docs/spacing-audit/extract-all-gaps.js' }); await page.waitForTimeout(300); return await page.evaluate(() => window.__gapResult); }"
```

For a specific component's internal gaps (e.g., buybox, summary):
```bash
playwright-cli -s=audit eval "window.__componentSelector = '.lusena-pdp-buy-box'"
```
then:
```bash
playwright-cli -s=audit run-code "async (page) => { await page.addScriptTag({ path: 'docs/spacing-audit/extract-component.js' }); await page.waitForTimeout(300); return await page.evaluate(() => window.__componentResult); }"
```

#### Step 4: Read section-level data

```bash
playwright-cli -s=audit eval "JSON.stringify(window.__lusenaSpacingAudit.sections.map(function(s){return {id:s.id, classes:s.classes, paddingTop:s.paddingTop, paddingBottom:s.paddingBottom}}))"
playwright-cli -s=audit eval "JSON.stringify(window.__lusenaSpacingAudit.sectionGaps)"
```

#### Step 5: Report to user

Format all data in tables:
- Section padding table (with LUSENA tier identification)
- Inter-section gaps table
- Intra-section gaps table (from extract-all-gaps.js)
- Component-specific gaps table (from extract-component.js)
- Bugs table
- Recommendations with rationale

### Mode C: Create a new spec (baselining)

Use when the user wants to create a spec for a page that doesn't have one yet.

#### Steps 1-2: Same as Mode A

Navigate, resize, inject `measure.js`.

#### Step 3: Extract raw data

```bash
playwright-cli -s=audit eval "JSON.stringify(window.__lusenaSpacingAudit.sectionGaps)"
playwright-cli -s=audit eval "JSON.stringify(window.__lusenaSpacingAudit.sections.map(function(s){return {id:s.id, classes:s.classes, paddingTop:s.paddingTop, paddingBottom:s.paddingBottom}}))"
```

For intra-section gaps, use the all-gaps extractor:
```bash
playwright-cli -s=audit run-code "async (page) => { await page.addScriptTag({ path: 'docs/spacing-audit/extract-all-gaps.js' }); await page.waitForTimeout(300); return await page.evaluate(() => window.__gapResult); }"
```

#### Step 4: Build spec JSON

Using the measured data and the spec schema (`docs/spacing-audit/spec-schema.md`), construct a spec file:

1. Read `docs/spacing-audit/spec-schema.md` for the format reference
2. Read an existing spec (e.g., `docs/spacing-audit/specs/homepage-desktop.json`) as a template
3. Map measured values to expected values — round to nearest LUSENA token where appropriate
4. Save to `docs/spacing-audit/specs/{page}-{viewport}.json`
5. Create a matching `inject-spec-{page}-{viewport}.js` file

#### Step 5: Validate the new spec

Run the full Mode A workflow against the new spec. Everything should PASS (since we just baselined from live measurements). Any failures indicate a mismatch between the spec and reality — investigate.

## Spec format reference

See `docs/spacing-audit/spec-schema.md` for full documentation. Key structure:

```json
{
  "page": "homepage",
  "url": "/",
  "viewport": { "width": 1440, "height": 900 },
  "tolerancePx": 4,
  "sectionGaps": [
    { "between": ["hero", "trust"], "expectedGapPx": 0 }
  ],
  "sections": {
    "hero": {
      "matchClass": "lusena-hero",
      "expectedPaddingTop": 0,
      "expectedPaddingBottom": 0,
      "containers": {
        ".lusena-container": [
          {
            "matchClass": "lusena-text-center",
            "expectedGapToNext": 32,
            "children": [
              { "matchClass": "lusena-type-caption", "expectedGapToNext": 16 }
            ]
          }
        ]
      }
    }
  }
}
```

## Bug detection heuristics

The measurement script (`measure.js`) auto-detects these issues:

| # | Type | Severity | What it catches |
|---|------|----------|-----------------|
| 1 | `unreset-p-margin` | error | `<p>` with browser-default margin (>8px) inside flex/grid container |
| 2 | `off-grid-spacing` | warning | Gap doesn't match any LUSENA token within 2px tolerance |
| 3 | `element-overlap` | info | Negative gap — elements overlapping by >2px |
| 4 | `unreset-heading-margin` | error | `<h1>`–`<h6>` with default margin (>4px) inside flex/grid |
| 5 | `double-margin` | warning | Both siblings have margin in a non-collapsing context (flex/grid) — creates additive spacing |
| 6 | `excessive-gap` | warning | Gap >150px — likely a layout bug or invisible spacer |
| 7 | `off-tier-padding` | info | Section padding doesn't match standard LUSENA tiers (0, 48, 64, 96px) |

LUSENA token values for `off-grid-spacing` check: 4, 8, 16, 24, 32, 40, 48, 64, 80, 96, 128, 192px.

## LUSENA spacing tiers

| Tier class | Mobile | Desktop | Use for |
|------------|--------|---------|---------|
| `lusena-spacing--full-bleed` | 0 | 0 | Full-width media, hero images |
| `lusena-spacing--compact` | 32px | 48px | Trust bars, utility bars, main product section |
| `lusena-spacing--standard` | 48px | 64px | Content sections, info sections, FAQ |
| `lusena-spacing--spacious` | 64px | 96px | CTAs, conversion sections, final CTAs |
| `lusena-spacing--hero` | 80px | 128px | Hero banners |

## Technical details

### How measurement works

- Uses `getBoundingClientRect()` for box-edge positions
- Uses `getComputedStyle()` for margins, padding, display, line-height
- **Walks 5 levels deep** from each `<section>` element inside `<main>`
- Filters out invisible elements (`display:none`, zero dimensions)
- Skips non-visual tags: `<script>`, `<style>`, `<template>`, `<noscript>`, `<link>`, `<br>`, `<svg>`
- Skips absolute/fixed positioned elements (intentional overlaps)
- Only measures vertical gaps (skips horizontal siblings in flex-row/grid-row)

### Why 5 levels deep

The PDP buybox lives at depth 4-5 from the section root: `section > .lusena-container > .lusena-grid--pdp > .lusena-pdp-buy-box > children`. The original 3-level limit missed buybox internal spacing entirely. 5 levels catches all known LUSENA component structures.

### Transform compensation

Dawn's `scroll-trigger animate--slide-in` adds `transform: translateY(12.5px)` to offscreen elements. The measurement script compensates by extracting `translateY` from the CSS transform matrix and subtracting it from bounding rect values. This gives the true CSS-defined gap, not the visually shifted one.

### Known variance: inline element bounding boxes

`<span>` elements (e.g., kickers with `lusena-type-caption`) use `display: inline`, which means `getBoundingClientRect()` returns the line-box height, not the em-box. This typically adds ~3px of variance. The default tolerance of 4px accounts for this. If a check involves an inline element, note this in the spec with a higher `tolerancePx` if needed.

### Known variance: padding-top used as gap

Some elements (e.g., `.lusena-pdp-summary__tagline`) use `padding-top` instead of `margin-top` for visual spacing. Since `getBoundingClientRect()` measures the border-box, the bounding boxes touch (gap = 0px) even though the text has visual separation. This is not a bug — the padding is inside the element. When reporting, note these as "0px (Xpx visual via padding)" rather than flagging as an issue.

### Comparison matching rules

1. **Sections** are matched by finding an inner `<section>` whose class list contains `matchClass`
2. **Container children** are matched in DOM order — first rule matches first visible child with that class
3. **`repeat: true`** matches all consecutive siblings with the same class (e.g., accordion items)
4. **Gaps** are only checked when `expectedGapToNext` is present — omit to skip checking
5. **Nested children** at depth 2 are supported via `children` array on any child rule

## Available specs

| File | Page | Viewport |
|------|------|----------|
| `specs/homepage-desktop.json` | Homepage | 1440x900 |

## Page-specific notes

### PDP (`/products/*`)

The PDP has a deeply nested DOM structure. Key selectors for component extraction:

| Component | Selector | What it measures |
|-----------|----------|-----------------|
| Buybox | `.lusena-pdp-buy-box` | Summary → proof → divider → variant → ATC → guarantee → payment → details |
| Summary | `.lusena-pdp-summary` | Eyebrow → title → tagline → price → delivery |
| Feature card | `.lusena-pdp-feature-highlights__card` | Icon-wrap → text block |
| Quality stack | `.lusena-pdp-quality-evidence__stack` | Evidence item → evidence item gaps |
| FAQ list | `.lusena-faq__list` | Accordion item → accordion item gaps |

The buybox is the most critical area for conversion — audit it with `extract-component.js` using `.lusena-pdp-buy-box` selector, in addition to the auto-scanner.

### Homepage (`/`)

Homepage spec exists at `specs/homepage-desktop.json`. Use Mode A for validation.

## Troubleshooting

### "NO DATA" after injecting measure.js
The page might not have a `<main>` or `#MainContent` element, or it may have redirected. Check `playwright-cli -s=audit eval "document.querySelector('main') ? 'found' : 'missing'"`.

### SKIP results in comparison
The section or element class wasn't found in the measurement data. Check that:
- The `matchClass` in the spec matches the actual class on the live page
- The section is visible (not hidden by conditional Liquid logic)
- The element is a direct visible child at the expected depth

### Stale measurements after CSS changes
Shopify hot-reload may navigate to a different page when CSS files are saved. After making CSS changes, re-navigate to the target page and re-inject `measure.js` from scratch. Always use `playwright-cli -s=audit goto` to force a fresh page load.

### Console errors during injection
The `addScriptTag` approach creates a `<script>` element. Chrome logs errors for CORS/CSP issues but the script still executes. Check for actual data presence rather than relying on clean console output.

### playwright-cli eval fails with complex JS
If you see `SyntaxError` or `not well-serializable`, the inline JS is too complex for shell escaping. Write the logic to a `.js` file in `docs/spacing-audit/` and inject via `addScriptTag`. Use the permanent helper scripts (`extract-all-gaps.js`, `extract-component.js`) whenever possible.

### Viewport must be set before navigation for accurate mobile measurements
Some CSS (e.g., Shopify's responsive JS) evaluates on page load. For mobile audits: resize first, then `playwright-cli -s=audit goto` to reload the page at the correct viewport. Do NOT just resize after the page has loaded — you may get hybrid desktop/mobile measurements.
