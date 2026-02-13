# PDP Mobile Sticky ATC Parity Plan (Draft shop -> Shopify theme)

Date: 2026-02-10

## Goal

Port the provided draft-shop PDP fragment (mobile sticky add-to-cart bar) into the Shopify theme PDP with exact visual and interaction parity:

- fixed bottom mobile bar
- top trust row (`shield-check` icon + `60 dni na zwrot · Darmowa dostawa`)
- product thumbnail + price + per-night line + selected color line
- sticky add-to-cart button
- show/hide behavior tied to main PDP CTA visibility

## Scope

In scope:
- Sticky bar DOM structure, classes, spacing, sizing, and shadows from the provided fragment.
- Mobile behavior and breakpoint behavior exactly as draft classes imply (`md:hidden`).
- Dynamic PDP data binding for price, variant state, selected color, and image.
- Existing show/hide animation (`translate-y-full` <-> visible state) kept and mapped to parity classes.

Out of scope:
- Reworking desktop PDP buy box layout.
- Rebuilding unrelated PDP sections/snippets.
- Changing the store content model or creating new metafields.

## Non-goals

- No broad refactor of PDP scripts.
- No changes to gallery structure beyond data reuse for sticky thumbnail updates.

## Source of truth

- User-provided exact fragment markup/classes in the implementation request (single source for parity).
- Existing theme integration path:
  - `templates/product.json` -> `sections/lusena-main-product.liquid`
  - `snippets/lusena-pdp-sticky-atc.liquid`
  - `snippets/lusena-pdp-scripts.liquid`

## Target in theme

- `snippets/lusena-pdp-sticky-atc.liquid`
  - Replace current sticky bar markup with fragment-equivalent structure and classes.
  - Keep Liquid data hooks required by existing/additional JS updates.
- `snippets/lusena-pdp-scripts.liquid`
  - Extend variant update logic for sticky per-night line, sticky selected color, sticky thumbnail.
  - Keep IntersectionObserver show/hide logic with existing trigger (`#main-cta`).

## Decisions (final) - 2026-02-10

1. Breakpoint strategy: match draft fragment (`md`), i.e. 768px behavior from existing utility CSS.
2. Data strategy:
   - `price` = selected variant price (`money_without_trailing_zeros` / JS formatter on change).
   - `per-night` = selected variant price / 365 (same rule as current PDP summary).
   - `color` = selected color option value if color option exists; fallback to selected variant title/value.
   - `image` = selected variant featured image; fallback to product featured image.
3. Interaction strategy: keep existing sticky show/hide behavior (hidden while main CTA is in view, shown after it scrolls out), but with fragment visual classes.
4. Copy strategy: preserve fragment copy exactly where static (`60 dni na zwrot · Darmowa dostawa`, button text from existing sticky label setting if already aligned).

## Open questions / unresolved assumptions

None.

## Data sources and content model

- Product and variant JSON already embedded in `sections/lusena-main-product.liquid`.
- Existing section settings reused:
  - `price_per_night_prefix`
  - `price_per_night_suffix`
  - `sticky_add_to_cart_label`
- Existing product form id reused (`product_form_id`) so sticky button submits the same product form.

## Target UX spec

### Mobile (< 768px)

- Bar fixed at bottom, full width, `z-40`, white/surface background, top border, subtle top shadow.
- Two stacked rows:
  - trust row with icon + `60 dni na zwrot · Darmowa dostawa`
  - product row with image, text stack, and CTA
- Text stack:
  - price line (`text-sm`, medium)
  - per-night line (`text-xs`, accent color)
  - selected color line (`text-xs`, secondary)
- CTA:
  - height `h-11`, `text-xs`, accent background, disabled visuals as provided.
- Hidden/shown by transform transition (`translate-y-full` off-screen, visible state on scroll past main CTA).

### Desktop (>= 768px)

- Bar remains hidden via `md:hidden`.
- No desktop visual change to PDP layout.

## Implementation approach

Files to change:
1. `snippets/lusena-pdp-sticky-atc.liquid`
   - Render fragment-equivalent HTML structure/classes.
   - Add hooks for JS updates:
     - `data-lusena-sticky-atc`
     - `data-lusena-sticky-atc-button`
     - `data-lusena-sticky-price`
     - `data-lusena-sticky-price-per-night`
     - `data-lusena-sticky-variant`
     - `data-lusena-sticky-image`
2. `snippets/lusena-pdp-scripts.liquid`
   - Update sticky fields in `updateUIForVariant`.
   - Keep existing stock/button state sync and show/hide observer behavior.

## Milestones / deliverables

1. Sticky snippet matches provided fragment structure and classes.
2. Variant changes update sticky price/per-night/color/image correctly.
3. Sticky visibility behavior remains correct.
4. Theme validation passes for touched files.

## Verification checklist

Manual:
- Mobile viewport (~390x844):
  - sticky bar appears after main CTA scrolls out
  - trust row present and styled correctly
  - image, price, per-night, and color values are correct
  - button submits add-to-cart and disabled state follows availability
- Desktop viewport (~1280x900):
  - sticky bar is hidden

Variant interactions:
- Switching variant updates sticky price, per-night line, color label, and thumbnail.
- Unavailable variant disables sticky button.

Tooling:
- Run Shopify MCP `validate_theme` for all touched files and fix until clean.

Optional visual debugging:
- Use Playwright against `http://127.0.0.1:9292/` if mismatch is reported or layout is ambiguous.

## Risks / edge cases

- Products without a color option need fallback label logic for the third text line.
- Variants without dedicated featured images need robust fallback to product featured image.
- Money format differences across shops can alter decimal rendering; JS formatter should stay aligned with current PDP behavior.
