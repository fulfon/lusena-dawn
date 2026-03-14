# Progress

*Last updated: 2026-03-14*

## LUSENA-styled pages (13 of ~21 total)

- [x] **Homepage** (`index.json`) — 9 sections: hero, trust bar, problem/solution, bestsellers, testimonials, bundles (card grid), heritage, FAQ, final CTA. Full UX audit completed 2026-03-08 (copy, flow, visual rhythm, value anchors, spacing). Newsletter removed (footer handles it).
- [x] **Product page** (`product.json`) — 6 sections: main-product, feature highlights, quality evidence, truth table, FAQ (shared `lusena-faq`), final CTA (shared `lusena-final-cta`). Full UX audit completed 2026-03-09 (visual rhythm, content rewrite, legal compliance, FAQ consolidation, conversion CTA). Per-product metafield overrides for headline/tagline/per-night. Returns deep-link. PDP buy-box spacing overhauled.
- [x] **Collection page** (`collection.json`) — 1 section: main-collection + product card snippet
- [x] **Quality page** (`page.nasza-jakosc.json`) — 10 sections: hero, trust bar, origin, momme, certificates, fire test, qc, comparison table, FAQ, final CTA. 6A section removed (content merged into momme). "30%" corrected to "15%". Spacing audit completed 2026-03-10 (3 off-grid fixes + 1 tier upgrade).
- [x] **Returns page** (`page.zwroty.json`) — 5 sections: hero, steps, editorial, FAQ, final CTA
- [x] **About page** (`page.o-nas.json`) — 5 sections: hero, trust bar, story, values, final CTA
- [x] **Cart page** (`cart.json`) — 2 sections: cart-items (with upsell), cart-footer (totals, shipping bar, CTA, trust row)
- [x] **Search page** (`search.json`) — 1 section: lusena-search (product grid, non-product results, empty state with bestsellers, predictive search, Polish translations)
- [x] **Blog listing** (`blog.json`) — 1 section: lusena-blog (2-col grid, pagination, rich empty state with viewport fill)
- [x] **Article page** (`article.json`) — 2 sections: lusena-article (hero, richtext, share button, LD+JSON) + lusena-newsletter (with secondary shop link)
- [x] **404 page** (`404.json`) — 1 section: lusena-404 (centered error message, bestseller grid, viewport-fill)
- [x] **Generic page** (`page.json`) — 1 section: lusena-main-page (breadcrumbs, title, richtext via `.lusena-richtext`, viewport-fill, compact spacing)
- [x] **Contact page** (`page.contact.json`) — 2 sections: lusena-contact-form (breadcrumbs, heading, LUSENA form system, customer pre-fill, viewport-fill, full-width mobile button) + lusena-newsletter

## Dawn → LUSENA page migration — COMPLETE (all customer-facing pages branded)

Full plan: `memory-bank/doc/features/dawn-pages-migration-plan.md`

