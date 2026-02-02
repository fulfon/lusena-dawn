# LUSENA × Dawn — Theme change log (tracked in Git)

## What is this codebase?

This repository started from the official Shopify **Dawn** theme and is being adapted into a **LUSENA**-ready storefront (PL-first, premium feel, proof-first messaging, WCAG-minded UI).

Source of truth for brand direction: `docs/LUSENA_BrandBook_v1.md` (local path: `C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-dawn\docs\LUSENA_BrandBook_v1.md`).

## How to use this file

- For each “bigger” change set, create a Git commit and add an entry here.
- Entries should be **semi-detailed**: what changed, why, and where (key files/settings).
- Always reference the commit (hash + message) so it’s easy to diff/revert.
- Keep only the **latest 8** change entries detailed.
- Keep **ALL commit history** in a rolling summary list (dateTime + hash + subject), sorted descending by commit date/time.

---

**Note:** The newest changelog entry might show `(current)` instead of a hash when we keep everything in a single commit (a commit can’t reliably include its own hash inside its contents). Entries under **Legacy commits** are kept for archival purposes and might reference commits that are no longer reachable from the current Git history (hashes and timestamps might be unavailable).

## Recent commits (detailed, last 8)
### (current) — feat(lusena): PDP swatches + variant media switching

**Goal:** Match the LUSENA draft PDP option UI (color circles + text pills) and allow per-color imagery by switching the gallery on variant change.

**What changed**
- Rendered Color/Kolor/Colour options as circular swatches (using Shopify swatch data when available, with a small name-to-color fallback).
- Rendered other options as pill buttons, with the selected state styled via `:checked` so it updates instantly.
- Added variant media switching: main media updates to the selected variant’s image (and the secondary tile picks the next best media), with `prefers-reduced-motion` handling.

**Key files**
- `sections/lusena-main-product.liquid`

### dc1ed64 — fix(lusena): sync page offset to header height

**Goal:** Remove the tiny desktop gap between the fixed LUSENA header and the first section (most visible on white first sections like `/o-nas`), without affecting mobile or breaking existing layouts.

**What changed**
- Replaced hardcoded non-home `<main>` top padding with a CSS variable-driven offset (`--lusena-header-height`) so content starts exactly under the header.
- Added a small header-height sync in `lusena-header` that measures only the “header bar” (excluding the expanding mobile menu panel) and writes `--lusena-header-height` (and `--header-height` for Dawn compatibility).
- Updates on resize (and via `ResizeObserver` when available) to stay correct if the header height changes.

**Key files**
- `layout/theme.liquid`
- `sections/lusena-header.liquid`

### a3fd8e3 — fix(lusena): make scroll-reveal consistent across pages

**Goal:** Ensure “Reveal sections on scroll” works across all LUSENA custom pages/sections, while keeping the hero/header stack clickable and merchant-adjustable.

**What changed**
- Standardized LUSENA sections on Dawn’s scroll-reveal system (`scroll-trigger` + `animate--slide-in` / `animate--fade-in`), gated by `settings.animations_reveal_on_scroll`.
- Added `data-cascade` to repeated-item containers (cards/rows) so reveals get Dawn’s subtle stagger.
- Hardened `assets/animations.js` initialization so offscreen elements don’t “pre-animate” and section reloads in theme editor behave correctly.
- Fixed hero motion/controls interaction by animating wrapper elements (so merchant-controlled transforms and mobile button sizing remain independent).
- Updated developer docs (AGENTS + UI/UX + migration notes) to reflect the current motion approach (no GSAP).

**Key files**
- `assets/animations.js`
- `sections/lusena-hero.liquid`
- `sections/lusena-main-product.liquid`
- `sections/lusena-main-collection.liquid`
- `sections/lusena-about-*.liquid`
- `sections/lusena-quality-*.liquid`
- `sections/lusena-returns-*.liquid`
- `AGENTS.md`
- `docs/UI_UX_Instructions.md`
- `docs/shopify_dawn_migration_plan.md`

### 6f5f6de — fix(lusena): trust bar launch-safe proof points

**Goal:** Make the trust bar launch-ready without reviews while keeping proof-first reassurance and clean mobile readability.

