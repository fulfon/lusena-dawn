# PDP Gallery Zoom Lightbox Parity Plan (Draft shop -> Shopify theme)

Created: 2026-02-14  
Status: Planned  
Owner: Codex

## Goal

Port the draftshop gallery zoom/lightbox update to the live LUSENA Shopify PDP so image zoom behavior is functionally equivalent on desktop and mobile.

## Scope

### In scope
- Match draft lightbox behavior for product images: open/close, slide navigation, desktop click-to-zoom, desktop mouse-follow pan, mobile pinch/double-tap/pan/swipe.
- Preserve current LUSENA gallery variant filtering and proof tile behavior.
- Match mobile and desktop UX affordances (zoom icon, hints, disabled nav when zoomed).
- Add safe-area handling parity (`env(safe-area-inset-*)`) and ensure viewport meta supports it.
- Keep accessibility parity for dialog semantics, keyboard nav, and focus behavior.

### Out of scope
- Reworking Dawn default `product-media-gallery` / `media-gallery.js` path (not used by `templates/product.json`).
- Adding video zoom behavior (images only).
- Full rewrite of PDP gallery architecture outside zoom/lightbox requirements.

## Source of truth (Draft shop)

- `lusena-shop/src/components/product/MediaGallery.tsx`
- `lusena-shop/src/components/product/ImageLightbox.tsx`
- `lusena-shop/src/lib/utils.ts` (`cn()` behavior reference)
- `assets/lusena-shop.css` (resolved utility token values)

## Target in theme (Shopify)

- `templates/product.json` (live section route)
- `sections/lusena-main-product.liquid` (renders gallery snippet stack)
- `snippets/lusena-pdp-media.liquid` (gallery markup; add lightbox markup/hooks)
- `snippets/lusena-pdp-scripts.liquid` (gallery/lightbox logic)
- `snippets/lusena-pdp-styles.liquid` (lightbox/gallery styles)
- `layout/theme.liquid` (viewport meta)
- `layout/password.liquid` (viewport meta consistency)

## Decisions (final) - 2026-02-14

1. Interaction model: implement exact draft zoom/lightbox behavior for image media; proof tile remains non-zoomable.
2. Data model: reuse existing LUSENA visible-media pipeline (`[color=...]`, `[shared]`, proof tile append) and derive lightbox slides from visible image items only.
3. Breakpoint strategy: keep current theme gallery switching at `750px` (existing LUSENA PDP behavior), while preserving desktop/mobile interaction parity on both sides.
4. Safe area support: update viewport meta to include `viewport-fit=cover` and use safe-area paddings in lightbox top/bottom bars.
5. Stability: use stable named close handler + controlled listener binding in vanilla JS (no inline callback churn equivalent).

## Open questions / unresolved assumptions

- None.

## Data sources & content model

- Product media source: `product.media` and existing parsed alt-tag filtering in `snippets/lusena-pdp-scripts.liquid`.
- Active gallery state: existing `state.visibleItems` and `state.activeIndex` extended with lightbox index mapping.
- Proof tile source: existing `shop.metafields.lusena.oeko_tex_certificate` flow in `snippets/lusena-pdp-media.liquid`.
- Missing media fallback: keep existing placeholder/proof fallbacks; lightbox opens only for valid image slides.
- Translation strategy: keep consistent with current LUSENA PDP implementation pattern (PL-first inline copy in this fragment).

## Target UX spec (Desktop + Mobile)

### Desktop (~1280px)
- Clicking active stage image opens fullscreen lightbox on current visible image.
- In lightbox: click image toggles `1x <-> 1.5x`; when zoomed, pointer movement pans image.
- Arrow keys + on-screen arrows navigate slides when not zoomed.
- Escape closes; clicking backdrop closes; close button always available.
- Top counter and bottom usage hint match draft behavior.

### Mobile (~390px)
- Tapping image slide opens fullscreen lightbox.
- Pinch zoom up to `2.5x`, double-tap toggles zoom, single-finger pan while zoomed.
- Horizontal swipe changes slide only when not zoomed.
- Safe-area top/bottom spacing applies on notched devices.

