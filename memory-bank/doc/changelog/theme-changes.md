# LUSENA × Dawn — Theme change log (tracked in Git)

## What is this codebase?

This repository started from the official Shopify **Dawn** theme and is being adapted into a **LUSENA**-ready storefront (PL-first, premium feel, proof-first messaging, WCAG-minded UI).

Source of truth for brand direction: `docs/LUSENA_BrandBook_v2.md` (local path: `C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-dawn\docs\LUSENA_BrandBook_v2.md`).

## How to use this file

- For each “bigger” change set, create a Git commit and add an entry here.
- Entries should be **semi-detailed**: what changed, why, and where (key files/settings).
- Always reference the commit (hash + message) so it’s easy to diff/revert.
- Keep only the **latest 8** change entries detailed.
- Keep **ALL commit history** in a rolling summary list (dateTime + hash + subject), sorted descending by commit date/time.

---

**Note:** The newest changelog entry might show `(current)` instead of a hash when we keep everything in a single commit (a commit can’t reliably include its own hash inside its contents). Entries under **Legacy commits** are kept for archival purposes and might reference commits that are no longer reachable from the current Git history (hashes and timestamps might be unavailable).

## Recent commits (detailed, last 8)

### (current) — Bundle creative sessions, cart upsell UI redesign, product docs overhaul

**Goal:** Complete all 3 bundle creative sessions (Phase C), redesign cart upsell UI for both drawer and cart page, overhaul product metafields reference with orchestrator+copywriter architecture, modernize product CSV tooling, polish bundle PDP CSS.

**What changed**
- **Bundle Phase C complete:** All 3 bundle creative sessions finished (Nocna Rutyna, Piekny Sen, Scrunchie Trio). Each went through orchestrator + Polish copywriter flow, legal check, 2-3 customer validation runs. New product docs created. Metafields filled via CSV import + manual upsell metafield setup.
- **Cart upsell UI redesign (5 commits 228fb6d-47ebbb8 + uncommitted polish):** Unified `.lusena-upsell-card` system for cart drawer and cart page. Two card types: bundle nudge (two-tile with gain-framed headlines, real product titles/images) and cross-sell (bottom-row layout). `bundle_nudge_map` restructured from flat strings to objects (`{label, handle, tile_label?}`). Real product data resolved via `all_products[handle]`. Shared `assets/lusena-bundle-swap.js` for add+remove cart API. Image placeholder fix for Dawn's `div:empty { display: none }`. Upsell moved inside scrollable body (no fixed positioning). Compact layout for small screens.
- **Product metafields reference overhaul:** Creative workflow redesigned: orchestrator+copywriter architecture (lesson from Piekny Sen session). Added bundle addendum, info architecture guard, exclusion list, buybox-level exclusion, tagline/benefits rendering context (desktop vs mobile alternative views), review presentation format. Tagline and benefit field specs rewritten.
- **Product CSV tooling:** Old per-product `generate_import_csv.py` + 5 individual CSVs deleted. Replaced by unified `generate_import_from_export.py` that patches copy/metafield columns from MD product files. CLAUDE.md updated with sync workflow.
- **Bundle PDP CSS polish:** Next-step pending indicators (`is-next.is-pending` with teal dot pulse + "nastepny" label), swatch breathe animation rework (teal glow via box-shadow instead of opacity), mobile flow reorder (benefits before care), reduced motion improvements.
- **Customer validation skill:** Added page context (buybox UI elements, below-fold content), repetition detection question #10 for all 4 personas, repetition report section in aggregation template.
- **Product setup checklist:** Added section D (upsell configuration) with per-product upsell metafields and bundle-only metafields including `bundle_nudge_map` JSON schema.

**Key files**
- `snippets/cart-drawer.liquid`, `sections/lusena-cart-items.liquid` — unified upsell card HTML + CSS
- `assets/lusena-bundle-swap.js` (NEW) — shared bundle swap cart API
- `assets/lusena-bundle-pdp.css` — next-step indicators, breathe animation, mobile ordering
- `docs/product-metafields-reference.md` — creative workflow overhaul + bundle addendum
- `docs/product-setup-checklist.md` — upsell metafield definitions
- `memory-bank/doc/products/nocna-rutyna.md`, `piekny-sen.md`, `scrunchie-trio.md` (NEW) — bundle product docs
- `.claude/skills/lusena-customer-validation/skill.md` — page context + repetition question
- `memory-bank/doc/products/imports/generate_import_from_export.py` (NEW) — unified CSV import script
- `snippets/lusena-bundle-options.liquid`, `snippets/lusena-bundle-scripts.liquid` — minor fixes
- `templates/product.bundle.json`, `templates/product.json` — template updates

### ff53459 — Complete bundle PDP template (Phase B M1-M4), color strategy, section polish

**Goal:** Build the full bundle product page from research through production-ready: metafield research, visual scaffolding, progressive disclosure color selector, ATC/Buy Now integration with Simple Bundles, sticky ATC bar, cart integration, and all polish passes. Also: finalize color strategy, complete Phase A admin setup, polish existing sections.

