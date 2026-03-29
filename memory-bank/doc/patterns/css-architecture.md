# CSS Architecture

## Migration status

**Migration complete (2026-03-04).** All old CSS files (`lusena-shop.css`, `lusena-spacing.css`, `lusena-missing-utilities.liquid`) have been deleted. The theme now runs on a single CSS architecture.

## Layer stack

```
1. Inline <style> block
   ├── @font-face declarations (Inter Variable, Source Serif 4)
   ├── :root CSS custom properties (colors, fonts, media, grid, components)
   ├── .color-{scheme} dynamic variables (generated from theme settings)
   └── html/body base styles

2. base.css (3,641 lines)
   └── Dawn foundation: reset, grid, buttons, forms, accessibility

3. Cart CSS (conditional — only if cart_type == 'drawer')
   ├── component-cart-drawer.css
   ├── component-cart.css / component-totals.css / component-price.css / component-discounts.css

4. Standalone LUSENA assets (loaded globally via <link> in theme.liquid)
   ├── lusena-foundations.css (~40KB) — single source of truth for tokens, spacing, typography, components
   ├── lusena-button-system.css — button/icon-button primitives
   ├── lusena-header.css — header section (fixed positioning, nav, mobile menu, cart badge)
   ├── lusena-hero.css — hero section (layout, animations, buttons, content positioning)
   └── lusena-footer.css — footer section (dark bg, grid, newsletter, bottom bar)

5. Page-specific assets (loaded per-page via <link> in their section)
   ├── lusena-pdp.css (~34KB) — PDP + sticky ATC styles (loaded in lusena-main-product.liquid)
   ├── lusena-cart-page.css — cart items + footer + quantity styles (loaded in lusena-cart-items.liquid)
   └── lusena-search.css — search page styles (loaded in lusena-search.liquid)

6. Component {% stylesheet %} blocks (small, section-scoped CSS only)
   └── Compiled into compiled_assets/styles.css (~59KB after 2026-03-26 extraction, ~73KB hard limit)
```

## compiled_assets truncation — CRITICAL pattern

### The problem

Shopify compiles ALL `{% stylesheet %}` blocks from every section and snippet into one file: `compiled_assets/styles.css`. This file **silently truncates at ~73KB** — no error, no warning, CSS just stops mid-rule. Any rules after the cut-off point are lost.

### The rule: standalone vs {% stylesheet %}

| CSS size | Where to put it | Loaded via |
|----------|----------------|------------|
| **Small** (≤50 lines, section-scoped) | `{% stylesheet %}` block in the section | compiled_assets (shared) |
| **Large** (>50 lines) or **shared** | `assets/lusena-*.css` standalone file | `<link>` tag in theme.liquid or section |

### Mandatory verification after adding section CSS

After adding or expanding CSS in any `{% stylesheet %}` block:

1. Start dev server (`shopify theme dev`)
2. Open any page in the browser
3. Check compiled_assets size via DevTools Network tab — filter for `compiled_assets`
4. **The file must stay under 55KB** (leaves ~18KB safety margin)
5. If it exceeds 55KB, extract the largest `{% stylesheet %}` block into a standalone asset file

### How to extract a section's CSS into a standalone asset

1. Create `assets/lusena-{section-name}.css` with the CSS content
2. Empty the `{% stylesheet %}` block in the section (leave a comment pointing to the new file)
3. Add `{{ 'lusena-{section-name}.css' | asset_url | stylesheet_tag }}` to `theme.liquid` (global sections) or the section file itself (page-specific sections)
4. Verify the page visually — CSS is identical, just loaded differently

### Current inventory of standalone assets (2026-03-29)

| File | Scope | Loaded in |
|------|-------|-----------|
| `lusena-foundations.css` | Global tokens + components | theme.liquid |
| `lusena-button-system.css` | Button/icon-button primitives | theme.liquid |
| `lusena-header.css` | Header section | theme.liquid |
| `lusena-hero.css` | Hero section | theme.liquid |
| `lusena-footer.css` | Footer section | theme.liquid |
| `lusena-pdp.css` | PDP page | lusena-main-product.liquid |
| `lusena-cart-page.css` | Cart page (items + footer + qty) | lusena-cart-items.liquid |
| `lusena-search.css` | Search page | lusena-search.liquid |
| `lusena-bundles.css` | Bundle card grid | lusena-bundles.liquid (per-section) |
| `lusena-benefit-bridge.css` | Benefit bridge section | lusena-benefit-bridge.liquid (per-section) |
| `lusena-icon-animations.css` | Animated icon keyframes | lusena-pdp-feature-highlights.liquid (per-section) |

