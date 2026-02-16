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
### (current) — fix(lusena): stabilize PDP gallery crossfade and mobile variant sync

**Goal:** Finalize PDP gallery variant-switch parity for crossfade + lazy loading and fix the mobile mismatch where indicator dots/index moved but the visible slide stayed on the previous shared image.

**What changed**
- Added explicit desktop stage crossfade sequencing (`fade out -> swap -> fade in`) for thumbnail changes and variant-driven gallery switches.
- Added mobile variant-switch sequencing so track opacity transition happens before content swap, then fades back in.
- Restored index-selection behavior expected from the previous flow while clarifying shared-media handling for color switches.
- Fixed mobile viewport synchronization by scrolling the mobile track to the resolved target index after variant-change selection, so visible slide and dots stay aligned.
- Implemented lazy-loading parity updates: desktop stage eager/high priority, desktop thumbs lazy, mobile first visible media eager/high priority, remaining visible media lazy (including runtime re-sync after filtered gallery updates).
- Added implementation contract for this fragment migration.

**Key files**
- `snippets/lusena-pdp-media.liquid`
- `snippets/lusena-pdp-scripts.liquid`
- `snippets/lusena-pdp-styles.liquid`
- `docs/PDP_Gallery_Crossfade_Lazy_Parity_Plan.md`

### 4b9caa2 — feat(lusena): finalize returns page and PDP parity updates

**Goal:** Finish draft-shop parity for the `/zwroty` page and key PDP fragments (payment strip, sticky ATC, and gallery zoom/lightbox) in the live LUSENA Dawn flow.

**What changed**
- Reworked `/zwroty` page sections (`hero`, `steps`, `faq`) to match draft parity in structure, typography, spacing defaults, iconography, and interactions.
- Added two new `/zwroty` sections: editorial comparison ("why 60 days") and final CTA, then wired them into `templates/page.zwroty.json` order/content.
- Replaced PDP text payment chips with SVG payment logos (Visa, BLIK, PayPo, Przelewy24) and responsive desktop/mobile layouts while keeping secure-payment copy configurable.
- Added PDP gallery zoom/lightbox support: desktop click-zoom with pointer pan, keyboard/backdrop controls, and mobile pinch/double-tap/pan/swipe behavior with safe-area-compatible viewport handling.
- Rebuilt sticky ATC into dedicated mobile + desktop variants and updated PDP scripts to synchronize all sticky instances for variant price/per-night/label/image/availability updates.
- Added parity implementation plans for `/zwroty` and PDP fragments in `docs/`, and updated the draftshop parity skill with the primary local draft source path.

**Key files**
- `templates/page.zwroty.json`
- `sections/lusena-returns-hero.liquid`
- `sections/lusena-returns-steps.liquid`
- `sections/lusena-returns-editorial.liquid`
- `sections/lusena-returns-faq.liquid`
- `sections/lusena-returns-final-cta.liquid`
- `snippets/lusena-pdp-payment.liquid`
- `snippets/lusena-pdp-media.liquid`
- `snippets/lusena-pdp-scripts.liquid`
- `snippets/lusena-pdp-sticky-atc.liquid`
- `snippets/lusena-pdp-styles.liquid`
- `assets/lusena-payment-visa.svg`
- `assets/lusena-payment-blik.svg`
- `assets/lusena-payment-paypo.svg`
- `assets/lusena-payment-przelewy24.svg`
- `layout/theme.liquid`
- `layout/password.liquid`
- `docs/Page_Zwroty_Parity_Plan.md`
- `docs/Page_Zwroty_Final_CTA_Parity_Plan.md`
- `docs/PDP_Sticky_ATC_Desktop_Mobile_Parity_Plan.md`
- `docs/PDP_Payment_Icons_Strip_Parity_Plan.md`
- `docs/PDP_Gallery_Zoom_Lightbox_Parity_Plan.md`
- `.codex/skills/lusena-draftshop-fragment-parity/SKILL.md`

### 7eb6712 — fix(ci): resolve LHCI product handle dynamically

**Goal:** Eliminate recurring Lighthouse 404 failures on product URLs by resolving a valid published product handle at runtime in CI.

**What changed**
- Added a `Resolve published product handle` step in the CI workflow that calls Shopify Admin API and extracts the first `active + published` product handle.
- Added explicit fail-fast behavior with clear error output when no published product exists or API auth fails, instead of letting Lighthouse fail later with opaque audit noise.
- Updated `shopify/lighthouse-ci-action@v1` input to use the resolved handle output from the resolver step.
- Kept the existing LHCI thresholds and collection audit configuration unchanged.

**Key files**
- `.github/workflows/ci.yml`
- `docs/THEME_CHANGES.md`

### 1ad8a9e — fix(ci): stabilize Lighthouse target and skip remote theme pull

**Goal:** Make CI Lighthouse runs deterministic by avoiding fallback `gift-card` 404s and preventing stale remote theme template data from being pulled into the check.

**What changed**
- Added explicit `product_handle` to the Lighthouse GitHub Action, with repo variable support and fallback to `silk-pillowcase`.
- Removed `pull_theme` from the Lighthouse action configuration to avoid importing remote/stale template data during CI.
- Kept the existing accessibility threshold and collection target unchanged.

**Key files**
- `.github/workflows/ci.yml`
- `docs/THEME_CHANGES.md`

### 1ccc2b8 — feat(lusena): complete PDP + cart parity rollout

**Goal:** Deliver draft-shop parity for PDP and cart UX in the active LUSENA Dawn flow, including buy-box composition, value-proof sections, breadcrumbs, and cart drawer interactions.

