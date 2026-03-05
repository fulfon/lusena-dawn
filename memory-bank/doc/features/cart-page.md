# Cart Page

*Migrated: 2026-03-05*

## Overview

Full-page cart (`/cart`) with visual parity to the cart drawer. Two LUSENA sections replace Dawn's `main-cart-items` and `main-cart-footer`.

## Files

| File | Purpose |
|------|---------|
| `sections/lusena-cart-items.liquid` | Items list, upsell cross-sell zone, cart header, empty state |
| `snippets/lusena-cart-quantity.liquid` | Quantity stepper (bordered group, icon buttons, "Usuń" text remove) |
| `sections/lusena-cart-footer.liquid` | Totals, free shipping bar, CTA, trust row, continue shopping |
| `templates/cart.json` | Wires the two sections; block order: `["subtotal", "buttons"]` |

## JS compatibility

Cart.js does NOT query table/tr/td — safe to use div-based flex layout. Preserved IDs, classes, and web components:
- **IDs:** `main-cart-items`, `CartItem-{N}`, `Quantity-{N}`, `Remove-{N}`, `Line-item-error-{N}`, `cart`, `checkout`
- **Classes:** `.js-contents`, `.cart-item`, `.cart__items--disabled`, `.loading__spinner`, `.cart-item__error-text`, `.cart-item__name`, `.is-empty`
- **Web components:** `<cart-items>`, `<cart-remove-button>`, `<quantity-input>`, `<quantity-popover>`, `<cart-note>`

## Layout architecture

### Viewport-fill strategy
- `<main>` gets `display: flex; flex-direction: column; min-height: 100dvh` — pushes site footer below fold on all screens
- **Mobile:** flex chain (`main` → `.shopify-section` → `cart-items` → `.lusena-container` → `form` → `#main-cart-items` → `.js-contents`) with `flex: 1` propagates height down; `margin-top: auto` on upsell pushes it to footer
- **Desktop:** cart content stays compact at top; remaining space is empty background below cart footer; site footer below fold

### Block reorder (CSS order)
Footer blocks render in HTML as: shipping bar → subtotal → buttons. CSS `order` reorders them visually: **Totals (-2) → Shipping (-1) → CTA (auto)** — matching the drawer.

### Border/line strategy
- Item separators: `border-bottom` on each `.lusena-cart-item` (except `:last-child`)
- Upsell top: `border-top` on `.lusena-cart-upsell` (full-bleed width via negative margins)
- Footer: NO `border-top` on `.lusena-cart-footer__inner` — upsell tinted background edge provides separation
- Totals: `border-top` on `.lusena-cart-totals` (right-aligned within footer blocks)

## Upsell cross-sell

Same waterfall logic as cart drawer:
1. Check global enable toggle + distinct-product suppression (threshold setting)
2. Find trigger product (hero role metafield → first item)
3. Resolve candidate: primary metafield → secondary → global fallback → DEV hardcoded fallback

**DEV-ONLY:** Hardcoded `all_products['the-compare-at-price-snowboard']` as last resort + hardcoded `'Beżowy'` color label. Must be replaced before production.

Custom JS on ATC button avoids opening the cart drawer (uses direct `/cart/add.js` fetch + page reload).

## Cart footer features

- **Free shipping bar:** Configurable threshold (`settings.lusena_free_shipping_threshold`), progress track with pill animation, truck icon, qualified state (green)
- **Gift note accordion:** Optional (`settings.lusena_enable_gift_mode`), `<details>` element
- **Trust row:** Shield-check icon + "60 dni na zwrot · Bezpieczna płatność"
- **Continue shopping:** Text link to `/collections/all`
- **Dynamic checkout buttons:** Rendered below CTA when available
