# PDP Gallery Crossfade + Lazy Loading Parity Plan (Draft shop -> Shopify theme)

Created: 2026-02-16  
Status: Planned  
Owner: Codex

## Goal

Migrate the latest draftshop PDP gallery updates for:
- crossfade behavior
- conditional lazy loading

Target is 1:1 behavior parity with the current draft implementation in `lusena-shop/src/components/product/MediaGallery.tsx`.

## Scope

### In scope
- Desktop main-stage crossfade on thumbnail change.
- Crossfade reset behavior when visible gallery items change due to variant/color switch.
- Mobile gallery fade transition during variant/color-driven gallery reset.
- Lazy/eager loading behavior parity for gallery images (desktop + mobile).
- Keep existing LUSENA gallery filtering (`[color=...]`, `[shared]`) and proof tile behavior intact.

### Out of scope
- Reworking gallery layout structure, spacing, or iconography.
- Replacing existing LUSENA lightbox implementation.
- Dawn default `media-gallery` code path not used by `templates/product.json`.

## Source of truth (Draft shop)

- `lusena-shop/src/components/product/MediaGallery.tsx`
- `lusena-shop/src/pages/Product.tsx` (items array changes are driven by color selection)
- `assets/lusena-shop.css` (resolved utility timing/opacity classes used by draft)

## Target in theme (Shopify)

- `templates/product.json` (renders `lusena-main-product`)
- `sections/lusena-main-product.liquid`
- `snippets/lusena-pdp-media.liquid`
- `snippets/lusena-pdp-scripts.liquid`
- `snippets/lusena-pdp-styles.liquid`

## Decisions (final) - 2026-02-16

1. Interaction model: implement exact draft behavior for crossfade/lazy loading, without changing current LUSENA gallery architecture.
2. Breakpoint strategy: keep existing theme gallery display switch (`750px`) and apply parity logic within that existing split.
3. Data handling: no new settings/metafields/locales; reuse current variant/media filtering and selection state.

## Open questions / unresolved assumptions

None.

## Data sources & content model

- Product media source remains `product.media`.
- Variant/color scope remains current script logic (`getVisibleMediaForColor` and `buildVisibleItems`).
- Proof tile remains optional and appended when certificate data exists.
- No new merchant-configurable content for this migration.

## Target UX spec (Desktop + Mobile)

### Desktop (~1280px)
- Clicking a thumbnail fades main stage out, swaps media, then fades back in using 300ms timing.
- Active thumb state behavior remains unchanged.
- Main stage image remains eager-loaded.

### Mobile (~390px)
- On variant/color change that changes visible gallery items:
  - mobile gallery track fades out,
  - resets to first item/left edge,
  - fades in (300ms).
- Scroll/dot interactions continue to work as-is.

### Lazy loading parity
- Desktop thumbnails: lazy.
- Desktop main stage image: eager (high priority).
- Mobile slides: first visible media eager (high priority), remaining slides lazy.

### Accessibility
- Keep current button semantics and labels unchanged.
- Keep current zoom/lightbox keyboard behavior unchanged.
- No aria contract changes.

## Theme capability & conflict audit

| Capability / token | Draft source | Resolved draft value | Exists in theme? | Conflict detected? | Planned implementation path | Target file |
|---|---|---|---|---|---|---|
| Desktop stage crossfade timing | `lusena-shop/src/components/product/MediaGallery.tsx:31`, `lusena-shop/src/components/product/MediaGallery.tsx:174` | fade-out -> swap -> fade-in, `300ms`, `ease-in-out` | Partial (stage image has opacity transition but no 300ms swap orchestration) | No | Add JS fade orchestration state/timer around stage swaps | `snippets/lusena-pdp-scripts.liquid` |
| Mobile reset fade on items array change | `lusena-shop/src/components/product/MediaGallery.tsx:57`, `lusena-shop/src/components/product/MediaGallery.tsx:200` | track opacity transition `300ms` during items reset | No (track has no opacity transition/state class today) | No | Add mobile track fade class + JS reset/fade flow | `snippets/lusena-pdp-styles.liquid`, `snippets/lusena-pdp-scripts.liquid` |
| Transition token `duration-300 ease-in-out` | `lusena-shop/src/components/product/MediaGallery.tsx:174`, `lusena-shop/src/components/product/MediaGallery.tsx:200` | `transition: opacity 300ms cubic-bezier(.4,0,.2,1)` | Yes (`assets/lusena-shop.css` has `.duration-300`, `.ease-in-out`) | No | Use scoped semantic CSS with same resolved values | `snippets/lusena-pdp-styles.liquid` |
| Mobile first slide eager / others lazy | `lusena-shop/src/components/product/MediaGallery.tsx:216`, `lusena-shop/src/components/product/MediaGallery.tsx:315` | `i === 0` eager + high priority, others lazy | No (currently all mobile slides lazy) | No | Add Liquid first-slide conditional loading/fetch priority | `snippets/lusena-pdp-media.liquid` |
| Desktop main image eager + high priority | `lusena-shop/src/components/product/MediaGallery.tsx:178`, `lusena-shop/src/components/product/MediaGallery.tsx:317` | eager + high priority for active stage | Partial (stage initial image eager, no explicit priority attribute) | No | Add explicit priority attr on initial stage image and preserve eager swaps | `snippets/lusena-pdp-media.liquid`, `snippets/lusena-pdp-scripts.liquid` |
| Thumbnail lazy loading | `lusena-shop/src/components/product/MediaGallery.tsx:265` | lazy | Yes (`snippets/lusena-pdp-media.liquid:72`) | No | Reuse existing | `snippets/lusena-pdp-media.liquid` |

