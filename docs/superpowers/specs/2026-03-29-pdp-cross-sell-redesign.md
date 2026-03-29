# PDP Cross-sell Checkbox — UI/UX Redesign

*2026-03-29*

## Summary

Redesign the PDP cross-sell checkbox (scrunchie add-on at 39 zl) to align with LUSENA's premium aesthetic and existing UI patterns (cart upsell cards, bundle step chips). The current implementation works functionally but is visually inconsistent with the shop.

## Design decisions

### Visual style: Hybrid upsell card

The card combines the cart upsell card structure with the bundle chip's compactness:

- **Background:** `var(--lusena-color-n0)` (white)
- **Border:** `1px solid color-mix(in srgb, var(--lusena-text-2) 6%, transparent)`
- **Left accent:** `3px solid color-mix(in srgb, var(--lusena-accent-cta) 40%, transparent)` — strengthens to full `var(--lusena-accent-cta)` on hover and checked state
- **Border-radius:** `var(--lusena-btn-radius)` (6px)
- **Box-shadow:** `0 1px 2px rgba(0,0,0,0.03)` — checked state: `0 1px 3px rgba(14,94,90,0.08)`
- **Padding:** `10px 12px`
- **Transition:** `border-color var(--lusena-transition-fast), box-shadow var(--lusena-transition-fast)`

### Size: Standard compact (Size A)

- **Product image:** 40x40px, `border-radius: var(--lusena-btn-radius)`, variant-specific image
- **Checkbox:** 16x16px, 1.5px border, 3px radius. Unchecked: white bg, #b8b8b8 border. Checked: `var(--lusena-accent-cta)` fill, white checkmark
- **Row gap:** 10px between checkbox, image, info, pricing
- **Title font:** 12.5px / weight 500 / `var(--lusena-text-1)`
- **Hint font:** 10.5px / `var(--lusena-text-2)` at 60% opacity
- **Price font:** 12.5px / weight 600 / `var(--lusena-text-1)` / tabular-nums
- **Strikethrough font:** 10.5px / `var(--lusena-text-2)` / line-through / 45% opacity

### Layout: Single row

```
[ checkbox ] [ image ] [ title + hint ] [ price ]
                                         [ was  ]
```

All elements in a single flex row with `align-items: center`. Pricing is right-aligned, stacked vertically (current price above strikethrough). Same layout on mobile and desktop — only padding adjustments needed.

### Content

- **Title:** "Dodaj scrunchie" (lowercase product name, no "jedwabna" prefix — keep it short)
- **Educational hint:** "Taniej w komplecie" — explains WHY the discount exists without being salesy. Positioned below the title.
- **No savings callout** — no "Oszczedzasz 20 zl" or similar. The crossed-out price communicates the value.
- **No color text label** — the product image communicates the color. When the main product color changes, the scrunchie image silently updates to the matching color.

### Color auto-matching behavior (unchanged)

Already implemented in the inline JS:

1. Customer selects a color on the main product
2. JS finds the matching scrunchie variant by color name
3. Updates the cross-sell image `src` and `data-variant-id`
4. Fallback: highest-inventory available variant if no color match

### Interaction states

| State | Visual |
|-------|--------|
| Default (unchecked) | White card, 40% teal left accent, empty checkbox |
| Hover | Left accent strengthens to full teal |
| Checked | Full teal left accent, filled teal checkbox with white checkmark, slightly stronger shadow |
| ATC loading | Button shows shimmer + spinner (existing `setBtnLoading` helper) |

### Scope (unchanged)

- Appears on all individual product PDPs (pillowcase, bonnet, eye mask, heatless curlers)
- Hidden on scrunchie PDP (`product.handle != cs_handle`)
- Hidden on bundle PDPs (`template.suffix != 'bundle'`)
- Positioned between variant picker and ATC button (CSS order)

## What changes from current implementation

### CSS changes (in `assets/lusena-pdp.css`)

Replace the existing `.lusena-pdp-cross-sell-cb` styles (~115 lines) with the new design:

- Remove: teal-tinted background (`color-mix(... accent-cta 4% ...)`), 48px image, `--lusena-text-sm` font sizes, teal price color, separate `__pricing` column layout
- Add: white background, 3px teal left accent, 40px image, 12.5px font sizes, text-1 price color, single-row layout with `__hint` element

### Liquid changes (in `snippets/lusena-pdp-cross-sell-checkbox.liquid`)

- Remove `cs__color` / `data-lusena-cross-sell-color-label` span — no more "Kolor: X" text
- Add `cs__hint` span with "Taniej w komplecie"
- Adjust image dimensions: `width: 80` (2x for retina), rendered at 40x40

### JS changes

- Remove the line in variant change handler that updates `[data-lusena-cross-sell-color-label]` text
- Image update (`[data-lusena-cross-sell-image]` src swap) remains as-is

## Out of scope (on to-do list)

These items are tracked separately and not part of this redesign:

1. **Bundle PDP cross-sell** — add render slot to `lusena-main-bundle.liquid`
2. **Cart discount explanation** — "Rabat za zakup w zestawie" label next to discounted line items
3. **Scrunchie PDP education** — inform customer about discount when qualifying product is in cart
4. **Revert dead code** — `lusena-pdp-scripts.liquid` ATC intercept already removed; remaining cleanup
5. **Documentation updates** — threshold 289->275 references in bundle docs
