# LUSENA Button System + Loading Motion Parity Plan (Draft shop -> Shopify theme)

Created: 2026-02-19  
Status: Planned (awaiting implementation approval)  
Owner: Codex

## Goal

Migrate the recent draft-shop button standardization and loading-motion update into the active LUSENA Dawn theme with 1:1 visual and interaction parity across PDP actions, sticky ATC, cart drawer actions, icon-only controls, and related focus states.

Parity in this migration means:
- Same button visual system (variants, sizes, radius, focus ring, disabled treatment).
- Same loading UX primitives (text/dots swap, shimmer, reduced-motion behavior).
- Same interaction timing for PDP add-to-cart flows and cart upsell loading.
- Same icon-button ergonomics and focus affordances.

## Scope

### In scope
- PDP main actions: primary ATC + outline secondary button in `snippets/lusena-pdp-atc.liquid`.
- Sticky ATC desktop/mobile CTA loading propagation in `snippets/lusena-pdp-sticky-atc.liquid`.
- Cart drawer icon controls, quantity steppers, and upsell `Dodaj` loading behavior in `snippets/cart-drawer.liquid`.
- Header icon controls in `sections/lusena-header.liquid`.
- Lightbox nav/close controls and gallery/thumbnail focus-visible parity in PDP media files.
- Variant swatch focus-visible parity and quality-evidence toggle focus-visible parity.
- Shared loading animation CSS (shimmer + dots + reduced-motion handling) and shared button class primitives for touched surfaces.

### Out of scope
- Full rewrite of Dawn core button system (`assets/base.css` button primitive).
- New checkout/cart architecture beyond requested loading/state parity.
- Unrelated sections not listed in source change scope.

## Source of truth (Draft shop)

- `lusena-shop/src/components/ui/Button.tsx`
- `lusena-shop/src/components/ui/IconButton.tsx`
- `lusena-shop/src/index.css`
- `lusena-shop/src/pages/Product.tsx`
- `lusena-shop/src/components/product/StickyATC.tsx`
- `lusena-shop/src/components/cart/CartDrawer.tsx`
- `lusena-shop/src/components/layout/Header.tsx`
- `lusena-shop/src/components/product/ImageLightbox.tsx`
- `lusena-shop/src/components/product/QuantitySelector.tsx`
- `lusena-shop/src/components/product/VariantSelector.tsx`
- `lusena-shop/src/components/product/QualityEvidenceStack.tsx`
- `lusena-shop/src/components/product/MediaGallery.tsx`

## Target in theme (Shopify)

- `sections/lusena-main-product.liquid` (active PDP section rendered by `templates/product.json`)
- `snippets/lusena-pdp-atc.liquid`
- `snippets/lusena-pdp-sticky-atc.liquid`
- `snippets/lusena-pdp-scripts.liquid`
- `snippets/lusena-pdp-styles.liquid`
- `snippets/lusena-pdp-variant-picker.liquid`
- `snippets/lusena-pdp-media.liquid`
- `sections/lusena-pdp-quality-evidence.liquid`
- `snippets/cart-drawer.liquid`
- `sections/lusena-header.liquid`
- `snippets/lusena-missing-utilities.liquid` (only if minimal utility backfill is required)

## Decisions (final) - 2026-02-19

1. Reuse the existing LUSENA utility language (`rounded-brand`, accent tokens, `focus-visible` ring classes) and add only the missing loading primitives and state wiring.
2. Keep implementation on currently rendered LUSENA paths (no edits to unused Dawn section implementations).
3. Preserve theme breakpoints already used by LUSENA PDP/cart/header (`md`/`lg`) while matching draft behavior at ~390px and ~1280px.
4. Implement reduced-motion handling for button loading animations consistent with draft intent (`0.15s` reduction behavior).

## Open questions / unresolved assumptions

- `Buy now` behavior parity: draft notes show `await 500ms -> addToCart() -> await 350ms -> reset` (drawer-first behavior), while theme currently performs cart add then checkout redirect in `snippets/lusena-pdp-scripts.liquid`. Confirm which behavior should be implemented.

## Data sources & content model

