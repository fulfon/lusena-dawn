# Active Context

*Last updated: 2026-04-03*

## Current focus

**Phase 1B: PDP cross-sell — COMPLETE.** All cross-sell touchpoints are live and QA-tested. Next: content polish, homepage bundles wiring, product media.

## Recent completed work

### QA fixes — upsell/bundle test findings (2026-04-03)

Comprehensive QA test plan executed (84 tests, all passing). 7 findings documented, 4 fixed:
- **F1+F7:** Scrunchie education handle mismatches — `jedwabna-maska-do-spania-3d` → `jedwabna-maska-3d`, `jedwabny-walek-do-lokow` → `heatless-curlers` in both Liquid case statement (`lusena-main-product.liquid`) and JS label map (`lusena-scrunchie-education.liquid`).
- **F5:** Cart cross-sell card showed scrunchie at 59 zl instead of 39 zl. Added `lusena_cart_cross_sell_price` theme setting (default 3900). Cart drawer and cart page now show current price first, crossed-out original second, with "Taniej w komplecie" education text.
- **F6:** Bundle swap nudge button stopped working after first successful swap. Added `swapInProgress` guard flag in both cart drawer and cart page — resets on both success and error paths.
- **Compare price styling unified** — cross-sell card now matches bundle/cart-item pattern: 1.2rem, `--lusena-text-2`, 50% opacity strikethrough. Price order standardized: [current] [~~original~~] across all 8 locations.
- **F3+F4:** Confirmed intentional per bundle strategy docs (scrunchie→Trio nudge, no nudge after re-add post-swap).
- Test plan: `docs/qa-test-plan.md`

### Cart/ATC error handling hardening (2026-04-02)

- **User-visible error feedback** on all ATC failure paths: Polish error text ("Coś poszło nie tak") shown on button for 3s with red `.lusena-btn--error` state, then auto-restores. Covers: bundle ATC (4 paths), cross-sell checkbox ATC+Buy Now (4 paths), cart page upsell add, cart page bundle swap, cart drawer bundle swap.
- **`response.ok` check** added to cart-drawer `updateLine` - was silently passing Shopify 422/5xx responses to `renderContents`. Now throws to catch block, consistent with `lusena-bundle-swap.js` pattern.
- **`.catch()` added** to 4 secondary fetch calls (cart-drawer + icon-bubble re-renders in cross-sell-checkbox and bundle-scripts) that had no error handling.
- **Sticky ATC coverage** - single PDP sticky buttons (mobile + desktop) now show error feedback alongside main ATC, matching bundle PDP behavior.
- `.lusena-btn--error` CSS class added to `lusena-button-system.css`.
- 5 files changed (+88 lines): `lusena-button-system.css`, `lusena-cart-items.liquid`, `cart-drawer.liquid`, `lusena-bundle-scripts.liquid`, `lusena-pdp-cross-sell-checkbox.liquid`.

### Worktree launcher: smart resume + auto-cleanup (2026-04-02)

- **Smart resume:** [R] now launches `claude --name` (fresh) for empty worktrees (0 commits, no changes) instead of broken `claude --resume`. Non-empty worktrees still use `--resume`.
- **Auto-cleanup:** After Claude exits, `Invoke-AutoCleanup` checks if the branch was squash-merged to main (has commits + content matches main + no uncommitted changes). If all conditions met, worktree and branch are removed automatically. Otherwise does nothing.
- CLAUDE.md updated to document both behaviors.
- One file changed: `scripts/launch-claude-worktree.ps1` (+50 lines)

### Sticky ATC scrollbar shift fix (2026-04-01)

- Fixed sticky ATC bar shifting ~15px right when cart drawer opens (scrollbar disappearance widens viewport for `position: fixed` elements)
- Added `body.overflow-hidden .lusena-sticky-atc { right: var(--scrollbar-width, 0px); }` to `lusena-pdp.css` — consumes the CSS variable Dawn's `cart-drawer.js` already sets
- One file changed: `assets/lusena-pdp.css` (+4 lines)

### PDP sticky gallery boundary fix (2026-04-01)

- Gallery bottom now aligns with the care card (Pielegnacja) bottom border instead of the grid/section edge
- Added `contain: layout` to `.lusena-grid--pdp` (ensures grid is the sticky containing block)
- Added `padding-bottom: var(--lusena-space-4)` to `.lusena-gallery` on desktop — invisible padding offsets the sticky stop point by 32px to match the last accordion item's `margin-bottom`
- Applies to both standard and bundle PDPs (shared `.lusena-pdp` ancestor)
- One file changed: `assets/lusena-pdp.css` (+10 lines)

### Primary button loading state fix (2026-03-31)

- `.lusena-btn--primary.loading` rule added to `lusena-button-system.css` — preserves teal background when `aria-disabled` and `.loading` coexist
- Affected: PDP ATC, bundle ATC, both sticky ATC bars (all went gray during shimmer due to CSS specificity: disabled state at 0-2-0 overrode loading state)
- Upsell/nudge outline buttons audited — already correct (outline loading `!important` handles it)

