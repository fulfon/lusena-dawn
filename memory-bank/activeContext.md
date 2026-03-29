# Active Context

*Last updated: 2026-03-29*

## Current focus

**Phase 1B: PDP cross-sell checkbox — NEARLY COMPLETE.** Core feature works on all individual PDPs and bundle PDPs. UI redesigned and polished. Remaining: scrunchie PDP education (show discount info when qualifying product is in cart).

## Recent completed work

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
- `submitBundleBuyNowWithCrossSell()` for Buy Now + cross-sell → checkout redirect
- Schema: `cross_sell_enabled`, `cross_sell_handle`, `cross_sell_price` (same as single PDP)

**Verification completed:**
- Buy Now + Sticky ATC work with checkbox checked (single PDPs)
- Scope: hidden on scrunchie PDP (`product.handle != cs_handle`) and bundle PDPs (separate section)
- BXGY admin discount covers Nocna Rutyna + scrunchie and Piekny Sen + scrunchie

### PDP cross-sell checkbox — UI/UX redesign (2026-03-29, session 2)

Full visual redesign of the cross-sell card to match LUSENA's premium aesthetic:

**Design decisions:**
- **White card** with 3px teal left accent (`color-mix(... accent-cta 40% ...)`, full on hover/check)
- **Compact single row:** checkbox (16px) + image (40px) + title/hint + pricing
- **"Taniej w komplecie"** educational hint instead of "Kolor:" text
- **Image-only color communication** — no color text label; image auto-matches when main product color changes
- **Image placeholder** always renders (`surface-2` bg + dashed border, matching cart drawer upsell pattern)
- **Color indicator** in placeholder shows variant color name when no image exists (hidden via `img~` sibling selector when image loads)
- **Strikethrough price** matches cart drawer style (1.2rem, `text-2`, no opacity reduction)
- **Scroll animation** — `scroll-trigger animate--slide-in` gated by `animations_reveal_on_scroll`
- **Spacing** — `margin-top: 1.6rem` on wrapper, matching buy-box rhythm

**Bug fixes (same session):**
- **Button loading animation** — `setBtnLoading()` helper targets actual `<button>` (was targeting `<product-form>` wrapper, no animation played)
- **Double-add bug** — removed duplicate cross-sell handler from `lusena-pdp-scripts.liquid` `{% javascript %}` block (code was NOT dead as assumed — compiled_assets JS included it)
- **Double-click guard** — `aria-disabled` check at top of both ATC and Buy Now handlers
- **Idempotency guard** — `data-lusena-cross-sell-init` prevents re-initialization on hot reload

### PDP cross-sell checkbox — core implementation (2026-03-29, session 1)

Cross-sell checkbox on all individual product PDPs offering scrunchie at 39 zl (BXGY discount in Shopify admin).

**Strategic decisions (changed from original plan):**
- **All individual PDPs** (not poszewka-only) — consistent pricing builds trust for new brand
- **Free shipping threshold 275 zl** (was 289) — bonnet (239) + scrunchie (39) = 278 > 275 clears threshold
- **Shopify BXGY automatic discount** handles real pricing; theme displays preview price via section setting

**Key technical decisions (discovered during implementation):**
- `all_products[handle]` instead of product picker setting — Shopify dev server doesn't resolve product picker GIDs from file sync
- Inline `<script>` instead of `{% javascript %}` — compiled_assets JS truncation (same ~73KB limit as CSS)
- `/cart/add.js` instead of `/cart/add` — dev server returns 302 without `.js` extension
- ATC intercept on parent `<product-form>` element with `{ capture: true }` — at the target element, capture doesn't help
- Cart drawer re-render via direct section fetch + `DOMParser` + `drawer.open()`

### Earlier work (2026-03-29, session 1)

- **Benefit bridge redesign** — kicker, featured card, accent bar, transition text, standalone CSS
- **`lusena-link-arrow` CSS component** — replaces all hardcoded `→` arrows sitewide
- **Bundle options initial state** — first step open, others collapsed with pending chips
- **Bundle PDP chip dot fix** — pending dot: transparent outline instead of filled
- **Cart cross-sell loading refactor** — standard `loading__spinner` pattern
- **Token compliance rule** — mandatory design token usage in CSS
- **No-inline-scripts rule** — bans `node -e`/`python -c` for file analysis
- **Section design loop skill** — autonomous design iteration with 5-agent review
- **Migration lessons #55-61** — benefit bridge redesign lessons

## Next steps

1. **Cross-sell: Scrunchie PDP education** — show discount info on scrunchie PDP when qualifying product is in cart (JS reads `/cart.js`, checks for qualifying handles)
2. **Documentation sweep** — threshold 289→275 refs across bundle-strategy.md, upsell-strategy.md, product docs (50+ references)

## Decided: skip cart discount explanation

Cart line-item label ("Rabat za zakup w zestawie") is unnecessary because every path into the cart already explains the discounted price: PDP checkbox, cart upsell card, and (upcoming) scrunchie PDP education. A cart label would add visual noise for zero benefit.

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

**Upsell card CSS scoping:**
- Cart drawer: `<style>` tag in `snippets/cart-drawer.liquid`. All upsell selectors scoped under `.lusena-cart-drawer__upsell`.
- Cart page: `assets/lusena-cart-page.css` (standalone file). Upsell selectors scoped under `.lusena-cart-upsell`.

**Bidirectional cart sync:**
- Cart page → drawer: publishes `PUB_SUB_EVENTS.cartUpdate`, drawer subscriber fetches fresh section HTML
- Drawer → cart page: publishes `PUB_SUB_EVENTS.cartUpdate`, cart page `onCartUpdate()` override fetches sections
- Both use `DOMParser` to swap inner HTML of target containers
