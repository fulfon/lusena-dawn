# Progress

*Last updated: 2026-02-28*

## LUSENA-styled pages (6 of ~21 total)

- [x] **Homepage** (`index.json`) — 9 sections: hero, trust bar, problem/solution, bestsellers, heritage, testimonials, bundles, FAQ, newsletter
- [x] **Product page** (`product.json`) — 5 sections: main-product, feature highlights, quality evidence, truth table, details
- [x] **Collection page** (`collection.json`) — 1 section: main-collection + product card snippet
- [x] **Quality page** (`page.nasza-jakosc.json`) — 11 sections: hero, trust bar, origin, momme, certificates, fire test, 6a, qc, comparison table, FAQ, final CTA
- [x] **Returns page** (`page.zwroty.json`) — 5 sections: hero, steps, editorial, FAQ, final CTA
- [x] **About page** (`page.o-nas.json`) — 4 sections: hero, trust bar, story, values

## Dawn-default pages (pending LUSENA styling)

- [ ] Cart (`cart.json`)
- [ ] Blog listing (`blog.json`)
- [ ] Article (`article.json`)
- [ ] Search (`search.json`)
- [ ] Collections list (`list-collections.json`)
- [ ] 404 (`404.json`)
- [ ] Password (`password.json`)
- [ ] Generic page (`page.json`)
- [ ] Contact page (`page.contact.json`)
- [ ] Customer: login, register, account, addresses, order, activate, reset password

## Infrastructure completed

- [x] LUSENA spacing system (`assets/lusena-spacing.css`) — tiers, gaps, content-flow
- [x] CSS foundations file (`assets/lusena-foundations.css`) — designer-generated, 7 fixes applied, production-ready
- [x] CSS foundations brief (`docs/css-foundations-brief.md`) — self-contained spec for the designer
- [x] Button system (`snippets/lusena-button-system.liquid`)
- [x] Icon system (`snippets/lusena-icon.liquid`)
- [x] Section gap detector (`snippets/lusena-section-gap-detector.liquid`)
- [x] Header (`sections/lusena-header.liquid`)
- [x] Footer (`sections/lusena-footer.liquid`)
- [x] Product card (`snippets/lusena-product-card.liquid`)
- [x] Breadcrumbs (`snippets/lusena-breadcrumbs.liquid`)
- [x] Memory bank architecture

## CSS foundations migration

The new `lusena-foundations.css` replaces 3 files: `lusena-shop.css` (Tailwind), `lusena-spacing.css`, `lusena-missing-utilities.liquid`. Migration is section-by-section:

- [x] Phase 0: Load foundations alongside existing CSS in `layout/theme.liquid` + fix padding variable names
- [x] Phase 1: Migrate homepage sections (9/9 sections — hero, trust-bar, problem-solution, bestsellers, heritage, testimonials, bundles, faq, newsletter) + 5 visual regression fixes verified via Playwright
- [ ] Phase 2: Migrate other pages (PDP, quality, returns, about, collection)
- [ ] Phase 3: Remove old CSS files (`lusena-shop.css`, `lusena-spacing.css`, `lusena-missing-utilities.liquid`)

## Active migration backlogs

- **PDP:** 4 deferred items — see `memory-bank/doc/features/pdp-migration-backlog.md`
- **Homepage:** 6 deferred items — see `memory-bank/doc/features/homepage-migration-backlog.md`

## Cleanup backlog (not urgent — Dawn originals needed by theme editor)

- `sections/main-product.liquid` (100KB) — superseded by `lusena-main-product.liquid`
- `sections/header.liquid` — superseded by `lusena-header.liquid`
- `sections/footer.liquid` — superseded by `lusena-footer.liquid`
- 50+ other Dawn sections/snippets — remain as fallbacks for theme editor and unused templates
