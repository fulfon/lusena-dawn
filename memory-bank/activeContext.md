# Active Context

*Last updated: 2026-03-14*

## Current focus

**Ready for commit.** All uncommitted theme work (57 files, ~1400 insertions) reviewed, memory bank updated. Product setup in Shopify admin partially complete (first product configured, store-wide settings done). Documentation and creative workflow skills created.

Previous focus: Footer redesign + PDP UX audit + quality/FAQ refinements + cross-site standardization + quality page spacing audit + product setup docs + creative workflow skills.

## Recent completed work

### Footer redesign (2026-03-09)
- Social media links (Instagram, Facebook) using lusena-icon
- Payment icons bar (Visa, BLIK, PayPo, Przelewy24 SVGs)
- Legal links row with configurable `legal_menu` link list
- Newsletter UX rebuild: arrow submit button, success/error states, hCaptcha-compatible (position: relative fix)
- Schema renamed from "LUSENA footer (draft)" to "LUSENA footer"
- All Polish defaults in schema and footer-group.json

### PDP buy-box spacing overhaul (2026-03-09)
- Significant CSS tightening in `lusena-pdp.css` (margins reduced throughout mobile + desktop)
- Social proof reordered from slot 8 → slot 2 in buybox panels
- Benefits list styling fix (padding-left: 0, list-style: none)
- Gallery/lightbox breakpoint aligned to 768px (was 750px)
- Guarantee restructured (p instead of div, no nested p tags)
- Summary title margin-bottom: 0, delivery margin tightened

### PDP UX audit (2026-03-09)
**Visual rhythm** — alternating section backgrounds:
1. Main Product → surface-1 (white)
2. Feature Highlights → surface-2 (cream) — white icon circles, teal icons
3. Quality Evidence → brand-bg (porcelain) — white cards (surface-1), cream icon circles (surface-2), no hover effect
4. Truth Table → surface-1 (white) — cream mobile cards (surface-2)
5. FAQ → surface-2 (cream) — text accordions
6. Final CTA → brand-bg (porcelain) — "Sprawdź kolekcję" → /collections/all

**Content changes:**
- Feature highlights: heading "Co zyskujesz" added, bg_style=surface-2, border-top removed, icon-wrap white on cream
- Quality evidence: cards white (surface-1) on porcelain, icon-wrap cream (surface-2), accordion JS rewritten with scrollHeight (no fixed max-height), hover removed to avoid icon-circle blending
- Truth table: bg changed from brand to surface-1, subheading rewritten ("Większość tanich poszewek 'satynowych' to poliester. Porównaj fakty."), 3 existing rows rewritten with legally safe copy (Polish UOKiK compliant), 2 new rows (Hipoalergenność, Trwałość) — 5 rows total, inline SVGs → lusena-icon (circle-check, circle-x)
- Truth table mobile cards: background changed from transparent to surface-2 in `lusena-foundations.css`
- FAQ: consolidated from 10 to 6 items (removed: authenticity, oeko, origin, silk-vs-satin — redundant with earlier PDP sections)
- Final CTA: "Przekonaj się sama" / "Sprawdź kolekcję" → /collections/all
- Quality evidence: funnel-leaking CTAs removed from evidence-1 and evidence-2 (kept OEKO-TEX certificate link as it opens in new tab)
- Media diacritics: fixed Polish characters in OEKO-TEX proof tile (both desktop and mobile)

### PDP quality evidence content rewrite + fixes (2026-03-09, post-audit)
**Content rewrite — "Dlaczego LUSENA?" section reframed from "why silk?" → "why this brand?":**
- Card 1 (evidence-0): "Certyfikat OEKO-TEX® - sprawdź sama" — transparency/verification angle, `use_certificate_link: true`, CTA "Zweryfikuj na oeko-tex.com →"
- Card 2 (evidence-1): "Bezpośrednio z manufaktury - bez pośredników" — value proposition (direct import, no middlemen), legally safe ("przystępna cena" not "uczciwa cena", qualified superlatives)
- Card 3 (evidence-2): "Polska kontrola jakości i wysyłka tego samego dnia" — operations angle ("w dni robocze" qualifier added)
- Card 4 (evidence-3): NEW guarantee card replacing old 22 momme card — "60 nocy na test - zwrot bez pytań", icon `rotate-ccw`, concrete return process (email → free InPost label → 3-5 days refund)
- All copy vetted against Polish consumer law (UOKiK, Ustawa o prawach konsumenta, nieuczciwych praktykach rynkowych)

**Certificate link fix:** Changed from fetching PDF file (`shop.metafields.lusena.oeko_tex_certificate`) to building OEKO-TEX verification URL from certificate number metafield (`shop.metafields.lusena.oeko_tex_certificate_number`) — consistent with quality page. Fallback → `/pages/nasza-jakosc`.

**Buybox accordion fix:** Removed bottom border on last accordion item (`.lusena-pdp-accordion__item:last-child { border-bottom: 0; }`) — was touching the next section background.

