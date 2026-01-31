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


### 6187b7d — feat(lusena): mobile hero button size controls

**Goal:** Give merchants finer control over the hero button sizing on mobile.

**What changed**
- Added mobile-only controls for hero button height and button text size.
- Applied sizing via CSS variables, keeping desktop button sizing unchanged.

**Key files**
- `sections/lusena-hero.liquid`
- `templates/index.json`

### cbb4d8a — fix(lusena): mobile hero max height + responsive text controls

**Goal:** Let merchants precisely position hero copy separately on mobile vs desktop, and control the mobile hero image height (cropped from the bottom).

**What changed**
- Added mobile/desktop-specific hero text vertical position + fine-tune Y offset controls.
- Added `mobile_max_height_px` to cap hero height on mobile and anchor the hero image crop from the bottom.

**Key files**
- `sections/lusena-hero.liquid`
- `templates/index.json`

### abbe143 — chore: resolve homepage template merge conflict

**Goal:** Restore a valid `templates/index.json` after a merge introduced conflict markers.

**What changed**
- Resolved merge conflict markers in the homepage template and kept the latest hero images plus LUSENA hero settings.

**Key files**
- `templates/index.json`

### 179d0af — fix(lusena): hero overlay opacity + copy positioning

**Goal:** Make the hero overlay reliably visible (not hidden by Dawn base CSS) and allow merchants to adjust overlay opacity (0-90%) and hero copy vertical position in the theme editor.

**What changed**
- Prevented the hero overlay from being hidden by `div:empty { display: none; }` by ensuring the overlay element isn't empty.
- Added `overlay_opacity` setting (0-90%, default 50) and applied it via `rgb(0 0 0 / X%)`.
- Added `content_position` (radio) and `content_offset_y` (range) to fine-tune hero copy placement.

**Key files**
- `sections/lusena-hero.liquid`
- `templates/index.json`

### 055293b — fix(lusena): center quality benefit dot on first line

**Goal:** Fix the “Dlaczego 22 momme?” benefit marker alignment so the dot lines up with the first line of text (no “text under the marker” look).

**What changed**
- Made the gold dot use a line-height-aware `calc(...)` top offset instead of a fixed spacing utility.

**Key files**
- `sections/lusena-page-quality.liquid`

### f208bdd — fix(lusena): align quality page benefit bullets

**Goal:** Make the “Dlaczego 22 momme?” benefit markers match PDP styling and keep the marker aligned with its text (no stacked marker line breaks).

**What changed**
- Replaced the plain list marker with the same gold dot pattern used on PDP benefit lists.
- Forced a single-row flex layout so the marker never wraps onto its own line.

**Key files**
- `sections/lusena-page-quality.liquid`

### c6e29b9 — fix(lusena): close mobile menu on outside tap

**Goal:** Close the expanded mobile menu when the user taps/clicks anywhere outside the menu.

**What changed**
- Added a document-level outside-tap handler that closes the mobile menu when clicking outside the toggle and menu panel.

**Key files**
- `sections/lusena-header.liquid`

### d5e5458 — fix(lusena): align mobile menu vertical padding

**Goal:** Match the top and bottom padding of the expanded mobile menu so spacing feels balanced.

**What changed**
- Made the mobile menu content use equal vertical padding (`py-4`) so the gap above “SKLEP” matches the gap below “DLACZEGO JEDWAB?”.

**Key files**
- `sections/lusena-header.liquid`

---

## Older commits (summary only)

- 22e1ac1 — fix(lusena): remove homepage header spacer

- b441ec8 — fix(lusena): make header opaque at top

- 1dc0edd — fix(lusena): disable header scroll transition
- e607662 — fix(lusena): mobile header menu expands with background

- 0997b8a — fix(lusena): align hero copy to top on mobile
- f58cf0c — chore(a11y): remove skip links
- 6922ae6 — feat(lusena): separate hero images for mobile/desktop
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

