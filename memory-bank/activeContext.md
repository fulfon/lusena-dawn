# Active Context

*Last updated: 2026-03-21*

## Current focus

**Bundle Phase B — M2 visual scaffolding created, ready to assign templates in Shopify admin.** All 6 new files created: `product.bundle.json` template, `lusena-main-bundle` section, 3 new snippets (`lusena-bundle-summary`, `lusena-bundle-contents`, `lusena-bundle-options`), and `lusena-bundle-pdp.css`. M1 metafield research complete. Next: assign the 3 bundle products to `product.bundle` template in Shopify admin, then validate M2 visuals via Playwright, then M3 (JS interactivity + ATC).

**Full tracker:** `memory-bank/doc/bundle-implementation.md`

## Recent completed work

### Bundle Phase B — M2 visual scaffolding (2026-03-21)
- Created `templates/product.bundle.json` — 6 sections: main bundle buy box, feature highlights (bundle-specific content), quality evidence, truth table, FAQ (bundle-specific questions), final CTA
- Created `sections/lusena-main-bundle.liquid` — full buy box with schema (spacing, summary, color selector, ATC, delivery, guarantee, payment settings + benefit blocks)
- Created `snippets/lusena-bundle-summary.liquid` — emotional headline + title + tagline (metafield overrides) + price with crossed-out `lusena.bundle_original_price` + savings badge + delivery row
- Created `snippets/lusena-bundle-contents.liquid` — "What's included" list parsed from `simple_bundles.variant_options` metafield, deduplicates repeated products (e.g., 3× Scrunchie)
- Created `snippets/lusena-bundle-options.liquid` — color swatch fieldsets per component product, reuses shared `lusena-option__swatch` CSS, Polish/English color name mapping, single-option pre-selection
- Created `assets/lusena-bundle-pdp.css` — savings badge, contents list, option groups, ATC placeholder, buy-box order overrides

### Section and snippet polish (2026-03-21)
- **Proof chips:** reordered ("Na prezent" first), added JS row balancer that measures chip widths and optimizes CSS order for balanced rows
- **Quality evidence:** click area expanded to whole item (not just toggle button), icon color → gold (`--lusena-accent-2`), cursor pointer added
- **Heritage + problem-solution:** CTA spacing improved with `lusena-gap-cta-top` + `margin-top: var(--lusena-space-6)`
- **Science section:** kicker uses shared `.lusena-type-caption .lusena-kicker` classes, gold color
- **Quality comparison table:** inline SVGs replaced with `lusena-icon` renders
- **Clock icon animation:** reworked from continuous spin to gentle tick-tock (separate hour/minute hands)
- **PDP proof chip sizing:** tightened on mobile (gap, padding), restored on desktop via media query
- **PDP title:** desktop font-size reduced from 4rem to 3.2rem
- **Cart drawer JS:** scrollbar-width guard (prevents redundant recalculation)
- **Metafield checks simplified:** `mf_per_night.value == false` instead of `mf_per_night != blank and mf_per_night.value == false`
- **Copy fixes:** bonnet naming ("czepek do spania" in homepage FAQ), product names in product FAQ ("Czepek", "Maska 3D", "Wałek do loków"), stroke widths normalized

### Color strategy finalized (2026-03-20)
- **Full document:** `memory-bank/doc/color-strategy.md`
- **Palette:** Black (Czarny) + Dusty Rose (Brudny róż) + Champagne (Szampan) — unified capsule across all products
- **Research:** 4 independent streams (20+ competitor brands, color psychology, Polish market data, DTC strategy). Colors derived purely from cross-category sales data.
- **Shopify admin done:** placeholder variants renamed in both Shopify admin and Simple Bundles option labels

### Bundle M1 metafield research + Phase A complete (2026-03-19 — 2026-03-20)
- **M1 findings:** `simple_bundles.variant_options` is the working metafield (JSON array of option groups with `optionName`, `optionValues`, `defaultOptionName`). ATC uses `properties[...]` hidden inputs + `properties[_bundle_selection]` concatenated string. Backend works without widget.
- **Phase A:** 3 bundle products created and configured in Simple Bundles, ATC tested, all working
- **`compare_at_price` issue found:** Simple Bundles Price Sync clears it. Solution: `lusena.bundle_original_price` metafield (documented in `docs/product-metafields-reference.md`)

### Previous sessions (committed as c800179)
- Product copy sessions (5 products), bundle strategy, animated icons, percentage cleanup, pre-commit sync skill
- Color strategy research (4 streams, 20+ brands)

## Next steps

