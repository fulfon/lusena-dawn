# Cart Upsell UI Redesign - Design Spec

> **For agentic workers:** This is a design spec. Use `superpowers:writing-plans` to create the implementation plan.

**Goal:** Unify the cross-sell and bundle upgrade UI in both cart drawer and cart page with a cohesive, brand-aligned, gain-framed design that maximizes conversion while respecting LUSENA's premium positioning.

**Scope:** Visual and copy redesign of the existing upsell zone. No changes to the underlying swap/add logic (`lusena-bundle-swap.js`), metafield configuration, or upsell waterfall selection. The functional behavior stays identical - only the rendered HTML, CSS, and copy change.

---

## Context

### What exists today

Two visually disconnected UIs share the same upsell zone in cart drawer (`snippets/cart-drawer.liquid`) and cart page (`sections/lusena-cart-items.liquid`):

1. **Cross-sell card** - horizontal layout: product image (5.6rem) | title + message + color | price + "Dodaj" button. Clean but uses Dawn-era styling without LUSENA card container.
2. **Bundle nudge** (`snippets/lusena-bundle-nudge.liquid`) - dashed-border text-only box with "Dodaj do zestawu - +260 zl" button. No product image, no explanation of what the customer gets, cost-framed CTA.

### Problems identified

- **No visual cohesion** - dashed border vs clean card, different button styles, different layout paradigms
- **Cost-framed CTA** - "+260 zl" frames the action as paying more, not gaining value
- **No persuasion logic** - customer doesn't understand what they get or why they should upgrade
- **"Nocna Rutyna" means nothing** to a first-time visitor without context
- **Bundle CTA competes with checkout** - both are filled teal buttons

### Research basis

- **Thaler's Mental Accounting** - lump costs (one set price), fragment rewards (show both items). Source: Thaler (1985), *Marketing Science*
- **Zeigarnik Effect** - incomplete set tension drives completion. Source: Gousto A/B test: +20% additions with completion framing
- **Prospect Theory** - gain framing ("zaoszczedz 109 zl") is 2x more motivating than loss framing ("+260 zl"). Source: Kahneman & Tversky
- **Bundle strategy principle #4** - routine framing, not savings framing. Savings shown but secondary. Source: `memory-bank/doc/bundle-strategy.md`
- **Bundle strategy principle #3** - never attribute discount to the poszewka. Source: Wei, Yu & Li (2025); Khan & Dhar (2010)
- **CTA research** - brand-led, action-oriented copy increased additions by 83%. Source: ConvertCart industry study
- **PDP consistency** - gold savings chip (`rgba(140,106,60,0.08)` bg, `--lusena-accent-2` text) already used in bundle PDP buy-box. Cart should mirror this.

---

## Design decisions

### 1. Unified card container

Both cross-sell and bundle use the same card container class `.lusena-upsell-card`:

```css
.lusena-upsell-card {
  padding: var(--lusena-space-2);                          /* 1.6rem */
  background: var(--lusena-color-n0);                      /* white */
  border-radius: var(--lusena-btn-radius);                 /* 0.6rem */
  border: 1px solid color-mix(in srgb, var(--lusena-text-2) 5%, transparent);
  box-shadow: 0 1px 2px rgba(0,0,0,0.03);
  border-left: 0.25rem solid color-mix(in srgb, var(--lusena-accent-cta) 40%, transparent);
}
```

The teal left border accent visually connects both card types to the LUSENA brand without being loud.

### 2. Cross-sell layout (unchanged structure, unified styling)

Horizontal: `[image 5.6rem] | [title + message + color] | [price + button]`

- **Section label:** "Pasuje do" (Source Serif, `--lusena-text-2`)
- **Image:** 5.6rem x 5.6rem (unchanged from current), `border-radius: var(--lusena-radius-sm)`, `object-fit: cover`
- **Title:** 1.3rem, Inter, weight 500, `--lusena-text-1`
- **Message:** 1.15rem, Inter, `--lusena-text-2`, from `upsell_message` metafield
- **Color:** 1.05rem, Inter, muted label + bold value
- **Price:** 1.35rem, Inter, weight 500, `--lusena-text-1`, tabular-nums
- **CTA:** `lusena-btn--outline lusena-btn--size-xs`, text "Dodaj"

### 3. Bundle nudge layout (new two-tile design)

Vertical stack: `[headline] -> [tiles: "in cart" 30% + "add" ~70%] -> [pricing + CTA]`