**What changed**
- **Bundle Phase B complete (M1-M4):** Full `product.bundle.json` template with 6 sections and 8 new snippets. Progressive disclosure color selector with GPU-only animations (transform+opacity, 150ms stagger). Step counter "WYBIERZ KOLORY (1 z 3)". Pending placeholder chips. Independent chip re-editing. Two-state buttons (never disabled: incomplete → scroll+highlight swatches, complete → add to cart). Sticky ATC (mobile+desktop) with dynamic scroll detection via rAF `onScrollSettled()`. Swatch breathe highlight animation. Care accordion. Dimension stripping ("50×60" removed from labels). Clean property keys with step numbers (fixes Scrunchie Trio duplicate key bug). All 3 bundles tested via Playwright automated test matrix.
- **Cart integration:** `cart-drawer.liquid` — line item properties display (color selections) with `{% stylesheet %}` block for global CSS. `lusena-cart-items.liquid` — properties condition fix (`!= empty`), image centering. Underscore-prefixed properties (`_bundle_selection`) hidden from customer.
- **Bundle M1 metafield research:** `simple_bundles.variant_options` documented, ATC `properties[...]` format, `_bundle_selection` concatenation. `compare_at_price` clearing by Price Sync solved with `lusena.bundle_original_price` metafield.
- **Color strategy finalized:** 3-color unified capsule (Czarny + Brudny róż + Szampan). Full doc: `memory-bank/doc/color-strategy.md`. Shopify admin variants renamed.
- **Section polish:** Proof chips, quality evidence, heritage, science, clock animation, PDP title sizing, cart drawer scrollbar guard, icon color rule, bonnet naming, metafield checks.
- **Docs:** Bundle implementation tracker (M1-M4 complete). Product metafields reference (bundle metafields). Dev store access with `?view=bundle` URLs. 429 rate limit documentation. Swatch color sync documentation.

**Key files**
- `templates/product.bundle.json`, `sections/lusena-main-bundle.liquid`
- `snippets/lusena-bundle-summary.liquid`, `lusena-bundle-contents.liquid`, `lusena-bundle-options.liquid`, `lusena-bundle-atc.liquid`, `lusena-bundle-care.liquid`, `lusena-bundle-scripts.liquid`, `lusena-bundle-sticky-atc.liquid`
- `assets/lusena-bundle-pdp.css`
- `snippets/cart-drawer.liquid`, `sections/lusena-cart-items.liquid`
- `memory-bank/doc/bundle-implementation.md`, `memory-bank/doc/color-strategy.md`
- `docs/product-metafields-reference.md`

### c800179 — Product copy sessions, bundle strategy, animated icons, percentage claim cleanup, pre-commit sync

**Goal:** Finalize all 5 individual product copy sessions (creative workflow: research → draft → legal check → customer validation → finalize), define research-backed bundle architecture, build animated icon system for PDP feature highlights, clean up percentage-based momme claims site-wide, replace theme-changelog skill with pre-commit-sync.

