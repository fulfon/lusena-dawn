# PDP Cross-sell Checkbox — Scrunchie at 39 zl

*Date: 2026-03-29*
*Status: Approved*

## Summary

Add a cross-sell checkbox to all individual product PDPs (poszewka, bonnet, maska, curlers) offering the scrunchie at 39 zl (vs 59 zl standalone). The checkbox sits between the variant picker and ATC button. Shopify BXGY automatic discount handles the actual pricing; the theme controls all visual presentation.

## Strategic decisions

These were discussed and approved during brainstorming:

1. **Scope: all individual PDPs, not poszewka-only.** Consistent pricing builds trust for a new brand. The original strategy (poszewka-only) optimized for free-shipping conversion but created inconsistent customer experience.
2. **Free shipping threshold: lowered from 289 to 275 zl.** Ensures bonnet (239) + scrunchie (39) = 278 > 275 clears the threshold. Poszewka alone (269) still does NOT clear — scrunchie upsell mechanic preserved.
3. **Shopify BXGY automatic discount** handles pricing. Theme displays the price as a preview; Shopify applies the actual discount at cart/checkout.

## Pricing mechanism

- **Shopify admin:** Automatic BXGY discount — "Buy any LUSENA product, get 1 scrunchie at 39 zl"
- **Theme:** Global theme setting `lusena_cross_sell_price` (3900 groszy) for display on PDP and cart upsell
- **Cart display:** Shopify shows scrunchie at 59 zl with -20 zl line-item discount = 39 zl effective
- **Sync requirement:** Theme setting and Shopify discount must show the same price. Documented in section schema `info` text.

## UI design

### Placement

Between the variant picker (`lusena-pdp-buy-box__variant`) and ATC button (`lusena-pdp-buy-box__atc`) in the buy-box flex column. CSS `order` values adjusted accordingly.

### Layout

Compact horizontal row:

```
[checkbox] [48px scrunchie image] Dodaj jedwabna scrunchie    39 zl  59 zl
                                  Kolor: Czarny                      ^^^^
                                                               (crossed out)
```

- LUSENA checkbox style (`.lusena-checkbox` from foundations)
- Small product image (48x48, rounded, border)
- Product text: "Dodaj" + cross-sell product title (e.g., "Dodaj Scrunchie jedwabny")
- Price: cross-sell price prominent, original price crossed out
- Color label: "Kolor: {matched_color}" in muted text
- Subtle background tint to draw attention without being aggressive

### Visual tokens

- Background: `color-mix(in srgb, var(--lusena-accent-cta) 4%, var(--lusena-color-n0))`
- Border: `1px solid color-mix(in srgb, var(--lusena-color-n9) 10%, transparent)`
- Border-radius: `var(--lusena-btn-radius)`
- Padding: `var(--lusena-space-2)`
- Gap: `var(--lusena-space-2)` between elements
- Price font: `lusena-text-sm` with `lusena-text-bold` for the cross-sell price
- Crossed-out price: `text-decoration: line-through; opacity: 0.5`
- Color label: `lusena-text-xs`, muted color

### Mobile

Same layout, single row. Image may shrink to 40px on very narrow screens. The row should not wrap to multiple lines — keep it compact.

## Behavior

### Default state

**Unchecked.** EU Directive 2011/83 Article 22 prohibits pre-checked boxes for additional paid items. Also aligns with trust-first brand positioning.

### ATC button (main)

When checkbox is checked:
1. Intercept the `ProductForm` submit
2. Build `items[]` array: `[{ id: mainVariantId, quantity: 1 }, { id: scrunchieVariantId, quantity: 1 }]`
3. Single `POST /cart/add.js` with both items
4. On success: publish `cartUpdate` event (cart drawer opens as normal)

When unchecked: normal single-item add (no change to existing behavior).

### Buy Now button

When checkbox is checked:
1. Add both items via `POST /cart/add.js` with `items[]` array
2. On success: redirect to `/checkout`

When unchecked: current behavior (add main product, redirect to checkout).

### Sticky ATC

Reads the checkbox state from the main buy-box. Same behavior as main ATC — if checked, adds both items. The sticky ATC buttons already submit the same form via `form=` attribute; the intercept JS handles both paths.

### Color matching

Same 4-step algorithm used by cart upsell:
1. Read selected variant's color option value
2. Find scrunchie variant with matching color name → use it
3. Fallback: highest-inventory available scrunchie variant
4. Last resort: `scrunchie.selected_or_first_available_variant`