**What changed**
- Reworked the main PDP composition to match draft hierarchy: breadcrumbs, proof chips, buy-now action, guarantee/returns links, payment row, and buy-box detail panels; removed the previous standalone reviews fragment.
- Added and wired three new PDP follow-up sections in `templates/product.json`: feature highlights, quality evidence stack, and details/FAQ.
- Expanded PDP behavior scripts for returns deep-link opening, accordion sizing/state handling, spec-definition toggles, buy-now checkout redirect, sticky ATC synchronization, and tagged gallery/proof-tile flow.
- Rebuilt the cart drawer to parity: refined empty/non-empty states, single-card upsell with metafield-driven selection, session-backed "Dodano do koszyka" feedback, free-shipping progress bar, and explicit continue-shopping control.
- Standardized button radius parity (`6px`) and added targeted utility/class backfills plus icon extensions required by the new fragments.
- Added reusable implementation artifacts for future parity work (plan template + PDP plan docs, local `theme-dev` launcher script, and the draftshop parity skill files).

**Key files**
- `sections/lusena-main-product.liquid`
- `templates/product.json`
- `sections/lusena-pdp-feature-highlights.liquid`
- `sections/lusena-pdp-quality-evidence.liquid`
- `sections/lusena-pdp-details.liquid`
- `snippets/lusena-pdp-scripts.liquid`
- `snippets/lusena-pdp-styles.liquid`
- `snippets/cart-drawer.liquid`
- `snippets/lusena-breadcrumbs.liquid`
- `snippets/lusena-pdp-buybox-panels.liquid`
- `snippets/lusena-missing-utilities.liquid`
- `config/settings_data.json`
- `docs/PDP_BuyBox_Parity_Plan.md`
- `.codex/skills/lusena-draftshop-fragment-parity/SKILL.md`

### 3a51798 — refactor(lusena): split PDP into snippets

**Goal:** Make the product page (PDP) section easier to maintain by extracting `lusena-main-product` into focused snippet components, without changing the storefront output/behavior.

**What changed**
- Extracted the major PDP parts (media, summary, variant picker, buybox, trust/guarantee, accordions, cross-sell, reviews, sticky ATC) into `snippets/lusena-pdp-*.liquid`.
- Moved the section-scoped `{% stylesheet %}` and `{% javascript %}` blocks into dedicated snippets so behavior/styling can evolve independently.
- Kept the existing section schema/settings IDs and all JS hooks (`data-lusena-*`, `#main-cta`) stable.

**Key files**
- `sections/lusena-main-product.liquid`
- `snippets/lusena-pdp-accordions.liquid`
- `snippets/lusena-pdp-atc.liquid`
- `snippets/lusena-pdp-cross-sell.liquid`
- `snippets/lusena-pdp-guarantee.liquid`
- `snippets/lusena-pdp-media.liquid`
- `snippets/lusena-pdp-reviews.liquid`
- `snippets/lusena-pdp-scripts.liquid`
- `snippets/lusena-pdp-sticky-atc.liquid`
- `snippets/lusena-pdp-styles.liquid`
- `snippets/lusena-pdp-summary.liquid`
- `snippets/lusena-pdp-variant-picker.liquid`

### 09ba94a — fix(lusena): preserve PDP image index on color switch

**Goal:** Make color switching behave like a true “same angle, different color” comparison: keep the selected image index within color images, and jump to the first color image when the customer was viewing shared media.

**What changed**
- Tracked whether the currently selected image is color-specific vs shared, so switching colors always picks the equivalent image index for the newly selected color.
- When a shared image is selected, switching color always jumps to the first color image (so the change is immediately visible).
- Kept initialization aligned with the variant featured media to avoid unexpected first-load image jumps.

**Key files**
- `sections/lusena-main-product.liquid`

### cdcee94 — fix(lusena): correct PDP color gallery filtering

**Goal:** Fix edge cases where switching colors could show stale images from other variants or place shared images before color-specific ones.

**What changed**
- Hardened alt-tag parsing so `[color=…]` works reliably even with small formatting differences (e.g. extra spaces around `=`).
- Updated fallback when a color has no assigned images: show only shared/untagged media (instead of leaking other colors).

**Key files**
- `sections/lusena-main-product.liquid`

---

## All commits (summary, dateTime-desc)
- 2026-02-16T20:06:42+01:00 — (current) — fix(lusena): stabilize PDP gallery crossfade and mobile variant sync
- 2026-02-16T16:37:56+01:00 — 4b9caa2 — feat(lusena): finalize returns page and PDP parity updates
- 2026-02-13T19:00:05+01:00 — 7eb6712 — fix(ci): resolve LHCI product handle dynamically
- 2026-02-13T18:50:36+01:00 — 1ad8a9e — fix(ci): stabilize Lighthouse target and skip remote theme pull
- 2026-02-13T18:33:58+01:00 — 1ccc2b8 — feat(lusena): complete PDP + cart parity rollout
- 2026-02-07T16:30:27+01:00 — 3a51798 — refactor(lusena): split PDP into snippets
- 2026-02-04T20:48:18+01:00 — 09ba94a — fix(lusena): preserve PDP image index on color switch
- 2026-02-04T20:39:13+01:00 — cdcee94 — fix(lusena): correct PDP color gallery filtering
- 2026-02-03T19:25:59+01:00 — 8a6d37a — feat(lusena): PDP gallery grouped by color-tagged media
- 2026-02-02T19:08:42+01:00 — a171d76 — feat(lusena): PDP swatches + variant media switching
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
