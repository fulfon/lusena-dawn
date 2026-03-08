# Active Context

*Last updated: 2026-03-08*

## Current focus

**Homepage UX audit COMPLETE.** Two-session audit covering section order, copy, visual rhythm, spacing, value anchors, and conversion flow. All agreed changes implemented and visually verified.

## Recent completed work

### Homepage UX audit — Phase 2 (2026-03-08)
- **Background rhythm redesign:** Fixed two same-color collisions (bestsellers/testimonials, FAQ/final-CTA). Redesigned full 9-section background sequence so every transition has a visible color change:
  - Testimonials: `surface-1` → `surface-2` (cream)
  - Bundles: `surface-2` → `brand` (warm porcelain)
  - Heritage: `brand` → `surface-2` (cream)
  - Final CTA: `surface-1` → `brand` (warm porcelain)
- **Bundle card fixes:**
  - Removed placeholder prices from all 3 bundle cards (were hardcoded, not from products)
  - Fixed button text centering (removed errant `padding-top` on CTA button)
  - Fixed title-description gap (reset inherited h3 margins, flex gap handles spacing)
  - Equalized card heights (`flex-grow: 1` on card-info, `margin-top: auto` on CTA)
- **Value anchor on bestseller cards:** Added `show_value_anchor` parameter to `lusena-product-card.liquid`. Computes per-night price (`price / 365`), displayed in teal below the price. Only passed from `lusena-bestsellers.liquid` (homepage only for now).
- **Newsletter section removed from homepage.** Footer already has newsletter signup — having both was redundant and diluted the Final CTA. Homepage now ends: FAQ → Final CTA → Footer.
- **Reusable page audit skill created:** `.claude/skills/lusena-page-audit/skill.md`

### Homepage UX audit — Phase 1 (2026-03-07)
- Section reorder, hero/trust-bar/problem-solution/bestsellers/heritage copy rewrites
- Bundles section rebuilt as 3-card grid
- Heritage tiles deduplicated (supply chain narrative)
- FAQ expanded with Q5 (bonnet/scrunchie Polish descriptions)
- Final CTA section added

## Next steps

1. PDP migration backlog items (see `memory-bank/doc/features/pdp-migration-backlog.md`)
2. Homepage migration backlog remaining items (see `memory-bank/doc/features/homepage-migration-backlog.md`)

## Pending to-do items (flagged during homepage audit)

### Cross-site "30%" claim cleanup
The "30% gęstszy splot" / "30% więcej jedwabiu" claim is factually wrong (22/19 momme = ~15.8%, not 30%) and legally risky under Polish consumer law (UOKiK). Fixed on homepage trust bar. **Must review and fix on all other pages:**
- Quality page (`page.nasza-jakosc.json`) — momme section likely contains "30%" claim
- About page (`page.o-nas.json`) — hero or story may reference 30%
- PDP — proof chips or quality evidence may reference 30%
- Any other section using the 22 momme talking point

**Safe alternatives:** "Gęstszy splot, dłuższa trwałość" (qualitative) or "Ponad 15% więcej jedwabiu niż standard 19 momme" (accurate %).

### Bonnet naming convention
Decided: "bonnet" stays as the product name, but customer-facing copy must introduce it with Polish description on first mention: "jedwabny czepek na noc (bonnet)". Applied on homepage FAQ. **Must apply to:**
- PDP product descriptions
- About page (if mentioned)
- Quality page (if mentioned)
- Cart/checkout copy
- All cross-sell and upsell copy

### Value anchor expansion to other pages
Homepage bestsellers now have value anchor (`lusena-product-card__per-night`, gated by `show_value_anchor` param). Currently homepage-only. **Expand to other pages when ready:**
- Collection page product cards
- Search results product cards
- Bundles: will need crossed-out price + bundle price with savings badge once real bundle products exist

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
- **Stale doc: `memory-bank/doc/patterns/brand-tokens.md`** — Typography scale table doesn't match live CSS. Needs full review.

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
10. `compiled_assets/styles.css` — remaining small `{% stylesheet %}` blocks (~38KB, limit 73KB)

**MANDATORY:** After adding CSS to any `{% stylesheet %}` block, check compiled_assets size in DevTools — must stay under 55KB. See `memory-bank/doc/patterns/css-architecture.md` for full pattern.

Shared components in foundations: `.lusena-split`, `.lusena-accordion`, `.lusena-trust-bar`, `.lusena-testimonial`, `.lusena-content-card`, `.lusena-newsletter`, `.lusena-truth-table`.

Shared sections (reusable across pages): `lusena-faq` (homepage, quality, returns, PDP), `lusena-trust-bar` (homepage, about, quality), `lusena-final-cta` (homepage, about, quality, returns), `lusena-newsletter` (article, contact — with optional secondary link on article; removed from homepage 2026-03-08).