## Naming conventions

| Pattern | Example | Scope |
|---------|---------|-------|
| `lusena-spacing--*` | `lusena-spacing--standard` | Section tier classes |
| `lusena-content-flow*` | `lusena-content-flow--tight` | Container rhythm |
| `lusena-gap-*` | `lusena-gap-heading` | Element margins |
| `lusena-type-*` | `lusena-type-h1` | Typography classes |
| `lusena-container*` | `lusena-container--narrow` | Layout containers |
| `lusena-grid--*` | `lusena-grid--3` | Grid layouts |
| `lusena-stack*` | `lusena-stack--tight` | Flex-col + spacing |
| `lusena-btn*` | `lusena-btn--primary` | Button variants |
| `lusena-pdp-*` | `lusena-pdp-accordion` | PDP-specific components |
| `--lusena-space-*` | `--lusena-space-4` | Spacing tokens (numbered, 8px grid) |
| `--lusena-*` | `--lusena-text-1` | All CSS custom properties |
| `--color-*` | `--color-background` | Dawn theme color variables |

## Dawn margin neutralization

Dawn adds `margin-top: var(--spacing-sections-desktop)` between `.section` wrappers. `lusena-foundations.css` zeros this when either adjacent section uses a `lusena-spacing--*` class:

```css
.section:has(> [class*="lusena-spacing--"]) + .section,
.section + .section:has(> [class*="lusena-spacing--"]) {
  margin-top: 0;
}
```

## CSS selector scoping — MANDATORY for shared class names

### The problem

The cart drawer loads its inline `<style>` on **every page**. Page-specific CSS files (e.g., `lusena-cart-page.css`) load only on their page. If both define rules for the same class name (e.g., `.lusena-upsell-card`), the styles collide on that page — the drawer looks different depending on which page you're on.

### The rule

**Every `.lusena-upsell-card__*` selector (or any shared component class) MUST be scoped under its surface's wrapper:**

| Surface | Wrapper scope | Example |
|---------|--------------|---------|
| Cart drawer | `.lusena-cart-drawer__upsell` | `.lusena-cart-drawer__upsell .lusena-upsell-card__bn-headline { ... }` |
| Cart page | `.lusena-cart-upsell` | `.lusena-cart-upsell .lusena-upsell-card__bn-headline { ... }` |
| Future PDP upsell | `.lusena-pdp-upsell` (or similar) | `.lusena-pdp-upsell .lusena-upsell-card__bn-headline { ... }` |

### Why this matters

The upsell card HTML uses shared class names (`.lusena-upsell-card__*`) across multiple surfaces. Each surface styles the card differently (the drawer uses compact mobile layout, the cart page uses wider desktop layout). Without scoping:

- Drawer CSS fires on every page (inline `<style>` is global) and would style any future PDP upsell widget
- Page-specific CSS fires only on that page, making the drawer look inconsistent

### When writing new component CSS

1. **Before writing any selector**, ask: "Does another surface use this class name?"
2. If yes (or if it might in the future), **always scope** under the surface's wrapper element
3. Never use bare `.lusena-upsell-card__*`, `.loading__spinner`, or other shared selectors — always prefix with the surface wrapper

This was learned the hard way on 2026-03-26 when extracting cart CSS to a standalone file exposed pre-existing bleed between the cart page and cart drawer.

## Key constraints

- `{% stylesheet %}` blocks have ~73KB cumulative limit — large CSS must go in standalone asset files
- CSS `:has()` selector used for margin neutralization — modern browsers only (fine for Shopify's target)
- Liquid is NOT rendered inside `{% stylesheet %}` or `{% javascript %}` blocks
- Dawn's `font-size: 62.5%` makes `1rem = 10px` — all foundations tokens use rem