- Product variant state: Shopify `product.variants` + selected options in `snippets/lusena-pdp-scripts.liquid`.
- Cart operations: existing `product-form.js` + `cart-drawer` section rendering.
- Button labels:
  - Existing: `section.settings.add_to_cart_label`, `section.settings.buy_now_label`, `section.settings.sticky_add_to_cart_label`.
  - Planned for loading text: section settings in `sections/lusena-main-product.liquid` (to avoid hardcoded copy and keep merchant control).
- Stock/availability: existing `variant.available` flow with `data-lusena-stock-*`.
- Upsell CTA: existing cart upsell form in `snippets/cart-drawer.liquid`.

## Target UX spec (Desktop + Mobile)

### Desktop (~1280px)
- PDP primary and outline buttons keep existing layout/size but gain standardized loading overlay behavior.
- Sticky ATC CTA reflects the same loading state as main ATC interaction.
- Cart drawer upsell `Dodaj` uses loading dots + loading shimmer behavior while request is in-flight.
- Header and lightbox icon-only actions use consistent 44px/36px round hit-target treatment and accent focus ring.

### Mobile (~390px)
- Same loading semantics as desktop for PDP ATC and sticky ATC.
- Cart drawer quantity controls and close controls use consistent icon-button states and focus behavior.
- Gallery/variant/quality toggle controls expose explicit keyboard-visible focus state.

### Accessibility
- Loading buttons set `disabled`, `aria-busy="true"`, and preserve visible focus outline when focus-visible.
- Icon controls retain semantic `<button>`/`<a>` usage with explicit `aria-label`.
- Focus-visible states added where currently missing (thumbnails/swatches/accordion toggles/lightbox controls).

## Theme capability & conflict audit

| Capability / token | Draft source | Resolved draft value | Exists in theme? | Conflict detected? | Planned implementation path | Target file |
|---|---|---|---|---|---|---|
| `rounded-brand` | `Button.tsx`, `IconButton.tsx` | `6px` | Yes | No | Reuse existing utility | `assets/lusena-shop.css`, `snippets/lusena-missing-utilities.liquid` |
| Primary button base | `Button.tsx` | `bg-accent-cta`, white text, `duration-150` | Yes | No | Reuse current classes | `snippets/lusena-pdp-atc.liquid`, `snippets/cart-drawer.liquid` |
| Outline button base | `Button.tsx` | border accent + transparent bg | Yes | No | Reuse current classes | `snippets/lusena-pdp-atc.liquid`, `snippets/cart-drawer.liquid` |
| Focus ring standard | `Button.tsx`, `IconButton.tsx` | `focus-visible:ring-2 ring-accent-cta ring-offset-2` | Partial | Yes (some places still `ring-1 ring-primary/20` or none) | Normalize class usage on touched controls | `snippets/lusena-pdp-atc.liquid`, `sections/lusena-header.liquid`, `snippets/lusena-pdp-media.liquid`, `snippets/lusena-pdp-variant-picker.liquid`, `sections/lusena-pdp-quality-evidence.liquid` |
| Disabled visual state | `Button.tsx` | `disabled:bg-neutral-400 disabled:text-surface-1/70` | Partial | Yes (some controls use only opacity) | Standardize on touched action buttons | `snippets/lusena-pdp-atc.liquid`, `snippets/lusena-pdp-sticky-atc.liquid`, `snippets/cart-drawer.liquid` |
| Loading shimmer keyframes | `index.css` | `@keyframes btn-shimmer 0.9s` | No | No | Add scoped/shared CSS | `snippets/lusena-pdp-styles.liquid` (or dedicated new snippet) |
| Dot-wave keyframes + dots | `Button.tsx`, `index.css` | 3 dots, 6x6, `1.2s`, `200ms` stagger | No | No | Add shared class + markup hooks | `snippets/lusena-pdp-styles.liquid`, `snippets/lusena-pdp-atc.liquid`, `snippets/cart-drawer.liquid` |
| Loading overlay model | `Button.tsx` | hide children `opacity-0`, absolute centered overlay | No | Yes (theme uses spinner-inline/default Dawn) | Add loading wrapper spans + data hooks + CSS | `snippets/lusena-pdp-atc.liquid`, `snippets/lusena-pdp-sticky-atc.liquid`, `snippets/cart-drawer.liquid` |
| Outline loading palette | `index.css` | `#F0EEEB`, border `rgba(14,94,90,.30)`, teal shimmer | No | No | Add outline loading modifier class | `snippets/lusena-pdp-styles.liquid` |
| Reduced motion for loading | `index.css` | animation/transition duration `0.15s` | Partial | Yes (not applied to new loading classes) | Add explicit reduced-motion override for new classes | `snippets/lusena-pdp-styles.liquid` |
| Icon button `md` size | `IconButton.tsx` | `44x44` | Partial | No | Reuse existing utility + normalize classes | `sections/lusena-header.liquid`, `snippets/cart-drawer.liquid`, `snippets/lusena-pdp-media.liquid` |
| Icon button `sm` size | `IconButton.tsx` | `36x36` | Yes | No | Reuse existing min-size utilities | `snippets/cart-drawer.liquid` |
| Swatch focus ring | `VariantSelector.tsx` | accent ring on keyboard focus | No | No | Add focus-visible classes to color/text options | `snippets/lusena-pdp-variant-picker.liquid` |
| Quality accordion focus | `QualityEvidenceStack.tsx` | clear focus-visible ring on toggle | No | No | Add focus-visible classes | `sections/lusena-pdp-quality-evidence.liquid` |
| Media thumb focus | `MediaGallery.tsx` | focus-visible ring on thumbs | No | No | Add focus-visible classes | `snippets/lusena-pdp-media.liquid` |
| Lightbox icon controls | `ImageLightbox.tsx` | overlay icon style + focus ring parity | Partial | Yes (hover exists, focus style minimal) | Add focus-visible accent ring | `snippets/lusena-pdp-styles.liquid`, `snippets/lusena-pdp-media.liquid` |