**Panel text alignment fix:** Updated `.lusena-pdp-quality-evidence__panel-inner` padding-left from hardcoded 72px to calculated values: 76px mobile (20px padding + 40px icon + 16px gap), 80px desktop (24px + 40px + 16px). Collapsed header and expanded detail text now align perfectly.

### PDP content updates (2026-03-09, pre-audit)
- Per-product metafield overrides: `pdp_emotional_headline`, `pdp_tagline`, `pdp_show_price_per_night`
- Conditional specs rendering (blank rows hidden via `{%- if value_X != blank -%}`)
- Returns deep-link fixed (clicks `<summary>` instead of setting `.open` attribute)
- Sticky ATC per-night toggle via `pdp_show_price_per_night` metafield

### Quality page refinements (2026-03-09)
- 6A section removed from template (content merged into momme section's 4th benefit block)
- Background rhythm: origin → surface-2, qc → surface-2
- Icon system: emoji → lusena-icon names with fallback (`known_icons` allowlist)
- CTA links added to origin section
- Comparison table: CTA button added, row values updated ("30%" → "ponad 15% gęstszy splot")
- Hero CTA → direct OEKO-TEX verification link (https://www.oeko-tex.com/...)
- Momme: 4th benefit block added (6A grade content), body text updated

### Quality page spacing audit (2026-03-10)
- **Full spacing audit** completed on both viewports (desktop 1440x900, mobile 375x812)
- **3 off-grid fixes** in `assets/lusena-foundations.css` (truth-table mobile cards): grid gap 12→16px, card-line margin 12→16px, card-label margin 5→8px. Affects Quality + PDP mobile.
- **1 tier upgrade** in `sections/lusena-quality-certificates.liquid`: standard → spacious (64→96px desktop, 48→64px mobile). Creates "3-act structure" page rhythm.
- **Verification**: Desktop 0 bugs; Mobile 5 false positives (inline bounding-box variance, `<strong>` overlap, hero snug-top values).

### FAQ section improvements (2026-03-09)
- `bg_style` setting (white/cream/brand backgrounds)
- `anchor_id` setting for deep-linking (e.g., `#details` on PDP)
- `is_returns_target` per-block checkbox (enables deep-link from guarantee link)
- JS rewritten: `{% javascript %}` → inline `<script>`, arrow functions → function expressions, const/let → var
- PDP FAQ: 4 blocks removed (authenticity, oeko, origin, silk-vs-satin), remaining answers expanded

### Cross-site standardization (2026-03-09)
- Trust bar: canonical copy (sentence case, "Gęstszy i trwalszy") across homepage, about, quality
- Em-dash → hyphen standardization in all template JSON files and locales/pl.json
- 4 new icons in lusena-icon.liquid: instagram, facebook, circle-check, circle-x
- About hero: bg changed to brand, Polish-first defaults, values section kicker/heading added
- Returns final CTA: sentence case, InPost mention, simpler CTA, secondary link restyled as plain underlined text
- Testimonials: em-dash → hyphen in author attribution

### Previous sessions (already committed)
- Homepage UX audit (57beec8, 2026-03-08): bg rhythm, bundle cards, value anchors, newsletter removed
- Blog/article + system pages migration (29fc700, cbeba1a, 160e283, 2026-03-06)
- Search + cart migration (a874dde, 2026-03-05)
- CSS foundations migration (652d4ba, 6e02637, 2026-03-04)

## Next steps

1. **Commit uncommitted work** (57 files, ~1400 insertions) — READY
2. **Finish pillowcase product setup** — see `memory-bank/doc/products/poszewka-jedwabna.md` for remaining items:
   - Cost per item (when import cost known)
   - Finalize variant colors + add SKUs
   - Upload product media (photos/videos)
   - Optionally customize feature highlights (6 cards)
   - Assign to collections
3. **Add remaining products** to Shopify admin (scrunchie, bonnet, eye mask, heatless curlers)
4. **Replace dummy VAT registration** (PL0000000000) with real NIP before going live
5. **Configure footer settings** in Shopify admin: real Instagram/Facebook URLs, legal menu, test hCaptcha newsletter flow
6. PDP migration backlog items (see `memory-bank/doc/features/pdp-migration-backlog.md`)
7. Homepage migration backlog remaining items (see `memory-bank/doc/features/homepage-migration-backlog.md`)

## Pending to-do items

### Cross-site "30%" claim cleanup — MOSTLY COMPLETE
Fixed on: homepage trust bar, quality page (momme body, comparison table, trust bar), about page trust bar, returns trust bar, PDP quality evidence (old evidence-2 with "o 30% grubszy i trwalszy" replaced by guarantee card). **One remaining instance:** PDP `templates/product.json` feature-1 block title still says "22 momme - o 30% gęstszy niż standard" — must be corrected to qualitative alternative.

### Bonnet naming convention
Decided: "bonnet" stays as the product name, but customer-facing copy must introduce it with Polish description on first mention: "jedwabny czepek na noc (bonnet)". Applied on homepage FAQ. **Must apply to:**
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
- **PDP feature highlight "30%" claim:** `templates/product.json` feature-1 block title still says "22 momme - o 30% gęstszy niż standard". Must be corrected.

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