### Accessibility
- Dialog uses `role="dialog"` and `aria-modal="true"`.
- Focus is moved to close button on open; keyboard trap limited to lightbox controls.
- Escape/arrow keyboard support on desktop.
- Buttons retain proper labels and disabled/hidden behavior by state.

## Theme capability & conflict audit

| Capability / token | Draft source | Resolved draft value | Exists in theme? | Conflict detected? | Planned implementation path | Target file |
|---|---|---|---|---|---|---|
| Fullscreen overlay stack | `ImageLightbox.tsx:377` | `position: fixed; inset:0; z-index:60` | Partial (`z-50` exists, no `z-60`) | No | Add scoped semantic class with explicit `z-index: 60` | `snippets/lusena-pdp-styles.liquid` |
| Lightbox image sizing | `ImageLightbox.tsx:443` | `max-height:85vh; max-width:90vw; object-fit:contain` | Partial (`h-[85vh]` exists, `object-contain` missing in current fragment styles) | No | Add explicit scoped CSS instead of utility class dependency | `snippets/lusena-pdp-styles.liquid` |
| Zoom cursors | `ImageLightbox.tsx:444` | `cursor: zoom-in/zoom-out` | No (not in LUSENA scoped gallery) | No | Add state-driven class toggles in JS + scoped cursor rules | `snippets/lusena-pdp-scripts.liquid` |
| Gesture safety | `ImageLightbox.tsx:380,449` | `touch-action: none` | No | No | Apply on lightbox container/image only | `snippets/lusena-pdp-styles.liquid` |
| Safe-area paddings | `ImageLightbox.tsx:384,476` | `env(safe-area-inset-top/bottom)` | No | No | Add CSS vars + bar paddings; requires viewport meta update | `snippets/lusena-pdp-styles.liquid`, `layout/theme.liquid`, `layout/password.liquid` |
| Mobile scrollbar hide | `MediaGallery.tsx:124` (`scrollbar-hide`) | hidden scrollbar | Yes (`scrollbar-width:none` + `::-webkit-scrollbar`) | No | Reuse existing manual CSS implementation | `snippets/lusena-pdp-styles.liquid` |
| Carousel geometry | `MediaGallery.tsx:128-129` | `85vw`, `max-width:400px`, `height:min(60vh,85vw)`, `aspect 4/5` | Yes | No | Reuse existing LUSENA gallery rules | `snippets/lusena-pdp-styles.liquid` |
| `cn()` class merge | `MediaGallery.tsx`, `ImageLightbox.tsx` | conditional class composition | No direct helper in Liquid | No | Use semantic classes + JS classList toggles; avoid utility merge helper | `snippets/lusena-pdp-media.liquid`, `snippets/lusena-pdp-scripts.liquid` |

Audit rules:
- Resolve merged utility output before porting to Liquid.
- Do not carry conflicting utility classes into the final markup.
- Prefer semantic, scoped fragment CSS over global utility expansion.
- Add utility backfills only when justified and reusable.

## Parity contract table

| Selector / element | Property | Draft value | Theme target value | State | Breakpoint | Tolerance |
|---|---|---|---|---|---|---|
| `.lusena-lightbox` | overlay background | `rgba(0,0,0,0.92)` | `rgba(0,0,0,0.92)` | open | all | exact |
| `.lusena-lightbox__image` | max size | `max-h:85vh; max-w:90vw` | `max-h:85vh; max-w:90vw` | default | all | exact |
| `.lusena-lightbox__image` | transform | `scale(zoom) translate(x,y)` | same transform pipeline | zoomed | all | exact |
| `.lusena-lightbox__image` | cursor | `zoom-in` / `zoom-out` | `zoom-in` / `zoom-out` | zoom toggle | desktop | exact |
| `.lusena-lightbox__nav` | visibility | hidden while zoomed | hidden while zoomed | zoomed | desktop | exact |
| `.lusena-lightbox__top` | safe area padding | `max(0.75rem, env(safe-area-inset-top))` | same | default | mobile | exact |
| `.lusena-lightbox__bottom` | safe area padding | `max(1rem, env(safe-area-inset-bottom))` | same | default | mobile | exact |
| `[data-lusena-mobile-track]` | horizontal behavior | snap + hidden scrollbar | unchanged existing behavior | default | mobile | exact |

