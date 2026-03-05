# Progress

*Last updated: 2026-03-05*

## LUSENA-styled pages (8 of ~21 total)

- [x] **Homepage** (`index.json`) — 9 sections: hero, trust bar, problem/solution, bestsellers, heritage, testimonials, bundles, FAQ, newsletter
- [x] **Product page** (`product.json`) — 5 sections: main-product, feature highlights, quality evidence, truth table, FAQ (shared `lusena-faq`)
- [x] **Collection page** (`collection.json`) — 1 section: main-collection + product card snippet
- [x] **Quality page** (`page.nasza-jakosc.json`) — 11 sections: hero, trust bar, origin, momme, certificates, fire test, 6a, qc, comparison table, FAQ, final CTA
- [x] **Returns page** (`page.zwroty.json`) — 5 sections: hero, steps, editorial, FAQ, final CTA
- [x] **About page** (`page.o-nas.json`) — 5 sections: hero, trust bar, story, values, final CTA
- [x] **Cart page** (`cart.json`) — 2 sections: cart-items (with upsell), cart-footer (totals, shipping bar, CTA, trust row)
- [x] **Search page** (`search.json`) — 1 section: lusena-search (product grid, non-product results, empty state with bestsellers, predictive search, Polish translations)

## Dawn → LUSENA page migration (2 of 10 templates — 5 customer pages N/A)

Full plan: `memory-bank/doc/features/dawn-pages-migration-plan.md`

- [x] **Batch 0: Shared infrastructure** — `.lusena-form` layout, `.lusena-table` + `.lusena-line-item`, `.lusena-page-header` snippet, `.lusena-checkbox` (2026-03-04)
- [x] **Batch 1: Cart** — `cart.json` — 3 new files: `lusena-cart-items.liquid`, `lusena-cart-quantity.liquid`, `lusena-cart-footer.liquid`. Full drawer parity. (2026-03-05)
- [ ] **Batch 2: Content pages** — `404.json`, `page.json`, `page.contact.json`
- ~~**Batch 3: Customer auth**~~ — **N/A (Shopify-managed)** — Sign in page branded via admin settings (2026-03-05)
- ~~**Batch 4: Customer account**~~ — **N/A (Shopify-managed)** — Checkout, thank you, orders, order status, profile pages branded via admin settings (2026-03-05)
- [x] **Batch 5: Search** — `search.json` → `lusena-search`. Polish translations in `en.default.json`. list-collections skipped. (2026-03-05)
- [ ] **Batch 6: Blog** — `blog.json`, `article.json`
- [ ] **Batch 7: Password** — `password.json`

## Infrastructure completed

- [x] CSS foundations file (`assets/lusena-foundations.css`) — designer-generated, 7 fixes applied, production-ready
- [x] PDP standalone CSS (`assets/lusena-pdp.css`) — PDP styles + sticky ATC styles (avoids compiled_assets truncation)
- [x] CSS foundations brief (`docs/css-foundations-brief.md`) — self-contained spec for the designer
- [x] Button system standalone CSS (`assets/lusena-button-system.css`) — extracted from snippet {% stylesheet %} to avoid compiled_assets truncation (2026-03-05)
- [x] Header standalone CSS (`assets/lusena-header.css`) — extracted from section {% stylesheet %} (2026-03-05)
- [x] Hero standalone CSS (`assets/lusena-hero.css`) — extracted from section {% stylesheet %} (2026-03-05)
- [x] Footer standalone CSS (`assets/lusena-footer.css`) — extracted from section {% stylesheet %} (2026-03-05)
- [x] Icon system (`snippets/lusena-icon.liquid`)
- [x] Section gap detector (`snippets/lusena-section-gap-detector.liquid`)
- [x] Header (`sections/lusena-header.liquid`) — migrated to foundations
- [x] Footer (`sections/lusena-footer.liquid`) — migrated to foundations (2026-03-04)
- [x] Cart drawer (`snippets/cart-drawer.liquid`) — migrated to BEM + foundations (2026-03-04)
- [x] Sticky ATC (`snippets/lusena-pdp-sticky-atc.liquid`) — CSS moved to `lusena-pdp.css` (2026-03-04)
- [x] Product card (`snippets/lusena-product-card.liquid`)
- [x] Breadcrumbs (`snippets/lusena-breadcrumbs.liquid`)
- [x] Generic final CTA (`sections/lusena-final-cta.liquid`) — reusable across all pages
- [x] Preflight resets in foundations — button, anchor, img/video (2026-03-05)
- [x] compiled_assets truncation guard pattern documented (2026-03-05)
- [x] Memory bank architecture
- [x] Migration workflow (`memory-bank/doc/patterns/migration-lessons.md`) — single-pass Phases A–E with mandatory UX audit

## CSS foundations migration

