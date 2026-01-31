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

### 701b58d — fix(a11y): show skip link only on keyboard focus

**Goal:** Prevent the “Skip to content” link from appearing after mouse focus/clicks while keeping it accessible for keyboard users.

**What changed**
- Added a small override using `:focus-visible` (when supported) so the skip link becomes visible only on keyboard focus.

**Key files**
- `snippets/lusena-a11y-overrides.liquid`
- `layout/theme.liquid`

### 99d916b — fix(lusena): remove extra header menu links

**Goal:** Ensure only the primary header links are shown (SKLEP / O NAS / DLACZEGO JEDWAB?) and remove unwanted extra menu items (e.g. Home/Contact).

**What changed**
- Added `show_additional_menu` setting (default off) and gated rendering of extra menu items behind it.
- Keeps the header clean while still allowing optional extra links if explicitly enabled.

**Key files**
- `sections/lusena-header.liquid`
- `sections/header-group.json`

### 27317ae — fix(lusena): desktop-only header links + bold account icon

**Goal:** Show header primary links only on desktop (as in the draft) and make the account icon styling consistent with the cart icon.

**What changed**
- Replaced the utility-based breakpoint visibility with section-scoped CSS so links reliably show on desktop even if utility classes are missing.
- Removed the mobile header links row (links remain available in the hamburger menu).
- Made the account icon desktop-only and increased its stroke to match the cart icon weight.

**Key files**
- `sections/lusena-header.liquid`

### fcdcf27 — fix(lusena): header links on mobile + account icon + logo color

**Goal:** Ensure header links are visible in the storefront preview, show the account icon as configured, and allow controlling the logo color from Theme Editor.

**What changed**
- Added a compact mobile primary-links row (SKLEP / O NAS / DLACZEGO JEDWAB?) so links are visible even on small viewports without opening the menu.
- Made the account icon visible on mobile (it was previously hidden via `hidden sm:flex`).
- Added header settings for `logo_color` and optional `logo_svg_inline` so SVG logos can inherit the chosen color via `currentColor`.

**Key files**
- `sections/lusena-header.liquid`
- `sections/header-group.json`

---

## Older commits (summary only)

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

