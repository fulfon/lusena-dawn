# Active Context

*Last updated: 2026-02-28*

## Current focus

**CSS foundations migration** — Replacing the fragmented CSS setup (Tailwind build `lusena-shop.css` + hand-written `lusena-spacing.css` + patch file `lusena-missing-utilities.liquid`) with a single designer-crafted `lusena-foundations.css`.

## Recent completed work

- Created CSS foundations brief (`docs/css-foundations-brief.md`) — self-contained ~470-line spec for AI designer
- AI designer (Iterative Studio) generated `assets/lusena-foundations.css` (34KB, 800+ lines)
- Reviewed and applied 7 fixes to make foundations CSS production-ready:
  - Added `--lusena-space-10` (80px) token to complete the 8px scale
  - Added `--lusena-radius-sm` (2px) token (was referenced but undefined)
  - Rewrote all 5 spacing tiers to "slightly more generous" values (was 2x too large)
  - Added `lusena-spacing--snug-top` modifier (used by quality/returns heroes)
  - Added `lusena-section-gap-same` / `lusena-section-gap-different` classes
  - Renamed gap classes to match existing Liquid (`lusena-gap-heading`, etc.)
  - Added `lusena-content-flow` classes (backwards-compatible, no flex)
  - Added `lusena-object-cover` / `lusena-object-contain` utilities
- Memory bank architecture restructuring

## Pending decisions

- Migration strategy: load foundations alongside existing CSS first (Phase 0), then migrate sections one-by-one
- Which homepage section to migrate first as proof-of-concept (trust-bar recommended — small, self-contained)

## Next steps

1. **Load `lusena-foundations.css` into `layout/theme.liquid`** alongside existing CSS (Phase 0 — additive, no breakage)
2. **Migrate homepage sections** one-by-one from Tailwind classes to foundation classes (Phase 1)
3. **Migrate other pages** (PDP, quality, returns, about, collection)
4. **Remove old CSS** once all pages migrated: `lusena-shop.css`, `lusena-spacing.css`, `lusena-missing-utilities.liquid`
5. PDP migration backlog items (see `memory-bank/doc/features/pdp-migration-backlog.md`)
6. Homepage migration backlog items (see `memory-bank/doc/features/homepage-migration-backlog.md`)
7. Cart page LUSENA styling
8. Remaining Dawn-default pages (search, 404, blog, account, etc.)

## Known issues

- `lusena-missing-utilities.liquid` (351 lines) Tailwind patch file — will be removed after foundations migration
- `lusena-shop.css` (26KB compiled Tailwind) — will be removed after foundations migration
- `lusena-spacing.css` (9KB) — will be absorbed by foundations after migration
- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- Existing sections heavily use Tailwind classes (200+ instances across 39 sections) — migration is section-by-section
