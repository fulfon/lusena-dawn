# PDP Cart + Round Buttons Parity Plan (draft shop -> Shopify theme)

Created: 2026-02-10  
Status: Planned + approved by direct implementation request  
Owner: Codex

## Goal

Copy two UI fragments from the draft PDP/cart experience into the active Shopify theme implementation with desktop + mobile parity:

1. `Kontynuuj zakupy` option in cart drawer.
2. Draft-style rounded button system (6px brand radius) used across the storefront.

## Scope

- Cart drawer empty and non-empty states where continue-shopping controls appear.
- Global button corner radius used by Dawn button primitives.
- Keep current LUSENA cart logic (upsell, AJAX quantity/remove, existing structure).

## Non-goals

- Rewriting cart drawer architecture.
- Reworking cart copy/translations outside requested fragment.
- Changing PDP gallery/accordion behavior.

## Source Of Truth

- `lusena-shop/src/components/cart/CartDrawer.tsx`
- `lusena-shop/src/components/ui/Button.tsx`
- `lusena-shop/tailwind.config.js`

## Target In Theme

- `snippets/cart-drawer.liquid`
- `config/settings_data.json`

## Decisions (final)

- Continue shopping action is shown in both cart-empty and cart-with-items drawer states, matching draft behavior.
- Button shape parity uses draft `rounded-brand` radius (6px) globally.
- Existing breakpoints in theme stay unchanged (no layout breakpoint migration in this task).

## Open Questions / Unresolved Assumptions

- None.

## Data Sources & Content Model

- Cart data remains from Shopify `cart` object.
- Continue-shopping destination remains `routes.all_products_collection_url`.
- Radius source remains theme setting `settings.buttons_radius`, updated to draft parity value in theme data.

## Target UX Spec (Desktop + Mobile)

- Cart empty: continue-shopping action below empty-state message, draft-style outline shape/spacing.
- Cart with items: continue-shopping action shown under checkout CTA in footer, draft position and lightweight text treatment.
- Global primary/secondary buttons: rounded corners visually match draft brand radius (6px) on both desktop and mobile.

## Implementation Approach

- Update cart drawer markup/classes for continue-shopping controls to mirror draft structure/spacing.
- Update active theme settings data radius from `8` to `6` to align with draft `rounded-brand`.
- Keep all existing JS hooks (`data-cart-delta`, `data-cart-remove`, etc.) untouched.

## Milestones / Deliverables

1. Add plan file in `docs/`.
2. Implement cart drawer continue-shopping parity.
3. Implement global rounded button radius parity.
4. Validate touched theme files with Shopify Dev MCP `validate_theme`.
5. Provide verification checklist for user desktop/mobile parity confirmation.

## Verification Checklist

- Cart drawer empty state shows continue-shopping action with draft-like styling.
- Cart drawer non-empty footer shows continue-shopping action under checkout.
- Buttons across PDP/cart (and other pages using Dawn button primitive) reflect 6px rounded style on desktop/mobile.
- Cart drawer interactions (remove, quantity +/- , checkout) still work.

## Risks / Edge Cases

- Theme-level button radius change affects all button-based components; verify no visual regression in hero/forms.
- Continue-shopping action in non-empty footer must not interfere with checkout emphasis.