On variant change (customer picks a different color), the checkbox row updates:
- Scrunchie image (if color-specific images exist)
- Color label text
- Hidden variant ID

### Out of stock handling

- If ALL scrunchie variants are unavailable: hide the checkbox row entirely
- If the color-matched variant is unavailable but others exist: show the fallback variant with its color label

## Scope rules

Show the checkbox when ALL of these are true:
- `cross_sell_enabled` section setting is true
- `cross_sell_product` section setting is set (product exists)
- The current product is NOT the cross-sell product itself (no "add scrunchie" on the scrunchie PDP)
- The current template is NOT `product.bundle` (bundles have their own pricing)
- At least one variant of the cross-sell product is available

## Settings

### Theme settings (`settings_schema.json`)

Added to the LUSENA cart/upsell settings group:

```json
{
  "type": "number",
  "id": "lusena_cross_sell_price",
  "label": "Cena cross-sell (grosze)",
  "default": 3900,
  "info": "Musi odpowiadac rabatowi BXGY w Shopify admin (np. 3900 = 39 zl). Uzywane na PDP i w koszyku."
}
```

Single source of truth for the discounted price — used by PDP checkbox, cart drawer upsell, and cart page upsell.

### Section schema additions (`lusena-main-product.liquid`)

```json
{
  "type": "header",
  "content": "Cross-sell checkbox"
},
{
  "type": "checkbox",
  "id": "cross_sell_enabled",
  "label": "Pokazuj checkbox cross-sell w buy-boxie",
  "default": true
},
{
  "type": "product",
  "id": "cross_sell_product",
  "label": "Produkt cross-sell"
}
```

The price is read from the global theme setting `settings.lusena_cross_sell_price`, not duplicated here.

## Files

### New file

- `snippets/lusena-pdp-cross-sell-checkbox.liquid` — the checkbox row UI + color matching logic

### Modified files

- `sections/lusena-main-product.liquid` — render the new snippet between variant and ATC slots; add schema settings; pass cross-sell product data
- `snippets/lusena-pdp-scripts.liquid` — intercept ATC submit + Buy Now click to add scrunchie when checked; update scrunchie variant on color change
- `assets/lusena-pdp.css` — checkbox row styles; adjust `order` values for buy-box slots

### Cart upsell price sync

Update both cart upsell surfaces to display the cross-sell price (39 zl with 59 zl crossed out) instead of just the product price, for consistency with the PDP:
- `snippets/cart-drawer.liquid` — cross-sell card price area
- `sections/lusena-cart-items.liquid` — cross-sell card price area

Both read `settings.lusena_cross_sell_price` (the same global theme setting used by the PDP checkbox). When the cross-sell product matches the upsell product, show the discounted price with original crossed out.

## Testing matrix

| Product PDP | Checkbox visible? | + Scrunchie total | Clears 275? |
|-------------|-------------------|-------------------|-------------|
| Poszewka (269) | Yes | 308 zl | Yes |
| Bonnet (239) | Yes | 278 zl | Yes |
| Curlers (219) | Yes | 258 zl | No |
| Maska (169) | Yes | 208 zl | No |
| Scrunchie (59) | No (self) | — | — |
| Nocna Rutyna (399) | No (bundle) | — | — |
| Piekny Sen (349) | No (bundle) | — | — |
| Scrunchie Trio (139) | No (bundle) | — | — |

### Interaction tests

1. Check checkbox → click ATC → both items in cart, scrunchie at 39 zl (after BXGY discount)
2. Uncheck checkbox → click ATC → only main product in cart
3. Check checkbox → click Buy Now → both items added, redirect to checkout
4. Change variant color → scrunchie color label + variant ID updates
5. All scrunchie variants OOS → checkbox row hidden
6. Sticky ATC with checkbox checked → both items added
7. Cart drawer opens after cross-sell add → shows both items
8. Cart progress bar reflects correct total (after BXGY discount)

## Out of scope

- Cart upsell logic changes (waterfall, suppression rules) — no changes needed, existing suppression handles "already in cart"
- Scrunchie PDP changes — no cross-sell on the scrunchie page
- Bundle PDP changes — bundles have their own pricing system
- Shopify admin BXGY setup — already done by owner
- Free shipping threshold change — already done (275 zl in both admin and theme settings)