`lusena-foundations.css` replaced 3 old files: `lusena-shop.css` (Tailwind), `lusena-spacing.css`, `lusena-missing-utilities.liquid`. Migration was section-by-section:

- [x] Phase 0: Load foundations alongside existing CSS in `layout/theme.liquid` + fix padding variable names
- [x] Phase 1: Migrate homepage sections (9/9)
- [x] Phase 2 homepage: Editorial transformation of all 9 homepage sections
- [x] Phase 2b: Post-editorial fixes — 5 bugs + mobile marquee
- [x] Phase 2 about page: 3 sections + UX audit + generic final CTA
- [x] Phase 2 quality page: 8 sections + shared `.lusena-truth-table` + UX audit
- [x] Phase 2 returns page: 4 sections + FAQ consolidation
- [x] Phase 2 PDP: 15 files (5 sections + 10 snippets) + standalone `lusena-pdp.css`
- [x] Phase 2 collection: 3 files + Polish pluralization + OOS modifier
- [x] Phase 2 infrastructure: Header, footer, cart drawer, sticky ATC — all migrated to foundations
- [x] Phase 3: Body/main migration + old CSS deletion + dead code cleanup (2026-03-04)
- [x] Phase 3b: Preflight resets + bug fixes + compiled_assets truncation fix + standalone CSS extraction (2026-03-05)

## Phase 3 completed (2026-03-04 → 2026-03-05)

### Files deleted (11 total):
- `assets/lusena-shop.css` (26KB Tailwind) — replaced by `lusena-foundations.css`
- `assets/lusena-spacing.css` (266 lines) — absorbed into `lusena-foundations.css`
- `snippets/lusena-missing-utilities.liquid` (351 lines) — absorbed into `lusena-foundations.css`
- `snippets/lusena-spacing-system.liquid` — empty stub, no longer needed
- `snippets/lusena-pdp-accordions.liquid` — orphan snippet, never rendered
- `sections/lusena-page-about.liquid` — replaced by individual `lusena-about-*` sections
- `sections/lusena-page-quality.liquid` — replaced by individual `lusena-quality-*` sections
- `sections/lusena-page-returns.liquid` — replaced by individual `lusena-returns-*` sections
- `sections/lusena-pdp-details.liquid` — replaced by shared `lusena-faq`
- `sections/lusena-quality-final-cta.liquid` — replaced by generic `lusena-final-cta`
- `sections/lusena-returns-faq.liquid` — replaced by shared `lusena-faq`

### Standalone CSS files created (4 new):
- `assets/lusena-button-system.css` — extracted from `snippets/lusena-button-system.liquid` {% stylesheet %}
- `assets/lusena-header.css` — extracted from `sections/lusena-header.liquid` {% stylesheet %}
- `assets/lusena-hero.css` — extracted from `sections/lusena-hero.liquid` {% stylesheet %}
- `assets/lusena-footer.css` — extracted from `sections/lusena-footer.liquid` {% stylesheet %}

### Preflight resets added to foundations:
- `button { padding: 0; background: transparent; border: 0; cursor: pointer; font: inherit; color: inherit; }`
- `a { color: inherit; text-decoration: inherit; }`
- `img, video { max-width: 100%; height: auto; display: block; }`
- Trust bar CSS moved from {% stylesheet %} into foundations (was being truncated)

### Bug fixes (5):
- Header icons 20px → 44px (button system CSS truncated from compiled_assets)
- Trust bar icons 97px → 20px (SVG max-width + trust bar CSS truncated)
- Button text underlines on O Nas/Nasza Jakość (missing anchor reset)
- Certificate images oversized (missing img reset)
- Buybox accordion mismatch (browser default button padding + style inconsistency)

Load lines removed from `layout/theme.liquid`: `lusena-shop.css`, `lusena-spacing.css`, `lusena-missing-utilities`, `lusena-spacing-system`.

Body/main Tailwind classes moved to `lusena-foundations.css` global rules (body flex-col sticky footer + `#MainContent` flex-grow).

## Active migration backlogs

- **PDP:** 4 deferred items — see `memory-bank/doc/features/pdp-migration-backlog.md`
- **Homepage:** 6 deferred items — see `memory-bank/doc/features/homepage-migration-backlog.md`

## UX backlog (evaluate during polish phase)

- **Mobile header icons** — Currently only cart icon visible on mobile. Consider adding search icon and account/login icon to the mobile header for better discoverability.

## Cleanup backlog (not urgent — Dawn originals needed by theme editor)

- `sections/main-product.liquid` (100KB) — superseded by `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` — doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- `sections/header.liquid` — superseded by `lusena-header.liquid`
- `sections/footer.liquid` — superseded by `lusena-footer.liquid`
- 50+ other Dawn sections/snippets — remain as fallbacks for theme editor and unused templates
