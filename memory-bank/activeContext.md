# Active Context

*Last updated: 2026-03-29*

## Current focus

**Phase 1B: PDP cross-sell — COMPLETE.** All cross-sell touchpoints are live: PDP checkbox (all individual + bundle PDPs), scrunchie PDP education, cart drawer upsell. Remaining: documentation sweep (threshold 289->275 refs).

## Recent completed work

### Scrunchie PDP education (2026-03-29, session 4)

When a qualifying product is in the cart, the scrunchie PDP shows the discounted price (39 zl instead of 59 zl) with a personalized Polish hint.

**Architecture — server-side rendering + live JS sync:**
- **Server-side (no flash):** `lusena-main-product.liquid` checks `cart.items` via Liquid, maps handle to Polish instrumental case label, passes `education_active`, `education_price`, `education_label` to `lusena-pdp-summary.liquid`. Summary renders both price states (regular hidden or education hidden) on first paint.
- **Live sync:** `lusena-scrunchie-education.liquid` inline `<script>` subscribes to `PUB_SUB_EVENTS.cartUpdate`. On cart change, fetches `/cart.js`, re-evaluates qualifying items, toggles price display. Deferred subscription retry (`window.load`) handles PubSub not being loaded when inline script runs.
- **Sticky ATC:** MutationObserver on all `[data-lusena-sticky-price]` elements re-applies education price when `updateUIForVariant()` overwrites sticky text.

**Key decisions:**
- **Inline price swap (option C)** — no banners/cards, price itself IS the education. Premium brands adjust prices, not announce discounts.
- **Dynamic Polish text** — handle-to-label map with instrumental case (6 products + fallback). "Taniej z poszewka jedwabna w koszyku" feels curated, not generic.
- **Server-side rendering** — eliminates FOUC entirely. JS only for live cart sync.
- **Price order:** current (39 zl) left, compare (59 zl strikethrough) right — matches bundle PDP pattern.

**Files:**
- `snippets/lusena-scrunchie-education.liquid` — JS live sync (PubSub + cart check + sticky observer)
- `snippets/lusena-pdp-summary.liquid` — server-rendered education elements (data-lusena-education-row, data-lusena-education-hint)
- `sections/lusena-main-product.liquid` — server-side cart check + data-product-handle attribute + schema setting
- `assets/lusena-pdp.css` — education price CSS (mirrors __price + __compare-at styles)

### Bundle PDP cross-sell expansion (2026-03-29, session 3)

Extended the cross-sell checkbox to bundle PDPs (Nocna Rutyna, Piekny Sen). Scrunchie trio excluded (handle contains 'scrunchie').

**Key design decision:** Cross-sell appears AFTER all colors are picked (not immediately). Progressive disclosure: customer commits to bundle colors first, then sees the scrunchie offer as a final mini-step before ATC. This leverages sunk-cost psychology - they've invested time picking colors, so a 39 zl add feels trivial.

**Implementation:**
- Reused `lusena-pdp-cross-sell-checkbox` snippet with `skip_js: true` param (bundle scripts handle JS)
- Hidden initially (`lusena-bundle-cross-sell--hidden` class), revealed after `allSelected()` returns true
- 250ms stagger delay after last step collapse (matches step-to-step timing)
- LUSENA signature `translateY(-6px)` content fade on reveal
- JS-driven `openWrap()`/`closeWrap()` height animation (matching bundle step pattern)
- Color-matches scrunchie to last-picked bundle item color
- Stays visible during re-edits (only animates on initial reveal)
- Color indicator in placeholder when no variant images exist
- `submitBundleCartWithCrossSell()` sends JSON `items` array with bundle properties preserved
- `submitBundleBuyNowWithCrossSell()` for Buy Now + cross-sell -> checkout redirect
- Schema: `cross_sell_enabled`, `cross_sell_handle`, `cross_sell_price` (same as single PDP)

### PDP cross-sell checkbox — UI/UX redesign (2026-03-29, session 2)

Full visual redesign of the cross-sell card to match LUSENA's premium aesthetic.

### PDP cross-sell checkbox — core implementation (2026-03-29, session 1)

Cross-sell checkbox on all individual product PDPs offering scrunchie at 39 zl (BXGY discount in Shopify admin).

## Next steps

1. **Documentation sweep** — threshold 289->275 refs across bundle-strategy.md, upsell-strategy.md, product docs (50+ references)

## Decided: skip cart discount explanation

Cart line-item label ("Rabat za zakup w zestawie") is unnecessary because every path into the cart already explains the discounted price: PDP checkbox, cart upsell card, and scrunchie PDP education. A cart label would add visual noise for zero benefit.

## Known issues

- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` is a doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- **Swap race condition:** If `/cart/add.js` succeeds but `/cart/change.js` fails, customer has both items in cart. #13 cart merge handles this - the merge card appears on next render, offering to combine them.
- **Trigger item quantity > 1:** Swap removes all units (quantity 0), not just 1.
- **Cart color editing:** Bundle added via nudge auto-matches colors. Customer cannot change colors in cart — must use bundle PDP.

## Architecture note

**Cart drawer is now a section** (not a snippet render). `theme.liquid` uses `{%- section 'cart-drawer' -%}`. This enables Shopify's section rendering API for AJAX updates.

**Cross-sell checkbox architecture:**
- **Shared snippet:** `lusena-pdp-cross-sell-checkbox.liquid` renders HTML + variant data JSON for both single PDPs and bundles
- **Single PDP JS:** inline `<script>` in the snippet (ATC intercept on `<product-form>`, variant change listener)
- **Bundle PDP JS:** `lusena-bundle-scripts.liquid` handles everything (reveal on `allSelected()`, color match, `submitBundleCartWithCrossSell()`)
- **`skip_js` param:** when `true`, snippet skips inline script (bundle provides its own JS)

**Scrunchie PDP education architecture:**
- **Server-side:** `lusena-main-product.liquid` checks `cart.items`, passes education state to `lusena-pdp-summary.liquid`
- **Summary snippet:** renders both price rows (regular + education) with initial visibility from server state
- **Education script:** `lusena-scrunchie-education.liquid` handles live sync only (PubSub subscriber + cart check + sticky MutationObserver)
- **No FOUC:** correct price rendered on first paint, JS only for dynamic cart changes

**Upsell card CSS scoping:**
- Cart drawer: `<style>` tag in `snippets/cart-drawer.liquid`. All upsell selectors scoped under `.lusena-cart-drawer__upsell`.
- Cart page: `assets/lusena-cart-page.css` (standalone file). Upsell selectors scoped under `.lusena-cart-upsell`.

**Bidirectional cart sync:**
- Cart page -> drawer: publishes `PUB_SUB_EVENTS.cartUpdate`, drawer subscriber fetches fresh section HTML
- Drawer -> cart page: publishes `PUB_SUB_EVENTS.cartUpdate`, cart page `onCartUpdate()` override fetches sections
- Both use `DOMParser` to swap inner HTML of target containers