- [x] **Batch 0: Shared infrastructure** — `.lusena-form` layout, `.lusena-table` + `.lusena-line-item`, `.lusena-page-header` snippet, `.lusena-checkbox` (2026-03-04)
- [x] **Batch 1: Cart** — `cart.json` — 3 new files: `lusena-cart-items.liquid`, `lusena-cart-quantity.liquid`, `lusena-cart-footer.liquid`. Full drawer parity. (2026-03-05)
- [x] **Batch 2: Content pages** — `404.json` → `lusena-404`, `page.json` → `lusena-main-page`, `page.contact.json` → `lusena-main-page` + `lusena-contact-form` + `lusena-newsletter`. Breadcrumbs extended for `page` type. Polish translations for 404 + contact. Zero new CSS in foundations — all reused. (2026-03-06)
- ~~**Batch 3: Customer auth**~~ — **N/A (Shopify-managed)** — Sign in page branded via admin settings (2026-03-05)
- ~~**Batch 4: Customer account**~~ — **N/A (Shopify-managed)** — Checkout, thank you, orders, order status, profile pages branded via admin settings (2026-03-05)
- [x] **Batch 5: Search** — `search.json` → `lusena-search`. Polish translations in `en.default.json`. list-collections skipped. (2026-03-05)
- [x] **Batch 6: Blog + Article** — `blog.json` → `lusena-blog`, `article.json` → `lusena-article` + `lusena-newsletter`. New snippets: `lusena-article-card`, `lusena-share-button`, `lusena-date-pl`. Breadcrumbs extended. Newsletter enhanced with optional secondary link. (2026-03-06)
- [~] **Batch 7: Password** — `password.json` — **Abandoned (2026-03-06).** Not needed: page only shows when store is password-protected. Can revisit if needed; migration plan exists at `.claude/plans/dazzling-exploring-neumann.md`.

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
- [x] Bundles standalone CSS (`assets/lusena-bundles.css`) — bundle card grid styles (loaded per-section) (2026-03-07)
- [x] Reusable page audit skill (`.claude/skills/lusena-page-audit/`) — standardized UX audit checklist (2026-03-08)
- [x] Customer validation skill (`.claude/skills/lusena-customer-validation/`) — 4-persona copy evaluation (2026-03-14)
- [x] Legal check skill (`.claude/skills/lusena-legal-check/`) — EU/UOKiK compliance check (2026-03-14)
- [x] Spacing audit skill (`.claude/skills/lusena-spacing-audit/`) — automated spacing measurement + validation (2026-03-10)
- [x] Product metafields reference (`docs/product-metafields-reference.md`) — field-by-field PDP mapping + creative process (2026-03-14)
- [x] Product setup checklist (`docs/product-setup-checklist.md`) — metafield definitions + example values (2026-03-14)
- [x] Product catalog docs (`memory-bank/doc/products/`) — per-product admin data tracking (2026-03-14)
- [x] Spacing audit tooling (`docs/spacing-audit/`) — measurement JS scripts + spec schemas (2026-03-10)
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

## Shopify Admin: Product Setup

**Store-wide settings (completed 2026-03-14):**
- [x] Store currency → PLN
- [x] Poland market (only active market)
- [x] Shipping zone: Polska (free courier)
- [x] VAT: 23% tax-inclusive pricing enabled
- [x] VAT registration: dummy (PL0000000000 — replace before live)
- [x] Metafield definitions: 35 product metafields created under `lusena.*` namespace

**Products:**
- [~] **Poszewka jedwabna 50×60** — basic info, pricing (269 zł), shipping, SEO, most metafields done. Pending: cost per item, final colors/SKUs, media, feature highlights, collections. Full status: `memory-bank/doc/products/poszewka-jedwabna.md`
- [ ] Scrunchie jedwabny — not started
- [ ] Bonnet jedwabny — not started
- [ ] Opaska na oczy — not started
- [ ] Lokówki jedwabne — not started

## Active migration backlogs

- **PDP:** 4 deferred items — see `memory-bank/doc/features/pdp-migration-backlog.md`
- **Homepage:** Items 1 (bundles) DONE. Item 2 (value anchors) DONE. Remaining: 3 (tier ordering — manual config), 4 (UGC testimonials), 5 (hero animation), 6 (P/S accordion). See `memory-bank/doc/features/homepage-migration-backlog.md`

## UX backlog (evaluate during polish phase)

- **Mobile header icons** — Currently only cart icon visible on mobile. Consider adding search icon and account/login icon to the mobile header for better discoverability.
- **Cross-site "30%" claim cleanup** — MOSTLY DONE. Fixed on: homepage trust bar, quality page (momme, comparison, trust bar), about page trust bar, returns trust bar, PDP quality evidence (old card replaced by guarantee card). One remaining instance: PDP `product.json` feature-1 block title still says "22 momme - o 30% gęstszy niż standard".
- **Bonnet naming** — Apply Polish-first naming ("jedwabny czepek na noc (bonnet)") on all customer-facing pages. Homepage done, other pages pending.
- **Value anchors expansion** — Homepage bestsellers done (`lusena-product-card__per-night`, `show_value_anchor` param). Expand to collection/search pages when ready.

## Cleanup backlog (not urgent — Dawn originals needed by theme editor)

- `sections/main-product.liquid` (100KB) — superseded by `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` — doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- `sections/header.liquid` — superseded by `lusena-header.liquid`
- `sections/footer.liquid` — superseded by `lusena-footer.liquid`
- 50+ other Dawn sections/snippets — remain as fallbacks for theme editor and unused templates
