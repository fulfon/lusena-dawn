# #13 Cart Merge - Design Spec

## Goal

When both bundle components are in the cart as separate items (e.g., poszewka + bonnet), show a merge card that lets the customer combine them into the bundle and save money. This replaces the two individual line items with a single bundle line item via `LusenaBundle.swap()`.

## Why this exists

1. **Missed nudge path**: Customer may add both components independently, bypassing the existing bundle nudge (which suggests adding the complement).
2. **Swap race condition**: If a previous `LusenaBundle.swap()` call partially fails (add succeeds, remove fails), both individual items end up in cart alongside nothing — the merge card gives a clean recovery.
3. **Existing nudge bug**: When both components are in cart, the current nudge still shows "Dodaj bonnet" even though bonnet is already there. Clicking it would add the bundle but only remove the trigger, leaving a duplicate. The merge card replaces this broken state with the correct action.

## Bundle mapping

| Components in cart | Target bundle | Handle | Savings |
|---|---|---|---|
| `poszewka-jedwabna` + `silk-bonnet` | Nocna Rutyna | `nocna-rutyna` | 109 zl |
| `poszewka-jedwabna` + `jedwabna-maska-3d` | Piekny Sen | `piekny-sen` | 89 zl |

Scrunchie Trio is excluded (same-product bundle - can't detect "3 scrunchies" since they share a product handle).

**Conflict resolution**: If all three components are in cart (poszewka + bonnet + maska), only the highest-savings merge shows. Nocna Rutyna (109 zl) always wins over Piekny Sen (89 zl). One card only.

## Detection logic

Liquid-side detection during section render (same pattern as existing nudge). Runs in both cart drawer (`snippets/cart-drawer.liquid`) and cart page (`sections/lusena-cart-items.liquid`).

**Execution order:**
1. Loop `cart.items`, flag which component handles are present, store their item references (key, variant, color)
2. Check merge pairs (highest savings first): poszewka+bonnet, then poszewka+maska
3. For each pair: verify both components present AND target bundle NOT already in cart
4. First valid pair wins - render merge card, skip entire regular nudge waterfall
5. If no merge found - fall through to existing nudge waterfall (unchanged)

**Savings computation**: Computed dynamically. `bundle_original_price` metafield is in zl (integer, e.g., 508). `product.price` is in cents (e.g., 39900). Savings in cents = `bundle_original_price * 100 - product.price`. Display with `money_without_trailing_zeros` filter. Not hardcoded - updates automatically if prices change.

## Card UI

Reuses the existing bundle nudge card structure (Option A from brainstorming).

**Zone wrapper**: Same as existing nudge — `.lusena-cart-drawer__upsell` (drawer) / `.lusena-cart-upsell` (cart page).

**Zone label**: "Korzystniej w zestawie" (unchanged).

**Card container**: `.lusena-upsell-card` with `data-bundle-nudge` and merge-specific data attributes.

**Headline**: "Zamien na zestaw i zaoszczedz {savings}" — uses `money_without_trailing_zeros` filter.

**Two tiles** (both show "W koszyku" badge):
- Left tile: component 1 image (38px) + product title + "W koszyku" checkmark
- Right tile: component 2 image (38px) + product title + "W koszyku" checkmark
- Plus sign between tiles

Note: both tiles use the smaller 38px image size (like the existing "have" tile), since both items are already in cart. The existing nudge uses 38px for "have" and 56px for "add" — here there is no "add" tile.

**Bottom bar**: bundle price + crossed-out original + "Zamien na zestaw" CTA button.

**Button style**: `lusena-btn lusena-btn--outline lusena-btn--size-xs` (same as existing nudge, outline style for consistency).

## Data attributes

The merge card reuses `data-bundle-nudge` and `data-bundle-nudge-action` (same as existing nudge) with two additional attributes that signal the merge path:

| Attribute | Existing nudge | Merge card |
|---|---|---|
| `data-bundle-nudge` | present | present |
| `data-bundle-variant-id` | bundle variant ID | same |
| `data-replace-key` | single item key | absent |
| `data-replace-keys` | absent | JSON array of both item keys |
| `data-trigger-color` | single color string | absent |
| `data-property-map` | JSON array of slots + available values | absent |
| `data-properties` | absent | JSON object of final properties (pre-filled) |
| `data-bundle-nudge-action` | on CTA button | same |

**JS handler modification**: The existing click handler checks for `data-replace-keys` first. If present, it's the merge path — parse JSON array for removeKeys, use `data-properties` directly (no color matching needed). If absent, fall through to existing single-key path with color matching. One handler, minimal branching.

## Color matching

For the merge card, both items' colors are known at Liquid render time (read from each cart item's variant options). The Liquid pre-builds the final Simple Bundles properties object:

```json
{
  "Poszewka jedwabna - kolor": "Czarny",
  "Bonnet - kolor": "Szary",
  "_bundle_selection": "Czarny <> Szary"
}
```

This is output as `data-properties` on the card. The JS passes it directly to `LusenaBundle.swap()` without any runtime color matching.

The property keys must match the Simple Bundles slot names on each bundle's variant. The `_bundle_selection` key uses the `<>` separator convention already established by the existing nudge.

## Swap execution

`LusenaBundle.swap(bundleVariantId, [item1Key, item2Key], { sections, sectionsUrl, properties })`

- Adds the bundle variant with pre-filled color properties
- Removes both individual items sequentially (existing multi-key loop in swap.js)
- Last removal returns section HTML for re-render
- Drawer: `drawer.renderContents(state)` + publishes `cartUpdate`
- Cart page: `reRenderSections(state)` + publishes `cartUpdate`

## Surfaces

Both cart drawer and cart page, same as existing nudge:
- `snippets/cart-drawer.liquid` — merge detection + card HTML + click handler
- `sections/lusena-cart-items.liquid` — merge detection + card HTML + click handler

The merge detection block is added BEFORE the existing nudge waterfall in both files. If merge renders, the regular nudge is skipped entirely (set a flag like `show_merge = true` and wrap existing nudge in `unless show_merge`).

## Edge cases

| Scenario | Behavior |
|---|---|
| Both components + bundle already in cart | Merge card does NOT show (bundle already present). Regular nudge suppressed by `upsell_role == 'bundle'`. |
| poszewka + bonnet + maska (3 items) | Nocna Rutyna merge (109 zl) wins. Piekny Sen (89 zl) not shown. |
| Swap race (add bundle OK, remove item fails) | Cart has individual + bundle. Next render: bundle in cart triggers suppress, no merge card. Customer sees duplicate but UI is not broken. |
| Component quantity > 1 | Swap removes all quantity (sets to 0), same as existing nudge behavior. |
| One component out of stock | Not applicable - both are already in cart, so both are available. |

## Files to modify

| File | Change |
|---|---|
| `snippets/cart-drawer.liquid` | Add merge detection block + merge card HTML before existing nudge. Modify click handler to support `data-replace-keys`. |
| `sections/lusena-cart-items.liquid` | Same changes as cart drawer. |
| `assets/lusena-cart-page.css` | No changes expected - merge card reuses existing `.lusena-upsell-card__bn-*` classes. |

No new files. No new metafields. No changes to `lusena-bundle-swap.js` (already supports multiple removeKeys).

## Out of scope

- Scrunchie Trio merge (same-product bundle, can't detect)
- Showing multiple merge options simultaneously
- Animated transitions for merge card appearance
- Merge suggestions on PDP (abandoned in #12)
