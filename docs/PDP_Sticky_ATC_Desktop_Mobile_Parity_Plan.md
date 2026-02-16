# PDP Sticky ATC Desktop + Mobile Parity Plan (Draft shop -> Shopify theme)

Created: 2026-02-14  
Status: Planned  
Owner: Codex

## Goal

Migrate the updated draft-shop sticky ATC component to the Shopify PDP so both mobile and desktop sticky bars match draft behavior and visual design with parity-level accuracy.

## Scope

### In scope
- Sticky bar shell, mobile layout, and desktop layout from draft source.
- Draft parity for trust row/copy, CTA sizing, image/meta layout, and desktop divider/title/price/trust arrangement.
- Existing sticky show/hide behavior driven by `#main-cta` visibility.
- Variant-driven sticky updates (price, per-night text, selected variant label, image, availability/disabled state).

### Out of scope
- Rework of main buy-box layout and non-sticky PDP modules.
- New metafields/metaobjects for sticky content.
- Refactor of unrelated PDP JS logic.

## Source of truth (Draft shop)

- `lusena-shop/src/components/product/StickyATC.tsx`
- `lusena-shop/src/components/ui/Button.tsx`
- `lusena-shop/src/pages/Product.tsx`
- `lusena-shop/src/lib/pdp-content.ts`

## Target in theme (Shopify)

- `sections/lusena-main-product.liquid` (render path + settings already available)
- `snippets/lusena-pdp-sticky-atc.liquid`
- `snippets/lusena-pdp-scripts.liquid`
- `templates/product.json` (only if sticky label content update is needed for parity)

## Decisions (final) - 2026-02-14

1. Interaction model: match draft behavior exactly for sticky visibility (show after main CTA leaves viewport) while keeping current observer fallback logic.
2. Breakpoints: use draft breakpoint behavior (`md` split, ~768px) for mobile vs desktop sticky layout.
3. Content model: reuse current section settings and product data; use `sticky_add_to_cart_label` for mobile CTA and `add_to_cart_label` for desktop CTA to match draft’s short/long CTA pattern without adding new settings.
4. Styling strategy: where draft utility tokens are missing in theme CSS, implement scoped semantic classes in `snippets/lusena-pdp-sticky-atc.liquid` instead of global utility backfills.

## Open questions / unresolved assumptions

None.

## Data sources & content model

- Product/variant data comes from existing JSON already rendered in `sections/lusena-main-product.liquid`.
- Sticky dynamic fields remain variant-driven:
  - price
  - per-night price text
  - selected color/variant label
  - variant image fallback chain
  - availability/disabled state
- Existing settings reused:
  - `price_per_night_prefix`
  - `price_per_night_suffix`
  - `sticky_add_to_cart_label` (mobile CTA)
  - `add_to_cart_label` (desktop CTA)
- Fallback behavior:
  - no variant image -> product featured image -> placeholder box
  - no color option -> fallback to first variant option/title

## Target UX spec (Desktop + Mobile)

### Desktop (~1280px)
- Sticky bar is visible when main CTA is out of viewport and appears from bottom with same transform transition as draft.
- Horizontal layout includes thumbnail, truncated product title, divider, price + per-night text, divider, trust row, CTA.
- Container centers with max content width and desktop paddings matching draft proportions.
- CTA uses small button height (`44px`) and extended label text.

### Mobile (~390px)
- Sticky bar has two rows:
  - trust strip with shield icon and `60 dni na zwrot · Darmowa dostawa`
  - product row with image, price/per-night/variant stack, and CTA
- CTA remains compact (`44px`) with short label.
- Bottom fixed bar with translucent surface background + blur + top border + subtle top shadow.

### Accessibility
- Sticky CTA buttons remain native `button type="submit"` with shared `form` target.
- Existing focus-visible ring behavior preserved.
- Disabled state mirrors variant availability for all sticky CTAs.

## Theme capability & conflict audit

| Capability / token | Draft source | Resolved draft value | Exists in theme? | Conflict detected? | Planned implementation path | Target file |
|---|---|---|---|---|---|---|
| `bg-surface-1/95` | `lusena-shop/src/components/product/StickyATC.tsx:28` | rgba(255,255,255,0.95) background | No | No | Scoped CSS on sticky wrapper | `snippets/lusena-pdp-sticky-atc.liquid` |
| `backdrop-blur-sm` | `lusena-shop/src/components/product/StickyATC.tsx:28` | blur(4px) backdrop | Yes | No | Reuse utility class | `snippets/lusena-pdp-sticky-atc.liquid` |
| `max-w-screen-xl` | `lusena-shop/src/components/product/StickyATC.tsx:71` | centered max width ~1280px | No | No | Scoped desktop container max-width | `snippets/lusena-pdp-sticky-atc.liquid` |
| `max-w-[200px]` | `lusena-shop/src/components/product/StickyATC.tsx:82` | 200px title max-width | No | No | Scoped title max-width class | `snippets/lusena-pdp-sticky-atc.liquid` |
| `w-px` + `bg-secondary/15` | `lusena-shop/src/components/product/StickyATC.tsx:87` | 1px divider, rgba(74,74,74,0.15) | No | No | Scoped `.lusena-sticky-atc__divider` class | `snippets/lusena-pdp-sticky-atc.liquid` |
| `lg:px-10` | `lusena-shop/src/components/product/StickyATC.tsx:71` | 40px horizontal padding at lg | No | No | Scoped media query padding rule | `snippets/lusena-pdp-sticky-atc.liquid` |
| Existing `md:hidden` in theme sticky bar | `snippets/lusena-pdp-sticky-atc.liquid:42` | hides bar on desktop | Yes | Yes | Remove conflict; introduce explicit mobile + desktop sub-layouts | `snippets/lusena-pdp-sticky-atc.liquid` |
| Sticky hook selectors with single-node queries | `snippets/lusena-pdp-scripts.liquid:16-24` | only first matched element updated | Yes | Yes | Switch to multi-node updates for duplicated desktop/mobile sticky fields | `snippets/lusena-pdp-scripts.liquid` |

