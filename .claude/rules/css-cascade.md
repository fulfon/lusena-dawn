---
paths:
  - "assets/*.css"
  - "sections/*.liquid"
  - "snippets/*.liquid"
---
# CSS Cascade & Specificity — Critical Gotchas

## Load order (earlier = lower priority)
1. Dawn `base.css` (loaded first via `content_for_header`)
2. `{% stylesheet %}` blocks (compiled into `compiled_assets/styles.css`)
3. `assets/lusena-foundations.css` (loaded at line 300 of `theme.liquid`)
4. Standalone `assets/lusena-*.css` files (per-section via `asset_url | stylesheet_tag`)

**Consequence:** Section CSS in `{% stylesheet %}` at single-class specificity (0-1-0) will silently lose to foundations. This is the #1 recurring bug — documented in lessons 1, 12, and 19.

## The 0-2-0 pattern (mandatory for ALL section CSS)
```css
/* BAD — 0-1-0, loses to foundations */
.lusena-faq__answer { color: var(--lusena-accent-2); }

/* GOOD — 0-2-0, wins over foundations */
.lusena-faq .lusena-faq__answer { color: var(--lusena-accent-2); }
```
This applies to ANY property competing with foundations: `color`, `font-size`, `font-weight`, `margin`, `margin-inline`. No exceptions.

## Dawn base.css traps
- `div:empty { display: none }` — specificity (0,1,1), beats single-class selectors. Fix: `.my-class:empty { display: block }` at (0,2,0).
- `blockquote` gets `border-left` + `padding-left` (breaks testimonials).
- `.hidden { display: none !important }` — never use for opacity transitions. Use custom state classes.

## Viewport-fill flex chain (5 documented bugs)
For sparse pages (search, 404, empty cart, contact): chain `display: flex; flex-direction: column; flex: 1` through every wrapper from `main` to the section content. Missing ONE link breaks it. Mobile: flex chain + `margin-top: auto` on bottom element. Desktop: NO flex-grow on content sections (stays compact).

## Mobile overrides: source order matters
`@media` overrides at same specificity lose to base rules that appear later in the file. Place mobile overrides AFTER the base rules they modify, or bump specificity.
