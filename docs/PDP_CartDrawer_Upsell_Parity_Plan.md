# Cart Drawer Upsell Parity Plan (Draft shop -> Shopify theme)

Created: 2026-02-12  
Status: Implemented  
Owner: Codex

## Goal

Match the cart-drawer upsell UI/UX from draft shop in the Shopify theme with exact visual hierarchy and behavior for desktop and mobile.

## Scope

### In scope
- Single upsell card composition parity (thumbnail, copy column, right-aligned price + CTA column).
- Upsell success feedback strip (`Dodano do koszyka`) shown after upsell add.
- Remove hardcoded debug forcing that always injected an upsell.
- Preserve existing cart drawer footer, totals, free shipping bar, and quantity controls.

### Out of scope
- Reworking full upsell recommendation strategy.
- Rewriting cart page upsell (`sections/main-cart-footer.liquid`).

## Source of truth (Draft shop)

- `lusena-shop/src/components/cart/CartDrawer.tsx`
- `lusena-shop/src/lib/upsell.ts`

## Target in theme (Shopify)

- `snippets/cart-drawer.liquid`

## Decisions (final) - 2026-02-12

1. Render a single upsell card only to match draft UX exactly.
2. Remove hardcoded debug forcing and keep production recommendation logic only.
3. Keep upsell copy source from existing Shopify metafield/settings logic.
4. Add success feedback via lightweight client-side state around drawer rerenders.

## Open questions / unresolved assumptions

None.

## Data sources & content model

- Product recommendation source: existing `lusena` product metafields and fallback theme setting.
- Upsell benefit text: `metafields.lusena.upsell_message` with theme fallback.
- Optional upsell color row: derived from color-like product option on selected upsell variant.
- Success-state trigger: sessionStorage flag written on upsell submit and consumed after drawer rerender.

## Target UX spec (Desktop + Mobile)

### Desktop (~1280px)
- Upsell zone appears between cart line items and footer.
- Card layout: left image, middle text, right column with price above `Dodaj`.
- Success strip uses centered check icon + green copy.

### Mobile (~390px)
- Same hierarchy and spacing behavior as draft.
- Right column remains right-aligned and compact.
- Success strip remains in upsell slot with same vertical rhythm.

### Accessibility
- Existing semantic `button`/`form` behavior preserved.
- Success strip uses `aria-live="polite"`.

## Theme capability & conflict audit

| Capability / token | Draft source | Resolved draft value | Exists in theme? | Conflict detected? | Planned implementation path | Target file |
|---|---|---|---|---|---|---|
| Upsell card shell | `CartDrawer.tsx` | `flex`, gap `12px`, bordered card | Yes | No | Reuse existing theme utility classes | `snippets/cart-drawer.liquid` |
| Right column (price + CTA) | `CartDrawer.tsx` | `flex-col`, `items-end`, `justify-between` | Partial | Yes | Restructure markup to draft composition | `snippets/cart-drawer.liquid` |
| Success feedback row | `CartDrawer.tsx` | top border + `py-3` + centered icon/text | Partial | No | Add dedicated hidden row + JS toggle | `snippets/cart-drawer.liquid` |
| Debug force behavior | Theme only | Always-on upsell injection | Yes | Yes | Remove branch entirely | `snippets/cart-drawer.liquid` |

## Parity contract table

| Selector / element | Property | Draft value | Theme target value | State | Breakpoint | Tolerance |
|---|---|---|---|---|---|---|
| Upsell card root | Layout | `display:flex; gap:12px` | Same | default | all | exact |
| Upsell right column | Alignment | right-aligned, stacked | Same | default | all | exact |
| Upsell CTA | Size | `h-8`, compact x-padding | Same | default | all | exact |
| Upsell success strip | Display | centered row with check + green text | Same | success | all | exact |

## State fixture matrix

| State | Required fixture/data | Expected UI/UX |
|---|---|---|
| Empty cart | `cart == empty` | No upsell zone (existing empty state only) |
| Populated cart with recommendation | Eligible cart + available upsell | Single upsell card visible |
| Upsell added | Click `Dodaj` in upsell | Success strip appears in upsell area |
| Suppressed | 2+ distinct items / bundle / suppression metafield | No upsell shown |
| Missing color option | Upsell product without color option | Color row hidden, layout intact |

## Implementation approach

1. Remove second-item and debug-force branches from Liquid setup.
2. Replace upsell markup with draft-matching single-card composition.
3. Add hidden success strip and JS flag lifecycle to show post-submit feedback after drawer rerender.
4. Keep all non-upsell cart drawer behavior unchanged.

## Milestones / deliverables

1. Upsell logic and markup updated in theme snippet.
2. Theme validation passes for touched file.
3. User performs visual parity check in browser.

## Verification checklist (developer pre-check)

### Computed-style checks

Breakpoints:
- Mobile: ~390px
- Desktop: ~1280px

Check for critical selectors:
- Upsell card flex structure and gap
- Upsell right-column alignment
- CTA size and text weight
- Success strip visibility/state

### Behavior checks

- Upsell submit sets success feedback after drawer rerender.
- Quantity/remove interactions remain unchanged.
- Suppression paths no longer show debug-forced upsell.

## Verification checklist (user visual confirmation)

1. Compare draft vs theme upsell at ~390px and ~1280px.
2. Confirm card composition and button/price alignment.
3. Confirm success strip appears after upsell add.
4. Confirm no upsell appears in suppressed scenarios.

## Risks / edge cases

- Session storage may be unavailable in strict privacy contexts.
- Upsell color row depends on option naming containing `color`, `colour`, or `kolor`.

## Validation and wrap-up

- Shopify Dev MCP `validate_theme`: pass (`snippets/cart-drawer.liquid`)
- Files to include in summary:
  - `snippets/cart-drawer.liquid`
  - `docs/PDP_CartDrawer_Upsell_Parity_Plan.md`