#### Headline

```
"Dodaj {missing_item_name} i zaoszczedz {savings} zl"
```

- Gain-framed: names the specific product, states the savings as a GAIN
- Font: Inter, 1.35rem, weight 500, `--lusena-text-1`
- `{missing_item_name}` - accusative case product name from `bundle_nudge_map` metafield (already exists, keyed by trigger product handle)
- `{savings}` - computed in Liquid:
  ```liquid
  assign savings_cents = original_total_cents | minus: bundle_price_cents
  ```
  Where `original_total_cents = product.metafields.lusena.bundle_original_price.value | times: 100` and `bundle_price_cents = variant.price`. Rendered with `money_without_trailing_zeros`. This is the TOTAL bundle savings (e.g., 109 zl), NOT the incremental cost over the trigger item.

#### Two-tile row

Flex row with `gap: var(--lusena-space-1)`:

**"In cart" tile (left, ~30%):**
- `flex: 0 0 30%`
- Background: `color-mix(in srgb, var(--lusena-surface-2) 40%, transparent)` - muted, no teal
- Padding: `var(--lusena-space-1) var(--lusena-space-05)`
- Border-radius: `var(--lusena-radius-sm)`
- Layout: flex column, center-aligned
- Product image: 3.8rem x 3.8rem, `opacity: 0.75`, `border-radius: 0.4rem` - visually receded. Source: `trigger_product.featured_image` (already in Liquid scope as `trigger_product`)
- Check mark badge: `position: absolute; top: -0.3rem; right: -0.3rem`. 1.4rem circle, `background: var(--lusena-accent-cta)`, white inline SVG checkmark (`<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>`, stroke white, stroke-width 3). No `lusena-icon` snippet needed - inline SVG is simpler for this tiny badge.
- Product name: Inter, 1rem, weight 500, color `#888` - secondary. Source: `trigger_product.title`
- Status text: Inter, 0.9rem, `--lusena-accent-cta`, weight 500, text "W koszyku"

**"+" separator:** A standalone `<span>` element between the two tile `<div>`s. Font-size 1.6rem, color `--lusena-color-n300`, weight 300, `flex-shrink: 0`, `align-self: center`. `aria-hidden="true"` (decorative).

**"Add" tile (right, ~70%):**
- `flex: 1`
- Background: `color-mix(in srgb, var(--lusena-surface-2) 50%, transparent)`
- Border: `1px solid color-mix(in srgb, var(--lusena-text-2) 6%, transparent)` - slightly more prominent than "in cart" tile
- Padding: `var(--lusena-space-1)`
- Border-radius: `var(--lusena-radius-sm)`
- Layout: flex column, center-aligned
- Product image: 5.6rem x 5.6rem, full opacity, `border-radius: var(--lusena-radius-sm)` - visually dominant. **Image source:** Use the bundle product's `featured_image` (`upsell_product.featured_image` / `upsell_product_1.featured_image`). This shows the bundle set image, which visually represents the complete set. The customer sees their item on the left + the full set image on the right. No new metafield needed.
- Product name: Inter, 1.2rem, weight 500, `--lusena-text-1` - primary color. **Text source:** The missing component name from `bundle_nudge_map[trigger_product.handle]` (same as headline)
- No subtitle, no meta text

**Scrunchie Trio special case:** "In cart" tile shows "Scrunchie" with one scrunchie image. "Add" tile shows "2x Scrunchie" with the Scrunchie Trio bundle's featured image. The "2x" prefix is hardcoded in the `bundle_nudge_map` metafield value for this product.

**Visual weight ratio:** The "add" tile gets ~2.5x the visual area of the "in cart" tile. The customer's eye goes to the new item first.

#### Pricing row

Flex row below a hairline separator:
- Separator: `margin-top: var(--lusena-space-1); padding-top: var(--lusena-space-1); border-top: 1px solid color-mix(in srgb, var(--lusena-text-2) 5%, transparent)`
- Layout: `display: flex; align-items: center; justify-content: space-between; gap: var(--lusena-space-1)`

