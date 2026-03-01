# Active Context

*Last updated: 2026-03-01*

## Current focus

**CSS foundations migration** — Phase 1 (homepage) fully complete including visual verification and bug fixes. Ready for Phase 2 planning.

## Recent completed work

- **Phase 0a:** Fixed padding override variable names in `lusena-foundations.css`
- **Phase 0b:** Loaded `lusena-foundations.css` in `layout/theme.liquid`
- **Phase 1:** Migrated all 9 homepage sections from Tailwind to foundations + section stylesheets (zero Tailwind classes remain)
- **Phase 1 bug fixes** (5 visual regressions found via Playwright, all fixed):
  1. Testimonials broken — curly quotes (U+201C/U+201D) in HTML class attributes caused all CSS to fail silently; replaced with straight quotes
  2. FAQ not centered — `.lusena-container--narrow` missing `margin-inline: auto` + `padding-inline`; fixed in `lusena-foundations.css`
  3. Buttons not rounded — `border-radius: 6px` added to 5 selectors across hero, bundles, heritage, bestsellers
  4. Problem/Solution alignment — confirmed NOT a bug (items are aligned, content-dependent grid flow)
  5. Newsletter input tiny on mobile — `flex: 1` collapsed height in column layout; moved to desktop-only media query

## Pending decisions

- Phase 2 scope and approach (plan being prepared)

## Next steps

1. **Phase 2:** Migrate remaining pages — PDP, quality, returns, about, collection sections
2. **Phase 3:** Remove old CSS files (`lusena-shop.css`, `lusena-spacing.css`, `lusena-missing-utilities.liquid`)
3. PDP migration backlog items (see `memory-bank/doc/features/pdp-migration-backlog.md`)
4. Homepage migration backlog items (see `memory-bank/doc/features/homepage-migration-backlog.md`)
5. Cart page LUSENA styling
6. Remaining Dawn-default pages (search, 404, blog, account, etc.)

## Known issues

- `lusena-missing-utilities.liquid` (351 lines) Tailwind patch file — will be removed after Phase 3
- `lusena-shop.css` (26KB compiled Tailwind) — will be removed after Phase 3
- `lusena-spacing.css` (9KB) — will be absorbed by foundations after Phase 3
- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- Non-homepage sections still use Tailwind classes — migration is page-by-page in Phase 2

## Architecture note (from Phase 1 learnings)

CSS lives in two layers: (1) `lusena-foundations.css` — design tokens, utilities, containers; (2) per-section `{% stylesheet %}` blocks — all layout/component CSS. The Phase 1 migration swapped Tailwind utility classes for BEM + CSS variables but preserved the same visual appearance. A future visual refresh would rewrite the section stylesheets to fully adopt the designer's editorial rhythm philosophy.
