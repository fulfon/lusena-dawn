# LUSENA × Dawn — Theme change log (tracked in Git)

## What is this codebase?

This repository started from the official Shopify **Dawn** theme and is being adapted into a **LUSENA**-ready storefront (PL-first, premium feel, proof-first messaging, WCAG-minded UI).

Source of truth for brand direction: `docs/LUSENA_BrandBook_v1.md` (local path: `C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-dawn\docs\LUSENA_BrandBook_v1.md`).

## How to use this file

- For each “bigger” change set, create a Git commit and add an entry here.
- Entries should be **semi-detailed**: what changed, why, and where (key files/settings).
- Always reference the commit (hash + message) so it’s easy to diff/revert.
- Keep only the **latest 8** change entries detailed. Older entries should be compressed into a short summary list.

---

**Note (2026-01-30):** Git history in this repo was reset (new `Initial commit`). Entries under **Legacy commits** reference the pre-reset history and won’t match the current commit hashes.

## Recent commits (detailed, last 8)

### d5e5458 — fix(lusena): align mobile menu vertical padding

**Goal:** Match the top and bottom padding of the expanded mobile menu so spacing feels balanced.

**What changed**
- Made the mobile menu content use equal vertical padding (`py-4`) so the gap above “SKLEP” matches the gap below “DLACZEGO JEDWAB?”.

**Key files**
- `sections/lusena-header.liquid`

### b441ec8 — fix(lusena): make header opaque at top

**Goal:** Avoid the header being transparent at the very top of the page.

**What changed**
- Made the LUSENA header always use the “scrolled” background styles (opaque + blur) instead of switching from transparent on scroll.

**Key files**
- `sections/lusena-header.liquid`

### 22e1ac1 — fix(lusena): remove homepage header spacer

**Goal:** Remove the “blank header bar” effect at the top of the homepage so the hero starts at the very top under the fixed header.

**What changed**
- Applied the main content top padding (`pt-[72px]` / `lg:pt-[88px]`) only on non-homepage templates.

**Key files**
- `layout/theme.liquid`

### 1dc0edd — fix(lusena): disable header scroll transition

**Goal:** Keep the header visually static when starting to scroll from the top (no fade/resize animation).

**What changed**
- Removed the header transition classes so the transparent → scrolled header state change doesn’t animate.

**Key files**
- `sections/lusena-header.liquid`

### e607662 — fix(lusena): mobile header menu expands with background

**Goal:** Make the mobile header menu feel like a single, unified header element (no background cut-off), with a smooth expand/collapse animation.

**What changed**
- Rebuilt the mobile menu panel to live inside the header flow so the header height expands/collapses instead of using an absolutely-positioned dropdown.
- Ensured the header background switches to the same “scrolled” background while the menu is open so it reads as one element.
- Prevented “O NAS” from wrapping on narrow viewports.
- Improved a11y by toggling `aria-hidden` + `inert` on the mobile menu wrapper while closed.
- Fixed hero overlay opacity behavior so the slider visibly changes the overlay (uses an RGBA overlay layer above the image).

**Key files**
- `sections/lusena-header.liquid`
- `sections/lusena-hero.liquid`

### 0997b8a — fix(lusena): align hero copy to top on mobile

**Goal:** Align the homepage hero copy to the top on mobile so it matches the draft banner composition.

**What changed**
- Adjusted the hero content container to align to the top on mobile (with a small top padding), while keeping centered alignment on desktop.

**Key files**
- `sections/lusena-hero.liquid`

### f58cf0c — chore(a11y): remove skip links

**Goal:** Remove the “Skip to content” / “Skip to product info” skip links entirely.

**What changed**
- Removed the skip link anchors from the main theme layout, password layout, and product media gallery.
- Removed the temporary LUSENA skip-link focus override snippet (no longer needed).

**Key files**
- `layout/theme.liquid`
- `layout/password.liquid`
- `snippets/product-media-gallery.liquid`

### 6922ae6 — feat(lusena): separate hero images for mobile/desktop

**Goal:** Allow merchants to upload and control different hero images for mobile vs desktop on the homepage.

**What changed**
- Added `Hero image (desktop)` and `Hero image (mobile)` settings to the LUSENA hero section.
- Updated hero rendering to use a `<picture>` element (desktop image on `min-width: 768px`, mobile image otherwise), with fallbacks to the legacy `Hero image` setting.

**Key files**
- `sections/lusena-hero.liquid`

---

## Older commits (summary only)

- 701b58d — fix(a11y): show skip link only on keyboard focus
- 99d916b — fix(lusena): remove extra header menu links
- 27317ae — fix(lusena): desktop-only header links + bold account icon
- fcdcf27 — fix(lusena): header links on mobile + account icon + logo color
- 0f38fbe — fix(lusena): keep PDP sticky ATC fixed
- 7b69635 — feat(lusena): logo upload + primary header links
- 7079328 — fix(lusena): cart drawer overlay blur + upsell styling
- 3be1a33 — feat(lusena): nasza-jakosc certificate button + layout tweaks
- f906875 — fix(lusena): problem/solution typography + spacing
- 90e00a8 — fix(lusena): trust bar matches draft layout (icons + height)
- e47ec72 — fix(lusena): trust bar layout + remove border
- 922b24d — Initial commit

- (current) `1f6a5fb` — Update from Shopify for theme lusena-dawn/main
- (pre-reset / legacy) `2f6787f` — fix(lusena): match homepage to draft spacing + CTAs
- (pre-reset / legacy) `d93971a` — feat(lusena): migrate draft-shop UI into Dawn
- (pre-reset / legacy) `fcd1a02` — refactor(css,i18n): brandbook-aligned typography, animations & localization
- (pre-reset / legacy) `1b99f37` — feat(lusena): brandbook-aligned UI + cart conversion layer

