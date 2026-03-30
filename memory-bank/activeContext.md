# Active Context

*Last updated: 2026-03-30*

## Current focus

**Phase 1B: PDP cross-sell — COMPLETE.** All cross-sell touchpoints are live. Next: content polish, homepage bundles wiring, product media.

## Recent completed work

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
