# Active Context

*Last updated: 2026-03-05*

## Current focus

**CSS foundations migration — FULLY COMPLETE.** Phase 3 finished: old Tailwind CSS deleted, preflight resets added, all post-deletion bugs fixed, compiled_assets truncation resolved by extracting 3 large sections into standalone CSS files. All pages verified. Ready to commit and move to remaining Dawn-default page migrations.

## Recent completed work (2026-03-05)

- **Preflight resets** — Added missing Tailwind resets to `lusena-foundations.css`: `button` (padding/bg/border/cursor/font/color), `a` (color/text-decoration inherit), `img, video` (max-width/height/display). SVG intentionally excluded — SVGs expand to fill containers without explicit dimensions.
- **Bug fixes after Tailwind removal** — Fixed 5 bugs that surfaced after deleting `lusena-shop.css`:
  - Header icons shrank (44→20px) — `.lusena-icon-button--md` was truncated from compiled_assets
  - Trust bar icons expanded (20→97px) — SVG max-width:100% reset + trust bar CSS truncated
  - Button text underlined on O Nas/Nasza Jakość — missing `a { text-decoration: inherit }`
  - Certificate images oversized — missing `img { max-width: 100% }`
  - Buybox accordion mismatch with FAQ — browser default 6px button padding + inconsistent styling
- **Standalone CSS extraction (compiled_assets truncation fix)** — Extracted 3 largest `{% stylesheet %}` blocks into standalone assets: `lusena-header.css` (211 lines), `lusena-hero.css` (289 lines), `lusena-footer.css` (118 lines). Also extracted `lusena-button-system.css` (366 lines). Compiled CSS dropped from 64KB to ~38KB (well under 73KB limit).
- **Dead code cleanup** — Deleted 11 files total: 4 old CSS files + 5 dead sections + 2 dead snippets.
- **Architecture pattern documented** — New "compiled_assets truncation guard" pattern in `css-architecture.md` and `CLAUDE.md`: ≤50 lines → {% stylesheet %}, >50 lines → standalone asset, mandatory size check after adding section CSS.

## Next steps

1. **Commit Phase 3** — all changes verified, ready to commit
2. Cart page LUSENA styling (stashed as `cart-migration-wip`)
3. PDP migration backlog items (see `memory-bank/doc/features/pdp-migration-backlog.md`)
4. Homepage migration backlog items (see `memory-bank/doc/features/homepage-migration-backlog.md`)
5. Remaining Dawn-default pages (search, 404, blog, account, etc.)

## Known issues

- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` is a doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- Cart migration work stashed as `cart-migration-wip` — restore after Phase 3 commit

## Architecture note

CSS loads in this order via `layout/theme.liquid`:
1. `base.css` (Dawn foundation)
2. Cart CSS (conditional)
3. `lusena-foundations.css` — tokens, utilities, components, body/main rules (~40KB)
4. `lusena-button-system.css` — button/icon-button primitives
5. `lusena-header.css` — header section styles
6. `lusena-hero.css` — hero section styles
7. `lusena-footer.css` — footer section styles
8. `lusena-pdp.css` — PDP styles (loaded per-page in section file)
9. `compiled_assets/styles.css` — remaining small `{% stylesheet %}` blocks (~38KB, limit 73KB)

**MANDATORY:** After adding CSS to any `{% stylesheet %}` block, check compiled_assets size in DevTools — must stay under 55KB. See `memory-bank/doc/patterns/css-architecture.md` for full pattern.

Shared components in foundations: `.lusena-split`, `.lusena-accordion`, `.lusena-trust-bar`, `.lusena-testimonial`, `.lusena-content-card`, `.lusena-newsletter`, `.lusena-truth-table`.

Shared sections (reusable across pages): `lusena-faq` (homepage, quality, returns, PDP), `lusena-trust-bar` (homepage, about, quality), `lusena-final-cta` (about, quality, returns).
