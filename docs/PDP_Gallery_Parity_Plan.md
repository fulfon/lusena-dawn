# PDP Gallery Parity Plan (Draft shop → Shopify theme)

Created: 2026-02-08  
Status: Planned (implementation next)  
Owner: Codex (with Karol approvals on UX details)

## Goal

Make the **PDP (product page) gallery in the Shopify theme** look and behave **as close to 1:1 as possible** to the draft shop implementation in:

- `lusena-shop/src/components/product/MediaGallery.tsx`

This includes layout, sizing, active states, hover effects, mobile swipe/scroll behavior, and indicators.

## Source of Truth (what we’re copying)

Draft shop gallery behavior (React):

- **Desktop (>= 768px in draft):**
  - Left: vertical thumbnail strip (`~72px` wide), thumbnails are square.
  - Right: main viewer (square), image hover scale (`scale-105`) with smooth transition.
  - Active thumbnail gets a **2px accent border**.
  - “Bestseller” badge appears only for specific products and only when **first item** is active.
- **Mobile (< 768px in draft):**
  - Horizontal **scroll-snap** carousel (no arrows).
  - Cards width `85vw` (max `400px`), height `min(60vh, 85vw)`, aspect `4/5`.
  - Hidden scrollbar, `gap: 8px`.
  - Dots under carousel reflect scroll position (snap index).
- **Extra tile:** “Proof / certificate” tile with CTA text “Sprawdź certyfikat →” (opens certificate).
- Video tile exists in draft, but we will **not implement video tiles yet** (see decisions).

## Target in Shopify theme (where we implement)

Our store uses the custom PDP section:

- `templates/product.json` → section type `lusena-main-product`
- `sections/lusena-main-product.liquid` renders:
  - `snippets/lusena-pdp-media.liquid` (gallery markup)
  - `snippets/lusena-pdp-styles.liquid` (gallery CSS + PDP CSS)
  - `snippets/lusena-pdp-scripts.liquid` (variant + gallery JS)

## Decisions (confirmed)

1) **Bestseller badge**
- Show only when product is flagged as bestseller.
- Badge displays only when the **first gallery item** is active (desktop) / visible (mobile index = 0).
- We will implement a **recommended metafield**, with a **tag fallback**.

2) **Proof / certificate tile**
- Include it (match draft UX).
- Clicking the “Sprawdź certyfikat →” link opens the same certificate file/link as on `/pages/nasza-jakosc`.
- Use the existing certificate resolution logic used on the quality page (shop metafield first, fallback to a configured link).

3) **Video behavior**
- No “video placeholder” tiles for now.
- For any non-image product media: render its `preview_image` as an image (visual-only) OR optionally filter to images only (implementation detail to finalize during build).

4) **Main image interaction**
- No modal/lightbox/zoom. (Match draft.)

5) **Breakpoint**
- Keep **Dawn’s 750px breakpoint** for switching gallery layouts (even if the overall PDP grid uses Tailwind’s `md:` utilities at 768px).

## Data sources & content model

### 1) Gallery items (images)
Use `product.media`, with our existing color-tagging system preserved:

- We already support media alt “tags” like:
  - `[color=Beżowy]`
  - `[shared]`
  - and a clean alt prefix split by `|`

This logic currently lives in `snippets/lusena-pdp-scripts.liquid` and must continue to work after DOM changes.

### 2) Bestseller flag (recommended + fallback)
**Recommended (primary):** product metafield
- Namespace/key: `lusena.badge_bestseller`
- Type: boolean (true/false)

**Fallback:** product tag
- Tag: `lusena:bestseller` (or continue to support legacy `bestseller` if already used)

Implementation detail: theme will treat product as bestseller if:
- `product.metafields.lusena.badge_bestseller.value == true` OR
- `product.tags contains 'lusena:bestseller'` (and optionally `product.tags contains 'bestseller'` for backwards compatibility)

### 3) Certificate URL (same behavior as `nasza-jakosc`)
Re-use the logic already present in:
- `sections/lusena-quality-certificates.liquid`
- `sections/lusena-page-quality.liquid`

Resolution order:
1) `shop.metafields.lusena.oeko_tex_certificate` (type: `file_reference`) → use `.value.url`
2) Fallback: section setting URL (if present)

In the gallery proof tile:
- If no certificate URL is available, we omit the proof tile entirely (to avoid dead CTA).

## Target UX specification (Shopify)

### Desktop gallery (>= 750px)
Markup structure (conceptual):
- Wrapper `data-lusena-gallery`
  - Left thumb column:
    - `button` list, one per “visible” media item (+ optional proof tile)
    - Active thumb: accent border `2px`
  - Right main viewer:
    - Single `<img>` that updates when active media changes
    - Hover scale on image (`scale-105`) with `transition-transform duration-500`
    - Bestseller badge (conditionally visible; only when activeIndex == 0)

Behavior:
- Clicking a thumbnail changes the main viewer.
- Active thumb updates (`aria-current="true"`).

### Mobile gallery (< 750px)
Markup structure (conceptual):
- Horizontal scroll container with:
  - snap-x, snap-mandatory
  - each slide is a card containing the image (or proof tile)
  - slide sizes match draft: `w-[85vw] max-w-[400px]`, `height: min(60vh, 85vw)`, `aspect: 4/5`
- Dot indicator row:
  - count equals current “visible” items (including proof tile if present)
  - active dot reflects snapped index (computed from scrollLeft / (cardWidth + gap))

Behavior:
- Swipe/scroll updates dot indicator.
- If variant/color filtering changes which media are visible, dots update accordingly.
- Bestseller badge appears on first slide only when bestseller + index 0.