**What changed**
- **5 product copy sessions complete:** silk-scrunchie, silk-bonnet (title research: "czepek" > "bonnet", 239 zł), jedwabna-maska-3d (169 zł, highest validation scores), heatless-curlers (material correction: 22 momme 6A confirmed, title: "Jedwabny wałek do loków"), poszewka-jedwabna updates. Each went through legal check (EU/UOKiK) + 1-2 customer validation runs with 4 Polish personas.
- **Bundle strategy:** Research-backed architecture in `memory-bank/doc/bundle-strategy.md`. 3 Phase 1 bundles (Nocna Rutyna 399 zł, Piękny Sen 349 zł, Scrunchie Trio 139 zł). PDP cross-sell checkbox replaces Starter Kit (Presenter's Paradox). Free shipping threshold 299 zł. Original brandbook plan (§ 5.8) partially superseded.
- **Animated icon system:** New `snippets/lusena-icon-animated.liquid` (8 icons with CSS animation classes) + `assets/lusena-icon-animations.css` (keyframes, stagger delays, prefers-reduced-motion). `lusena-pdp-feature-highlights.liquid` loads animation CSS and renders animated icons. Animation specs documented per product.
- **Percentage claim cleanup:** All "30%", "15%" momme claims removed from brandbook, sections, templates, memory bank. Replaced with "gęstszy i trwalszy niż standard". Brandbook rule added.
- **Product documentation:** 4 new product docs, expanded metafields reference, setup checklist, CSV import/export tooling.
- **Skills:** `lusena-theme-changelog` deleted → replaced by `lusena-pre-commit-sync`. `lusena-customer-validation` expanded.
- **Minor section fixes:** ~20 Liquid sections touched (percentage claim cleanup, small CSS/content adjustments).

**Key files**
- `snippets/lusena-icon-animated.liquid`, `assets/lusena-icon-animations.css`
- `sections/lusena-pdp-feature-highlights.liquid`, `sections/lusena-pdp-quality-evidence.liquid`
- `memory-bank/doc/bundle-strategy.md`
- `memory-bank/doc/products/silk-bonnet.md`, `silk-scrunchie.md`, `jedwabna-maska-3d.md`, `heatless-curlers.md`
- `docs/product-metafields-reference.md`, `docs/product-setup-checklist.md`
- `docs/LUSENA_BrandBook_v2.md`
- `.claude/skills/lusena-pre-commit-sync/`, `.claude/skills/lusena-customer-validation/`

### 1be3e57 — Footer redesign, PDP polish, quality/FAQ/trust-bar refinements, spacing audit, product setup docs

**Goal:** Complete footer redesign with social/payment/newsletter UX, polish PDP buy-box spacing and content, refine quality page sections, enhance FAQ section with bg_style/anchor/deep-link features, standardize trust-bar copy and em-dashes across all pages, run quality page spacing audit, set up product catalog documentation and creative workflow skills.

**What changed**
- **Footer:** Social media links (Instagram, Facebook) via lusena-icon, payment icons bar (Visa, BLIK, PayPo, Przelewy24), legal links row, newsletter UX rebuild (arrow submit, success/error states, hCaptcha-compatible), schema renamed from "draft" to "LUSENA Footer", all Polish defaults.
- **PDP buy-box:** Significant CSS spacing tightening (mobile + desktop), social proof reordered to slot 2, benefits list padding fix, gallery/lightbox breakpoint aligned to 768px, guarantee restructured (p not div).
- **PDP content:** Truth table 2 new rows (hypoallergenic, durability) + lusena-icon, feature highlights bg_style + optional heading, per-product metafield overrides (headline, tagline, per-night toggle), conditional specs rendering, returns deep-link fix, final CTA added to template.
- **Quality page:** 6A section removed (content merged into momme 4th benefit), origin CTA links, QC bg + icon system (emoji → lusena-icon with fallback), comparison table CTA + corrected values (15% not 30%), hero CTA to OEKO-TEX verification, OEKO-TEX diacritics fix.
- **Quality page spacing audit (2026-03-10):** 3 off-grid CSS fixes in `lusena-foundations.css` (truth-table mobile cards: grid gap 12→16px, card-line margin 12→16px, card-label margin 5→8px), 1 tier upgrade in `lusena-quality-certificates.liquid` (standard→spacious).
- **FAQ section:** bg_style setting, anchor_id for deep-linking, is_returns_target per-block, JS rewritten (var/function for compatibility), 4 blocks removed from PDP FAQ, expanded answers.
- **Cross-site:** Trust bar canonical copy (sentence case), em-dash → hyphen standardization in all template JSON, 4 new icons (instagram, facebook, circle-check, circle-x).
- **About page:** Hero bg set to brand, Polish-first defaults, values section kicker/heading added, final CTA with secondary link.
- **Returns page:** Sentence case, InPost mention, simpler CTA.
- **Documentation:** Product metafields reference, product setup checklist, product catalog docs (`memory-bank/doc/products/`), spacing audit tooling (`docs/spacing-audit/`).
- **New skills:** lusena-customer-validation (4-persona copy evaluation), lusena-legal-check (EU/UOKiK compliance), lusena-spacing-audit (automated spacing measurement).

**Key files**
- `sections/lusena-footer.liquid`, `assets/lusena-footer.css`
- `snippets/lusena-pdp-buybox-panels.liquid`, `snippets/lusena-pdp-summary.liquid`, `snippets/lusena-pdp-sticky-atc.liquid`
- `assets/lusena-pdp.css`, `assets/lusena-foundations.css`
- `sections/lusena-faq.liquid`, `sections/lusena-pdp-truth-table.liquid`, `sections/lusena-pdp-feature-highlights.liquid`
- `sections/lusena-quality-qc.liquid`, `sections/lusena-quality-origin.liquid`, `sections/lusena-quality-momme.liquid`
- `snippets/lusena-icon.liquid`
- `templates/product.json`, `templates/page.nasza-jakosc.json`, `templates/page.o-nas.json`, `templates/page.zwroty.json`, `templates/index.json`

### 57beec8 — feat(lusena): complete homepage UX audit — visual rhythm, value anchors, bundle fixes

**Goal:** Two-session homepage audit covering section order, copy, visual rhythm, spacing, value anchors, and conversion flow.

**What changed**
- Background rhythm redesign: fixed same-color collisions, redesigned 9-section bg sequence.
- Bundle card fixes: removed placeholder prices, fixed button centering, equalized card heights.
- Value anchor on bestseller cards: per-night price computation via `show_value_anchor` param.
- Newsletter removed from homepage (footer handles it), replaced by `lusena-final-cta`.
- Reusable page-audit skill created.

**Key files**
- `templates/index.json`, `sections/lusena-bundles.liquid`, `assets/lusena-bundles.css`
- `snippets/lusena-product-card.liquid`, `sections/lusena-bestsellers.liquid`

### 29fc700 — chore(lusena): polish blog/article, trust-bar animations, breadcrumb fixes + repo cleanup

### cbeba1a — feat(lusena): migrate system pages (Batch 2) + polish blog/article (Batch 6)

### 160e283 — feat(lusena): migrate blog + article pages (Batch 6)

### a874dde — feat(lusena): migrate search page (Batch 5) + cart page (Batch 1) + Batch 4 cleanup

### 652d4ba — refactor(lusena): complete CSS foundations migration — Phase 2 + Phase 3

### 6e02637 — refactor(lusena): complete Phase 1 CSS migration — homepage sections + bug fixes

### 41e8ccc — refactor(lusena): restructure docs into memory bank + compact CLAUDE.md

**Goal:** Reduce per-session context overhead (~19k tokens freed) by extracting generic reference material from CLAUDE.md into layered documentation, and create a persistent memory bank for cross-session project continuity.

**What changed**
- Rewrote CLAUDE.md from 1,541 lines (~52KB) to 105 lines (~5KB).
- Created `memory-bank/` with 18 files.
- Extracted 4 reference docs into `docs/reference/`.
- Updated 3 skills with new paths; mirrored to .agent/ and .codex/.
- Added git pre-commit hook to auto-sync CLAUDE.md → AGENTS.md + copilot-instructions.md.

### 7087015 — feat(lusena): migrate quality/about/returns pages and extend PDP v2 proof blocks

**Goal:** Continue the v2 brandbook migration on high-impact content pages, add missing PDP proof modules, and codify migration workflows for repeatable implementation.

**What changed**
- Added new quality-page sections (`lusena-quality-6a`, `lusena-quality-comparison-table`, `lusena-quality-final-cta`) and rewired the quality page template to support a fuller proof-first narrative flow.
- Expanded PDP v2 content architecture with a new `lusena-pdp-truth-table` section, a larger detail schema in `lusena-pdp-details`, and updated buybox/icon/utility snippets used by PDP evidence and panel rendering.
- Refined About and Returns page composition by updating section templates and supporting sections (`lusena-about-story`, `lusena-about-values`, `lusena-page-returns`, `lusena-returns-faq`) for better v2 parity.
- Updated brandbook implementation docs and added migration artifacts/skills (`docs/PDP_V2_MIGRATION_BACKLOG.md`, `lusena-spacing`, `lusena-v2-page-migration`) across `.agent` and `.codex`.

**Key files**
- `templates/page.nasza-jakosc.json`
- `sections/lusena-quality-6a.liquid`
- `sections/lusena-quality-comparison-table.liquid`
- `sections/lusena-quality-final-cta.liquid`
- `sections/lusena-pdp-truth-table.liquid`
- `sections/lusena-pdp-details.liquid`
- `templates/product.json`
- `templates/page.o-nas.json`
- `templates/page.zwroty.json`
- `docs/PDP_V2_MIGRATION_BACKLOG.md`

### 9def2eb — feat(lusena): migrate homepage v2 copy and add newsletter capture

**Goal:** Align homepage messaging to the v2 brandbook in Polish, redesign heritage proof into a 3-tile evidence layout, and add a native newsletter capture section while documenting deferred migration scope.

**What changed**
- Reworked homepage template content to Polish-first v2 copy across hero, trust bar, problem/solution, testimonials, bundles, FAQ, and CTAs; increased bestseller count and wired updated heritage block configuration.
- Redesigned `lusena-heritage` from intro-body format into a centered heading + 3-tile evidence grid with image-or-icon fallback blocks, refreshed defaults/presets, and preserved scroll-trigger cascade behavior.
- Added new `lusena-newsletter` section with Shopify customer form integration (`contact[tags]=newsletter`), success/error states, responsive input/button layout, spacing overrides, and homepage template placement after FAQ.
- Added migration process documentation: a homepage v2 deferred backlog and a reusable `lusena-v2-page-migration` skill to standardize future page migrations and validation flow.
- Updated `docs/theme-brandbook-uiux.md` to reflect the new homepage section inventory and ordering with newsletter included.

**Key files**
- `templates/index.json`
- `sections/lusena-heritage.liquid`
- `sections/lusena-newsletter.liquid`
- `docs/theme-brandbook-uiux.md`
- `docs/HOMEPAGE_V2_MIGRATION_BACKLOG.md`
- `.claude/skills/lusena-v2-page-migration/SKILL.md`

### 567ef16 — feat(lusena): refine spacing system and refresh PDP + brandbook docs

**Goal:** Remove residual section-gap drift from Dawn defaults, tighten LUSENA spacing utility usage, and align PDP + brand documentation updates in one cohesive pass.

**What changed**
- Added spacing-system hardening in `assets/lusena-spacing.css`: neutralized Dawn `.section + .section` margin for LUSENA tier sections and introduced `lusena-gap-cta-top` for conditionally visible CTA elements.
- Updated section/snippet spacing usage to remove phantom gaps and keep CTA separation attached to visible elements (`lusena-bestsellers`, `lusena-main-collection`, `lusena-footer`, `lusena-returns-editorial`).
- Polished PDP support sections: updated `lusena-pdp-feature-highlights` card/grid behavior and switched `lusena-pdp-quality-evidence` to standard tier spacing with cleaner heading/toggle structure.
- Added first-item spacing fixes for FAQ and PDP accordion rows to remove extra top padding in stacked FAQ/accordion groups.
- Normalized PDP snippet markup structure (`media`, `summary`, `ATC`, `buybox panels`, `variant picker`, `cross-sell`, `accordions`) for consistent animation hooks and cleaner maintainability.
- Migrated brand docs from `docs/LUSENA_BrandBook_v1.md` to `docs/LUSENA_BrandBook_v2.md` and added a dedicated v1->v2 migration changelog document.
- Updated `.claude` spacing skill guidance with the new CTA-top utility and Dawn margin-neutralization debugging notes.

**Key files**
- `assets/lusena-spacing.css`
- `sections/lusena-bestsellers.liquid`
- `sections/lusena-main-collection.liquid`
- `sections/lusena-footer.liquid`
- `sections/lusena-pdp-feature-highlights.liquid`
- `sections/lusena-pdp-quality-evidence.liquid`
- `sections/lusena-faq.liquid`
- `sections/lusena-returns-faq.liquid`
- `snippets/lusena-pdp-media.liquid`
- `snippets/lusena-pdp-summary.liquid`
- `snippets/lusena-pdp-atc.liquid`
- `snippets/lusena-pdp-variant-picker.liquid`
- `docs/LUSENA_BrandBook_v2.md`
- `docs/lusena_brandbook_update_changelog_v1_to_v2.md`
- `.claude/skills/lusena-spacing/SKILL.md`

### 0a6c1ab — feat(lusena): standardize global section spacing system

**Goal:** Centralize vertical spacing across LUSENA sections with a tier/token system, reduce per-section padding drift, and make same-background section transitions more consistent.

**What changed**
- Added a global spacing foundation snippet with spacing tokens, section tier classes (`compact`, `standard`, `hero`, `full-bleed`), same-bg gap behavior, and semantic intra-section gap utilities (`lusena-gap-*`).
- Added section adjacency detection script that compares computed background colors of neighboring section surfaces and applies `lusena-section-gap-same` / `lusena-section-gap-different`.
- Wired both snippets globally in `layout/theme.liquid`.
- Migrated LUSENA section roots from section-local padding CSS to tier classes with optional schema overrides (`0 = use global default`) and aligned override variable naming.
- Updated brandbook and implementation docs to reflect the new spacing system and marked the spacing standardization plan as implemented.

**Key files**
- `layout/theme.liquid`
- `snippets/lusena-spacing-system.liquid`
- `snippets/lusena-section-gap-detector.liquid`
- `sections/lusena-trust-bar.liquid`
- `sections/lusena-problem-solution.liquid`
- `sections/lusena-bestsellers.liquid`
- `sections/lusena-heritage.liquid`
- `sections/lusena-testimonials.liquid`
- `sections/lusena-bundles.liquid`
- `sections/lusena-faq.liquid`
- `sections/lusena-main-product.liquid`
- `sections/lusena-main-collection.liquid`
- `sections/lusena-pdp-feature-highlights.liquid`
- `sections/lusena-pdp-quality-evidence.liquid`
- `sections/lusena-pdp-details.liquid`
- `sections/lusena-about-hero.liquid`
- `sections/lusena-about-story.liquid`
- `sections/lusena-about-values.liquid`
- `sections/lusena-quality-hero.liquid`
- `sections/lusena-quality-momme.liquid`
- `sections/lusena-quality-fire-test.liquid`
- `sections/lusena-quality-origin.liquid`
- `sections/lusena-quality-qc.liquid`
- `sections/lusena-quality-certificates.liquid`
- `sections/lusena-returns-hero.liquid`
- `sections/lusena-returns-steps.liquid`
- `sections/lusena-returns-editorial.liquid`
- `sections/lusena-returns-faq.liquid`
- `sections/lusena-returns-final-cta.liquid`
- `sections/lusena-science.liquid`
- `sections/lusena-comparison.liquid`
- `docs/theme-brandbook-uiux.md`
- `docs/SPACING_STANDARDIZATION_PLAN.md`
- `AGENTS.md`
- `copilot-instructions.md`

### a2551d3 — feat(lusena): optimize accordion UX and sync theme docs

**Goal:** Improve touch/animation behavior consistency for FAQ-style accordions and apply draft-parity polish updates across key LUSENA surfaces, while aligning repo guidance/skills docs with the current theme architecture.

**What changed**
- Reworked accordion runtime logic in LUSENA FAQ and PDP contexts to use explicit `data-state` ownership with height-transition cleanup guards, reducing rapid-tap race conditions and honoring reduced-motion behavior with deterministic open/close states.
- Updated accordion/panel styling for smoother touch interaction (tap-highlight removal, tuned transition curves, `contain` usage) and synchronized chevron/opacity motion behavior.
- Applied parity polish across customer-facing UI fragments: mobile header menu bottom border/padding correction, about-values hover card behavior scoping, breadcrumb overflow/truncation handling, and cart drawer "Kontynuuj zakupy" sizing normalization.
- Simplified the BLIK payment SVG asset payload and removed obsolete `docs/UI_UX_Instructions.md` in favor of the newer brandbook-driven guidance.
- Updated agent/assistant workflow docs and added the new `lusena-draftshop-fragment-parity` skill definitions for `.agent` and `.claude`.

**Key files**
- `sections/lusena-faq.liquid`
- `sections/lusena-returns-faq.liquid`
- `snippets/lusena-pdp-scripts.liquid`
- `snippets/lusena-pdp-styles.liquid`
- `sections/lusena-header.liquid`
- `sections/lusena-about-values.liquid`
- `snippets/cart-drawer.liquid`
- `snippets/lusena-breadcrumbs.liquid`
- `assets/lusena-payment-blik.svg`
- `AGENTS.md`
- `.agent/skills/lusena-theme-changelog/SKILL.md`
- `.claude/skills/lusena-theme-changelog/SKILL.md`
- `.agent/skills/lusena-draftshop-fragment-parity/SKILL.md`
- `.claude/skills/lusena-draftshop-fragment-parity/SKILL.md`

### 924911d — feat(lusena): unify button system and loading parity across PDP and cart

**Goal:** Standardize button primitives and loading-state behavior across PDP, sticky ATC, cart drawer, and header controls, while tightening global typography delivery and PDP section spacing controls.

**What changed**
- Added a new shared snippet-level button system (`lusena-btn` and `lusena-icon-button`) with loading shimmer/dots, focus-visible treatment, reduced-motion handling, and standardized size/variant classes.
- Replaced legacy per-component utility-heavy button markup in PDP ATC, sticky ATC, cart drawer CTAs, header icon controls, and quality certificates CTA with the shared button classes.
- Added loading lifecycle timing controls (`data-loading-min-ms`, `data-loading-hold-ms`) and synchronized runtime behavior between `product-form`, sticky ATC mirrors, and buy-now flow; added explicit busy/disabled release logic.
- Stabilized cart drawer history ownership (`pushedHistoryEntry`) to prevent redundant `history.back()` transitions after open/close cycles.
- Self-hosted Inter + Source Serif 4 variable fonts from Shopify assets and removed Google Fonts remote loading in `layout/theme.liquid`.
- Added merchant-configurable spacing settings to PDP detail/follow-up sections and added loading-label schema fields for main/sticky PDP actions.
- Extended internal documentation with the parity plan + brandbook UI/UX implementation guide and refined the draftshop parity skill checklist.

**Key files**
- `snippets/lusena-button-system.liquid`
- `snippets/lusena-pdp-atc.liquid`
- `snippets/lusena-pdp-sticky-atc.liquid`
- `snippets/lusena-pdp-scripts.liquid`
- `snippets/cart-drawer.liquid`
- `assets/product-form.js`
- `assets/cart-drawer.js`
- `layout/theme.liquid`
- `sections/lusena-main-product.liquid`
- `sections/lusena-pdp-details.liquid`
- `sections/lusena-pdp-feature-highlights.liquid`
- `sections/lusena-pdp-quality-evidence.liquid`
- `docs/LUSENA_Button_System_Loading_Parity_Plan.md`
- `docs/theme-brandbook-uiux.md`
- `.codex/skills/lusena-draftshop-fragment-parity/SKILL.md`

### 86ba8b3 — fix(lusena): improve touch cart drawer close and history behavior

**Goal:** Make cart interactions feel native on touch devices and avoid stale focus/open states when customers navigate to and from cart-related views.

**What changed**
- Added history-state management to the cart drawer so opening the drawer creates a back-stack entry and browser back closes the drawer instead of unexpectedly changing pages.
- Updated drawer focus handling for pointer/touch activations so close actions don’t force focus restoration in cases where it causes sticky focus states.
- Added touch-focused icon behavior for the LUSENA header and drawer icon buttons: no tap highlight, no hover background on coarse pointers, and blur/reset on history `pageshow`.
- Made cart drawer product image/title links close the drawer when they target the current product page (same-path navigation), avoiding redundant same-page reloads.

**Key files**
- `assets/cart-drawer.js`
- `sections/lusena-header.liquid`
- `snippets/cart-drawer.liquid`
- `docs/THEME_CHANGES.md`

---

## All commits (summary, dateTime-desc)
- 2026-03-25 — (current) — Bundle creative sessions, cart upsell UI redesign, product docs overhaul
- 2026-03-25 — 47ebbb8 — feat(lusena): mobile compact layout for bundle nudge card in drawer
- 2026-03-25 — 0559049 — chore(lusena): delete lusena-bundle-nudge snippet and foundations CSS
- 2026-03-24 — b476fa9 — feat(lusena): unified upsell card in cart page - complete HTML and CSS
- 2026-03-24 — 835182c — fix(lusena): cart drawer upsell - opacity cascade fix + compact padding
- 2026-03-24 — 228fb6d — feat(lusena): unified upsell card in cart drawer - two-tile bundle, gain-framed copy
- 2026-03-21 — ff53459 — feat(lusena): complete bundle PDP template — progressive disclosure, sticky ATC, cart integration
- 2026-03-21 — 8499891 — merge: resolve product.json conflict — keep Polish product names + Shopify admin additions
- 2026-03-21 — abf08a9 — feat(lusena): bundle template scaffolding, color strategy, section polish
- 2026-03-21 — 847c0b0 — Update from Shopify for theme lusena-dawn/main
- 2026-03-15 — c800179 — feat(lusena): product copy sessions, bundle strategy, animated icons, percentage cleanup
- 2026-03-09 — 1be3e57 — feat(lusena): footer redesign, PDP/quality polish, spacing audit, product setup docs
- 2026-03-08 — 57beec8 — feat(lusena): complete homepage UX audit — visual rhythm, value anchors, bundle fixes
- 2026-03-06 — 29fc700 — chore(lusena): polish blog/article, trust-bar animations, breadcrumb fixes + repo cleanup
- 2026-03-06 — cbeba1a — feat(lusena): migrate system pages (Batch 2) + polish blog/article (Batch 6)
- 2026-03-06 — 160e283 — feat(lusena): migrate blog + article pages (Batch 6)
- 2026-03-05 — a874dde — feat(lusena): migrate search page (Batch 5) + cart page (Batch 1) + Batch 4 cleanup
- 2026-03-04 — 652d4ba — refactor(lusena): complete CSS foundations migration — Phase 2 + Phase 3
- 2026-03-04 — 6e02637 — refactor(lusena): complete Phase 1 CSS migration — homepage sections + bug fixes
- 2026-03-03 — e979668 — docs: update memory bank and CLAUDE.md for CSS foundations migration
- 2026-03-03 — e26bee2 — feat(lusena): add CSS foundations file and designer brief
- 2026-02-28 — 41e8ccc — refactor(lusena): restructure docs into memory bank + compact CLAUDE.md
- 2026-02-28T09:33:32+01:00 — 7087015 — feat(lusena): migrate quality/about/returns pages and extend PDP v2 proof blocks
- 2026-02-22T17:01:40+01:00 — 9def2eb — feat(lusena): migrate homepage v2 copy and add newsletter capture
- 2026-02-22T14:43:58+01:00 — 567ef16 — feat(lusena): refine spacing system and refresh PDP + brandbook docs
- 2026-02-22T12:11:24+01:00 — f178fd9 — fix(lusena): align PDP spacing with global gap tokens
- 2026-02-22T11:20:24+01:00 — 0a6c1ab — feat(lusena): standardize global section spacing system
- 2026-02-21T18:07:48+01:00 — 636e65e — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-02-21T18:05:45+01:00 — 53339f1 — chore: remove CLAUDE.md and clean duplicate PDP motion flag
- 2026-02-21T18:03:32+01:00 — 242c49d — feat(lusena): standardize global section spacing system
- 2026-02-21T15:17:18+01:00 — a2551d3 — feat(lusena): optimize accordion UX and sync theme docs
- 2026-02-21T11:32:06+01:00 — 924911d — feat(lusena): unify button system and loading parity across PDP and cart
- 2026-02-18T20:28:57+01:00 — 86ba8b3 — fix(lusena): improve touch cart drawer close and history behavior
- 2026-02-17T20:47:16+01:00 — 170a28b — upsell css fix
- 2026-02-16T20:21:46+01:00 — 573f97a — fix(lusena): hide cart label in cart icon bubble rerenders
- 2026-02-16T20:07:33+01:00 — 186361d — fix(lusena): stabilize PDP gallery crossfade and mobile variant sync
- 2026-02-16T16:38:50+01:00 — 4b9caa2 — feat(lusena): finalize returns page and PDP parity updates
- 2026-02-13T19:00:49+01:00 — 7eb6712 — fix(ci): resolve LHCI product handle dynamically
- 2026-02-13T18:51:05+01:00 — 1ad8a9e — fix(ci): stabilize Lighthouse target and skip remote theme pull
- 2026-02-13T18:33:58+01:00 — 1ccc2b8 — feat(lusena): complete PDP + cart parity rollout
- 2026-02-07T16:30:27+01:00 — 3a51798 — refactor(lusena): split PDP into snippets
- 2026-02-04T20:48:18+01:00 — 09ba94a — fix(lusena): preserve PDP image index on color switch
- 2026-02-04T20:39:13+01:00 — cdcee94 — fix(lusena): correct PDP color gallery filtering
- 2026-02-03T19:25:59+01:00 — 8a6d37a — feat(lusena): PDP gallery grouped by color-tagged media
- 2026-02-02T19:08:42+01:00 — a171d76 — feat(lusena): PDP swatches + variant media switching
- 2026-02-02T16:41:07+01:00 — bb4cfc3 — docs: add Playwright verification workflow
- 2026-02-02T16:37:30+01:00 — dc1ed64 — fix(lusena): sync page offset to header height
- 2026-02-02T16:19:43+01:00 — a3fd8e3 — fix(lusena): make scroll-reveal consistent across pages
- 2026-02-02T16:10:59+01:00 — 6f5f6de — fix(lusena): trust bar launch-safe proof points
- 2026-02-02T13:12:18+01:00 — 0a6644e — feat(lusena): motion layer + remove GSAP
- 2026-02-02T10:34:57+01:00 — b076f77 — feat(lusena): refine section spacing defaults
- 2026-02-01T23:02:37+01:00 — e96c48a — feat(lusena): per-section spacing + split page sections
- 2026-01-31T23:58:51+01:00 — f19d702 — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-01-31T23:58:34+01:00 — 184fe6b — docs: update theme changelog
- 2026-01-31T23:58:01+01:00 — 7efa557 — feat(lusena): auto-hide header on scroll
- 2026-01-31T22:53:52Z — 5a1ac3c — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T22:53:33Z — 90374e6 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T22:53:09Z — 70bedf7 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T22:17:31Z — 3fe4d5e — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T22:17:07Z — ea6f51f — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T23:08:56+01:00 — 7b3b60a — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-01-31T23:04:08+01:00 — 6499dff — docs: update theme changelog
- 2026-01-31T23:03:09+01:00 — 27fcb56 — feat(lusena): independent mobile hero offsets
- 2026-01-31T22:51:00+01:00 — 6339ab2 — docs: update theme changelog
- 2026-01-31T22:50:10+01:00 — 6187b7d — feat(lusena): mobile hero button size controls
- 2026-01-31T21:48:29Z — 56962b8 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:29:54Z — 9a3bd86 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:28:18Z — 1e2447a — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:28:07Z — ccbea04 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:27:32Z — b1feff8 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:27:22Z — e3bb38d — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:26:35Z — cc904c3 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:26:22Z — f8c1a53 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:25:54Z — 9f4023d — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:25:38Z — 0acd0a1 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:07:58Z — d6eaeab — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:48:52+01:00 — 36ae2bd — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-01-31T21:44:42+01:00 — 6b28e86 — docs: update changelog + fix utf-8
- 2026-01-31T21:34:41+01:00 — cbb4d8a — fix(lusena): mobile hero max height + responsive text controls
- 2026-01-31T20:17:40Z — 5e44bda — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:00:04+01:00 — 4a950cc — docs: update theme changelog
- 2026-01-31T20:55:28+01:00 — abbe143 — chore: resolve homepage template merge conflict
- 2026-01-31T20:48:14+01:00 — 179d0af — fix(lusena): hero overlay opacity + copy positioning
- 2026-01-31T19:11:19Z — 77ada10 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T20:05:29+01:00 — e26de8d — reduce readability from .9 to .89
- 2026-01-31T19:56:33+01:00 — 3236ecf — docs: refine lusena-theme-changelog commit guidance
- 2026-01-31T19:17:43+01:00 — f15ccab — docs: log quality benefit dot alignment
- 2026-01-31T19:16:47+01:00 — 055293b — fix(lusena): center quality benefit dot on first line
- 2026-01-31T19:07:38+01:00 — dbdbba5 — docs: add quality page bullet alignment entry
- 2026-01-31T19:05:54+01:00 — f208bdd — fix(lusena): align quality page benefit bullets
- 2026-01-31T18:55:13+01:00 — 6e793db — docs: log outside-tap mobile menu close
- 2026-01-31T18:54:29+01:00 — c6e29b9 — fix(lusena): close mobile menu on outside tap
- 2026-01-31T18:51:22+01:00 — 65418df — docs: log mobile menu padding tweak
- 2026-01-31T18:50:55+01:00 — d5e5458 — fix(lusena): align mobile menu vertical padding
- 2026-01-31T18:49:27+01:00 — 2b57e46 — docs: log opaque header change
- 2026-01-31T18:48:32+01:00 — b441ec8 — fix(lusena): make header opaque at top
- 2026-01-31T18:46:48+01:00 — 22e1ac1 — fix(lusena): remove homepage header spacer
- 2026-01-31T18:42:52+01:00 — ea014bc — docs: log header scroll transition fix
- 2026-01-31T18:42:12+01:00 — 1dc0edd — fix(lusena): disable header scroll transition
- 2026-01-31T18:38:15+01:00 — db80086 — docs: update theme changelog
- 2026-01-31T18:35:44+01:00 — e607662 — fix(lusena): mobile header menu expands with background
- 2026-01-31T16:31:47+01:00 — 9eb49d5 — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-01-31T15:30:29Z — 711edc8 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T16:29:42+01:00 — baef5d6 — docs: add changelog entry for hero copy alignment
- 2026-01-31T16:29:25+01:00 — 0997b8a — fix(lusena): align hero copy to top on mobile
- 2026-01-31T15:39:26+01:00 — 9e47acb — docs: add changelog entry for removing skip links
- 2026-01-31T15:39:15+01:00 — f58cf0c — chore(a11y): remove skip links
- 2026-01-31T15:34:52+01:00 — c6f0953 — docs: add changelog entry for skip link focus
- 2026-01-31T15:34:20+01:00 — 701b58d — fix(a11y): show skip link only on keyboard focus
- 2026-01-31T15:13:25+01:00 — 3397cfd — chore: resolve merge conflicts
- 2026-01-31T15:09:55+01:00 — c7626e4 — docs: add changelog entry for hero mobile/desktop images
- 2026-01-31T15:09:34+01:00 — 6922ae6 — feat(lusena): separate hero images for mobile/desktop
- 2026-01-31T15:04:47+01:00 — 7032270 — docs: add changelog entry for header menu cleanup
- 2026-01-31T15:04:30+01:00 — 99d916b — fix(lusena): remove extra header menu links
- 2026-01-31T14:58:34+01:00 — 290b629 — docs: add changelog entry for desktop-only header links
- 2026-01-31T14:58:10+01:00 — 27317ae — fix(lusena): desktop-only header links + bold account icon
- 2026-01-31T13:52:38Z — 626d6bf — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T14:39:57+01:00 — eaa726f — docs: add changelog entry for header fixes
- 2026-01-31T14:39:28+01:00 — fcdcf27 — fix(lusena): header links on mobile + account icon + logo color
- 2026-01-31T13:38:49Z — 6f098e9 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T13:36:21Z — ee686d2 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T13:35:36Z — e0bacf9 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T13:34:01Z — 505a16f — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T14:20:43+01:00 — 2d40998 — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-01-31T14:15:39+01:00 — e71c1f9 — docs: add changelog entry for PDP sticky ATC fix
- 2026-01-31T14:13:33+01:00 — 0f38fbe — fix(lusena): keep PDP sticky ATC fixed
- 2026-01-31T14:05:45+01:00 — 14408f2 — fix(lusena): header links defaults + bolder cart icon
- 2026-01-31T14:02:14+01:00 — ea9152c — docs: add changelog entry for header logo + links
- 2026-01-31T14:02:03+01:00 — 7b69635 — feat(lusena): logo upload + primary header links
- 2026-01-31T13:51:28+01:00 — ce5aa0e — chore(lusena): remove redundant utility fallbacks
- 2026-01-31T13:45:09+01:00 — 76b4d93 — docs: add changelog entry for cart drawer overlay
- 2026-01-31T13:44:39+01:00 — 7079328 — fix(lusena): cart drawer overlay blur + upsell styling
- 2026-01-31T12:08:38Z — 9cabf8b — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T13:02:45+01:00 — 854cdd5 — docs: add changelog entry for nasza-jakosc updates
- 2026-01-31T13:02:23+01:00 — 3be1a33 — feat(lusena): nasza-jakosc certificate button + layout tweaks
- 2026-01-31T11:55:13Z — 744d0d4 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T11:46:04Z — b42c92f — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T10:57:27Z — 581de2d — Update from Shopify for theme lusena-dawn/main
- 2026-01-30T22:38:02+01:00 — 9ad7892 — chore: update theme changelog skill
- 2026-01-30T22:38:02+01:00 — 7209847 — docs: keep theme changelog to last 8 entries
- 2026-01-30T22:34:15+01:00 — f906875 — fix(lusena): problem/solution typography + spacing
- 2026-01-30T22:10:22+01:00 — e1d78e4 — docs: update theme changelog
- 2026-01-30T22:09:58+01:00 — 90e00a8 — fix(lusena): trust bar matches draft layout
- 2026-01-30T20:58:03Z — 1f6a5fb — Update from Shopify for theme lusena-dawn/main
- 2026-01-30T21:44:13+01:00 — e47ec72 — fix(lusena): trust bar layout + remove border
- 2026-01-30T20:41:45+01:00 — 922b24d — Initial commit

## Legacy commits (pre-reset history, summary only)
- unknown — 2f6787f — fix(lusena): match homepage to draft spacing + CTAs
- unknown — d93971a — feat(lusena): migrate draft-shop UI into Dawn
- unknown — fcd1a02 — refactor(css,i18n): brandbook-aligned typography, animations & localization
- unknown — 1b99f37 — feat(lusena): brandbook-aligned UI + cart conversion layer
