# Product Page (product.json)

**Status:** Full UX audit completed 2026-03-09, production-ready

## Visual rhythm (alternating backgrounds)

```
1. Main Product       → surface-1 (white)
2. Feature Highlights → surface-2 (cream)    — white icon circles
3. Quality Evidence   → brand-bg (porcelain) — white cards, cream icon circles
4. Truth Table        → surface-1 (white)    — cream mobile cards
5. FAQ                → surface-2 (cream)    — text accordions
6. Final CTA          → brand-bg (porcelain)
```

## Section inventory

| # | Section | Background | Spacing tier | Status |
|---|---------|-----------|-------------|--------|
| 1 | `lusena-main-product` | surface-1 | custom (inline overrides) | Done |
| 2 | `lusena-pdp-feature-highlights` | surface-2 | standard | Done (heading "Co zyskujesz", bg_style, white icon-wrap, border-top removed, animated icons via `lusena-icon-animated` + `lusena-icon-animations.css` 2026-03-15) |
| 3 | `lusena-pdp-quality-evidence` | brand-bg | standard | Done (white cards, cream icon circles, no hover, explicit height accordion with `data-state` + `prefers-reduced-motion` (rewritten 2026-03-28), funnel CTAs removed, content rewritten "why LUSENA?" angle, certificate verification URL from metafield, panel text alignment fix 76/80px, `rotate-ccw` icon added, CTA links use `lusena-link-arrow` class (2026-03-29)) |
| 4 | `lusena-pdp-truth-table` | surface-1 | standard | Done (5 rows, legally safe copy, lusena-icon, cream mobile cards) |
| 5 | `lusena-faq` (shared) | surface-2 | standard | Done (6 items, anchor_id=details, is_returns_target) |
| 6 | `lusena-final-cta` (shared) | brand-bg | spacious | Done ("Sprawdź kolekcję" → /collections/all) |

## PDP snippets (13)

- `lusena-pdp-media.liquid` — Gallery/media (breakpoint aligned to 768px, OEKO-TEX tile diacritics fixed)
- `lusena-pdp-summary.liquid` — Title, price, rating (per-product metafield overrides: headline, tagline, per-night toggle; scrunchie education price swap)
- `lusena-pdp-variant-picker.liquid` — Variant selection
- `lusena-pdp-atc.liquid` — Add to cart button
- `lusena-pdp-buybox-panels.liquid` — Buybox info panels (social proof reordered to slot 2, spacing tightened, conditional specs rendering, last-item border removed)
- `lusena-pdp-proof-chips.liquid` — Evidence chips
- `lusena-pdp-guarantee.liquid` — Guarantee messaging (restructured: p instead of div, no nested p tags)
- `lusena-pdp-cross-sell.liquid` — Cross-sell recommendations (cart drawer upsell)
- `lusena-pdp-cross-sell-checkbox.liquid` — PDP cross-sell checkbox (scrunchie at 39 zl via BXGY). White card with teal accent, compact row, "Taniej w komplecie" hint, color-matched image. Reused on bundle PDPs with `skip_js: true` param.
- `lusena-pdp-payment.liquid` — Payment methods / trust signals
- `lusena-pdp-sticky-atc.liquid` — Sticky add-to-cart bar (per-night toggle via `pdp_show_price_per_night` metafield)
- `lusena-pdp-scripts.liquid` — PDP JavaScript (returns deep-link, cross-sell ATC intercept + Buy Now + variant change)
- `lusena-pdp-styles.liquid` — Doc-only stub (CSS in `assets/lusena-pdp.css`)

## Bundle product page (`product.bundle.json`)

Separate template for bundle products. Uses `lusena-main-bundle` section (custom buy box) + 5 shared PDP sections. Architecture decision documented in `memory-bank/doc/bundle-implementation.md`.