Left side (pricing):
- **Bundle price:** Inter, 1.4rem, weight 500, `--lusena-text-1` (e.g., "399 zl")
- **Crossed-out original:** Inter, 1.1rem, `--lusena-color-n300`, `text-decoration: line-through` (e.g., "508 zl")
- **Gold savings chip:** matches PDP `.lusena-bundle-savings` exactly:
  ```css
  display: inline-flex;
  background: rgba(140, 106, 60, 0.08);
  color: var(--lusena-accent-2);
  font-family: var(--lusena-font-ui);
  font-size: 1.15rem;
  font-weight: 500;
  padding: 0.3rem 0.8rem;
  border-radius: var(--lusena-btn-radius);
  ```
  Text: "Oszczedzasz {savings} zl" (matches PDP wording, uses hyphen not em dash)

Right side (CTA):
- **CTA button:** `lusena-btn--outline lusena-btn--size-xs`, text "Dodaj do zestawu"

### 4. Section labels

| Context | Cross-sell | Bundle |
|---------|-----------|--------|
| Label | "Pasuje do" | "Korzystniej w zestawie" |
| Font | Source Serif 4 (`--lusena-font-brand`) | Source Serif 4 (`--lusena-font-brand`) |
| Size | 1.2rem | 1.2rem |
| Color | `--lusena-text-2` | `--lusena-text-2` |

**Rationale for label change:** The previous "Uzupelnij do zestawu" was vague and didn't communicate value. "Korzystniej w zestawie" frames the set as a better deal without being discount-y - the customer understands this is about value, not just completeness. "Pasuje do" remains for cross-sell as it's a gentle complement framing.

### 5. Button hierarchy

| Button | Style | Text | Purpose |
|--------|-------|------|---------|
| Checkout | Filled teal (`lusena-btn--primary`) | "Przejdz do kasy" | Leave cart - primary action |
| Bundle CTA | Outline teal (`lusena-btn--outline`) | "Dodaj do zestawu" | Stay in cart - secondary |
| Cross-sell CTA | Outline teal (`lusena-btn--outline`) | "Dodaj" | Stay in cart - secondary |

**Rule:** Filled teal = leave the cart. Outline teal = stay and add something.

**Intentional change from prior spec:** The `2026-03-24-bundle-nudge-design.md` spec used `lusena-btn--primary` (filled teal) for the bundle CTA. This redesign intentionally downgrades it to outline. Reason: in brainstorming, we identified that two filled teal buttons in the drawer (bundle CTA + checkout) compete for attention and confuse the visual hierarchy. The checkout button must remain the only primary action. The bundle card's gain-framed headline, two-tile layout, and gold savings chip provide sufficient visual prominence without needing a filled button. The prior spec is superseded by this one for all CTA styling decisions.

### 6. Upsell zone container

Same for both drawer and cart page:

```css
/* Shared */
background: color-mix(in srgb, var(--lusena-surface-2) 50%, transparent);
border-top: 1px solid color-mix(in srgb, var(--lusena-text-2) 10%, transparent);

/* Drawer */
padding: var(--lusena-space-2) var(--lusena-space-3);

/* Cart page - uses existing negative margin pattern */
padding: var(--lusena-space-2) var(--lusena-space-4);
```

Cart page: upsell zone spans the full content column width, positioned below the last cart item, above totals. Uses negative margins to break out of the cart items padding (existing pattern in `lusena-cart-items.liquid`).

### 7. Responsive behavior

- **Drawer (~375px):** "In cart" tile at 30%, "add" tile fills remainder. Both tiles stack content vertically (image above name). All sizes in rem - scales with root font size.
- **Short screens (max-height: 700px):** Compact variant already exists in cart drawer CSS. The bundle card should reduce padding to `var(--lusena-space-1)` and tile images proportionally (3rem "in cart", 4.4rem "add").
- **Cart page mobile:** Same layout as drawer - the content column is ~375px on mobile anyway.
- **Cart page desktop:** Same layout, more horizontal breathing room from page padding. No layout change needed.

### 8. Color matching

No color information displayed in the bundle nudge card. The system auto-matches the trigger item's color for both bundle components (existing behavior in `cart-drawer.liquid` and `lusena-cart-items.liquid`). Showing color in the card adds clutter without persuasive value.

Cross-sell card retains the "Kolor: **Czarny**" line since it's a single product add where the customer may want to confirm the color.

### 9. Loading state

Same as current: button gets `loading` class, spinner dots appear, button text hidden. After swap completes, cart re-renders via Sections API (drawer) or `window.location.reload()` (cart page).

### 10. Success state

Cart drawer: existing "Dodano do koszyka" success bar (below upsell zone) continues to work for cross-sell adds. For bundle swaps, the cart re-renders entirely (bundle replaces the individual item), so no explicit success state is needed - the customer sees the bundle in their cart.

