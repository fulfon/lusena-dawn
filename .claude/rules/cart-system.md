---
paths:
  - "sections/*cart*"
  - "snippets/*cart*"
  - "assets/*cart*"
  - "assets/*bundle*"
  - "assets/lusena-bundle*"
---
# Cart System Architecture

## Key structural facts
- **Cart drawer is a `section`** (not a snippet). `theme.liquid` uses `{%- section 'cart-drawer' -%}`. This enables section rendering API for AJAX updates.
- **Cart page:** `lusena-cart-items.liquid` (items + empty state), `lusena-cart-footer.liquid` (totals + checkout). Standalone CSS in `assets/lusena-cart-page.css` (634 lines).

## AJAX re-rendering
Both cart page and drawer use Shopify's section rendering API (`?sections=` param). `reRenderSections()` fetches HTML, `DOMParser` swaps inner content. Cart page overrides `cart-items.onCartUpdate()`.

## Bidirectional pubsub sync
- Page -> drawer: publishes `PUB_SUB_EVENTS.cartUpdate`, drawer subscriber fetches fresh HTML
- Drawer -> page: same event, cart page `onCartUpdate()` fetches sections
- `pubsub.js` subscribers wrapped in `DOMContentLoaded` (race condition fix)

## Upsell CSS scoping (prevents bleed)
- **Drawer:** `<style>` in `snippets/cart-drawer.liquid`, selectors under `.lusena-cart-drawer__upsell`
- **Cart page:** `assets/lusena-cart-page.css`, selectors under `.lusena-cart-upsell`
- Drawer loads on every page; cart page only on /cart. Scoping prevents cross-contamination.

## Bundle swap
- `assets/lusena-bundle-swap.js` — add then remove (not atomic). Known race condition: add succeeds, change fails = both items in cart. Cart merge (#13) will handle this.
- Preserved Dawn IDs/classes for JS compatibility (`cart-drawer`, `cart-items`).

## Interaction locking during swap
Bundle swap mutates the entire cart (add + remove), so all interactions are locked during the swap to prevent concurrent mutations:
- **Cart page:** `cart__items--disabled` class on `#main-cart-items` (pointer-events: none, opacity 0.5). Must be explicitly removed on success (container element survives `reRenderSections` innerHTML swap).
- **Cart drawer:** `lusena-cart-drawer__item--loading` class on ALL `[data-cart-item]` rows + all buttons disabled. Cleaned up naturally on success (full DOM replacement via `renderContents`).
- **Cross-sell "Dodaj" button:** NOT locked during swap — single `/cart/add.js` call doesn't conflict with existing item mutations. Self-disables to prevent double-clicks.
- **Qty/remove operations:** Cart page uses Dawn's `cart__items--disabled` (global lock). Drawer uses per-row `enableItemLoading`/`disableItemLoading` (scoped lock).