Audit rules:
- Resolve merged utility output before porting.
- Avoid conflicting focus/disabled/loading class combinations on same element.
- Prefer scoped, semantic classes for loading primitives over large global utility additions.

## Parity contract table

| Selector / element | Property | Draft value | Theme target value | State | Breakpoint | Tolerance |
|---|---|---|---|---|---|---|
| `.lusena-btn--primary` | `height` | `48px` (`h-12`) | `48px` | default | all | exact |
| `.lusena-btn--outline` | `height` | `48px` (`h-12`) | `48px` | default | all | exact |
| `.lusena-sticky-atc__button` | `height` | `44px` (`h-11`) | `44px` | default | all | exact |
| `.lusena-cart-upsell__add` | `height` | `32px` (`h-8`) | `32px` | default | all | exact |
| `.btn-loading-shimmer::after` | animation | `btn-shimmer 0.9s infinite` | same | loading | all | exact |
| `.btn-loading-shimmer--outline` | `background-color` | `#F0EEEB` | `#F0EEEB` | loading | all | exact |
| `.btn-loading-shimmer--outline` | `border-color` | `rgba(14,94,90,.30)` | same | loading | all | exact |
| `.btn-loading-dots span` | size | `6px x 6px` | `6px x 6px` | loading | all | exact |
| `.btn-loading-dots span` | animation | `dot-wave 1.2s ease-in-out infinite` | same | loading | all | exact |
| `.btn-content` | opacity transition | `150ms` fade to `0` | same | loading | all | exact |
| `.lusena-icon-button--md` | dimensions | `44px` square | `44px` square | default | all | exact |
| `.lusena-icon-button--sm` | dimensions | `36px` square | `36px` square | default | all | exact |
| focus-visible controls | ring | `2px accent + offset 2` | same | keyboard focus | all | exact |

## State fixture matrix