**Bundle-specific snippets (7):**
- `lusena-bundle-summary.liquid` — headline, title, tagline (metafield overrides), price row with savings badge, delivery
- `lusena-bundle-contents.liquid` — "What's included" parsed from `simple_bundles.variant_options`
- `lusena-bundle-options.liquid` — color swatch fieldsets per component product (first step open, others collapsed with pending chips)
- `lusena-bundle-atc.liquid` — Add to cart button for bundles
- `lusena-bundle-care.liquid` — Care accordion for bundle products
- `lusena-bundle-scripts.liquid` — Bundle JS (progressive disclosure reveal after `allSelected()`, cross-sell color match, `submitBundleCartWithCrossSell()`)
- `lusena-bundle-sticky-atc.liquid` — Sticky ATC for bundle pages (mobile + desktop)

**Shared PDP snippets used by bundle (4):**
- `lusena-pdp-media.liquid`, `lusena-pdp-proof-chips.liquid`, `lusena-pdp-guarantee.liquid`, `lusena-pdp-payment.liquid`

**Scrunchie education snippet (1):**
- `lusena-scrunchie-education.liquid` — Server-side price swap (~~59 zl~~ 39 zl) when qualifying product is in cart. Dynamic Polish hint text. Live cart sync via `PUB_SUB_EVENTS.cartUpdate`. MutationObserver syncs sticky ATC price.

## Recent changes (2026-03-29)

- **PDP cross-sell checkbox** — all individual PDPs + bundle PDPs offer scrunchie at 39 zl (BXGY discount). UI: white card with teal accent, compact row, "Taniej w komplecie" hint, color-matched image. Bundle PDPs: progressive disclosure reveal after all colors picked, LUSENA signature `translateY(-6px)` slide-in. Schema: `cross_sell_enabled`, `cross_sell_handle`, `cross_sell_price`. Cross-sell JS in `lusena-pdp-scripts.liquid` (individual) and `lusena-bundle-scripts.liquid` (bundles, `skip_js: true`).
- **Scrunchie PDP education** — server-side render + live JS sync. `lusena-main-product.liquid` checks `cart.items`, maps handle to Polish instrumental case label, passes flags to `lusena-pdp-summary.liquid`. Live sync via `lusena-scrunchie-education.liquid` inline script subscribing to `PUB_SUB_EVENTS.cartUpdate`. Sticky ATC synced via MutationObserver on `[data-lusena-sticky-price]`.
- **`lusena-link-arrow` adoption** — quality evidence accordion CTAs and PDP media certificate CTA now use `lusena-link-arrow` class instead of hardcoded `→` characters
- **Bundle options initial state** — first step renders open, subsequent steps collapsed with pending chips
- **Bundle PDP chip dot** — pending state dot changed from filled to transparent outline

## Changes (2026-03-28)

- **Card 5 freed from universal OEKO-TEX** — all 8 products now have product-specific card 5 (creative sessions documented in each product MD file)
- **3 new animated icons** — moon (glow pulse), feather (float), palette (swatch pulse) added to animated icon system
- **Icon semantic system** — 8 variable icons each with fixed meaning. Icons reassigned across products.
- **Quality evidence accordion rewrite** — `max-height`/opacity → explicit `height` transitions, `data-state` attribute, `prefers-reduced-motion` support, `contain: layout style`, webkit tap highlight fix
- **Feature highlights schema** — 4 new icon options added to dropdown (palette, feather, moon, clock)
- **Lightbox gestures** — `is-gesturing` class toggle on image during touch interactions

### Older changes (2026-03-21)
- **Proof chips:** reordered ("Na prezent" first), JS row balancer added for optimal chip layout
- **Quality evidence:** click area expanded to full item (not just toggle), icon color → gold
- **PDP title:** desktop font-size reduced 4rem → 3.2rem
- **Metafield checks:** simplified `mf_per_night.value == false` pattern

## Pending work

See `memory-bank/doc/features/pdp-migration-backlog.md` for remaining deferred items:
- ~~Checkbox upsell component~~ — DONE (2026-03-29, cross-sell checkbox on all PDPs)
- Reviews widget integration
- Notify-me flow for out-of-stock
- Schema cleanup pass