Audit rules:
- Resolve draft utility classes into concrete CSS behavior before porting.
- Avoid introducing conflicting utility classes in Liquid markup.
- Prefer scoped semantic CSS/JS in current LUSENA PDP snippet stack.

## Parity contract table

| Selector / element | Property | Draft value | Theme target value | State | Breakpoint | Tolerance |
|---|---|---|---|---|---|---|
| Desktop stage content | opacity transition | `300ms ease-in-out` | `300ms ease-in-out` | thumb switch | desktop | exact |
| Desktop stage switch flow | timing | fade-out -> swap at ~300ms -> fade-in | same | thumb switch | desktop | exact |
| Mobile track | opacity transition | `300ms ease-in-out` | `300ms ease-in-out` | variant/gallery reset | mobile | exact |
| Mobile reset behavior | scroll position | reset to first slide and left=0 after items change | same | variant/gallery reset | mobile | exact |
| Mobile first media image | loading | eager | eager | initial/current first | mobile | exact |
| Mobile first media image | priority | high | high | initial/current first | mobile | exact |
| Mobile non-first media | loading | lazy | lazy | default | mobile | exact |
| Desktop thumbs | loading | lazy | lazy | default | desktop | exact |

## State fixture matrix

| State | Required fixture/data | Expected UI/UX |
|---|---|---|
| Initial render | product with 3+ media | stage visible, first slide active, no flash |
| Desktop thumb change | click thumb 1 -> 2 | smooth 300ms crossfade |
| Variant switch (different color media) | variant with different media subset | desktop stage fades to new first item, mobile track fades out/in and resets to index 0 |
| Variant switch (shared only fallback) | variant with no color-specific media | first shared item selected with same fade/reset behavior |
| Proof active | proof tile selected | no stage-image zoom cues; no broken fade |
| Mobile scroll | swipe carousel | dots and active index remain in sync after migration |
| Reduced motion | prefers-reduced-motion enabled | transitions disabled where already defined, no broken state |

## Implementation approach

1. Update `snippets/lusena-pdp-media.liquid`:
- add conditional loading/fetch priority for first mobile slide image.
- ensure stage image includes explicit high-priority loading attribute.
2. Update `snippets/lusena-pdp-styles.liquid`:
- add semantic fade classes for desktop stage and mobile track with 300ms ease-in-out.
- keep current hover/zoom styles unchanged.
3. Update `snippets/lusena-pdp-scripts.liquid`:
- add crossfade timer/state orchestration for desktop stage swaps.
- add mobile track fade/reset flow when variant updates gallery items.
- preserve existing selection, dot syncing, proof, and lightbox flows.

Implementation rules:
- Modify only the active LUSENA PDP path.
- Keep `data-*` hooks stable.
- Preserve accessibility semantics and existing lightbox behavior.

## Milestones / deliverables

1. Plan approved by user.
2. Theme implementation completed in touched files.
3. Shopify `validate_theme` passes for touched files.
4. User visual confirmation on mobile + desktop parity.

## Verification checklist (developer pre-check)

### Computed-style checks

Breakpoints:
- Mobile: ~390px
- Desktop: ~1280px

Check:
- stage/track opacity transition timing
- first/non-first loading attributes
- reset to first item on variant switch
- dots/active thumb sync unchanged

### Behavior checks

- Desktop thumbnail click triggers crossfade.
- Variant change triggers desktop crossfade + mobile fade/reset.
- Mobile swipe still updates active dot/index.
- Proof tile and lightbox behavior remain stable.

## Verification checklist (user visual confirmation)

1. Compare draft vs theme at ~390px and ~1280px.
2. Check thumbnail switch animation smoothness on desktop.
3. Change color/variant and confirm gallery reset/fade behavior on mobile.
4. Confirm first mobile slide loads immediately and others lazy-load.

## Risks / edge cases

- Race conditions if users click thumbs rapidly during fade timer.
- Variant updates while lightbox is open may need guard logic to avoid stale active item.
- If a product has only one visible media, fade/reset should not create visual flicker.

## Validation and wrap-up

- Shopify Dev MCP `validate_theme`: pending
- Files expected in summary:
  - `snippets/lusena-pdp-media.liquid`
  - `snippets/lusena-pdp-styles.liquid`
  - `snippets/lusena-pdp-scripts.liquid`
- Optional after approval:
  - Update `docs/THEME_CHANGES.md`
  - Create commit
