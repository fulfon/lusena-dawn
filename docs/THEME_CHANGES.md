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

