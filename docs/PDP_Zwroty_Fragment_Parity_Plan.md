---
title: PDP "/zwroty" fragment parity plan (Draft shop -> Shopify theme PDP)
date: 2026-02-10
status: planned
owner: Codex + Karol
---

## Goal

Port the draft-shop PDP "zwroty" fragment into the Shopify PDP and match it exactly on desktop and mobile.

This fragment is:
- Buy-box delivery/returns micro-line:
  - `To zamowienie kwalifikuje sie do darmowej dostawy · Dostawa: 1-2 dni robocze · 60 dni na zwrot`
- Link behavior from the micro-line and guarantee strip:
  - Open the `returns` accordion item in `#details` and smooth-scroll to `#details`.
- Returns panel content in the PDP details accordion:
  - "Zwroty i gwarancja 60 dni" with two paragraphs (returns + guarantee).

## Scope

In scope:
- Exact markup/copy/ordering for the delivery+returns micro-line in PDP buy box.
- Exact interaction parity for "60 dni na zwrot" and "Jak to dziala?" links.
- Exact returns accordion title/content parity in `#details`.
- Desktop and mobile parity.

Out of scope:
- Full `/pages/zwroty` page redesign (already implemented via `templates/page.zwroty.json`).
- Unrelated PDP sections (gallery, cross-sell, reviews, etc.).

## Source of truth (draft shop)

- `lusena-shop/src/pages/Product.tsx`
  - Buy-box micro-module above variants (delivery + ETA + returns link).
  - Link handler opening `returns` accordion + scrolling to `#details`.
  - Unified accordion `returns` item content.
- `lusena-shop/src/lib/pdp-content.ts`
  - `DELIVERY_MICRO` labels.
  - `ACCORDION_TITLES.returns`.
- `lusena-shop/src/lib/products.ts`
  - `returnsInfo`, `guaranteeInfo`, `shippingInfo` data model.

## Target in theme

- `sections/lusena-main-product.liquid`
  - PDP buy box section wiring and settings.
- `snippets/lusena-pdp-summary.liquid`
  - Delivery/returns micro-line markup.
- `snippets/lusena-pdp-guarantee.liquid`
  - Guarantee strip link (must keep same open-returns behavior).
- `sections/lusena-pdp-details.liquid`
  - Returns accordion item title and body copy.
- `snippets/lusena-pdp-scripts.liquid`
  - Open-returns behavior and smooth scroll to `#details`.
- `snippets/lusena-pdp-styles.liquid`
  - Typography/spacing for the micro-line to match draft.
- `templates/product.json`
  - Default copy values if needed.

## Decisions (final, 2026-02-10)

1. Returns link behavior is `A`:
   - Exact draft parity.
   - Clicking "60 dni na zwrot" or "Jak to dziala?" opens `returns` accordion and scrolls to `#details`.
   - No direct redirect to `/pages/zwroty`.
2. Parity target is draft PDP fragment, not the standalone returns page layout.
3. Breakpoint behavior for this fragment follows the draft PDP implementation (`md` mobile/desktop behavior already used in this PDP stack).

## Open questions / unresolved assumptions

None.

## Data sources and content model

- Delivery line:
  - Existing section settings:
    - `delivery_qualifies_label`
    - `delivery_free_fallback_label`
    - `delivery_eta_label`
    - `delivery_returns_link_label`
  - Runtime rule:
    - show `delivery_qualifies_label` when selected variant price >= 199 PLN threshold
    - otherwise show fallback line
- Returns accordion panel:
  - Use product-level metafields when available (existing LUSENA PDP pattern), with robust fallback copy matching draft intent.
- Link action:
  - Shared `data-lusena-open-returns` hook handled in `snippets/lusena-pdp-scripts.liquid`.

## Target UX spec (desktop + mobile)

Desktop:
- Delivery micro-line appears directly under price/per-night block.
- Layout:
  - Truck icon on the left.
  - Inline text chain with middle dots.
  - ETA segment visually emphasized.
  - "60 dni na zwrot" appears as an interactive link with underline on hover.
- Click on returns link:
  - Opens `returns` accordion item.
  - Smooth-scrolls to `#details`.

Mobile:
- Same information architecture/order as draft:
  - Price/per-night
  - Delivery micro-line
  - Variant selector
  - CTA
  - Guarantee
  - Other buy-box modules
- Same click behavior as desktop.
- Typographic sizing and spacing match draft micro-module scale.

## Implementation approach

1. Update micro-line markup in `snippets/lusena-pdp-summary.liquid`:
   - Include all three segments (delivery qualifier/fallback, ETA, returns link) in one inline row.
   - Keep returns link on `data-lusena-open-returns`.
2. Ensure styles in `snippets/lusena-pdp-styles.liquid` match draft spacing/weight for:
   - icon size
   - text size
   - middle-dot spacing
   - emphasized ETA segment
3. Validate that guarantee link in `snippets/lusena-pdp-guarantee.liquid` uses the same open-returns path.
4. Align returns panel copy/title in `sections/lusena-pdp-details.liquid` with draft fragment.
5. Verify JS behavior in `snippets/lusena-pdp-scripts.liquid`:
   - opens `data-lusena-accordion-returns`
   - scrolls to `#details`
   - preserves single-open accordion behavior.
6. Run Shopify theme validation for all touched files and fix until valid.

## Milestones / deliverables

1. Delivery+returns micro-line parity in buy box.
2. Returns deep-link interaction parity (both triggers).
3. Returns accordion content/title parity.
4. Clean `validate_theme` result on touched files.
5. User visual check pass on mobile and desktop.

## Verification checklist

Manual (required):
- Desktop (~1280px):
  - Micro-line shows delivery + ETA + returns link with correct order and punctuation.
  - "60 dni na zwrot" opens returns accordion and scrolls to details.
  - "Jak to dziala?" in guarantee strip does the same.
- Mobile (~390px):
  - Same behavior and ordering.
  - Spacing and text sizing match draft.
- Product price threshold:
  - >= 199 shows "kwalifikuje sie" label.
  - < 199 shows fallback free-delivery label.

Technical:
- Shopify MCP `validate_theme` run for all touched files.
- No regressions in existing accordion interactions.

## Risks and edge cases

- Encoding mismatches in existing PL copy files may produce mojibake if edited carelessly.
- If `#details` section is removed/reordered in template, link behavior can degrade; keep anchor stable.
- Products missing metafield content should still render safe fallback text (no empty returns panel).
