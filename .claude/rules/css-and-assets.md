---
paths:
  - "assets/*.css"
  - "sections/*.liquid"
  - "snippets/*.liquid"
---
# CSS Architecture & Compiled Assets

`assets/lusena-foundations.css` is the single source of truth for all CSS tokens, spacing, typography, components, and global rules. Use its classes for all section work. Class API: `memory-bank/doc/patterns/spacing-system.md`.

## compiled_assets truncation guard (MANDATORY)

Shopify compiles all `{% stylesheet %}` blocks into one `compiled_assets/styles.css` that silently truncates at ~73KB.

- <=50 lines of section-scoped CSS -> OK in `{% stylesheet %}`
- >50 lines or shared CSS -> must go in standalone `assets/lusena-*.css`
- After adding CSS to `{% stylesheet %}`: check compiled_assets size in DevTools Network tab - must stay under 55KB
- If over 55KB: extract the largest block (see `memory-bank/doc/patterns/css-architecture.md`)
