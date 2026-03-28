# Active Context

*Last updated: 2026-03-28*

## Current focus

**#13 Cart merge is the next task.** Detect when both bundle components are in cart separately, show a "Zamien na zestaw i zaoszczedz X zl" card using the existing cart nudge UI and `LusenaBundle.swap()`. This replaces the abandoned #12 PDP banner approach.

## Recent completed work

### Homepage benefit bridge + reorder (2026-03-28)

**New section: `lusena-benefit-bridge`:**
- "Co zmieni się po pierwszej nocy?" heading + 3 benefit cards
- Cards: "Gładka skóra o poranku" (sparkles), "Włosy bez porannego chaosu" (star), "Krem pracuje całą noc" (droplets)
- Copy written by Polish copywriter subagent, legally checked, persona-validated
- Standard spacing tier, brand background, teal icon circles, scroll animations
- Mobile: stacked with separators between cards

**Homepage reorder:**
- Benefit bridge at position 3 (NEW)
- Bestsellers stays at 4, Testimonials at 5
- Problem/Solution moved from 3 to 6 (evaluation-mode section)
- P/S background changed from `brand` to `surface-1` for clean alternation

**P/S copy refresh (4 items rewritten):**
- Removed "roztocza" and unsubstantiated "białka jedwabiu" claims
- Shortened all items to 1 sentence
- Kept "rzep" metaphor (strongest per all 4 personas) and "krem pracuje dla poduszki" reframe
- Added proper hedging ("sprzyja redukcji", "pomaga zachować")

**Research backing:**
- 4 independent customer personas evaluated original P/S section (avg scores: persuasion 6.0, emotion 4.5, premium 5.5)
- CRO research: social proof in positions 3-4 delivers +18-27% conversion lift
- No successful silk brand (Slip, Blissy, Fishers Finery) leads with problem/solution after hero


### #12 PDP bundle detection banner — ABANDONED (2026-03-28)

**What we tried:** A banner between variant picker and ATC on the PDP buy-box that detects cart complement via `fetch('/cart.js')` and offers one-click swap to bundle. Fully implemented (snippet + CSS + JS), committed, and tested on preview theme.

**Why abandoned:** The PDP buy-box is already dense (summary, chips, variant picker, ATC, guarantee, payment, benefits, accordion). Adding any element between variant picker and ATC — even a compact card without zone wrapper — disrupts the purchase flow and adds visual noise at the critical decision point. Tested both a full zone layout and a stripped-down inline card; neither fit.

**Decision:** Use #13 (cart merge) instead. The cart is where the customer reviews their purchase — a "combine these into a bundle and save" message fits naturally there. The existing cart nudge card system is already proven. All code was cleanly reverted (snippet deleted, section render line removed, CSS removed). Spec and plan docs remain in `docs/superpowers/specs/` and `docs/superpowers/plans/` as decision history.

