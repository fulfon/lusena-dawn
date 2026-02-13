# PDP Buy Box Parity Plan (Draftshop → Theme)

## Goal

Port the **LUSENA draft shop PDP buy box fragment** (right column, above the fold) into the Shopify theme PDP so that it **matches the draft shop exactly** (layout, spacing, typography, copy, states, and breakpoints).

Target fragment (copy + structure):

- Eyebrow: “Gładsza skóra i lśniące włosy — od pierwszej nocy.”
- Title: “Jedwabna Poszewka 22 Momme”
- Short description (desktop only): “100% jedwab morwowy Grade 6A z Suzhou, 22 momme, certyfikat OEKO-TEX® Standard 100. Jedwab redukuje tarcie o 43% vs bawełna — Twoja skóra i włosy poczują różnicę.”
- Price: “249 zł”
- Per-night line: “Tylko 0,68 zł / noc (przy rocznym użytkowaniu)”
- Delivery micro-line: “To zamówienie kwalifikuje się do darmowej dostawy · Dostawa: 1–2 dni robocze · 60 dni na zwrot”
- Proof chips: “OEKO-TEX® 100”, “22 momme”, “Wysyłka 24h z PL”, “60 dni na zwrot”, “Na prezent”
- Variant label: “Wybierz kolor: Beżowy”
- CTA buttons: “Dodaj do koszyka – wysyłka dziś”, “Kup teraz”
- Stock: “Na stanie, gotowe do wysyłki”
- Guarantee strip: “60 dni gwarancji spokojnego snu · Jak to działa?”
- Payments: “Visa”, “Mastercard”, “BLIK”, “PayPo”, “Przelewy24”, “Bezpieczna płatność”

## Scope

### In scope
- PDP right-column buy box markup and styling.
- Mobile/desktop **ordering** and spacing (Tailwind `order-*` + `md:order-*` pattern).
- Copy parity (strings and punctuation: en dashes, middots, commas).
- Icons parity (Lucide-style SVGs: `truck`, `shield-check`, `layers`, `rotate-ccw`, `gift`, `lock`).
- Variant selection UI parity (swatches/pills, selected state styling).
- Price + per-night formatting parity (price without trailing zeros; per-night with two decimals).

### Out of scope (for this change)
- Full PDP below-the-fold content parity (feature highlights, full details accordion structure, FAQ content).
- Changing Shopify data model (creating metafield definitions in Admin).

## Source of truth (draft shop)

- Layout + ordering: `lusena-shop/src/pages/Product.tsx`
- Microcopy constants: `lusena-shop/src/lib/pdp-content.ts`
- Proof chips UI: `lusena-shop/src/components/product/ProofChips.tsx`
- Variant selector UI: `lusena-shop/src/components/product/VariantSelector.tsx`
- Button styling: `lusena-shop/src/components/ui/Button.tsx`
- Tailwind tokens (colors/radii/fonts): `lusena-shop/tailwind.config.js`

## Target in theme (Shopify Dawn)

- PDP section: `sections/lusena-main-product.liquid`
- Buy box snippets:
  - `snippets/lusena-pdp-summary.liquid`
  - `snippets/lusena-pdp-variant-picker.liquid`
  - `snippets/lusena-pdp-atc.liquid`
  - `snippets/lusena-pdp-guarantee.liquid`
  - new: `snippets/lusena-pdp-proof-chips.liquid`
  - new: `snippets/lusena-pdp-payment.liquid`
- Supporting:
  - `snippets/lusena-icon.liquid` (add missing icons)
  - `snippets/lusena-pdp-styles.liquid` (selected-state styles, breakpoint alignment)
  - `snippets/lusena-pdp-scripts.liquid` (price/per-night formatting + optional “open returns” behavior)
- Template defaults (PL-first copy): `templates/product.json`

## Decisions (final) — 2026-02-08

1. **Breakpoints:** match draft shop Tailwind breakpoints (`md = 768px`), not Dawn’s 750px.
2. **Copy source:** use section settings for microcopy defaults (so the UI renders correctly even without metafields). Where feasible, allow a product metafield override later without changing markup.
3. **“Kup teraz” behavior:** keep UI identical; behavior can initially submit the same ATC flow (draft behavior). If we later want true buy-now, we’ll add a dedicated redirect-to-checkout flow.
4. **Payment methods list:** static labels (as in draft shop), not derived from Shopify payment providers.

## Data sources & content model

- `product.title`: Shopify product title.
- Eyebrow (`product.subtitle`) and short description (`product.shortDescription`): **section settings** (defaults set to the draft copy).
- Price: `current_variant.price`.
- Per-night: computed from `current_variant.price / 365`.
- Variant selections: Shopify variants/options (render as swatches for “color/kolor” options).
- Proof chips / payment methods: static list in Liquid snippet (matches draft).

## UX spec (must match draft)

### Desktop (≥ 768px)
- Right column is sticky (`top-32`) and ordered:
  1) Eyebrow + title + short description
  2) Price + per-night
  3) Delivery micro-line
  4) Proof chips
  5) Divider line
  6) Variant selector
  7) CTAs + stock
  8) Guarantee strip
  9) Payment reassurance

### Mobile (< 768px)
- Right column is not sticky.
- Proof chips move after guarantee, and mobile benefits list appears at the end (if benefit blocks exist).

## Milestones / deliverables

1. Buy box markup matches draft shop DOM structure + Tailwind classes.
2. Icons match (size/color) and are available via `lusena-icon`.
3. Price + per-night formatting stable on variant change.
4. `templates/product.json` defaults are PL-first and match the fragment.

## Verification checklist

- Theme validation passes (`validate_theme`) for all touched files.
- Visual checks (Playwright):
  - Mobile viewport (~390×844): correct ordering (proof chips after guarantee), correct text.
  - Desktop viewport (~1280×900): correct ordering, sticky behavior, correct spacing and typography.
- Variant change:
  - Updates price, per-night, stock state, and selected label.

## Risks / edge cases

- Store `money_format` can affect decimal output; we ensure **price** and **per-night** formatting remain consistent after variant changes.
- Products with multiple options (size + color) might render additional selectors; parity is guaranteed for the primary “color/kolor” option.
