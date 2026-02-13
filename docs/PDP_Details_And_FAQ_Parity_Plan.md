---
title: PDP "Szczegóły i pytania" (Draftshop Parity)
date: 2026-02-09
status: draft
---

## Goal

Port the draft-shop PDP fragment:

- Section heading: "Szczegóły i pytania"
- Unified accordion items:
  - "Materiały i specyfikacja" (with specs table + micro-definitions)
  - "Pielęgnacja"
  - "Co zawiera opakowanie"
  - "Wysyłka i dostawa"
  - "Zwroty i gwarancja 60 dni"
  - FAQ items:
    - "Czy to prawdziwy jedwab?"
    - "Jak zweryfikować certyfikat OEKO-TEX?"
    - "Jak prać jedwabną poszewkę?"
    - "Skąd jest wysyłka i ile trwa?"
    - "Co jeśli mi się nie spodoba?"
    - "Dlaczego jedwab z Suzhou?"

into the Shopify theme PDP so it matches the draft shop on mobile and desktop in layout, typography, spacing, and interaction.

## Scope

- Match the fragment’s:
  - Layout and spacing (mobile + desktop)
  - Accordion behavior: single-open, collapsible
  - Chevron rotation on open
  - Accordion open/close animation (height) consistent with draft (Tailwind/Radix-style)
  - Specs table zebra striping and inline "?" micro-definitions for: "Splot", "Gęstość", "Klasa"
  - Returns deep-link behavior: clicking "60 dni na zwrot" / guarantee link opens returns panel and scrolls to `#details`
  - Scroll-reveal integration via Dawn `scroll-trigger` classes (gated by `settings.animations_reveal_on_scroll`)

## Non-goals

- Reordering other PDP sections (feature highlights, quality evidence, cross-sell, reviews) unless required for parity of this fragment’s placement.
- Implementing a full reviews system (draft has an empty-state module).

## Source Of Truth (Draft Shop)

- Fragment placement + markup: `lusena-shop/src/pages/Product.tsx`
  - "Szczegóły i pytania" section (unified accordion)
  - `SpecsTable` sub-component (definitions behavior)
- Copy strings + definitions:
  - Accordion titles + `SPEC_DEFINITIONS`: `lusena-shop/src/lib/pdp-content.ts`
- Example content payloads used by the draft PDP:
  - `faq`, `care`, `whatsIncluded`, `shippingInfo`, `returnsInfo`, `guaranteeInfo`, `specs`: `lusena-shop/src/lib/products.ts`
- Visual tokens / breakpoints: `lusena-shop/tailwind.config.js` (notably `md: 768px`)

## Target In Theme

- Template entrypoint: `templates/product.json` (currently uses `sections/lusena-main-product.liquid`)
- Existing PDP infra:
  - Tailwind-like utilities already present in `assets/lusena-shop.css`
  - Fonts loaded in `layout/theme.liquid` (Inter + Source Serif 4)
  - Existing returns deep-link logic in `snippets/lusena-pdp-scripts.liquid`
  - Existing buy-box accordions: `snippets/lusena-pdp-accordions.liquid` rendered inside `sections/lusena-main-product.liquid`

## Decisions (Confirmed)

1. Placement of the fragment on Shopify PDP:
   - Full-width section below Quality Evidence (match draft flow).

2. Keep or remove buy-box accordions (`snippets/lusena-pdp-accordions.liquid`):
   - Remove/hide from buy box to avoid duplicate "details" UI.

3. Data model for content:
   - Two product-specific panels (first in accordion): configurable per product via metafields (heading + content).
   - Remaining panels: configurable per product via list metafield (`lusena.pdp_details_panels`) with global section-block fallback.

## Open Questions (Resolved)

- Use 200ms ease-out for accordion open/close (draft timing).

## Data Sources & Content Model (Recommended)

### Product-specific (metafields; varies per product)

- Panel 1 (specs): heading + 8 fixed-row values rendered as a table
- Panel 2 (care): heading + bullet list

### Global (section settings; shared defaults)

- Shipping text (default)
- Returns + guarantee copy (default)
- Spec micro-definitions for "Splot", "Gęstość", "Klasa" (static educational copy; editable in section settings)

### Fallback logic

- If a product metafield is blank or missing, fall back to the section’s configured default.
- Ability to hide an entire panel when both product + fallback are blank.

## Target UX Spec (Draft Parity)

- Wrapper: `section#details` with top border (`border-t border-brand-bg`)
- Inner container:
  - vertical padding: mobile `py-12`, desktop `py-20`
  - centered heading:
    - font: serif (Source Serif 4)
    - size: `24px` mobile, `28px` desktop
    - desktop leading: `36px`
    - margins: `mb-8` mobile, `mb-12` desktop
- Accordion width: centered `max-w-3xl` with `mx-auto`
- Accordion item:
  - bottom border: `border-b border-secondary/20`
  - trigger:
    - `min-height: 44px`
    - `py-4`
    - hover color: `accent-cta`
    - chevron rotates 180deg when open
  - content:
    - typography: `text-sm`, body color `text-secondary`
    - padding: `pb-4`
    - open/close animation using `accordion-up/down` keyframes (0.2s ease-out)
- Specs table:
  - `text-sm`
  - zebra striping: `bg-surface-2/50` for even rows
  - definition row: `bg-brand-bg/60`, `text-xs`, `leading-relaxed`
  - definition triggers on labels:
    - inline "?" in `accent-cta`, `10px`
    - only for: Splot/Gęstość/Klasa
    - single-open behavior (opening one closes others)

## Implementation Approach (Theme)

- Add a dedicated section (new file) that renders the fragment as in draft.
  - Use the existing Tailwind utility classes already present in the theme (`assets/lusena-shop.css`) for 1:1 styling.
  - Use `<details>/<summary>` for native accessibility, with small JS to enforce "single" behavior and Radix-like animation attributes.
- Extend `snippets/lusena-pdp-scripts.liquid`:
  - Accordion: enforce single-open and set `data-state` + `--radix-accordion-content-height` for animation parity.
  - Specs table: manage definition toggles (`aria-expanded`, hide/show definition rows).
  - Keep existing "open returns and scroll to #details" behavior.
- Update `templates/product.json` to insert the new section and order it according to Decision 1.
- If Decision 2 Option A: remove/hide the buy-box accordions render from `sections/lusena-main-product.liquid`.

### Expected file changes

- Add: `sections/lusena-pdp-details-and-faq.liquid` (new)
- Update: `templates/product.json`
- Update (maybe): `sections/lusena-main-product.liquid`
- Update: `snippets/lusena-pdp-scripts.liquid`

## Milestones / Deliverables

1. New Shopify section renders the fragment with correct markup and classes.
2. JS behavior matches draft:
   - single-open accordion
   - animated open/close
   - returns link opens the returns panel and scrolls
   - specs micro-definitions toggles work
3. Theme validation clean via Shopify Dev MCP `validate_theme`.
4. Manual parity check checklist completed by user (mobile + desktop).

## Verification Checklist (User-Led)

- Mobile (~390px):
  - heading size/spacing matches draft
  - accordion opens/closes with animation
  - only one accordion item open at a time
  - "?" definition rows toggle correctly
  - clicking returns link opens returns panel and scrolls
- Desktop (~1280px):
  - typography matches (serif heading, sizes, line-height)
  - `max-w-3xl` centering matches
  - hover/focus states match

## Risks / Edge Cases

- Products that are not silk: FAQ questions about silk/poszewka must be hidden or overridden.
- Missing metafields: ensure graceful fallbacks and no empty panels.
- Double-rendering if buy-box accordions remain enabled (Decision 2).