**Bundle mapping (still valid for #13):** poszewka + bonnet → Nocna Rutyna (saves 109 zl), poszewka + maska → Piekny Sen (saves 89 zl). Scrunchie Trio not applicable (same-product bundle). Conflict: higher savings wins.

### End-to-end manual testing — ALL PASSED (2026-03-28)

Full test matrix executed manually, all scenarios passing:
- **Bundle nudge cards:** Poszewka → Nocna Rutyna, Bonnet → Nocna Rutyna, Maska 3D → Piekny Sen, Scrunchie → Scrunchie Trio — correct pricing and savings on all
- **Regular cross-sell:** Walek → Scrunchie at 59 zl (only product with non-bundle primary)
- **Bundle swaps:** All 4 swap directions working (poszewka, bonnet, maska, scrunchie triggers)
- **Smart suppress:** Nocna Rutyna/Piekny Sen in cart suppresses all upsells. Scrunchie Trio does not suppress. 2 distinct items suppresses regular cross-sell but allows bundle nudge through.
- **Cart page AJAX:** Re-renders without full page reload for swaps, quantity changes, removes
- **Bidirectional sync:** Cart page ↔ drawer sync working

### Cart AJAX re-rendering + CSS extraction + polish (2026-03-26/27)

**CSS extraction (compiled_assets truncation fix):**
- Extracted cart items/footer/quantity CSS from `{% stylesheet %}` → `assets/lusena-cart-page.css` (634 lines)
- Extracted search page CSS from `{% stylesheet %}` → `assets/lusena-search.css` (156 lines)
- compiled_assets reduced from ~85KB (truncated) to ~59KB (safe margin)
- All original `{% stylesheet %}` blocks replaced with `/* CSS extracted to ... */` comments

**Cart page AJAX section re-rendering (replaces full-page reloads):**
- Added `reRenderSections()` with `getSectionConfigs()` and `getSectionNames()` helpers
- Bundle swap and cross-sell add now use Shopify section rendering API (`sections` param)
- Override of `cart-items.onCartUpdate()` for full re-render: items + footer + empty state toggle
- Cart page publishes `PUB_SUB_EVENTS.cartUpdate` for bidirectional sync with drawer

**Cart drawer → section promotion:**
- `theme.liquid`: changed `render 'cart-drawer'` to `section 'cart-drawer'` — enables section rendering API

**Cart drawer improvements:**
- Per-item loading state: `.lusena-cart-drawer__item--loading` with opacity fade during qty changes
- `enableItemLoading()` / `disableItemLoading()` helpers with button disable/enable
- Bidirectional sync: drawer re-renders when cart page changes cart (pubsub subscriber)
- Fixed `pubsub.js` race condition — wrapped subscribers in `DOMContentLoaded` handler
- Scoped all upsell CSS selectors to `.lusena-cart-drawer__upsell` (prevents bleed to cart page)
- CSS refinements: item info `justify-content: flex-start`, item name font-family/letter-spacing, price `display: block`/`line-height`, remove button `min-height: auto`, shipping bar selector specificity

**Cart item properties enhancement:**
- Properties wrapped in `.lusena-cart-item__properties` container with pre-check for visibility
- Property labels cleaned up: split on ` - ` and ` (` to remove bundle suffixes
- Values escaped for XSS safety

**Money filter & copy normalization:**
- `money`/`money_with_currency` → `money_without_trailing_zeros` across cart (footer, items)
- Price-per-night suffix: `" / noc"` → `"/noc"` (PDP section, sticky ATC, product card, product.json)
- Typo fix: "zaoszczedz" → "zaoszczędź" (proper Polish ę) in cart drawer and cart items

**PDP fixes:**
- Removed scroll-trigger animation from payment badges (should render statically)
- Proof chips: `requestAnimationFrame(balance)` → `balance()` (synchronous)

**Button system & animations:**
- Spinner uses opacity cross-fade instead of display toggle; overrides Dawn's `.hidden {display:none!important}`
- `animations.js`: children of `[data-cascade]` containers get stagger order via `closest()` check

**Documentation reorganization:**
- 30+ files deleted from `docs/` (completed parity plans, old references, migration plans)
- Key docs relocated: brand → `memory-bank/doc/brand/`, product refs → `memory-bank/doc/products/`, templates → `memory-bank/doc/patterns/`
- Changelog deleted: `memory-bank/doc/changelog/theme-changes.md`
- Path references updated in CLAUDE.md, AGENTS.md, copilot-instructions.md, all skill files

## Next steps

1. **#13 Cart merge (NEXT TASK)** — detect when both bundle components are in cart separately (e.g., poszewka + bonnet), show "Zamien na zestaw i zaoszczedz 109 zl" card in cart drawer and cart page. Use existing cart nudge UI and `LusenaBundle.swap()`. Mapping: poszewka+bonnet → Nocna Rutyna (109 zl), poszewka+maska → Piekny Sen (89 zl). Also handles swap race condition (add succeeds, remove fails → both items in cart).
2. **Phase 1B: PDP cross-sell checkbox** — scrunchie at 39 zl on poszewka PDP

## Known issues

- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` is a doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- **Swap race condition:** If `/cart/add.js` succeeds but `/cart/change.js` fails, customer has both items in cart. #13 (cart merge) will handle this.
- **Trigger item quantity > 1:** Swap removes all units (quantity 0), not just 1.
- **Cart color editing:** Bundle added via nudge auto-matches colors. Customer cannot change colors in cart — must use bundle PDP.

## Architecture note

**Cart drawer is now a section** (not a snippet render). `theme.liquid` uses `{%- section 'cart-drawer' -%}`. This enables Shopify's section rendering API for AJAX updates.

**Upsell card CSS scoping:**
- Cart drawer: `<style>` tag in `snippets/cart-drawer.liquid`. All upsell selectors scoped under `.lusena-cart-drawer__upsell`.
- Cart page: `assets/lusena-cart-page.css` (standalone file). Upsell selectors scoped under `.lusena-cart-upsell`.
- This prevents CSS bleed between drawer (loads on every page) and cart page (loads only on /cart).

**Bidirectional cart sync:**
- Cart page → drawer: publishes `PUB_SUB_EVENTS.cartUpdate`, drawer subscriber fetches fresh section HTML
- Drawer → cart page: publishes `PUB_SUB_EVENTS.cartUpdate`, cart page `onCartUpdate()` override fetches sections
- Both use `DOMParser` to swap inner HTML of target containers
