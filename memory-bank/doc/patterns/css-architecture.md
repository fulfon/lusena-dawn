# CSS Architecture

## Migration status

We are migrating from a fragmented CSS setup to a single `assets/lusena-foundations.css`. During transition, both old and new files coexist. See `memory-bank/progress.md` for phase status.

## Target layer stack (after migration completes)

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

4. lusena-foundations.css (34KB — single source of truth)
   ├── Color tokens (N0-N900, brand, status, scrims)
   ├── Spacing tokens (8px baseline: space-1 through space-24)
   ├── Typography system (5 semantic classes + richtext)
   ├── Z-index layering scale
   ├── Transition tokens
   ├── Section spacing tiers + snug-top + same-bg gap handling
   ├── Dawn margin neutralization
   ├── Layout grid & containers
   ├── Component patterns (product cards, testimonials, badges, trust bar, etc.)
   ├── Form system (inputs, selects, swatches, pills, quantity)
   ├── Inverted section logic (token remapping)
   ├── Interactive states (drawer, modal, overlay, accordion)
   └── Utility classes (bg, text, flex, aspect, hidden, object-fit, etc.)

5. Inline snippets (rendered via {% render %})
   ├── lusena-button-system — Button/icon-button primitives
   └── lusena-pdp-styles — PDP-specific component styles

6. Component {% stylesheet %} blocks
   └── Compiled into compiled_assets/styles.css (~73KB limit)
```

## Old layer stack (being phased out)

These files will be removed once all sections are migrated to foundations classes:
- `assets/lusena-shop.css` (26KB Tailwind) → replaced by foundations
- `assets/lusena-spacing.css` (266 lines) → absorbed into foundations
- `snippets/lusena-missing-utilities.liquid` (351 lines) → absorbed into foundations

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

## Key constraints

- `{% stylesheet %}` blocks have ~73KB cumulative limit — large CSS must go in standalone asset files
- CSS `:has()` selector used for margin neutralization — modern browsers only (fine for Shopify's target)
- Liquid is NOT rendered inside `{% stylesheet %}` or `{% javascript %}` blocks
- Dawn's `font-size: 62.5%` makes `1rem = 10px` — all foundations tokens use rem
