# PDP Bundle Detection Banner (#12)

## Problem

When a customer has a bundle complement in their cart (e.g., poszewka) and visits the other component's PDP (e.g., bonnet), nothing tells them they could save money by buying the bundle instead. They add the individual product, pay full price for both (508 zl), and miss the bundle savings (399 zl). This also creates a secondary problem: both components in the cart separately, with no bundle merge mechanism.

## Solution

A banner between the variant picker and ATC button on the PDP. It detects cart contents via `fetch('/cart.js')` on page load, and if a bundle complement is found, reveals a compact card offering a one-click swap to the bundle. Clicking the CTA adds the bundle and removes the individual from cart using the existing `lusena-bundle-swap.js`.

This eliminates the need for #13 (cart merge) — by intercepting at the PDP, the most common path to having both components in cart separately is prevented.

## Design decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Placement | Between variant picker and ATC | Natural decision point — customer has chosen a color, about to commit. Doesn't disrupt browsing flow. |
| Action | One-click swap (not link to bundle PDP) | Avoids duplicate-in-cart problem. Reuses proven `LusenaBundle.swap()`. Fastest path. |
| Visual style | Cart nudge design language | Same card shell, accent stripe, label, pricing row, outline CTA. Visual consistency across surfaces. |
| Layout | Compact — "have" row only, no "add" tile | Customer is already viewing the "add" product on the PDP. Showing a thumbnail is redundant. Saves ~60px vertical space, keeps ATC reachable on mobile. |
| Tone | "Korzystniej w zestawie" — helpful recommendation | Matches cart nudge label. Premium feel, not promotional. |

## Bundle mapping

| PDP product (handle) | Cart has (handle) | Bundle (handle) | Bundle price | Original total | Savings |
|---|---|---|---|---|---|
| `silk-bonnet` | `poszewka-jedwabna` | `nocna-rutyna` | 399 zl | 508 zl | 109 zl |
| `poszewka-jedwabna` | `silk-bonnet` | `nocna-rutyna` | 399 zl | 508 zl | 109 zl |
| `jedwabna-maska-3d` | `poszewka-jedwabna` | `piekny-sen` | 349 zl | 438 zl | 89 zl |
| `poszewka-jedwabna` | `jedwabna-maska-3d` | `piekny-sen` | 349 zl | 438 zl | 89 zl |

**Conflict resolution:** If cart has both bonnet and maska, and customer is on poszewka PDP, show Nocna Rutyna (higher savings: 109 zl vs 89 zl).

**Not applicable:** Scrunchie Trio (same-product bundle), Walek (no bundle), bundle PDPs.

## Banner HTML structure

```
[zone wrapper — surface-2 background, hairline borders]
  [label — "Korzystniej w zestawie" in brand font]
  [card — white, teal left accent stripe, faint border + shadow]
    [headline — "Dodaj czepek i zaoszczedz 109 zl"]
    [have-row — horizontal: small thumbnail + "Poszewka jedwabna" + "W koszyku ✓"]
    [bottom-row — pricing (399 zl / ~~508 zl~~) + outline CTA "Kup jako zestaw"]
```

Hidden by default (`display: none`). JS reveals after cart check.

## CSS approach

Reuse existing `.lusena-upsell-card` token values from cart nudge:
- Card: `--lusena-color-n0` background, `--lusena-btn-radius`, `0 1px 2px rgba(0,0,0,0.03)` shadow, `0.25rem solid color-mix(in srgb, var(--lusena-accent-cta) 40%, transparent)` left border
- Zone: `color-mix(in srgb, var(--lusena-surface-2) 50%, transparent)` background
- Label: `var(--lusena-font-brand)`, `1.2rem`, `var(--lusena-text-2)`
- Headline: `1.35rem`, `font-weight: 500`, `var(--lusena-text-1)`
- Pricing: both `1.4rem`; new price `font-weight:500`, was price `text-2 line-through`
- CTA: `lusena-btn lusena-btn--outline lusena-btn--size-xs`

New classes scoped under `.lusena-pdp-bundle-banner` to avoid collision. CSS goes in `assets/lusena-pdp.css` (existing PDP stylesheet).

Mobile (<=767px): zone padding reduces, have-row image shrinks, CTA goes full-width below pricing.

## Technical implementation

### Data flow

1. **Liquid renders hidden banner container** in `lusena-main-product.liquid` between variant picker and ATC snippets
2. Banner element carries `data-bundle-map` attribute — a JSON array of complement entries for the current product, rendered by Liquid
3. **JS on page load** fetches `/cart.js`, checks cart items against the map
4. If match found: populates banner content (product name, image, prices, savings), reveals banner
5. If no match: banner stays hidden, zero visual impact