### Proof / certificate tile (desktop + mobile)
Visual:
- Same “certificate” look as draft: centered shield icon + title + short body + CTA “Sprawdź certyfikat →”.

Interaction:
- CTA opens `certificate_url` in new tab (`target="_blank" rel="noopener"`).

## Implementation approach (high-level)

We’ll modify the existing LUSENA PDP gallery (not Dawn’s default gallery) because:
- `templates/product.json` uses `lusena-main-product`
- `snippets/lusena-pdp-scripts.liquid` already contains sophisticated variant + media filtering logic (color tagging), which we must keep.

### Files to change (expected)

- `snippets/lusena-pdp-media.liquid`
  - Replace current “stage + horizontal thumbs” markup with:
    - Desktop: vertical thumbs + stage
    - Mobile: scroll-snap carousel + dots
  - Add proof tile markup (conditionally, only if certificate_url exists)
  - Update bestseller badge condition to metafield/tag-based

- `snippets/lusena-pdp-styles.liquid`
  - Add/adjust CSS to match draft sizing and behaviors:
    - gallery layout switch at **750px**
    - hide scrollbar on mobile carousel
    - thumb active border 2px accent
    - dot indicator styling
  - Ensure reduced-motion respects hover/transition where appropriate

- `snippets/lusena-pdp-scripts.liquid`
  - Extend existing gallery JS to support:
    - mobile carousel index tracking + dot updates
    - keeping desktop + mobile views in sync with the same “active media”
    - updating bestseller badge visibility based on active index
    - proof tile presence (and that it is not removed by color filtering)
  - Preserve existing media filtering:
    - `[color=...]` / `[shared]` parsing
    - thumb ordering/visibility updates on variant change

Optional refactor (only if it reduces duplication cleanly):
- Create a small snippet/helper for certificate URL resolution so the logic isn’t copy-pasted (not required, but nice-to-have).

## Milestones & deliverables

### Milestone 0 — Plan sign-off (this document)
Deliverable:
- `docs/PDP_Gallery_Parity_Plan.md` approved.

### Milestone 1 — Gallery markup parity
Deliverables:
- Updated `snippets/lusena-pdp-media.liquid` with:
  - desktop + mobile structures present
  - proof tile rendering (conditional)
  - bestseller badge logic (metafield/tag)

Acceptance checks:
- No modal opens on click.
- Gallery renders without JS errors.

### Milestone 2 — CSS parity
Deliverables:
- Updated `snippets/lusena-pdp-styles.liquid` implementing:
  - desktop vertical strip sizing (72px), gaps (8/12px), borders, hover scale
  - mobile scroll-snap sizing + scrollbar hiding + dots
  - breakpoint at 750px for gallery switching

Acceptance checks:
- Matches draft spacing and active states visually.

### Milestone 3 — JS parity (behavior)
Deliverables:
- Updated `snippets/lusena-pdp-scripts.liquid` supporting:
  - desktop thumbnail selection
  - mobile dot indicators that track scroll position
  - variant/color media filtering still works
  - stage image updates correctly

Acceptance checks:
- Mobile swipe updates dots accurately.
- Switching variants updates visible slides and does not break scrolling.

### Milestone 4 — Certificate integration parity
Deliverables:
- Proof tile uses the same certificate URL source as `nasza-jakosc`.

Acceptance checks:
- CTA opens the correct PDF/link in a new tab.

### Milestone 5 — Verification + hardening
Deliverables:
- Theme validation runs cleanly (Shopify Dev MCP `validate_theme`).
- Visual verification using Playwright as needed.
- Update `docs/THEME_CHANGES.md` entry after implementation (per repo workflow).

## Verification checklist (manual)

On a product with multiple media:
- Desktop (>= 750px):
  - thumbnails appear vertically, 72px, correct gaps
  - clicking thumbnail swaps main image
  - active thumb border matches accent
  - main image hover scale works
  - bestseller badge only shows if bestseller flag and only on first item
- Mobile (< 750px):
  - swipe scroll snaps per card
  - dots match slide count and current slide
  - first slide shows badge only for bestseller products
- Variant/color behavior:
  - selecting a color changes which media appear (based on `[color=...]` and `[shared]`)
  - active item stays valid when the visible set changes
- Certificate:
  - proof tile exists only if certificate URL exists
  - link opens correct certificate

## Verification checklist (Playwright)

If we need pixel-level confidence, we’ll:
1) Ensure the Shopify theme dev server is running at `http://127.0.0.1:9292/` (`shopify theme dev` if not).
2) Use Playwright MCP to:
   - open a PDP
   - capture viewport screenshots at representative widths:
     - mobile (e.g. 390px)
     - tablet (e.g. 820px)
     - desktop (e.g. 1280px)
   - verify interaction:
     - click thumbnails (desktop)
     - scroll carousel and confirm dots update (mobile)

## Risks / edge cases to handle

- **750–767px range:** gallery switches to desktop layout at 750px while the overall Tailwind `md:` grid kicks in at 768px; this is acceptable but we’ll verify it doesn’t look awkward.
- **Products with only 1 media:** ensure dots/thumbs don’t render unnecessarily and layout stays stable.
- **Non-image media:** we must decide whether to:
  - filter out entirely, or
  - include as preview image only (no playback). We’ll implement the simplest behavior first and adjust if needed.
- **Certificate missing:** omit proof tile when no URL is resolved.

## Implementation notes (do / don’t)

- Do not re-introduce Dawn’s modal/lightbox for images.
- Preserve existing variant/media filtering logic in `lusena-pdp-scripts.liquid`.
- Keep all new interactivity accessible:
  - thumbnails are buttons
  - active state reflected via `aria-current`
  - avoid trapping scroll; keep passive listeners for scroll tracking

