# PDP Cart UI/UX Parity Plan (draft shop -> Shopify theme)

Created: 2026-02-11  
Status: Implemented (pending visual parity review)  
Owner: Codex

## Goal

Copy the complete draft-shop cart experience used from PDP into the active Shopify theme so desktop and mobile behavior matches the draft as closely as Shopify cart constraints allow.

## Scope

- PDP cart actions behavior:
  - `Add to cart`: add item and open cart drawer.
  - `Buy now`: immediately redirect to accelerated checkout flow.
- Cart drawer UI structure, visual hierarchy, spacing, and interaction states (desktop + mobile).
- Cart drawer behaviors: overlay, focus handling, escape/close, quantity +/- controls, remove flow, upsell card area, subtotal/footer stack, and continue-shopping action.
- Keep the current LUSENA PDP section (`sections/lusena-main-product.liquid`) as the entry point.

## Non-goals

- Rebuilding the full cart page (`templates/cart.json`).
- Reworking non-cart PDP fragments (gallery, details accordion, cross-sell sections).
- Replacing Shopify core add-to-cart transport (`product-form.js` + section re-render flow).

## Source Of Truth (Draft Shop)

- `lusena-shop/src/pages/Product.tsx`
- `lusena-shop/src/components/cart/CartDrawer.tsx`
- `lusena-shop/src/components/ui/Button.tsx`
- `lusena-shop/src/context/CartContext.tsx`

## Target In Theme

- `snippets/cart-drawer.liquid`
- `snippets/lusena-pdp-atc.liquid` (only if needed for trigger parity)
- `snippets/lusena-missing-utilities.liquid` (only for missing utility parity classes)
- `locales/en.default.json` (only if new translation keys are introduced)

## Decisions (Final)

- Breakpoint behavior follows draft parity for this fragment (`md` behavior at 768px where relevant), even if Dawn often uses 750px elsewhere.
- Cart drawer remains Shopify drawer-based and server-rendered; draft UX is mapped to Shopify cart object and AJAX section updates.
- Upsell stays enabled in the theme but is rendered in draft-style UI location and visual treatment.
- PDP `Kup teraz` is direct fast-checkout entry (checkout redirect), not just an add-to-cart trigger.
- PDP `Dodaj do koszyka` opens cart drawer (with upsell + shipping progress module).
- Exact cart copy and control ordering in the drawer will match draft structure for both empty and non-empty states.

## Open Questions / Unresolved Assumptions

- None.

## Data Sources & Content Model

- Cart line items, quantities, prices: Shopify `cart` object.
- Add/remove/update: Shopify AJAX cart endpoints via existing drawer hooks.
- Upsell candidates: existing theme metafield/settings logic (kept), rendered with draft visual layout.
- Footer totals: Shopify `cart.total_price`.
- Free-shipping progress: threshold-aligned implementation in theme with configurable/fallback constant matching draft behavior.

## Target UX Spec (Desktop + Mobile)

- PDP actions:
  - Clicking `Dodaj do koszyka` updates cart and opens the drawer.
  - Clicking `Kup teraz` takes user directly to checkout.
- Drawer shell:
  - Overlay blur/scrim with right-side panel slide-in/out.
  - Full-height panel with header, scrollable body, fixed footer structure.
- Header:
  - Draft-like title and close control hit-area.
- Empty state:
  - Icon circle, title/subtitle stack, primary browse button, secondary close text action.
- Non-empty line items:
  - Image block, title/variant text, line price, optional compare-at strike.
  - Quantity stepper with disabled decrement at minimum quantity.
  - “Usuń” remove action placement and typography.
- Mid-to-lower drawer area:
  - Draft-style upsell card zone and success feedback treatment.
  - Free-shipping progress micro-module above checkout CTA.
- Footer:
  - “Suma” row, checkout button, trust micro-strip, continue-shopping action.
- Accessibility:
  - Dialog semantics, keyboard close via `Escape`, focus trap continuity with existing Dawn drawer behavior, labeled controls.

## Implementation Approach

1. Replace `snippets/cart-drawer.liquid` markup/class structure to mirror draft cart drawer composition and control hierarchy.
2. Keep required Dawn hooks/IDs/selectors (`CartDrawer`, `CartDrawer-Overlay`, drawer section re-render compatibility).
3. Add minimal CSS inside snippet for any missing draft utility behavior that is not in `assets/lusena-shop.css`.
4. Keep/adjust existing cart line update script so +/- and remove interactions still refresh sections correctly.
5. Update PDP action handlers (`snippets/lusena-pdp-atc.liquid` + `snippets/lusena-pdp-scripts.liquid`) so:
   - Add-to-cart keeps standard drawer-open behavior.
   - Buy-now performs add + checkout redirect.

## Milestones / Deliverables

1. Plan file added in `docs/`.
2. Cart drawer parity implementation in theme snippet(s).
3. Shopify theme validation pass for touched files.
4. Desktop/mobile manual verification checklist shared with user.

## Verification Checklist

- Desktop (~1280px):
  - Add to cart from PDP opens drawer with matching hierarchy/spacing.
  - Quantity +/- and remove update totals and preserve drawer behavior.
  - Upsell area, free-shipping module, footer stack match draft ordering and style intent.
- Mobile (~390px):
  - Drawer covers viewport height correctly and remains usable with keyboard + touch.
  - Typography scale, spacing density, and button sizing match draft.
  - Sticky and PDP add-to-cart flow still triggers drawer reliably.
- Accessibility:
  - `Esc` closes drawer, overlay closes drawer, focus remains trapped while open and restored on close.

## Risks / Edge Cases

- Shopify section re-render can reset transient UI states (e.g., inline upsell feedback); behavior must be re-checked after each update.
- If some draft utility classes are missing from compiled theme CSS, targeted utility backfills may be needed.
- Existing unrelated local changes in theme files require careful, non-destructive edits.
