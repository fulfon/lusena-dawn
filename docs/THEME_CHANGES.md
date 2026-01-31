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

### 0f38fbe — fix(lusena): keep PDP sticky ATC fixed

**Goal:** Ensure the mobile sticky add-to-cart bar stays fixed to the viewport bottom (like the draft shop), instead of being constrained inside the PDP section.

**What changed**
- Prevented the global GSAP section reveal from applying transforms to the PDP section.
- This avoids creating a transformed containing block, which breaks `position: fixed` descendants like the sticky ATC bar.

**Key files**
- `assets/lusena-animations.js`

### 7b69635 — feat(lusena): logo upload + primary header links

**Goal:** Replace the text logo with an uploadable logo and harden the primary header navigation to match the draft (SKLEP / O NAS / DLACZEGO JEDWAB?).

**What changed**
- Added an uploadable header logo (image picker) with adjustable width and a text fallback.
- Added primary header links on desktop and in the mobile menu (SKLEP / O NAS / DLACZEGO JEDWAB?).
- Removed visible “Menu”/“Cart” labels by switching to `aria-label` attributes (icons only).

**Key files**
- `sections/lusena-header.liquid`

### 7079328 — fix(lusena): cart drawer overlay blur + upsell styling

**Goal:** Match the draft shop cart drawer overlay behavior (blur + click-outside-close) and improve the “Pairs well with” card styling.

**What changed**
- Restored the Dawn drawer overlay approach and added a blurred backdrop on the active cart drawer.
- Switched the overlay element back to Dawn’s `.cart-drawer__overlay` so it reliably covers the viewport and is clickable to close.
- Added missing utility-class fallbacks used by the cart upsell card so layout/typography matches the draft.

**Key files**
- `snippets/cart-drawer.liquid`
- `snippets/lusena-missing-utilities.liquid`

### 3be1a33 — feat(lusena): nasza-jakosc certificate button + layout tweaks

**Goal:** Match the `Nasza jakość` draft page and let merchants manage the OEKO‑TEX certificate PDF from Shopify Admin.

**What changed**
- Added missing utility-class fallbacks used by `lusena-page-quality` so bullet lists render and indent correctly (matching the draft output).
- Updated the certificate CTA to prefer a store metafield `lusena.oeko_tex_certificate` (type: `file_reference`) with a section setting URL fallback.
- Normalized letter-spacing for the section and ensured the Suzhou heading stays on one line on `md+`.

**Key files**
- `sections/lusena-page-quality.liquid`
- `snippets/lusena-missing-utilities.liquid`

### f906875 — fix(lusena): problem/solution typography + spacing

**Goal:** Match the draft shop’s Problem/Solution section typography and inter-column spacing on desktop and mobile.

**What changed**
- Increased the “The Problem” / “The Solution” kicker size and the main heading size to match the draft.
- Increased the column gap on desktop to match the draft.
- Added higher-specificity section-scoped CSS to avoid utility-order issues.
- Added missing `.md:gap-24` utility as a fallback for other sections that rely on it.

**Key files**
- `sections/lusena-problem-solution.liquid`
- `snippets/lusena-missing-utilities.liquid`

### 90e00a8 — fix(lusena): trust bar matches draft layout (icons + height)

**Goal:** Match the `lusena-shop/` draft trust strip 1:1 (icon-to-text alignment, responsive stacking, and bar height).

**What changed**
- Updated trust bar item layout to stack on mobile and align icon-left/text-right from `sm` breakpoint (matching the draft’s `flex-col sm:flex-row` behavior).

**Key files**
- `sections/lusena-trust-bar.liquid`

### e47ec72 — fix(lusena): trust bar layout + remove border

**Goal:** Remove the visible divider line between hero and trust strip and tighten the trust bar spacing to match the draft.

**What changed**
- Adjusted `lusena-trust-bar` layout/styling and removed the top border to eliminate the thin line between hero and trust strip.

**Key files**
- `sections/lusena-trust-bar.liquid`

### 922b24d — Initial commit

**Goal:** Publish the theme to GitHub as the new baseline history after resolving `index-pack failed` push issues.

**What changed**
- Initialized the repository and pushed the full theme as a clean baseline.

**Key files**
- (baseline snapshot of the whole theme)

---

## Older commits (summary only)

- (current) `1f6a5fb` — Update from Shopify for theme lusena-dawn/main
- (pre-reset / legacy) `2f6787f` — fix(lusena): match homepage to draft spacing + CTAs
- (pre-reset / legacy) `d93971a` — feat(lusena): migrate draft-shop UI into Dawn
- (pre-reset / legacy) `fcd1a02` — refactor(css,i18n): brandbook-aligned typography, animations & localization
- (pre-reset / legacy) `1b99f37` — feat(lusena): brandbook-aligned UI + cart conversion layer