## Parity contract table

| Selector / element | Property | Draft value | Theme target value | State | Breakpoint | Tolerance |
|---|---|---|---|---|---|---|
| `.lusena-sticky-atc` | `background-color` | `rgba(255,255,255,0.95)` | `rgba(255,255,255,0.95)` | default | all | exact |
| `.lusena-sticky-atc` | `backdrop-filter` | `blur(4px)` | `blur(4px)` | default | all | exact |
| `.lusena-sticky-atc` | `transform` hidden state | `translateY(100%)` | `translateY(100%)` | hidden | all | exact |
| `.lusena-sticky-atc__trust-text` | copy | `60 dni na zwrot · Darmowa dostawa` | same | default | mobile+desktop | exact |
| `.lusena-sticky-atc__mobile .lusena-sticky-atc__image` | `width/height` | `44px` | `44px` | default | mobile | exact |
| `.lusena-sticky-atc__desktop .lusena-sticky-atc__image` | `width/height` | `40px` | `40px` | default | desktop | exact |
| `.lusena-sticky-atc__desktop-title` | `max-width` | `200px` (+ larger at lg) | `200px` (+ larger at lg) | default | desktop | exact |
| `.lusena-sticky-atc__divider` | `width/background` | `1px`, `rgba(74,74,74,0.15)` | same | default | desktop | exact |
| `.lusena-sticky-atc__button` | `height` | `44px` | `44px` | default | all | exact |

## State fixture matrix

| State | Required fixture/data | Expected UI/UX |
|---|---|---|
| Hidden | Main CTA in viewport | Sticky bar translated off-screen |
| Visible | Main CTA above viewport | Sticky bar visible at bottom |
| Variant available | Any available variant selected | Sticky CTA enabled (mobile + desktop) |
| Variant unavailable | Out-of-stock variant selected | Sticky CTA disabled (mobile + desktop) |
| With image | Variant has featured image | Sticky thumbnail updates to variant image |
| Without image | Variant/product has no image | Placeholder/previous fallback shown without layout shift |
| Long product title | Product with long title | Desktop title truncates, no overlap with CTA |
| Long variant value | Long color/option label | Mobile variant line truncates cleanly |

## Implementation approach

1. Update `snippets/lusena-pdp-sticky-atc.liquid` to render both mobile and desktop sticky sub-layouts with draft-equivalent structure and scoped CSS for missing tokens.
2. Preserve existing data hooks and add duplicated hooks where needed for desktop fields.
3. Update `snippets/lusena-pdp-scripts.liquid` to support multiple sticky elements (price/per-night/variant/image/CTA) via node lists instead of single-node selectors.
4. Keep visibility observer logic unchanged apart from selector compatibility.
5. Run Shopify validation on touched files and fix any violations.

## Milestones / deliverables

1. Plan approved by user.
2. Sticky desktop+mobile implementation completed in theme files.
3. Shopify `validate_theme` passes for touched files.
4. Parity checks complete at ~390px and ~1280px.

## Verification checklist (developer pre-check)

### Computed-style checks

Breakpoints:
- Mobile: ~390px
- Desktop: ~1280px

Check:
- sticky wrapper background alpha + blur
- trust row spacing and divider
- image dimensions (44px mobile / 40px desktop)
- CTA height + paddings
- desktop divider line thickness/color
- title truncation and container width behavior

### Behavior checks

- Sticky remains hidden while `#main-cta` is visible.
- Sticky appears once `#main-cta` leaves viewport.
- Variant switch updates all sticky fields in both layouts.
- Availability toggle disables both sticky CTA buttons.

## Verification checklist (user visual confirmation)

1. Compare draft vs theme sticky ATC on PDP at ~390px and ~1280px.
2. Confirm trust row text, spacing, and CTA labels match updated draft UI.
3. Confirm variant/image/price/per-night synchronization works on both layouts.
4. Confirm no overlap or clipping with long product titles.

## Risks / edge cases

- Desktop sticky may appear less frequently on products where the sticky buy box keeps main CTA in viewport; this is expected because draft logic uses the same trigger condition.
- Duplicating sticky fields for mobile+desktop requires JS updates to all matching nodes; missing one selector would create mismatch between layouts.
- Button label parity depends on section setting values currently configured in template data.

## Validation and wrap-up

- Shopify Dev MCP `validate_theme`: pending
- Files to include in summary:
  - `snippets/lusena-pdp-sticky-atc.liquid`
  - `snippets/lusena-pdp-scripts.liquid`
  - `docs/PDP_Sticky_ATC_Desktop_Mobile_Parity_Plan.md`
  - `templates/product.json` (if text defaults are adjusted)
- Optional after approval:
  - Update `docs/THEME_CHANGES.md`
  - Create commit
