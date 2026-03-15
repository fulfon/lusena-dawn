# Active Context

*Last updated: 2026-03-15*

## Current focus

**All product copy + bundle strategy COMPLETE.** 5 individual products finalized (creative sessions with legal checks + customer validation). Research-backed bundle architecture approved with 3 Phase 1 bundles. Animated icon system built for PDP feature highlights.

**Next:** Bundle creative sessions (headline, tagline, 3 benefits per bundle) → enter all products + bundles into Shopify admin → upload media when physical products arrive.

## Recent completed work

### Bundle strategy (2026-03-15)
- Research-backed bundle architecture in `memory-bank/doc/bundle-strategy.md`
- 3 Phase 1 bundles: Nocna Rutyna (399 zł, 21.5%), Piękny Sen (349 zł, 20.3%), Scrunchie Trio (139 zł, 21.5%)
- PDP cross-sell checkbox (scrunchie at 39 zł) replaces old Starter Kit — Presenter's Paradox research
- Free shipping threshold set to 299 zł
- Original brandbook bundle plan (§ 5.8) partially superseded with research basis documented

### Heatless curlers copy finalization (2026-03-15)
- Material correction: confirmed 22 momme 6A silk (was previously uncertain)
- Title changed: "Lokówki jedwabne" → "Jedwabny wałek do loków" (market research: "wałek" is universal in PL)
- Custom care instructions (PP cotton filling requires different handling)
- Legal check PASS, customer validation finalized (1 run — no copy-level improvements possible)
- Full doc: `memory-bank/doc/products/heatless-curlers.md`

### Animated icon system for PDP (2026-03-15)
- New `snippets/lusena-icon-animated.liquid` — 8 animated SVG icons (heart, layers, droplets, wind, shield-check, sparkles, gift, clock)
- New `assets/lusena-icon-animations.css` — CSS keyframes, stagger delays via `--lusena-anim-stagger`, `prefers-reduced-motion` fallback
- `sections/lusena-pdp-feature-highlights.liquid` updated to load animation CSS and render animated icons
- Icon animation specs documented per product in `memory-bank/doc/products/{handle}.md`

### Product copy sessions complete (2026-03-14)
- **Silk scrunchie** — copy finalized (legal PASS, 2 validation runs, trust 7.4, premium 7.0)
- **Silk bonnet** — copy finalized (title research: "czepek" > "bonnet", pricing: 239 zł, legal PASS, 2 validation runs)
- **Jedwabna maska 3D** — copy finalized (2 validation runs, trust 7.75, premium 7.9 — highest scores)
- **Poszewka jedwabna** — additional metafield data entered
- All product docs: `memory-bank/doc/products/{handle}.md`

### Cross-site percentage claim cleanup (2026-03-14)
- All "30%", "15%" momme claims removed from brandbook, sections, templates, docs
- Replaced with qualitative "gęstszy i trwalszy niż standard"
- Rule added to brandbook: never use percentages for momme comparison without own test documentation

### Product documentation infrastructure (2026-03-14)
- Expanded `docs/product-metafields-reference.md` — universal fields marked, creative workflow documented
- Refined `docs/product-setup-checklist.md` — metafield definitions per product type
- 4 new product docs + CSV export/import tooling (`memory-bank/doc/products/exports/`, `imports/`)
- Updated product template and README

### Skills infrastructure (2026-03-15)
- `lusena-theme-changelog` deleted (replaced by `lusena-pre-commit-sync`)
- `lusena-pre-commit-sync` created across `.agent/`, `.claude/`, `.codex/`, `.opencode/`
- `lusena-customer-validation` skill expanded (Polish personas, aggregated scoring)

### Previous sessions (already committed as 1be3e57)
- Footer redesign, PDP/quality polish, spacing audit, product setup docs (2026-03-09/10)
- Homepage UX audit (57beec8, 2026-03-08)
- Blog/article + system pages migration (29fc700, cbeba1a, 160e283, 2026-03-06)
- Search + cart migration (a874dde, 2026-03-05)
- CSS foundations migration (652d4ba, 6e02637, 2026-03-04)

## Next steps

1. **Bundle creative sessions** — headline, tagline, 3 benefits per bundle (Nocna Rutyna, Piękny Sen, Scrunchie Trio)
2. **Enter all products into Shopify admin** — owner copies metafield values from `memory-bank/doc/products/*.md`; CSV imports available in `memory-bank/doc/products/imports/`
3. **Create Phase 1 bundles** in Shopify admin using Shopify Bundles app (free)
4. **Upload product media** when physical products arrive (photos, videos — critical per all 4 validation personas)
5. **Replace dummy VAT registration** (PL0000000000) with real NIP before going live
6. **Configure footer settings** in Shopify admin: real Instagram/Facebook URLs, legal menu, test hCaptcha newsletter flow
7. **PDP cross-sell checkbox** — implement scrunchie upsell at 39 zł (see `pdp-migration-backlog.md` item 1)
8. **Set free shipping threshold** to 299 zł in Shopify admin
9. PDP migration backlog items (see `memory-bank/doc/features/pdp-migration-backlog.md`)
10. Homepage migration backlog remaining items (see `memory-bank/doc/features/homepage-migration-backlog.md`)

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
9. `lusena-bundles.css` — Bundles card grid (loaded per-section)
10. `lusena-icon-animations.css` — Animated icon keyframes (loaded per-section in feature highlights)
11. `compiled_assets/styles.css` — remaining small `{% stylesheet %}` blocks (~38KB, limit 73KB)

**MANDATORY:** After adding CSS to any `{% stylesheet %}` block, check compiled_assets size in DevTools — must stay under 55KB. See `memory-bank/doc/patterns/css-architecture.md` for full pattern.

Shared components in foundations: `.lusena-split`, `.lusena-accordion`, `.lusena-trust-bar`, `.lusena-testimonial`, `.lusena-content-card`, `.lusena-newsletter`, `.lusena-truth-table`.

Shared sections (reusable across pages): `lusena-faq` (homepage, quality, returns, PDP), `lusena-trust-bar` (homepage, about, quality), `lusena-final-cta` (homepage, about, quality, returns, PDP), `lusena-newsletter` (article, contact — with optional secondary link on article; removed from homepage 2026-03-08).