### 11. Accessibility

- Upsell zone: `aria-live="polite"` (existing)
- "+" separator: `aria-hidden="true"` (decorative)
- Tiles: purely visual, not interactive - no tab stops or roles needed
- "W koszyku" status: informational text within the card, no `aria-live` needed (it's static per render)
- Check mark badge: `aria-hidden="true"` (visual indicator only, status communicated by "W koszyku" text)

---

## CSS placement

The new bundle tile layout CSS is estimated at ~60-70 lines (tile layout, check badge, pricing row, savings chip, responsive adjustments). Combined with the existing cross-sell card CSS already in the `{% stylesheet %}` blocks:

**Decision:** Keep upsell CSS in the `{% stylesheet %}` blocks of `cart-drawer.liquid` and `lusena-cart-items.liquid` where it currently lives. The `.lusena-bundle-nudge` styles (~30 lines) are removed from `lusena-foundations.css`, and the new tile styles are section-scoped. Net change to compiled_assets is approximately +30-40 lines, which is within budget.

**Post-implementation check required:** Verify `compiled_assets/styles.css` stays under 55KB after the changes (per CLAUDE.md truncation guard).

---

## Files to modify

| File | Change |
|------|--------|
| `snippets/cart-drawer.liquid` | Replace upsell card HTML for both cross-sell and bundle code paths. The existing `{% render 'lusena-bundle-nudge' %}` call (line ~1043) is replaced with inline two-tile layout HTML. Update `{% stylesheet %}` block with unified card and tile styles. |
| `sections/lusena-cart-items.liquid` | Mirror the same changes as cart drawer. The existing `{% render 'lusena-bundle-nudge' %}` call (line ~428) is replaced with inline two-tile layout HTML. Update `{% stylesheet %}` block. |
| `snippets/lusena-bundle-nudge.liquid` | **Delete** - markup is now inline in the cart drawer and cart page. The separate snippet is no longer needed since both the HTML structure and data requirements are fundamentally different. |
| `assets/lusena-foundations.css` | Remove `.lusena-bundle-nudge` component styles (lines ~1209-1240, ~30 lines). |

## Files NOT modified

| File | Why |
|------|-----|
| `assets/lusena-bundle-swap.js` | Swap logic is unchanged - same API calls, same sections rendering |
| Product metafields | Same `bundle_nudge_map`, `bundle_original_price`, `upsell_primary/secondary` |
| `templates/product.bundle.json` | Bundle PDP unaffected |
| Upsell waterfall logic | Same trigger/candidate selection in Liquid header |

---

## Copy reference

**Important:** All customer-facing copy uses hyphens (-), never em dashes. Do not copy em dashes from `bundle-strategy.md`.

### Bundle headlines (gain-framed, per bundle)

| Trigger item | Bundle | Headline |
|-------------|--------|----------|
| Czepek | Nocna Rutyna | "Dodaj poszewke i zaoszczedz 109 zl" |
| Poszewka | Nocna Rutyna | "Dodaj czepek i zaoszczedz 109 zl" |
| Poszewka | Piekny Sen | "Dodaj maske 3D i zaoszczedz 89 zl" |
| Maska 3D | Piekny Sen | "Dodaj poszewke i zaoszczedz 89 zl" |
| Scrunchie | Scrunchie Trio | "Dodaj 2 scrunchie i zaoszczedz 38 zl" |

The headline is dynamically constructed in Liquid:
```liquid
assign added_label = nudge_map[trigger_product.handle]
assign savings_cents = original_total_cents | minus: bundle_price_cents
```
Rendered as: `Dodaj {{ added_label }} i zaoszczedz {{ savings_cents | money_without_trailing_zeros }}`

### Section labels

- Cross-sell: "Pasuje do"
- Bundle: "Korzystniej w zestawie"

### Tile labels

- "In cart" tile: trigger product title (from `trigger_product.title`) + status "W koszyku"
- "Add" tile: missing component name from `bundle_nudge_map[trigger_product.handle]`

---

## What this does NOT cover

- **PDP bundle detection banner** (#12) - "Masz poszewke w koszyku?" on PDP
- **Cart merge** (#13) - detecting when both bundle components are in cart separately
- **PDP cross-sell checkbox** (Phase 1B) - scrunchie checkbox on poszewka PDP
- **Homepage bundles section** - separate task
