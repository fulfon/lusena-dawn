# Active Context

*Last updated: 2026-04-04*

## Current focus

**Content polish in progress.** FAQ sections trimmed and improved on both PDP templates. Next: continue content review across all pages, bundle product media.

## Recent completed work

### FAQ trim and improvement — bundle + single PDPs (2026-04-04)

Trimmed redundant FAQ questions on both PDP templates after analysis, legal compliance check (EU 655/2013, Polish UOKiK, LUSENA brandbook), and 4-persona customer validation.

**Bundle PDP** (`product.bundle.json`): 6→4 questions. Removed: "Co zawiera zestaw?" (scroll-up UX), "Jak prać?" (duplicate of buy-box care accordion), "Dlaczego zestaw?" (own 6-card section already covers it). Added: "Jak długo służy jedwab przy codziennym użytkowaniu?" (only info gap on the page). Refined: colors answer no longer hardcodes color names (future-proof), returns trimmed.

**Single PDP** (`product.json`): 6→5 questions. Removed: "Wysyłka i dostawa" (redundant), "Jak prać?" (duplicate), old per-product effects list (showed all 5 products' effects on every PDP). Added: "Skąd wiem, że to prawdziwy jedwab?" (3/4 personas requested — actionable OEKO-TEX verification). Fixed 3 legal issues: Q1 title dropped "cery trądzikowej" (medical condition), Q1 body fixed absolute absorption claim ("nie wchłania" → "wchłania znacznie mniej"), Q3 rewritten with proper hedging and no unsubstantiated "2-4 tygodni" timeline. Q2 made product-neutral (removed "jednej poszewki").

### Header: trust anchor + mobile menu utilities (2026-04-04)

Added "60 dni na zwrot" trust anchor to desktop header — teal color (per brand token: teal = trust/guarantees), rotate-ccw icon, border-left separator, positioned between nav links and action icons. Desktop-only in header bar. On mobile: removed from header bar (stays clean: hamburger | logo | cart), added to hamburger menu utilities row (right-aligned, teal). Also added search (Szukaj) and account (Konto) links with icons to mobile hamburger menu — previously completely inaccessible on mobile. Schema settings for trust anchor text, page, and toggle. Design rationale: Zwroty page repositioned from utility nav link to passive trust signal, reducing purchase friction without adding nav clutter. 2 files changed (+132 lines): `lusena-header.css`, `lusena-header.liquid`.

### Homepage card standardization (2026-04-04)

Unified visual patterns across bestsellers product cards and bundle cards:

1. **Badge consolidation** — 3 custom badge implementations (`.lusena-product-card__badge`, `.lusena-bundles__badge`, `.lusena-media-stage__bestseller`) replaced by shared `.lusena-badge--overlay` in foundations. Frosted glass (white 90% + blur 4px). PDP keeps position overrides for larger gallery context. Badge text standardized to "Bestseller" (was "Best Seller" on PDP).

2. **Full-card links** — Bundle cards changed from `<div>` with CTA button to full `<a>` links (matching product card pattern). CTA button + `cta_label` schema setting removed. Both compact rows and full cards are now clickable links.

3. **Typography hierarchy** — Title bumped to 1.6rem on both product cards and bundle cards (was 1.4rem). Bundle card type scale: title 1.6 > price 1.4 > editorial 1.3 > contents/savings 1.2. Redundant `font-family` declarations removed (inherit from body).

4. **Savings badge** — Moved from inline text in pricing row to gold-tinted chip overlay on bottom-right of card image. Style matches bundle PDP savings chip: `rgba(140, 106, 60, 0.08)` + `backdrop-filter: blur(4px)` + `border-radius`. Bestseller badge top-left (white), savings bottom-right (gold) — distinct visual roles.

5. **Spacing** — Pricing gap aligned to 0.8rem (matching product card + PDP). Card info grouped by function: identity tight (title+contents 0.2rem), editorial breathes (0.6rem above), commercial tight (price+compare 0.2rem).

6. **Hover** — Title underline on hover (`text-underline-offset: 4px`) added to both product cards and bundle cards. Wrapped in `@media (hover: hover)`.

6 files changed across 5 commits. Net -118 lines (cleanup of custom implementations).

### Bundle sticky ATC class fix (2026-04-04)

Fixed `lusena-bundle-sticky-atc.liquid` using `lusena-sticky-atc__variant` class for the crossed-out original price — should have been `lusena-sticky-atc__compare` (matching the standard PDP sticky and the app-wide convention). Semantic fix only, no visual change. Reviewed price display patterns across all 10+ locations — confirmed order (new first, old second) and layout (row for evaluation contexts, stacked for tight/cart contexts) are already consistent and optimal.

### Homepage bundles section — product-driven rewrite (2026-04-03)

Rewrote `lusena-bundles` section from static text placeholders to product-driven editorial cards. Section now pulls real data from Shopify bundle products (prices, URLs, images via product picker) while keeping hand-crafted editorial copy in block settings. Desktop: equal 3-column grid with Bestseller badge on Nocna Rutyna. Mobile: hero card (Nocna Rutyna full card) + 2 compact rows (Piękny Sen, Scrunchie Trio) with SVG thumbnail slots. Savings calculated from `lusena.bundle_original_price` metafield. OOS handling on both card types. Section intro copy: "Zbuduj swoją nocną rutynę" / "Każdy zestaw to gotowy pomysł - na nocną rutynę albo idealny prezent." CSS cascade bug (desktop-only cards not hiding on mobile) caught in QA and fixed via specificity bump. 5 files: `lusena-bundles.liquid` (rewrite), `lusena-bundles.css` (rewrite), `index.json` (3 bundle products wired). Design spec: `docs/superpowers/specs/2026-04-03-homepage-bundles-section-design.md`. SVG thumbnails done (2026-04-04, monochrome gold illustrations + compact row polish). Pending: bundle product photography.

### Wide container tier for trust bar (2026-04-03)

Added `.lusena-container--wide` (max-width: 180rem / 1800px) to `lusena-foundations.css` as a third container tier between standard (120rem) and full-bleed. Applied to trust bar section so items spread further apart on wide screens. Explored applying to bestsellers but reverted — product card grids need fixed proportions; wide containers only suit utility strips with discrete, evenly-spaced items.

### Packaging list fix + CSV icon sync (2026-04-03)

Fixed "Co zawiera opakowanie" accordion rendering all items on one line instead of separate `<li>` entries. Root cause: CSV import stored `list.single_line_text_field` metafield as a single semicolon-separated string. Fix: defensive split in `lusena-pdp-buybox-panels.liquid` (checks if array has 1 entry containing `'; '`, splits it). Same fix applied to `pdp_care_steps` for safety. Also synced 6 feature card icon changes from product MD docs into the import script and regenerated CSV (nocna-rutyna C3/C5, piekny-sen C1/C3, scrunchie-trio C1/C3). Shopify product data now fully in sync with codebase. Handle renames applied in Shopify admin, `bundle_nudge_map` set for all 3 bundles.

### Bundle contents component links (2026-04-03)

Component product names in the "W zestawie" checklist on bundle PDPs are now clickable links to their individual product pages. Uses `all_products` lookup with the 5 known product handles, matched by title against Simple Bundles `variant_options.optionName`. Graceful fallback to plain text if no match. Subtle hover styling (teal + underline). 3 files: `lusena-bundle-contents.liquid`, `lusena-main-bundle.liquid` (passes `product`), `lusena-bundle-pdp.css`.

**Note:** All links now work — handle renames applied in Shopify admin (see "Product handle standardization" below).

### Bundle mobile sticky ATC pricing fix (2026-04-03)

Replaced "Oszczędzasz X zł" savings text with strikethrough original price (`<s>`) on mobile bundle sticky bar - now matches desktop pattern. Added image placeholder divs for bundles without product images yet. Fixed Dawn `div:empty` trap hiding placeholders (bumped `.lusena-sticky-atc__image` to 0-2-0 specificity + `display: block`). 2 files: `lusena-bundle-sticky-atc.liquid`, `lusena-pdp.css`.

### Product handle standardization (2026-04-03)

Standardized 3 English product handles to Polish for SEO consistency:
- `silk-bonnet` → `czepek-jedwabny` (research confirmed "czepek" is the dominant PL search term)
- `silk-scrunchie` → `scrunchie-jedwabny` (matches product title, "scrunchie" is the PL market standard)
- `heatless-curlers` → `walek-do-lokow` (research confirmed "wałek do loków" is the entire market convention)

35 files updated: theme code (Liquid/JSON), memory bank, product docs (renamed), skills, CSV/Python imports, specs/plans. 5 existing Polish handles unchanged. Product doc files renamed accordingly (`czepek-jedwabny.md`, `scrunchie-jedwabny.md`, `walek-do-lokow.md`).

**Shopify admin action: DONE.** Handles renamed, `bundle_nudge_map` set for all 3 bundles, CSV reimported. Shopify auto-created 301 redirects.

### QA fixes — upsell/bundle test findings (2026-04-03)

Comprehensive QA test plan executed (84 tests, all passing). 7 findings documented, 4 fixed:
- **F1+F7:** Scrunchie education handle mismatches — `jedwabna-maska-do-spania-3d` → `jedwabna-maska-3d`, `jedwabny-walek-do-lokow` → `walek-do-lokow` in both Liquid case statement (`lusena-main-product.liquid`) and JS label map (`lusena-scrunchie-education.liquid`).
- **F5:** Cart cross-sell card showed scrunchie at 59 zl instead of 39 zl. Added `lusena_cart_cross_sell_price` theme setting (default 3900). Cart drawer and cart page now show current price first, crossed-out original second, with "Taniej w komplecie" education text.
- **F6:** Bundle swap nudge button stopped working after first successful swap. Added `swapInProgress` guard flag in both cart drawer and cart page — resets on both success and error paths.
- **Compare price styling unified** — cross-sell card now matches bundle/cart-item pattern: 1.2rem, `--lusena-text-2`, 50% opacity strikethrough. Price order standardized: [current] [~~original~~] across all 8 locations.
- **F3+F4:** Confirmed intentional per bundle strategy docs (scrunchie→Trio nudge, no nudge after re-add post-swap).
- Test plan: `docs/qa-test-plan.md`

### Cart/ATC error handling hardening (2026-04-02)

- **User-visible error feedback** on all ATC failure paths: Polish error text ("Coś poszło nie tak") shown on button for 3s with red `.lusena-btn--error` state, then auto-restores. Covers: bundle ATC (4 paths), cross-sell checkbox ATC+Buy Now (4 paths), cart page upsell add, cart page bundle swap, cart drawer bundle swap.
- **`response.ok` check** added to cart-drawer `updateLine` - was silently passing Shopify 422/5xx responses to `renderContents`. Now throws to catch block, consistent with `lusena-bundle-swap.js` pattern.
- **`.catch()` added** to 4 secondary fetch calls (cart-drawer + icon-bubble re-renders in cross-sell-checkbox and bundle-scripts) that had no error handling.
- **Sticky ATC coverage** - single PDP sticky buttons (mobile + desktop) now show error feedback alongside main ATC, matching bundle PDP behavior.
- `.lusena-btn--error` CSS class added to `lusena-button-system.css`.
- 5 files changed (+88 lines): `lusena-button-system.css`, `lusena-cart-items.liquid`, `cart-drawer.liquid`, `lusena-bundle-scripts.liquid`, `lusena-pdp-cross-sell-checkbox.liquid`.

### Worktree launcher: smart resume + auto-cleanup (2026-04-02)

- **Smart resume:** [R] now launches `claude --name` (fresh) for empty worktrees (0 commits, no changes) instead of broken `claude --resume`. Non-empty worktrees still use `--resume`.
- **Auto-cleanup:** After Claude exits, `Invoke-AutoCleanup` checks if the branch was squash-merged to main (has commits + content matches main + no uncommitted changes). If all conditions met, worktree and branch are removed automatically. Otherwise does nothing.
- CLAUDE.md updated to document both behaviors.
- One file changed: `scripts/launch-claude-worktree.ps1` (+50 lines)

### Sticky ATC scrollbar shift fix (2026-04-01)

- Fixed sticky ATC bar shifting ~15px right when cart drawer opens (scrollbar disappearance widens viewport for `position: fixed` elements)
- Added `body.overflow-hidden .lusena-sticky-atc { right: var(--scrollbar-width, 0px); }` to `lusena-pdp.css` — consumes the CSS variable Dawn's `cart-drawer.js` already sets
- One file changed: `assets/lusena-pdp.css` (+4 lines)

### PDP sticky gallery boundary fix (2026-04-01)

- Gallery bottom now aligns with the care card (Pielegnacja) bottom border instead of the grid/section edge
- Added `contain: layout` to `.lusena-grid--pdp` (ensures grid is the sticky containing block)
- Added `padding-bottom: var(--lusena-space-4)` to `.lusena-gallery` on desktop — invisible padding offsets the sticky stop point by 32px to match the last accordion item's `margin-bottom`
- Applies to both standard and bundle PDPs (shared `.lusena-pdp` ancestor)
- One file changed: `assets/lusena-pdp.css` (+10 lines)

### Primary button loading state fix (2026-03-31)

- `.lusena-btn--primary.loading` rule added to `lusena-button-system.css` — preserves teal background when `aria-disabled` and `.loading` coexist
- Affected: PDP ATC, bundle ATC, both sticky ATC bars (all went gray during shimmer due to CSS specificity: disabled state at 0-2-0 overrode loading state)
- Upsell/nudge outline buttons audited — already correct (outline loading `!important` handles it)

### Checkout button fix + loading animation (2026-03-30)

- **Root cause:** `routes.checkout_url` is not a valid Shopify Liquid property — rendered to empty string, making cart drawer `<a href="">` reload current page instead of navigating to checkout
- **Cart drawer:** Replaced `<a>` with `<button data-lusena-drawer-checkout>` + JS `window.location.href = '/checkout'` + loading animation (shimmer + "Przekierowuję..." text swap) + bfcache reset
- **Cart page:** Added loading animation markup + JS to existing submit button
- **theme.liquid:** Hardcoded `/checkout` in `window.routes.checkout_url`
- **Workflow:** CLAUDE.md Browser Interactions section now points to `/lusena-preview-check`. Skill updated to instruct subagent to load `/playwright-cli` first.

### PDP sticky gallery (2026-03-30)

Swapped desktop sticky behavior: gallery (left column) is now `position: sticky` instead of buybox (right column). Gallery stays pinned at `top: 12.8rem` while user scrolls through the taller buybox content. Applies to both standard and bundle PDPs via shared `.lusena-pdp .lusena-gallery` selector. One CSS file changed: `assets/lusena-pdp.css`.

### Phase D cross-sell (2026-03-29) — all 4 sessions consolidated

All PDP cross-sell touchpoints shipped in one day:
1. **PDP cross-sell checkbox** — scrunchie at 39 zl (BXGY) on all individual PDPs + bundle PDPs. White card, teal accent, custom checkbox, color-matched image.
2. **Bundle PDP cross-sell timing** — checkbox reveals after all colors are picked (sunk-cost psychology), with LUSENA signature `translateY(-6px)` slide-in animation.
3. **Scrunchie PDP education** — server-side price swap (39 zl instead of 59 zl) when qualifying product is in cart. Dynamic Polish hint. No FOUC via Liquid-rendered initial state. Live sync via PubSub + MutationObserver.
4. **Cart interaction locking** — full-cart lock during bundle swaps prevents concurrent mutations.

Full architecture details: `memory-bank/doc/features/pdp.md` (cross-sell, education) and `memory-bank/doc/features/cart-page.md` (locking, merge).

### Documentation sweep (2026-03-30)

Comprehensive memory bank audit covering 67 commits. Updated:
- Free shipping threshold 289 -> 275 across all strategy docs, product docs, rules (18 stale refs fixed)
- Cross-sell checkbox + scrunchie education added to systemPatterns.md component systems
- Cross-sell flow added to productContext.md customer journey
- Cart interaction locking added to cart-page.md
- PDP CSS size ~34KB -> ~42KB, foundations ~40KB -> ~50KB across all references
- Upsell strategy roadmap phases marked DONE with actual completion dates
- activeContext consolidated from 4 sessions to summary + architecture pointers

### Earlier in commit range (2026-03-28)

- Benefit bridge, cart merge (#13), card 5 sessions, accordion rewrite, 3 icons, link-arrow, Claude Code infra, migration lessons #55-61
- Full details in `progress.md`

## Next steps

1. Bundle product media (when physical products arrive)
2. Verify product picker handles resolve in theme editor (may need manual re-selection)
3. Content polish — review all page copy for consistency
4. UX backlog items (bonnet naming, value anchors expansion)

## Key decisions (reference)

- **Skip cart discount explanation** — every path into cart already explains the 39 zl price. Cart label adds noise for zero benefit.
- **Cross-sell on bundles: post-color timing** — appears after `allSelected()`, not immediately. Sunk-cost > impulsive.
- **Scrunchie education: inline price swap** — no banners/cards, price itself IS the education. Premium brands adjust prices, not announce discounts.
- **Free shipping threshold: 275 zl** (was 289, originally 269. Updated in settings_schema, settings_data, and all strategy/product docs)
- **Compare price order: [current] [~~original~~]** — consistent across all 8 locations (PDP, cart items, upsell cards, product cards). Established as theme standard.

## Known issues

- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` is a doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- **Swap race condition:** If `/cart/add.js` succeeds but `/cart/change.js` fails, customer has both items in cart. #13 cart merge handles this - the merge card appears on next render, offering to combine them.
- **Trigger item quantity > 1:** Swap removes all units (quantity 0), not just 1.
- **Cart color editing:** Bundle added via nudge auto-matches colors. Customer cannot change colors in cart — must use bundle PDP.

## Architecture notes (quick reference)

Architecture details live in the feature docs. Quick pointers for orientation:
- **Cross-sell checkbox architecture:** `systemPatterns.md` § Component systems
- **Scrunchie education architecture:** `systemPatterns.md` § Component systems
- **Cart upsell/merge/sync:** `memory-bank/doc/features/cart-page.md`
- **Cart drawer = section** (not snippet render): `theme.liquid` uses `{%- section 'cart-drawer' -%}` for section rendering API
- **Upsell CSS scoping:** drawer under `.lusena-cart-drawer__upsell`, cart page under `.lusena-cart-upsell`
- **Bidirectional cart sync:** PubSub + DOMParser innerHTML swap (details in cart-page.md)