### Data source for mapping

Liquid snippet renders the map based on current product handle. The mapping is small (3 products, 4 combinations) — a Liquid `case` statement in the banner snippet is sufficient. No new metafields needed.

```liquid
{%- case product.handle -%}
  {%- when 'poszewka-jedwabna' -%}
    {%- assign bundle_complements = '[
      {"cart_handle":"silk-bonnet","bundle_handle":"nocna-rutyna","complement_label":"poszewke","savings_priority":1},
      {"cart_handle":"jedwabna-maska-3d","bundle_handle":"piekny-sen","complement_label":"poszewke","savings_priority":0}
    ]' -%}
  {%- when 'silk-bonnet' -%}
    {%- assign bundle_complements = '[
      {"cart_handle":"poszewka-jedwabna","bundle_handle":"nocna-rutyna","complement_label":"czepek","savings_priority":1}
    ]' -%}
  {%- when 'jedwabna-maska-3d' -%}
    {%- assign bundle_complements = '[
      {"cart_handle":"poszewka-jedwabna","bundle_handle":"piekny-sen","complement_label":"maske 3D","savings_priority":1}
    ]' -%}
{%- endcase -%}
```

Bundle product data (title, price, original price, image, variant ID) rendered via `all_products[bundle_handle]` in Liquid and embedded as data attributes. This avoids an extra API call at runtime.

### Color matching

The swap needs colors for both bundle components:
- **Cart product color:** read from cart item's variant options (from `/cart.js` response)
- **Current PDP color:** read from the currently selected variant picker option

These are passed to `LusenaBundle.swap()` which builds the `properties[...]` and `_bundle_selection` for Simple Bundles, same as the cart nudge.

### Swap flow

1. Customer clicks "Kup jako zestaw"
2. CTA shows loading state (spinner, same pattern as cart nudge)
3. `LusenaBundle.swap(bundleVariantId, [cartItemKey], { properties, sections })` executes:
   - POST `/cart/add.js` — add bundle with color properties
   - POST `/cart/change.js` — remove individual (quantity 0)
4. Cart drawer opens showing the bundle
5. Banner updates to success state or hides
6. PubSub `cartUpdate` event published for header cart badge

### Error handling

- If `/cart/add.js` fails: show error, restore CTA button. No cart change.
- If `/cart/add.js` succeeds but `/cart/change.js` fails: customer has both bundle + individual. Cart drawer still opens. The duplicate is a minor issue — customer can remove the individual manually. This is the existing race condition behavior, acceptable for launch.

## Files to create/modify

| File | Action | Purpose |
|------|--------|---------|
| `snippets/lusena-pdp-bundle-banner.liquid` | **Create** | Banner HTML + Liquid mapping logic |
| `sections/lusena-main-product.liquid` | **Modify** | Render the banner snippet between variant picker and ATC |
| `assets/lusena-pdp.css` | **Modify** | Add `.lusena-pdp-bundle-banner` styles |
| `assets/lusena-pdp-scripts.liquid` or inline `<script>` | **Modify** | Cart fetch + banner reveal + swap handler |

## Not in scope

- Scrunchie Trio detection (same-product bundle, no complement pattern)
- Walek (no bundle includes it)
- Bundle PDPs (never show this banner)
- Sticky ATC changes (banner is in buy-box only)
- #13 Cart merge (superseded by this feature)
- Retry logic for swap race condition (acceptable for launch, low frequency)

## Test scenarios

| # | Scenario | Expected |
|---|----------|----------|
| 1 | Bonnet PDP, poszewka in cart | Banner shows: Nocna Rutyna, 399 zl, saves 109 zl |
| 2 | Poszewka PDP, bonnet in cart | Banner shows: Nocna Rutyna, 399 zl, saves 109 zl |
| 3 | Maska PDP, poszewka in cart | Banner shows: Piekny Sen, 349 zl, saves 89 zl |
| 4 | Poszewka PDP, maska in cart | Banner shows: Piekny Sen, 349 zl, saves 89 zl |
| 5 | Poszewka PDP, bonnet + maska in cart | Banner shows: Nocna Rutyna (higher savings) |
| 6 | Any PDP, empty cart | No banner |
| 7 | Any PDP, only scrunchie in cart | No banner |
| 8 | Walek PDP, anything in cart | No banner |
| 9 | Bundle PDP, anything in cart | No banner (bundle template, not standard PDP) |
| 10 | Click "Kup jako zestaw" | Bundle added, individual removed, cart drawer opens |
| 11 | Click swap, then check cart | Bundle with correct colors, individual gone |
| 12 | Mobile: banner visibility | Banner visible between variant picker and ATC, doesn't push ATC out of initial viewport |