## State fixture matrix

| State | Required fixture/data | Expected UI/UX |
|---|---|---|
| Empty | product with no valid image slide | lightbox does not open; gallery remains stable |
| Populated | product with 3+ images | open at tapped/clicked image, counter visible |
| Active/Selected | click desktop thumb / mobile slide | correct slide opens and matches visible gallery order |
| Hover | desktop stage image | zoom affordance visible (icon), hover cues preserved |
| Disabled | zoomed state | nav arrows hidden/disabled while zoom > 1 |
| Loading | image fetch delay | skeleton/pending state before image load |
| Error | invalid image URL | fallback message tile shown (non-crashing) |
| Success | normal close | fade-out then return to prior page state |
| Long content | long alt text | aria labels stay valid; layout unaffected |

## Implementation approach

1. Add lightbox markup container and control hooks into `snippets/lusena-pdp-media.liquid` (kept outside media track, mounted once).
2. Extend `snippets/lusena-pdp-scripts.liquid` with a dedicated lightbox module that:
   - builds slides from current visible image items,
   - opens from desktop stage click and mobile image slide click,
   - implements zoom/pan/gesture logic,
   - uses stable named handlers for `popstate`, keyboard, and touch/mouse listeners.
3. Add scoped lightbox styles to `snippets/lusena-pdp-styles.liquid` for overlay bars, controls, transform transitions, cursor states, safe-area spacing, and reduced-motion handling.
4. Update viewport meta `content` to `width=device-width,initial-scale=1,viewport-fit=cover` in `layout/theme.liquid` and `layout/password.liquid`.

Implementation rules:
- Modify only the code path used by the live template.
- Keep JS hooks stable (`data-*` selectors).
- Preserve semantic HTML and accessibility behavior.
- Normalize inline numeric styles from Liquid math to CSS-safe format.

## Milestones / deliverables

1. Plan approved by user.
2. Fragment implementation complete in theme files.
3. Shopify `validate_theme` passes on touched files.
4. Parity checks completed for required states and breakpoints.

## Verification checklist (developer pre-check)

### Computed-style checks

Breakpoints:
- Mobile: ~390px
- Desktop: ~1280px

Check for critical selectors:
- font-size
- line-height
- spacing (margin/padding/gap)
- dimensions (width/height/min/max)
- alignment (text-align, align-items, justify-content)
- visibility/display in each state

### Behavior checks

- Open lightbox from desktop stage image and mobile image slide.
- Escape closes; backdrop closes; close button closes.
- Desktop click toggles zoom and mouse-follow pan works only when zoomed.
- Mobile pinch/double-tap/pan works, swipe navigation only when zoom is 1.

## Verification checklist (user visual confirmation)

1. Compare draft vs theme at ~390px and ~1280px.
2. Confirm spacing/typography/colors match.
3. Confirm interactions and state transitions match.
4. Report mismatches with screenshot + viewport.

## Risks / edge cases

- Listener leaks in long browsing sessions if open/close lifecycle cleanup is incomplete.
- Variant switch while lightbox is open can invalidate current slide mapping.
- iOS Safari gesture differences may require tuning move thresholds and pinch clamps.
- Global viewport meta update affects entire storefront; needs quick smoke-check.

## Validation and wrap-up

- Shopify Dev MCP `validate_theme`: pending
- Files to include in summary:
  - `snippets/lusena-pdp-media.liquid`
  - `snippets/lusena-pdp-scripts.liquid`
  - `snippets/lusena-pdp-styles.liquid`
  - `layout/theme.liquid`
  - `layout/password.liquid`
- Optional after approval:
  - Update `docs/THEME_CHANGES.md`
  - Create commit