**What changed**
- Removed ratings/reviews from trust bar defaults (avoid “0 reviews” / placeholder numbers at launch).
- Replaced the first item with a concrete material proof point (“22 momme / 30% gęstszy splot”) and added a dedicated `layers` icon.
- Improved mobile layout/spacing (semantic list markup, consistent title/subtitle stacking, increased grid gap).
- Aligned scroll-reveal behavior with Dawn (`scroll-trigger` on items + `data-cascade` on the container, gated by `settings.animations_reveal_on_scroll`).

**Key files**
- `sections/lusena-trust-bar.liquid`
- `snippets/lusena-icon.liquid`
- `templates/index.json`
- `templates/page.nasza-jakosc.json`

### 0a6644e — feat(lusena): motion layer + remove GSAP

**Goal:** Replace external animation dependencies with a lightweight, accessible motion layer that supports a premium feel without sacrificing performance or stability.

**What changed**
- Removed the GSAP/ScrollTrigger dependency and replaced LUSENA reveals/staggers with a native `IntersectionObserver` motion layer.
- Tuned Dawn scroll-reveal timings (less “floaty”) and reduced scroll zoom intensity.
- Improved cart drawer overlay/slide transitions and added `prefers-reduced-motion` fallbacks.
- Added a subtle hero intro (image settle + copy fade-up) with reduced-motion handling.

**Key files**
- `assets/lusena-animations.js`
- `assets/base.css`
- `layout/theme.liquid`
- `assets/animations.js`
- `assets/component-cart-drawer.css`
- `sections/lusena-hero.liquid`
- `sections/lusena-science.liquid`

### b076f77 — feat(lusena): refine section spacing defaults

**Goal:** Improve the global vertical rhythm (premium feel) and reduce “manual spacing” work in the theme editor, while keeping conversion-critical sections readable and scannable.

**What changed**
- Tuned global section gap (`spacing_sections`) to a consistent, 8px-based rhythm.
- Adjusted default padding (desktop + mobile) across LUSENA sections to reduce overly-large whitespace while keeping a premium “breathing” layout.
- Normalized Dawn template paddings (cart/search/blog/page/contact) to consistent 8px multiples.
- Added a generated section inventory + purpose report for reference.

**Key files**
- `config/settings_data.json`
- `sections/lusena-*.liquid`
- `templates/(cart|search|blog|page|page.contact).json`
- `docs/SECTIONS_AUDIT.md`

### e96c48a — feat(lusena): per-section spacing + split page sections

**Goal:** Make vertical spacing adjustable (mobile/desktop) between LUSENA sections, and split page-sized LUSENA sections into smaller, reorderable sections.

**What changed**
- Added per-section spacing settings (mobile + desktop) across LUSENA sections to control top/bottom padding.
- Split monolithic page sections into multiple Shopify sections for Quality, About, and Returns pages to enable independent spacing and ordering.
- Updated page templates to use the new split sections.

**Key files**
- `sections/lusena-*-*.liquid`
- `sections/lusena-(bestsellers|bundles|comparison|faq|heritage|main-collection|main-product|problem-solution|science|testimonials|trust-bar).liquid`
- `templates/page.nasza-jakosc.json`
- `templates/page.o-nas.json`
- `templates/page.zwroty.json`

### 7efa557 — feat(lusena): auto-hide header on scroll

**Goal:** Let merchants optionally auto-hide the header on scroll down and reveal it on scroll up, with separate toggles for mobile and desktop.

**What changed**
- Added `auto_hide_on_scroll_mobile` and `auto_hide_on_scroll_desktop` toggles in the header section settings.
- Implemented scroll-direction detection that hides the header on downward scroll and shows it on upward scroll (menu open keeps header visible).

**Key files**
- `sections/lusena-header.liquid`
- `sections/header-group.json`

---

