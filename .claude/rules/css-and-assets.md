---
paths:
  - "assets/*.css"
  - "sections/*.liquid"
  - "snippets/*.liquid"
---
# CSS Architecture & Compiled Assets

`assets/lusena-foundations.css` is the single source of truth for all CSS tokens, spacing, typography, components, and global rules. Use its classes for all section work. Class API: `memory-bank/doc/patterns/spacing-system.md`.

## Token compliance (MANDATORY)

Before writing ANY new CSS, read `assets/lusena-foundations.css` to check what tokens and classes already exist. Never write custom values when a token covers it.

### Colors
- **Never use raw RGB/hex** — always reference tokens: `var(--lusena-accent-cta)`, `var(--lusena-text-2)`, etc.
- **For opacity variants** use `color-mix()`: `color-mix(in srgb, var(--lusena-accent-cta) 30%, transparent)` — never `rgb(14 94 90 / 0.3)`. This ensures the value updates automatically if the token changes.

### Typography
- **Use foundation type classes in Liquid markup**: `lusena-type-hero`, `lusena-type-h1`, `lusena-type-h2`, `lusena-type-body`, `lusena-type-caption` — never define custom font-size/line-height/font-family in section CSS when a foundation class exists.
- Only override with section CSS when the design genuinely requires a value outside the type scale.

### Icons
- **Use `lusena-icon-circle`** (4.8rem) for icon circles — override only bg/border/color, never size.
- **Use `lusena-icon-*` size classes** (`lusena-icon-xs` through `lusena-icon-xl`) — never custom width/height on icon SVGs.

### Spacing
- All padding, margin, gap must use `var(--lusena-space-*)` tokens.
- Section padding: use tier classes (`lusena-spacing--standard`, etc.).

### Transitions
- Use `var(--lusena-transition-fast)` (150ms) or `var(--lusena-transition-base)` (250ms) — never raw `300ms ease`.

### Radius
- Use `var(--lusena-btn-radius)` (6px) — never raw `border-radius` values.

### Dawn base.css traps
- `div:empty { display: none }` at specificity (0,1,1) — empty decorative divs need 0-2-0 selector: `.lusena-section .lusena-section__element:empty` or `.lusena-section .lusena-section__element`.
- `blockquote` gets `border-left` + `padding-left` from Dawn — override if using blockquotes.

## compiled_assets truncation guard (MANDATORY)

Shopify compiles all `{% stylesheet %}` blocks into one `compiled_assets/styles.css` that silently truncates at ~73KB.

- <=50 lines of section-scoped CSS -> OK in `{% stylesheet %}`
- >50 lines or shared CSS -> must go in standalone `assets/lusena-*.css`
- After adding CSS to `{% stylesheet %}`: check compiled_assets size in DevTools Network tab - must stay under 55KB
- If over 55KB: extract the largest block (see `memory-bank/doc/patterns/css-architecture.md`)