### Checkout button fix + loading animation (2026-03-30)

- **Root cause:** `routes.checkout_url` is not a valid Shopify Liquid property — rendered to empty string, making cart drawer `<a href="">` reload current page instead of navigating to checkout
- **Cart drawer:** Replaced `<a>` with `<button data-lusena-drawer-checkout>` + JS `window.location.href = '/checkout'` + loading animation (shimmer + "Przekierowuję..." text swap) + bfcache reset
- **Cart page:** Added loading animation markup + JS to existing submit button
- **theme.liquid:** Hardcoded `/checkout` in `window.routes.checkout_url`
- **Workflow:** CLAUDE.md Browser Interactions section now points to `/lusena-preview-check`. Skill updated to instruct subagent to load `/playwright-cli` first.

### PDP sticky gallery (2026-03-30)

Swapped desktop sticky behavior: gallery (left column) is now `position: sticky` instead of buybox (right column). Gallery stays pinned at `top: 12.8rem` while user scrolls through the taller buybox content. Applies to both standard and bundle PDPs via shared `.lusena-pdp .lusena-gallery` selector. One CSS file changed: `assets/lusena-pdp.css`.

### Phase D cross-sell (2026-03-29) — all 4 sessions consolidated

All PDP cross-sell touchpoints shipped in one day:
1. **PDP cross-sell checkbox** — scrunchie at 39 zl (BXGY) on all individual PDPs + bundle PDPs. White card, teal accent, custom checkbox, color-matched image.
2. **Bundle PDP cross-sell timing** — checkbox reveals after all colors are picked (sunk-cost psychology), with LUSENA signature `translateY(-6px)` slide-in animation.
3. **Scrunchie PDP education** — server-side price swap (39 zl instead of 59 zl) when qualifying product is in cart. Dynamic Polish hint. No FOUC via Liquid-rendered initial state. Live sync via PubSub + MutationObserver.
4. **Cart interaction locking** — full-cart lock during bundle swaps prevents concurrent mutations.

Full architecture details: `memory-bank/doc/features/pdp.md` (cross-sell, education) and `memory-bank/doc/features/cart-page.md` (locking, merge).

### Documentation sweep (2026-03-30)

Comprehensive memory bank audit covering 67 commits. Updated:
- Free shipping threshold 289 -> 275 across all strategy docs, product docs, rules (18 stale refs fixed)
- Cross-sell checkbox + scrunchie education added to systemPatterns.md component systems
- Cross-sell flow added to productContext.md customer journey
- Cart interaction locking added to cart-page.md
- PDP CSS size ~34KB -> ~42KB, foundations ~40KB -> ~50KB across all references
- Upsell strategy roadmap phases marked DONE with actual completion dates
- activeContext consolidated from 4 sessions to summary + architecture pointers

### Earlier in commit range (2026-03-28)

- Benefit bridge, cart merge (#13), card 5 sessions, accordion rewrite, 3 icons, link-arrow, Claude Code infra, migration lessons #55-61
- Full details in `progress.md`

## Next steps

1. Homepage bundles section — wire up real products (Phase C remaining)
2. Bundle product media (when physical products arrive)
3. Content polish — review all page copy for consistency
4. UX backlog items (mobile header icons, bonnet naming, value anchors expansion)

## Key decisions (reference)

- **Skip cart discount explanation** — every path into cart already explains the 39 zl price. Cart label adds noise for zero benefit.
- **Cross-sell on bundles: post-color timing** — appears after `allSelected()`, not immediately. Sunk-cost > impulsive.
- **Scrunchie education: inline price swap** — no banners/cards, price itself IS the education. Premium brands adjust prices, not announce discounts.
- **Free shipping threshold: 275 zl** (was 289, originally 269. Updated in settings_schema, settings_data, and all strategy/product docs)
- **Compare price order: [current] [~~original~~]** — consistent across all 8 locations (PDP, cart items, upsell cards, product cards). Established as theme standard.

## Known issues

- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` is a doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- **Swap race condition:** If `/cart/add.js` succeeds but `/cart/change.js` fails, customer has both items in cart. #13 cart merge handles this - the merge card appears on next render, offering to combine them.
- **Trigger item quantity > 1:** Swap removes all units (quantity 0), not just 1.
- **Cart color editing:** Bundle added via nudge auto-matches colors. Customer cannot change colors in cart — must use bundle PDP.

## Architecture notes (quick reference)

Architecture details live in the feature docs. Quick pointers for orientation:
- **Cross-sell checkbox architecture:** `systemPatterns.md` § Component systems
- **Scrunchie education architecture:** `systemPatterns.md` § Component systems
- **Cart upsell/merge/sync:** `memory-bank/doc/features/cart-page.md`
- **Cart drawer = section** (not snippet render): `theme.liquid` uses `{%- section 'cart-drawer' -%}` for section rendering API
- **Upsell CSS scoping:** drawer under `.lusena-cart-drawer__upsell`, cart page under `.lusena-cart-upsell`
- **Bidirectional cart sync:** PubSub + DOMParser innerHTML swap (details in cart-page.md)