## All commits (summary, dateTime-desc)
- 2026-02-02T19:08:42+01:00 — (current) — feat(lusena): PDP swatches + variant media switching
- 2026-02-02T16:37:30+01:00 — dc1ed64 — fix(lusena): sync page offset to header height
- 2026-02-02T16:19:43+01:00 — a3fd8e3 — fix(lusena): make scroll-reveal consistent across pages
- 2026-02-02T16:10:59+01:00 — 6f5f6de — fix(lusena): trust bar launch-safe proof points
- 2026-02-02T13:12:18+01:00 — 0a6644e — feat(lusena): motion layer + remove GSAP
- 2026-02-02T10:34:57+01:00 — b076f77 — feat(lusena): refine section spacing defaults
- 2026-02-01T23:02:37+01:00 — e96c48a — feat(lusena): per-section spacing + split page sections
- 2026-01-31T23:58:51+01:00 — f19d702 — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-01-31T23:58:34+01:00 — 184fe6b — docs: update theme changelog
- 2026-01-31T23:58:01+01:00 — 7efa557 — feat(lusena): auto-hide header on scroll
- 2026-01-31T22:53:52Z — 5a1ac3c — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T22:53:33Z — 90374e6 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T22:53:09Z — 70bedf7 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T22:17:31Z — 3fe4d5e — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T22:17:07Z — ea6f51f — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T23:08:56+01:00 — 7b3b60a — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-01-31T23:04:08+01:00 — 6499dff — docs: update theme changelog
- 2026-01-31T23:03:09+01:00 — 27fcb56 — feat(lusena): independent mobile hero offsets
- 2026-01-31T22:51:00+01:00 — 6339ab2 — docs: update theme changelog
- 2026-01-31T22:50:10+01:00 — 6187b7d — feat(lusena): mobile hero button size controls
- 2026-01-31T21:48:29Z — 56962b8 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:29:54Z — 9a3bd86 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:28:18Z — 1e2447a — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:28:07Z — ccbea04 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:27:32Z — b1feff8 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:27:22Z — e3bb38d — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:26:35Z — cc904c3 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:26:22Z — f8c1a53 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:25:54Z — 9f4023d — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:25:38Z — 0acd0a1 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:07:58Z — d6eaeab — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:48:52+01:00 — 36ae2bd — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-01-31T21:44:42+01:00 — 6b28e86 — docs: update changelog + fix utf-8
- 2026-01-31T21:34:41+01:00 — cbb4d8a — fix(lusena): mobile hero max height + responsive text controls
- 2026-01-31T20:17:40Z — 5e44bda — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T21:00:04+01:00 — 4a950cc — docs: update theme changelog
- 2026-01-31T20:55:28+01:00 — abbe143 — chore: resolve homepage template merge conflict
- 2026-01-31T20:48:14+01:00 — 179d0af — fix(lusena): hero overlay opacity + copy positioning
- 2026-01-31T19:11:19Z — 77ada10 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T20:05:29+01:00 — e26de8d — reduce readability from .9 to .89
- 2026-01-31T19:56:33+01:00 — 3236ecf — docs: refine lusena-theme-changelog commit guidance
- 2026-01-31T19:17:43+01:00 — f15ccab — docs: log quality benefit dot alignment
- 2026-01-31T19:16:47+01:00 — 055293b — fix(lusena): center quality benefit dot on first line
- 2026-01-31T19:07:38+01:00 — dbdbba5 — docs: add quality page bullet alignment entry
- 2026-01-31T19:05:54+01:00 — f208bdd — fix(lusena): align quality page benefit bullets
- 2026-01-31T18:55:13+01:00 — 6e793db — docs: log outside-tap mobile menu close
- 2026-01-31T18:54:29+01:00 — c6e29b9 — fix(lusena): close mobile menu on outside tap
- 2026-01-31T18:51:22+01:00 — 65418df — docs: log mobile menu padding tweak
- 2026-01-31T18:50:55+01:00 — d5e5458 — fix(lusena): align mobile menu vertical padding
- 2026-01-31T18:49:27+01:00 — 2b57e46 — docs: log opaque header change
- 2026-01-31T18:48:32+01:00 — b441ec8 — fix(lusena): make header opaque at top
- 2026-01-31T18:46:48+01:00 — 22e1ac1 — fix(lusena): remove homepage header spacer
- 2026-01-31T18:42:52+01:00 — ea014bc — docs: log header scroll transition fix
- 2026-01-31T18:42:12+01:00 — 1dc0edd — fix(lusena): disable header scroll transition
- 2026-01-31T18:38:15+01:00 — db80086 — docs: update theme changelog
- 2026-01-31T18:35:44+01:00 — e607662 — fix(lusena): mobile header menu expands with background
- 2026-01-31T16:31:47+01:00 — 9eb49d5 — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-01-31T15:30:29Z — 711edc8 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T16:29:42+01:00 — baef5d6 — docs: add changelog entry for hero copy alignment
- 2026-01-31T16:29:25+01:00 — 0997b8a — fix(lusena): align hero copy to top on mobile
- 2026-01-31T15:39:26+01:00 — 9e47acb — docs: add changelog entry for removing skip links
- 2026-01-31T15:39:15+01:00 — f58cf0c — chore(a11y): remove skip links
- 2026-01-31T15:34:52+01:00 — c6f0953 — docs: add changelog entry for skip link focus
- 2026-01-31T15:34:20+01:00 — 701b58d — fix(a11y): show skip link only on keyboard focus
- 2026-01-31T15:13:25+01:00 — 3397cfd — chore: resolve merge conflicts
- 2026-01-31T15:09:55+01:00 — c7626e4 — docs: add changelog entry for hero mobile/desktop images
- 2026-01-31T15:09:34+01:00 — 6922ae6 — feat(lusena): separate hero images for mobile/desktop
- 2026-01-31T15:04:47+01:00 — 7032270 — docs: add changelog entry for header menu cleanup
- 2026-01-31T15:04:30+01:00 — 99d916b — fix(lusena): remove extra header menu links
- 2026-01-31T14:58:34+01:00 — 290b629 — docs: add changelog entry for desktop-only header links
- 2026-01-31T14:58:10+01:00 — 27317ae — fix(lusena): desktop-only header links + bold account icon
- 2026-01-31T13:52:38Z — 626d6bf — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T14:39:57+01:00 — eaa726f — docs: add changelog entry for header fixes
- 2026-01-31T14:39:28+01:00 — fcdcf27 — fix(lusena): header links on mobile + account icon + logo color
- 2026-01-31T13:38:49Z — 6f098e9 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T13:36:21Z — ee686d2 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T13:35:36Z — e0bacf9 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T13:34:01Z — 505a16f — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T14:20:43+01:00 — 2d40998 — Merge branch 'main' of https://github.com/fulfon/lusena-dawn
- 2026-01-31T14:15:39+01:00 — e71c1f9 — docs: add changelog entry for PDP sticky ATC fix
- 2026-01-31T14:13:33+01:00 — 0f38fbe — fix(lusena): keep PDP sticky ATC fixed
- 2026-01-31T14:05:45+01:00 — 14408f2 — fix(lusena): header links defaults + bolder cart icon
- 2026-01-31T14:02:14+01:00 — ea9152c — docs: add changelog entry for header logo + links
- 2026-01-31T14:02:03+01:00 — 7b69635 — feat(lusena): logo upload + primary header links
- 2026-01-31T13:51:28+01:00 — ce5aa0e — chore(lusena): remove redundant utility fallbacks
- 2026-01-31T13:45:09+01:00 — 76b4d93 — docs: add changelog entry for cart drawer overlay
- 2026-01-31T13:44:39+01:00 — 7079328 — fix(lusena): cart drawer overlay blur + upsell styling
- 2026-01-31T12:08:38Z — 9cabf8b — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T13:02:45+01:00 — 854cdd5 — docs: add changelog entry for nasza-jakosc updates
- 2026-01-31T13:02:23+01:00 — 3be1a33 — feat(lusena): nasza-jakosc certificate button + layout tweaks
- 2026-01-31T11:55:13Z — 744d0d4 — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T11:46:04Z — b42c92f — Update from Shopify for theme lusena-dawn/main
- 2026-01-31T10:57:27Z — 581de2d — Update from Shopify for theme lusena-dawn/main
- 2026-01-30T22:38:02+01:00 — 9ad7892 — chore: update theme changelog skill
- 2026-01-30T22:38:02+01:00 — 7209847 — docs: keep theme changelog to last 8 entries
- 2026-01-30T22:34:15+01:00 — f906875 — fix(lusena): problem/solution typography + spacing
- 2026-01-30T22:10:22+01:00 — e1d78e4 — docs: update theme changelog
- 2026-01-30T22:09:58+01:00 — 90e00a8 — fix(lusena): trust bar matches draft layout
- 2026-01-30T20:58:03Z — 1f6a5fb — Update from Shopify for theme lusena-dawn/main
- 2026-01-30T21:44:13+01:00 — e47ec72 — fix(lusena): trust bar layout + remove border
- 2026-01-30T20:41:45+01:00 — 922b24d — Initial commit

## Legacy commits (pre-reset history, summary only)
- unknown — 2f6787f — fix(lusena): match homepage to draft spacing + CTAs
- unknown — d93971a — feat(lusena): migrate draft-shop UI into Dawn
- unknown — fcd1a02 — refactor(css,i18n): brandbook-aligned typography, animations & localization
- unknown — 1b99f37 — feat(lusena): brandbook-aligned UI + cart conversion layer
