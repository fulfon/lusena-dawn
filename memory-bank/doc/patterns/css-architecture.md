# CSS Architecture

## Layer stack (loading order in layout/theme.liquid)

```
1. Inline <style> block (lines 51-287)
   ├── @font-face declarations (Inter Variable, Source Serif 4)
   ├── :root CSS custom properties (colors, fonts, media, grid, components)
   ├── .color-{scheme} dynamic variables (generated from theme settings)
   └── html/body base styles

2. base.css (3,641 lines)
   └── Dawn foundation: reset, grid, buttons, forms, accessibility

3. Cart CSS (conditional — only if cart_type == 'drawer')
   ├── component-cart-drawer.css
   ├── component-cart.css
   ├── component-totals.css
   ├── component-price.css
   └── component-discounts.css

4. lusena-shop.css (26KB — Tailwind compiled)
   ├── Brand colors: --brand-bg, --primary, --accent-cta
   ├── Tailwind base, components, utilities
   └── Responsive breakpoint classes (sm:, md:, lg:, xl:)

5. lusena-spacing.css (266 lines — spacing source of truth)
   ├── :root spacing tokens (mobile-first)
   ├── @media (min-width:768px) desktop overrides
   ├── Tier classes (.lusena-spacing--*)
   ├── Semantic gap classes (.lusena-gap-*)
   ├── Content-flow utilities (.lusena-content-flow*)
   └── Dawn margin neutralization (.section + .section override)

6. Inline snippets (rendered via {% render %})
   ├── lusena-missing-utilities — Tailwind utility patches
   ├── lusena-button-system — Button/icon-button primitives
   └── lusena-spacing-system — Doc-only stub (empty)

7. Component {% stylesheet %} blocks
   └── Compiled into compiled_assets/styles.css (~73KB limit)
```

## Naming conventions

| Pattern | Example | Scope |
|---------|---------|-------|
| `lusena-spacing--*` | `lusena-spacing--standard` | Section tier classes |
| `lusena-content-flow*` | `lusena-content-flow--tight` | Container rhythm |
| `lusena-gap-*` | `lusena-gap-heading` | Element margins |
| `lusena-btn*` | `lusena-btn--primary` | Button variants |
| `lusena-icon-button*` | `lusena-icon-button--ghost` | Icon button variants |
| `lusena-pdp-*` | `lusena-pdp-accordion` | PDP-specific components |
| `--lusena-*` | `--lusena-space-lg` | CSS custom properties |
| `--color-*` | `--color-background` | Dawn theme color variables |
| `--font-*` | `--font-body-family` | Dawn typography variables |

## Dawn margin neutralization

Dawn adds `margin-top: var(--spacing-sections-desktop)` between `.section` wrappers. LUSENA's `lusena-spacing.css` zeros this when either adjacent section uses a `lusena-spacing--*` class:

```css
.section:has(> [class*="lusena-spacing--"]) + .section,
.section + .section:has(> [class*="lusena-spacing--"]) {
  margin-top: 0;
}
```

This ensures LUSENA's tier padding is the sole spacing authority for styled sections.

## Key constraints

- `{% stylesheet %}` blocks have ~73KB cumulative limit — spacing CSS must go in `assets/lusena-spacing.css`
- CSS `:has()` selector used for margin neutralization — modern browsers only (fine for Shopify's target)
- Liquid is NOT rendered inside `{% stylesheet %}` or `{% javascript %}` blocks
- `lusena-missing-utilities.liquid` is a growing tech debt bucket (351 lines of Tailwind patches)
