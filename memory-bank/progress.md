# Progress

*Last updated: 2026-03-29*

## LUSENA-styled pages (14 of ~21 total)

- [x] **Homepage** (`index.json`) — 10 sections: hero, trust bar, benefit bridge (NEW 2026-03-28), bestsellers, testimonials, problem/solution (moved to pos 6), bundles (card grid), heritage, FAQ, final CTA. Full UX audit completed 2026-03-08. Benefit bridge added 2026-03-28 (3 benefit cards, legally checked, persona-validated). P/S copy refreshed. Newsletter removed (footer handles it).
- [x] **Product page** (`product.json`) — 6 sections: main-product, feature highlights (animated icons), quality evidence, truth table, FAQ (shared `lusena-faq`), final CTA (shared `lusena-final-cta`). Full UX audit completed 2026-03-09 (visual rhythm, content rewrite, legal compliance, FAQ consolidation, conversion CTA). Per-product metafield overrides for headline/tagline/per-night. Returns deep-link. PDP buy-box spacing overhauled. Animated icons added 2026-03-15.
- [x] **Collection page** (`collection.json`) — 1 section: main-collection + product card snippet
- [x] **Quality page** (`page.nasza-jakosc.json`) — 10 sections: hero, trust bar, origin, momme, certificates, fire test, qc, comparison table, FAQ, final CTA. 6A section removed (content merged into momme). Spacing audit completed 2026-03-10 (3 off-grid fixes + 1 tier upgrade).
- [x] **Returns page** (`page.zwroty.json`) — 5 sections: hero, steps, editorial, FAQ, final CTA
- [x] **About page** (`page.o-nas.json`) — 5 sections: hero, trust bar, story, values, final CTA
- [x] **Cart page** (`cart.json`) — 2 sections: cart-items (with upsell), cart-footer (totals, shipping bar, CTA, trust row)
- [x] **Search page** (`search.json`) — 1 section: lusena-search (product grid, non-product results, empty state with bestsellers, predictive search, Polish translations)
- [x] **Blog listing** (`blog.json`) — 1 section: lusena-blog (2-col grid, pagination, rich empty state with viewport fill)
- [x] **Article page** (`article.json`) — 2 sections: lusena-article (hero, richtext, share button, LD+JSON) + lusena-newsletter (with secondary shop link)
- [x] **404 page** (`404.json`) — 1 section: lusena-404 (centered error message, bestseller grid, viewport-fill)
- [x] **Generic page** (`page.json`) — 1 section: lusena-main-page (breadcrumbs, title, richtext via `.lusena-richtext`, viewport-fill, compact spacing)
- [x] **Contact page** (`page.contact.json`) — 2 sections: lusena-contact-form (breadcrumbs, heading, LUSENA form system, customer pre-fill, viewport-fill, full-width mobile button) + lusena-newsletter
- [x] **Bundle product page** (`product.bundle.json`) — 6 sections: lusena-main-bundle (progressive disclosure color selector with GPU-only animations, sticky ATC with scroll+highlight, ATC + Buy Now, care accordion, savings display), feature highlights, quality evidence, truth table, FAQ, final CTA. Phase B complete (2026-03-21). Pending: Phase C creative sessions + product media.

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
- [x] Button system standalone CSS (`assets/lusena-button-system.css`) — extracted from snippet {% stylesheet %} to avoid compiled_assets truncation (2026-03-05), primary loading state fix (2026-03-31)
- [x] Header standalone CSS (`assets/lusena-header.css`) — extracted from section {% stylesheet %} (2026-03-05)
- [x] Hero standalone CSS (`assets/lusena-hero.css`) — extracted from section {% stylesheet %} (2026-03-05)
- [x] Footer standalone CSS (`assets/lusena-footer.css`) — extracted from section {% stylesheet %} (2026-03-05)
- [x] Icon system (`snippets/lusena-icon.liquid`)
- [x] Animated icon system (`snippets/lusena-icon-animated.liquid` + `assets/lusena-icon-animations.css`) — 11 animated SVG icons (heart, layers, droplets, wind, shield-check, sparkles, gift, clock, moon, feather, palette) with CSS keyframes, stagger delays, prefers-reduced-motion fallback (2026-03-15, expanded 2026-03-28 with moon/feather/palette)
- [x] Section gap detector (`snippets/lusena-section-gap-detector.liquid`)
- [x] Header (`sections/lusena-header.liquid`) — migrated to foundations
- [x] Footer (`sections/lusena-footer.liquid`) — migrated to foundations (2026-03-04)
- [x] Cart drawer (`snippets/cart-drawer.liquid`) — migrated to BEM + foundations (2026-03-04)
- [x] Sticky ATC (`snippets/lusena-pdp-sticky-atc.liquid`) — CSS moved to `lusena-pdp.css` (2026-03-04)
- [x] Product card (`snippets/lusena-product-card.liquid`)
- [x] Breadcrumbs (`snippets/lusena-breadcrumbs.liquid`)
- [x] Generic final CTA (`sections/lusena-final-cta.liquid`) — reusable across all pages
- [x] Bundles standalone CSS (`assets/lusena-bundles.css`) — bundle card grid styles (loaded per-section) (2026-03-07)
- [x] Bundle PDP standalone CSS (`assets/lusena-bundle-pdp.css`) — bundle buy box styles (loaded in lusena-main-bundle) (2026-03-21)
- [x] Bundle swap JS (`assets/lusena-bundle-swap.js`) — shared `LusenaBundle.swap()` for add bundle + remove individual (2026-03-24)
- [x] Unified upsell card system (`.lusena-upsell-card`) — cross-sell + bundle two-tile layout, gain-framed copy, real product titles/images via `bundle_nudge_map` handles, scrollable positioning, cross-sell bottom-row layout matching bundle pattern. CSS scoped per-surface (drawer: `<style>` tag, cart page: `assets/lusena-cart-page.css`). Desktop cart page: card right-aligned at max-width 48rem. (2026-03-24, polished 2026-03-25)
- [x] Cart upsell UI redesign spec (`docs/superpowers/specs/2026-03-24-cart-upsell-ui-redesign.md`) — research-backed design spec with Thaler/Zeigarnik/Prospect Theory citations (2026-03-24)
- [x] Cart page CSS extraction (`assets/lusena-cart-page.css`) — 625 lines extracted from cart-items, cart-footer, and cart-quantity `{% stylesheet %}` blocks. Resolved compiled_assets truncation (85KB → ~59KB). (2026-03-26, loading dots CSS removed 2026-03-29)
- [x] Search page CSS extraction (`assets/lusena-search.css`) — 156 lines extracted from lusena-search `{% stylesheet %}`. (2026-03-26)
- [x] Cart page AJAX section re-rendering — replaces `window.location.reload()` with Shopify section rendering API for bundle swaps and cross-sell adds. Full re-render: items + footer + empty state toggle. (2026-03-26)
- [x] Cart drawer section promotion — `theme.liquid` changed from `render 'cart-drawer'` to `section 'cart-drawer'`, enabling section rendering API (2026-03-26)
- [x] Bidirectional cart sync — cart page ↔ drawer sync via `PUB_SUB_EVENTS.cartUpdate` pubsub + direct cross-surface refresh (belt-and-suspenders). Drawer re-renders when cart page changes; cart page re-renders when drawer changes. (2026-03-26, direct sync added 2026-03-28)
- [x] Cart merge (#13) — detects both bundle components in cart, shows merge card with two "W koszyku" tiles. Removes both items, adds bundle via `LusenaBundle.swap()`. Pre-filled Simple Bundles color properties. Mapping: poszewka+bonnet → Nocna Rutyna (109 zl), poszewka+maska → Piekny Sen (89 zl). Higher savings wins. (2026-03-28)
- [x] Cart drawer per-item loading state — opacity fade + button disable during qty changes (2026-03-26)
- [x] Cart interaction locking during bundle swap — full-cart lock on cart page (`cart__items--disabled` on `#main-cart-items`) and all-row lock on cart drawer (`lusena-cart-drawer__item--loading` on all `[data-cart-item]`). Prevents concurrent mutations during add+remove sequence. Cross-sell "Dodaj" not locked (independent single-add). (2026-03-29)
- [x] Documentation reorganization — 30+ obsolete docs/ files deleted, key references relocated to memory-bank/doc/ (brand, product refs, templates). Path references updated across all agent instruction files and skills. (2026-03-27)
- [x] Worktree launcher improvements (`scripts/launch-claude-worktree.ps1`) — smart resume (fresh launch for empty worktrees vs `--resume` for active ones) + auto-cleanup (removes worktree+branch on exit when squash-merged to main). (2026-04-02)
- [x] Claude Code hooks (`.claude/hooks/`, 6 scripts) — branch-guard (PreToolUse/Bash, blocks commits on main), guard-dawn-edit (PreToolUse), session-context (SessionStart), post-compact-rules (PostCompact), theme-check-on-edit (PostToolUse), task-quality-gate (TaskCompleted). Configured in `.claude/settings.json`. (2026-03-28)
- [x] Claude Code rules (`.claude/rules/`, 8 files) — animations, bundle-system, cart-system, css-and-assets, css-cascade, no-inline-scripts, product-metafields, section-catalog. Auto-load by file path patterns. (2026-03-28, no-inline-scripts added 2026-03-29)
- [x] Icon semantic system — defined in `product-setup-checklist.md`. 8 variable icons (heart, wind, droplets, sparkles, moon, clock, feather, palette) each with one semantic meaning. (2026-03-28)
- [x] Card 5 creative sessions (all 8 products) — freed from universal OEKO-TEX, each product has unique product-specific angle. Full creative workflow (copywriter + legal + validation) for each. Universal cards reduced from 4 to 3 (positions 2/4/6). (2026-03-28)
- [x] Quality evidence accordion rewrite — `max-height`/opacity → explicit `height` transitions, `data-state` attribute, `prefers-reduced-motion` support. (2026-03-28)
- [x] Homepage benefit bridge section — redesigned 2026-03-29: kicker ("Jedwab morwowy 22 momme"), featured card modifier, accent bar, transition text, heading "Co zobaczysz rano?", standalone CSS `lusena-benefit-bridge.css`. Original added 2026-03-28.
- [x] `lusena-link-arrow` CSS component — CSS-only chevron via SVG mask in `lusena-foundations.css`. Replaces all hardcoded `→` arrows sitewide (6 sections/snippets + 4 templates). (2026-03-29)
- [x] Bundle options initial state — first step open, others collapsed with pending chips. (2026-03-29)
- [x] Cart cross-sell loading refactor — custom dots → standard `loading__spinner` pattern. (2026-03-29)
- [x] Token compliance rule in `.claude/rules/css-and-assets.md` — colors, typography, icons, spacing, transitions, radius, Dawn traps. (2026-03-29)
- [x] Section design loop skill (`.claude/skills/lusena-section-design-loop/`) — autonomous design iteration with 5-agent review panel. (2026-03-29)
- [x] Migration lessons #55-61 — benefit bridge redesign lessons: color-mix, type classes, icon classes, div:empty, reviewer write access, forward-reference, mobile card merging. (2026-03-29)
- [x] Reusable page audit skill (`.claude/skills/lusena-page-audit/`) — standardized UX audit checklist (2026-03-08)
- [x] Customer validation skill (`.claude/skills/lusena-customer-validation/`) — 4-persona copy evaluation (2026-03-14, expanded 2026-03-15)
- [x] Legal check skill (`.claude/skills/lusena-legal-check/`) — EU/UOKiK compliance check (2026-03-14)
- [x] Spacing audit skill (`.claude/skills/lusena-spacing-audit/`) — automated spacing measurement + validation (2026-03-10)
- [x] Pre-commit sync skill (`.claude/skills/lusena-pre-commit-sync/`) — memory bank documentation sync before commits (2026-03-15)
- [x] New section scaffolding skill (`.claude/skills/lusena-new-section/`) — boilerplate + spacing tier + CSS decision + schema (2026-03-28)
- [x] Product copy session skill (`.claude/skills/lusena-product-copy-session/`) — orchestrates full creative workflow from research through finalization (2026-03-28)
- [x] Product metafields reference (`memory-bank/doc/products/product-metafields-reference.md`) — field-by-field PDP mapping + creative process (2026-03-14)
- [x] Product setup checklist (`memory-bank/doc/products/product-setup-checklist.md`) — metafield definitions + example values (2026-03-14)
- [x] Product catalog docs (`memory-bank/doc/products/`) — per-product admin data tracking (2026-03-14)
- [x] Product CSV import/export tooling (`memory-bank/doc/products/imports/`, `exports/`) — Shopify CSV import files + generator script (2026-03-15)
- [x] Bundle strategy (`memory-bank/doc/bundle-strategy.md`) — research-backed bundle architecture, economics, decision triggers (2026-03-15)
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

**Color strategy (completed 2026-03-20):**
- [x] **Research-backed color palette finalized** — Black + Dusty Rose + Champagne unified capsule. Full doc: `memory-bank/doc/color-strategy.md`
- [x] **Rename Shopify variants** — placeholder names renamed to Czarny/Brudny róż/Szampan (done 2026-03-20)
- [x] **Update Simple Bundles option labels** — Polish color names set (done 2026-03-20, Nocna Rutyna fully updated; Piękny Sen + Scrunchie Trio still have English placeholder names in metafield — will auto-render correctly once updated in Simple Bundles admin)

**Products:**
- [~] **Poszewka jedwabna 50×60** — basic info, pricing (269 zł), shipping, SEO, most metafields done. Colors FINALIZED: A-Czarny (40) + B-Brudny róż (40) + C-Szampan (40). Pending: cost per item, rename Shopify variants, media, feature highlights, collections. Full status: `memory-bank/doc/products/poszewka-jedwabna.md`
- [x] **Scrunchie jedwabny** — Copy finalized (2026-03-14). Colors FINALIZED: A-Czarny (50) + B-Brudny róż (50) + C-Szampan (50). Full status: `memory-bank/doc/products/silk-scrunchie.md`
- [x] **Bonnet jedwabny (czepek do spania)** — Copy finalized (2026-03-14). Price: 239 zł. Colors FINALIZED: A-Czarny (30) + B-Brudny róż (30). Full status: `memory-bank/doc/products/silk-bonnet.md`
- [x] **Jedwabna maska 3D do spania** — Copy finalized (2026-03-14). Price: 169 zł. Color FINALIZED: A-Czarny (40). Full status: `memory-bank/doc/products/jedwabna-maska-3d.md`
- [x] **Heatless curlers (Jedwabny wałek do loków)** — Copy finalized (2026-03-15). Price: 219 zł. Color FINALIZED: B-Brudny róż (50). Full status: `memory-bank/doc/products/heatless-curlers.md`

## Bundle Strategy & Implementation

Full strategy: `memory-bank/doc/bundle-strategy.md`
Full implementation tracker: `memory-bank/doc/bundle-implementation.md`

**Phase A: Shopify admin setup (COMPLETE 2026-03-19):**
- [x] Bundle architecture defined (research-backed, brandbook partially superseded)
- [x] App selected: Simple Bundles & Kits (Infinite Options) — evaluated 10+ apps
- [x] All 5 individual products in Shopify with color variants
- [x] 3 bundle products created + configured in Simple Bundles
- [x] Add-to-cart verified for all 3 bundles via Playwright

**Phase B: Custom theme UI (COMPLETE):**
- [x] M1: Simple Bundles metafield research — `variant_options` documented, ATC format understood, backend confirmed (2026-03-20)
- [x] M2: Visual page — template + section + snippets + CSS. Spacing audit passed. Below-fold sections with bundle content. (2026-03-21)
- [x] M3: Full interactivity — progressive disclosure with GPU-only animations, swatch selection via click events, ATC + Buy Now, cart drawer + cart page showing all selected colors. Care accordion. Step progress counter. Pending placeholder chips. Independent chip re-editing. Scrunchie Trio duplicate key fix. (2026-03-21)
- [x] M4: Full test matrix passed (all 3 bundles × all flows). Sticky ATC (mobile + desktop) with two-state behavior: incomplete → scroll to selector + swatch breathe highlight; complete → add to cart. Dynamic scroll detection via rAF polling. All buttons never disabled. Single-option steps require customer click. (2026-03-21)
- [x] M4: Full test matrix passed — all 3 bundles × all flows, sticky ATC mobile+desktop (2026-03-21)

**Phase C: Content & polish (COMPLETE):**
- [x] **Nocna Rutyna** creative session — COMPLETE (2026-03-22). Product doc: `memory-bank/doc/products/nocna-rutyna.md`
- [x] **Piękny Sen** creative session — COMPLETE (2026-03-22). Product doc: `memory-bank/doc/products/piekny-sen.md`
- [x] **Scrunchie Trio** creative session — COMPLETE (2026-03-22). Product doc: `memory-bank/doc/products/scrunchie-trio.md`
- [x] Fill bundle metafields in Shopify admin — CSV imported + upsell metafields set manually (2026-03-24)
- [ ] Homepage bundles section — wire up real products
- [ ] Bundle product media (when physical products arrive)

**Phase 2A: Bundle upgrade upsell (COMPLETE 2026-03-24):**
- [x] Cart upsell cleanup — removed DEV-ONLY hardcoded fallback (snowboard + 'Bezowy')
- [x] Color-matched variant selection — trigger color auto-matched to upsell variant, highest-inventory fallback
- [x] Smart suppress — 2+ distinct items only blocks non-bundle upsells, bundle nudges pass through
- [x] Bundle nudge card — `snippets/lusena-bundle-nudge.liquid` with specific added product name, pricing comparison, incremental cost button
- [x] Shared swap JS — `assets/lusena-bundle-swap.js` (`LusenaBundle.swap()`) with FormData sections for re-render
- [x] Cart properties — auto-matched colors via `simple_bundles.variant_options`, step numbering for multi-packs, multi-pack color distribution
- [x] Bundle detection — uses `bundle_original_price != blank` (separates nudge from suppress)
- [x] All 3 bundles tested: Nocna Rutyna, Piekny Sen, Scrunchie Trio — all directions working
- [x] Upsell metafields configured: role, message (via CSV), primary/secondary (manual), bundle_nudge_map (JSON)

**Phase 2A testing (PASSED 2026-03-28):**
- [x] End-to-end manual test matrix — bundle nudge cards (4 triggers), regular cross-sell (walek), all 4 bundle swaps, smart suppress logic, cart page AJAX re-rendering, bidirectional cart sync

**Phase 2A remaining:**
- [x] #13 Cart merge — DONE (2026-03-28). Detects both bundle components in cart, shows merge card with "W koszyku" tiles. Removes both + adds bundle via `LusenaBundle.swap()`. Mapping: poszewka+bonnet → Nocna Rutyna (109 zl), poszewka+maska → Piekny Sen (89 zl). Higher savings wins.
- [~] #12 PDP bundle detection banner — ABANDONED (2026-03-28). Fully built and tested but doesn't fit the PDP buy-box flow (too dense). Reverted. Decision: use #13 cart merge instead.

**Phase D: Cross-sell (COMPLETE):**
- [x] PDP cross-sell checkbox — all individual PDPs + bundle PDPs (2026-03-29). Scrunchie at 39 zl via BXGY. UI: white card with teal accent, compact row, "Taniej w komplecie" hint, color-matched image. Bundle: progressive disclosure reveal after all colors picked, LUSENA signature slide-in animation.
- [x] Scrunchie PDP education (2026-03-29) — server-side price swap (~~59 zl~~ 39 zl) when qualifying product is in cart. Dynamic Polish hint ("Taniej z poszewka jedwabna w koszyku"). Live cart sync via PubSub. No flash (Liquid renders correct state on first paint). Sticky ATC synced via MutationObserver.

**Phase 2 (data-gated, after 8-12 weeks):**
- [ ] Kompletna Nocna Rutyna (poszewka + bonnet + maska = 499 zł)
- [ ] Duo dla Pary (2× poszewka = 429 zł, seasonal)

## Active migration backlogs

- **PDP:** 4 deferred items — see `memory-bank/doc/features/pdp-migration-backlog.md`
- **Homepage:** Items 1 (bundles) DONE. Item 2 (value anchors) DONE. Remaining: 3 (tier ordering — manual config), 4 (UGC testimonials), 5 (hero animation), 6 (P/S accordion). See `memory-bank/doc/features/homepage-migration-backlog.md`

## UX backlog (evaluate during polish phase)

- **Mobile header icons** — Currently only cart icon visible on mobile. Consider adding search icon and account/login icon to the mobile header for better discoverability.
- **Cross-site percentage claim cleanup** — COMPLETE (2026-03-14). All percentage-based momme claims (30%, 15%) removed site-wide, from brandbook, and from all docs. Replaced with qualitative "gęstszy i trwalszy niż standard". Rule added to brandbook: never use percentages for momme without own test documentation.
- **Bonnet naming** — Apply Polish-first naming ("jedwabny czepek na noc (bonnet)") on all customer-facing pages. Homepage done, other pages pending.
- **Value anchors expansion** — Homepage bestsellers done (`lusena-product-card__per-night`, `show_value_anchor` param). Expand to collection/search pages when ready.

## Cleanup backlog (not urgent — Dawn originals needed by theme editor)

- `sections/main-product.liquid` (100KB) — superseded by `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` — doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- `sections/header.liquid` — superseded by `lusena-header.liquid`
- `sections/footer.liquid` — superseded by `lusena-footer.liquid`
- 50+ other Dawn sections/snippets — remain as fallbacks for theme editor and unused templates