| State | Required fixture/data | Expected UI/UX |
|---|---|---|
| PDP ATC idle | Available variant | Main ATC visible text, no overlay, enabled |
| PDP ATC loading | Click ATC | Button disabled + `aria-busy`, text fades, loading text `Dodaję...`, shimmer active |
| PDP Buy now idle | Available variant | Outline button visible, enabled |
| PDP Buy now loading | Click Buy now | Outline button disabled + loading text `Przekierowuję...`, outline loading palette + shimmer |
| Sticky ATC loading | Trigger add from sticky or main CTA | Sticky CTA mirrors loading state with same visual model |
| Variant unavailable | Unavailable variant | ATC/Buy now/sticky buttons disabled, stock state updates |
| Cart upsell idle | Eligible upsell in cart | `Dodaj` outline button visible, no loading overlay |
| Cart upsell loading | Submit upsell form | `Dodaj` button shows loading dots + shimmer until request settles |
| Header icon focus | Keyboard tab on icon links | Accent focus ring visible, no layout shift |
| Lightbox nav focus | Keyboard tab on nav/close | Accent focus ring on overlay icon controls |
| Variant swatch focus | Keyboard focus on swatch/pill | Accent focus-visible ring present |
| Quality accordion focus | Keyboard focus on toggle | Accent focus-visible ring present |
| Reduced motion | OS prefers-reduced-motion | Loading animations/transitions reduced to ~0.15s |

## Implementation approach

1. Add shared button-loading primitives (keyframes, shimmer modifiers, loading-dots utility, reduced-motion override) in a scoped theme stylesheet surface used by PDP/cart/header media controls.
2. Refactor PDP action markup to include stable content/overlay spans and explicit loading text hooks (`data-*`) while preserving existing product-form integration.
3. Extend `snippets/lusena-pdp-scripts.liquid` to orchestrate ATC/Buy-now/sticky loading state lifecycle and timing parity (500ms pre-add + 350ms hold where applicable), synchronized with existing cart events.
4. Update cart drawer upsell and icon controls to shared icon-button/button classes and loading-dots behavior without breaking AJAX update/remove flows.
5. Add missing focus-visible states in variant picker, quality evidence toggles, gallery thumbnails/lightbox controls, and header icon actions.
6. Run Shopify MCP validation on all touched files and iterate until clean.

Implementation rules:
- Keep current `data-*` hooks stable unless explicit replacement is needed.
- Do not alter unrelated Dawn primitives.
- Keep Liquid text configurable via settings where new user-facing strings are introduced.

## Milestones / deliverables

1. Plan approved by user and open question resolved.
2. Button/loading primitive layer implemented.
3. PDP + sticky ATC loading parity implemented.
4. Cart drawer + icon-button parity implemented.
5. Focus-state parity implemented for variant/quality/media/header controls.
6. Shopify `validate_theme` passes for touched files.

## Verification checklist (developer pre-check)

### Computed-style checks

Breakpoints:
- Mobile: ~390px
- Desktop: ~1280px

Check for critical selectors:
- Button heights (`h-12`, `h-11`, upsell `h-8`)
- Focus ring thickness/color/offset
- Loading overlay positioning (`absolute inset-0` center)
- Shimmer gradients for primary vs outline
- Dot size, gap, and stagger timing

### Behavior checks

- PDP primary ATC loading transitions and reset behavior.
- PDP outline buy-now loading transitions and fallback paths.
- Sticky ATC loading mirroring.
- Cart upsell loading + success behavior remains intact.
- Header/lightbox/variant/quality keyboard focus states.

## Verification checklist (user visual confirmation)

1. Compare draft vs theme at ~390px and ~1280px for PDP buttons, sticky ATC, cart upsell button, and icon controls.
2. Verify loading visuals: text/dots swap, shimmer differences (primary vs outline), and reduced-motion behavior.
3. Verify focus-visible parity using keyboard Tab navigation.
4. Report any mismatch with page URL + viewport + state (idle/loading/focus).

## Risks / edge cases

- Product-form lifecycle currently toggles default Dawn `.loading` behavior; custom loading hooks must not regress cart-add reliability.
- Cart drawer rerenders can reset transient UI state; loading and success feedback wiring must survive rerender boundaries.
- Buy-now behavior mismatch risk if checkout redirect semantics are changed without explicit confirmation.

## Validation and wrap-up

- Shopify Dev MCP `validate_theme`: pending
- Files to include in summary:
  - `docs/LUSENA_Button_System_Loading_Parity_Plan.md`
  - (implementation files after approval)
- Optional after implementation:
  - Update `docs/THEME_CHANGES.md`
  - Create commit