1. **Assign bundle templates in Shopify admin** — assign 3 bundle products (Nocna Rutyna, Piękny Sen, Scrunchie Trio) to `product.bundle` template. Set `lusena.bundle_original_price` metafield on each (508, 438, 177).
2. **Bundle M2 visual validation** — Playwright screenshots of all 3 bundle URLs on desktop + mobile. Verify layout, savings badge, contents list, swatches, section order.
3. **Bundle M3 (functionality)** — swatch interaction JS, real ATC form with `properties[...]` hidden inputs, cart line items showing selected colors. Full plan: `memory-bank/doc/bundle-implementation.md`
4. **Bundle M4 (testing + sticky ATC)** — full test matrix, edge cases, sticky ATC mobile
5. **Bundle creative sessions (Phase C)** — headline, tagline, 3 benefits per bundle
6. **Homepage bundles section** — wire up real bundle products in `templates/index.json`
7. **PDP cross-sell checkbox** — implement scrunchie upsell at 39 zł (poszewka only — see `memory-bank/doc/upsell-strategy.md`)
8. **Upload product media** when physical products arrive
9. **Replace dummy VAT registration** (PL0000000000) with real NIP before going live
10. **Configure footer settings** in Shopify admin: real Instagram/Facebook URLs, legal menu, test hCaptcha newsletter flow
11. **Set free shipping threshold** to 289 zł in Shopify admin
12. PDP migration backlog items (see `memory-bank/doc/features/pdp-migration-backlog.md`)
13. Homepage migration backlog remaining items (see `memory-bank/doc/features/homepage-migration-backlog.md`)

## Pending to-do items

### Bonnet naming convention
Decided: Shopify title is "Jedwabny czepek do spania" (market-optimized). Customer-facing copy introduces with Polish description on first mention: "jedwabny czepek na noc (bonnet)". Applied on homepage FAQ. **Must apply to:**
- PDP product descriptions
- About page (if mentioned)
- Quality page (if mentioned)
- Cart/checkout copy
- All cross-sell and upsell copy

### Value anchor expansion to other pages
Homepage bestsellers now have value anchor (`lusena-product-card__per-night`, gated by `show_value_anchor` param). PDP has per-product toggle via `pdp_show_price_per_night` metafield. **Expand to:**
- Collection page product cards
- Search results product cards
- Bundles: crossed-out price + bundle price with savings badge once real bundle products exist

### Bestsellers product selection
When products are configured, set the bestsellers to show these 3 in this order:
1. **Poszewka jedwabna** — flagship, Tier 1, must be position #1
2. **Bonnet jedwabny** — completes "nocna rutyna" (face + hair)
3. **Scrunchie jedwabny** — most giftable, accessible entry point

This tells a story: protect your face → protect your hair at night → protect your hair by day.

## Deliberately skipped

- **Batch 7: Password page** (`password.json`) — Abandoned 2026-03-06. Not needed for launch.

## Known issues

- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` is a doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- **DEV-ONLY in cart upsell:** Hardcoded fallback product (`all_products['the-compare-at-price-snowboard']`) in both `lusena-cart-items.liquid` and `cart-drawer.liquid`. Hardcoded color label (`'Beżowy'`) in both files. Must be replaced with real product data before production.
- **Bundle options still show old English names** for Piękny Sen and Scrunchie Trio (Gray/Gold/Pink/Clear in `simple_bundles.variant_options` metafield). Template renders whatever's in the metafield — will auto-fix when option values are updated in Simple Bundles admin.

## Shopify-managed pages (not in theme — configured via admin)

**Shopify deprecated legacy/classic customer accounts in February 2026.** These pages are hosted by Shopify and branded via admin settings (Settings → Checkout → Customize):

| Page | Status |
|------|--------|
| Checkout | Branded (2026-03-05) |
| Thank you | Branded (2026-03-05) |
| Sign in | Branded (2026-03-05) |
| Orders | Branded (2026-03-05) |
| Order status | Branded (2026-03-05) |
| Profile | Branded (2026-03-05) |

**Branding applied:** Logo (PNG), main bg `#F7F5F2`, order summary bg `#F0EEEB`, accent/buttons `#0E5E5A`, error `#B91C1C`, white fields/cards, logo centered.

**Liquid templates for `customers/*` are dead code** — bypassed by the new system. Batches 3 & 4 permanently N/A. Further customization only via customer account UI extensions (app dev).

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
9. `lusena-bundle-pdp.css` — Bundle PDP styles (loaded in lusena-main-bundle section)
10. `lusena-bundles.css` — Bundles card grid (loaded per-section)
11. `lusena-icon-animations.css` — Animated icon keyframes (loaded per-section in feature highlights)
11. `compiled_assets/styles.css` — remaining small `{% stylesheet %}` blocks (~38KB, limit 73KB)

**MANDATORY:** After adding CSS to any `{% stylesheet %}` block, check compiled_assets size in DevTools — must stay under 55KB. See `memory-bank/doc/patterns/css-architecture.md` for full pattern.

Shared components in foundations: `.lusena-split`, `.lusena-accordion`, `.lusena-trust-bar`, `.lusena-testimonial`, `.lusena-content-card`, `.lusena-newsletter`, `.lusena-truth-table`.

Shared sections (reusable across pages): `lusena-faq` (homepage, quality, returns, PDP), `lusena-trust-bar` (homepage, about, quality), `lusena-final-cta` (homepage, about, quality, returns, PDP), `lusena-newsletter` (article, contact — with optional secondary link on article; removed from homepage 2026-03-08).
