# Cart Page

*Migrated: 2026-03-05 | AJAX re-rendering: 2026-03-26*

## Overview

Full-page cart (`/cart`) with visual parity to the cart drawer. Two LUSENA sections replace Dawn's `main-cart-items` and `main-cart-footer`. Uses AJAX section re-rendering for all cart mutations (no full-page reloads). Bidirectional sync with cart drawer via pubsub.

## Files

| File | Purpose |
|------|---------|
| `sections/lusena-cart-items.liquid` | Items list, upsell cross-sell zone, cart header, empty state, AJAX re-render JS |
| `snippets/lusena-cart-quantity.liquid` | Quantity stepper (bordered group, icon buttons, "Usuń" text remove) |
| `sections/lusena-cart-footer.liquid` | Totals, free shipping bar, CTA, trust row, continue shopping |
| `assets/lusena-cart-page.css` | All cart page CSS (625 lines — extracted from `{% stylesheet %}` blocks 2026-03-26) |
| `templates/cart.json` | Wires the two sections; block order: `["subtotal", "buttons"]` |

## JS architecture

### AJAX section re-rendering (2026-03-26)
All cart mutations (bundle swap, cross-sell add, qty change) use Shopify's section rendering API instead of full-page reloads. Key functions in `lusena-cart-items.liquid`:
- `getSectionNames()` — returns array of section IDs to re-fetch (`cart-items`, `cart-icon-bubble`, `cart-live-region-text`, `cart-footer`)
- `getSectionConfigs()` — maps section IDs to DOM element IDs and selectors for innerHTML swap
- `reRenderSections(state)` — parses section HTML via DOMParser, swaps target element contents, toggles `.is-empty`
- `cart-items.onCartUpdate()` override — overrides Dawn's default to do full re-render including footer and empty state

### Bidirectional cart ↔ drawer sync
- Cart page publishes `PUB_SUB_EVENTS.cartUpdate` after mutations → drawer subscriber fetches fresh section HTML
- Drawer publishes `PUB_SUB_EVENTS.cartUpdate` after line changes → cart page `onCartUpdate()` re-renders
- Both use DOMParser to swap innerHTML of target containers

### Dawn patches
- `assets/cart.js` — null guard on `trapFocus` when `.drawer__inner-empty` is absent from DOM (prevents JS error when cart empties after AJAX re-render removes the element)

### Cart interaction locking during bundle swap (2026-03-29)
Bundle swaps (add bundle + remove individual) are multi-step operations. To prevent concurrent mutations:
- **Cart page:** `.cart__items--disabled` class on `#main-cart-items` — disables pointer events and reduces opacity on all cart items during swap.
- **Cart drawer:** `.lusena-cart-drawer__item--loading` class on all `[data-cart-item]` elements — same visual treatment.
- Cross-sell "Dodaj" button is NOT locked (independent single-add, doesn't conflict with swap).
- Lock applied at swap start, removed after AJAX section re-render completes.

### Cart drawer BXGY discount display
Cart drawer item prices check `item.original_line_price > item.final_line_price` first (automatic/BXGY discounts), then fall back to `item.variant.compare_at_price > item.variant.price` (permanent sale pricing). This ensures the cross-sell scrunchie at 39 zl (vs 59 zl) shows the correct strikethrough in the cart.

### JS compatibility
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

## Upsell system (unified `.lusena-upsell-card`)

*Updated: 2026-03-25*

Cart page and cart drawer share a unified upsell card system (`.lusena-upsell-card`). Two card types:

### Bundle nudge (two-tile)
Triggered when a bundle component product is in the cart. Uses `lusena.bundle_nudge_map` metafield (JSON: `{trigger-handle: {label, handle, tile_label?}}`).
- Gain-framed headline: "Dodaj {label} i zaoszczędź {X} zł"
- Two tiles: "have" tile (checkmark via `lusena-icon` snippet, product image) + "add" tile (plus sign, component image via `all_products[handle]`). Tiles centered via `justify-content: center` on `__bn-tiles`.
- Real product titles resolved via `all_products[nudge_entry.handle].title`
- Real product images via `added_component.featured_image`
- Swap via `LusenaBundle.swap()` in `assets/lusena-bundle-swap.js` (add bundle + remove individual)

### Cross-sell (single product)
Triggered for products with `lusena.upsell_primary` metafield. Fallback chain: primary → secondary → global setting.
- Product image + info + price in top row
- ATC button in full-width bottom row (`__xs-bottom`) — matches bundle card's `__bn-bottom` rhythm
- Cart page: direct `/cart/add.js` fetch + AJAX section re-render (avoids opening drawer)
- Loading state: standard `loading__spinner` + `lusena-btn__loading-dots` pattern (refactored 2026-03-29, was custom dot-pulse animation)

### Layout
- Cart drawer: upsell inside scrollable `.lusena-cart-drawer__body` (scrolls with items)
- Cart page: inside `.js-contents`, right-aligned at `max-width: 48rem` on desktop
- Compact layout for small screens (max-height: 700px): reduced padding, smaller images
- Image placeholders: `:empty { display: block }` overrides Dawn's `div:empty { display: none }`

### CSS placement
- Cart drawer: `<style>` tag in `snippets/cart-drawer.liquid` (~150 lines, not in compiled_assets). Selectors scoped under `.lusena-cart-drawer__upsell`.
- Cart page: `assets/lusena-cart-page.css` (standalone file, 625 lines — extracted 2026-03-26). Selectors scoped under `.lusena-cart-upsell`.

## Cart merge (#13) — 2026-03-28

Detects when both components of a bundle are separately in the cart and offers to combine them into the bundle at a discount.

### Detection logic (Liquid)
- Scans `cart.items` for handle combinations: `poszewka-jedwabna` + `czepek-jedwabny` → Nocna Rutyna (109 zl savings), `poszewka-jedwabna` + `jedwabna-maska-3d` → Piekny Sen (89 zl savings)
- Higher savings wins if multiple merges are possible
- Merge detection runs before regular bundle nudge — merge card takes priority

### Merge card UI
- Two "W koszyku" tiles showing the items already in cart (product images, titles, colors)
- Gain-framed headline: "Kup razem i zaoszczędź {X} zł"
- Single CTA button to merge into bundle
- Present in both `sections/lusena-cart-items.liquid` and `snippets/cart-drawer.liquid`

### Merge JS
- Removes both individual items (quantity 0 via `/cart/change.js`)
- Adds bundle via `LusenaBundle.swap()` with pre-filled Simple Bundles color properties from the individual items
- AJAX section re-render after swap completes
- Bidirectional sync: merge on cart page updates drawer, merge on drawer updates cart page

## Cart footer features

- **Free shipping bar:** Configurable threshold (`settings.lusena_free_shipping_threshold`, current value: 275 zl, changed from 269 on 2026-03-29), progress track with pill animation, truck icon, qualified state (green)
- **Gift note accordion:** Optional (`settings.lusena_enable_gift_mode`), `<details>` element
- **Trust row:** Shield-check icon + "60 dni na zwrot · Bezpieczna płatność"
- **Continue shopping:** Text link to `/collections/all`
- **Dynamic checkout buttons:** Rendered below CTA when available
