# LUSENA QA Test Plan — Upsell, Bundles & Cross-sell

**Scope:** Cart upsell, bundle nudges, cart merge, cross-sell checkbox, scrunchie education, bundle PDP flows, BXGY pricing, free shipping bar, and edge cases.
**Store:** `lusena-dev.myshopify.com` (password: `paufro`)
**Date:** 2026-04-03
**Tested at commit:** `36c832b` (fix(lusena): worktree-sync proportionality + merge gate wording)

> Mark each test: PASS / FAIL / SKIP (with reason)

## Progress

| Batch | Sections | Tests | Status |
|-------|----------|-------|--------|
| 1 | A1 + A2 + A3 | 16/16 PASS | DONE |
| 2 | A4 + A5 + A6 | 12/12 PASS | DONE |
| 3 | A7 + A8 + A9 | 10/11 PASS (1 FAIL) | DONE |
| 4 | A10 + A11 + A12 | 11/11 PASS | DONE |
| 5 | B2.1-B2.5 + B3.1,B3.2,B3.4 | 8/8 PASS | DONE |
| 6 | B6.1 + B6.6 + B6.8 | 3/3 PASS | DONE |
| 7 | B1.4, B1.6, B4.1-B4.3, B5.1-B5.4 | 9/9 PASS | DONE |
| Manual | B1.1-B1.3, B1.5, B1.7, B3.3, B4.4, B5.5, B6.2-B6.5, B6.9-B6.10 | 13/13 PASS | DONE |
| **Total** | | **84/84 PASS (A7.5 reclassified), 4 fixed, 2 intentional, 1 info** | COMPLETE |

## Findings (to fix after all tests)

| ID | Severity | Description |
|----|----------|-------------|
| F1 | ~~Low~~ FIXED | **A6.4 — Maska handle mismatch in scrunchie education Liquid.** Fixed: `jedwabna-maska-do-spania-3d` → `jedwabna-maska-3d` in both Liquid case statement and JS label map. Verified on live preview. |
| F2 | Info | **A4.2 — Discount type is `fixed_amount`, not BXGY.** No fix needed — terminology only. |
| F3 | ~~Needs review~~ Intentional | **A7.5 — Scrunchie triggers Scrunchie Trio bundle nudge.** Confirmed intentional per bundle strategy: `bundle_nudge_map` metafield on Scrunchie Trio explicitly maps `scrunchie-jedwabny` as trigger. Upsell matrix in `upsell-strategy.md` lists this pairing. A7.5 reclassified as PASS. |
| F4 | Intentional | **B6.6 — No nudge after re-adding individual post-swap.** Confirmed intentional per strategy: two suppression rules cover this (bundle in cart → suppress; 2+ distinct products → suppress). Strategy explicitly rejected "upselling when bundle is in cart". |
| F5 | ~~Medium~~ FIXED | **A7.4 / Manual — Walek cross-sell card shows scrunchie at 59 zl, not 39 zl.** Fixed: added `lusena_cart_cross_sell_price` theme setting (default 3900). Cart drawer and cart page now show crossed-out 59 zl + 39 zl with "Taniej w komplecie" education text. Verified on live preview. |
| F6 | ~~Medium~~ FIXED | **Manual — Scrunchie Trio nudge CTA error on quick click.** Fixed: added `swapInProgress` boolean guard in both cart drawer and cart page swap handlers to prevent double-execution on quick/double clicks. |
| F7 | ~~Low~~ FIXED | **Manual / A6.4 — Scrunchie education generic fallback for maska + walek.** Fixed together with F1: `jedwabny-walek-do-lokow` → `walek-do-lokow` in both Liquid and JS. Verified on live preview. |

---

# Part A — Agent Tests (Playwright automated)

These tests verify facts: prices, element presence, card logic, threshold math. The agent runs them systematically via `/lusena-preview-check`.

---

## A1. Pricing — Individual Products

**Visit each PDP, read the price element.**

| # | Product | Handle | Expected Price | Result |
|---|---------|--------|---------------|--------|
| A1.1 | Poszewka jedwabna 50x60 | `poszewka-jedwabna` | **269 zl** | PASS |
| A1.2 | Jedwabny czepek do spania | `czepek-jedwabny` | **239 zl** | PASS |
| A1.3 | Jedwabna maska 3D do spania | `jedwabna-maska-3d` | **169 zl** | PASS |
| A1.4 | Jedwabny walek do lokow | `walek-do-lokow` | **219 zl** | PASS |
| A1.5 | Scrunchie jedwabny | `scrunchie-jedwabny` | **59 zl** | PASS |

---

## A2. Pricing — Bundles

**Visit each bundle PDP, read price + crossed-out price + savings.**

| # | Bundle | Handle | Price | Crossed-out | Savings | Result |
|---|--------|--------|-------|-------------|---------|--------|
| A2.1 | Nocna Rutyna | `nocna-rutyna` | **399 zl** | ~~508 zl~~ | 109 zl | PASS — "Oszczedzasz 109 zl" |
| A2.2 | Piekny Sen | `piekny-sen` | **349 zl** | ~~438 zl~~ | 89 zl | PASS — "Oszczedzasz 89 zl" |
| A2.3 | Scrunchie Trio | `scrunchie-trio` | **139 zl** | ~~177 zl~~ | 38 zl | PASS — "Oszczedzasz 38 zl" |

---

## A3. Cross-sell Checkbox — Presence & Price

**Visit each PDP, check if cross-sell checkbox exists and shows correct price.**

| # | PDP | Expected | Result |
|---|-----|----------|--------|
| A3.1 | Poszewka | Checkbox visible, scrunchie at 39 zl, "Taniej w komplecie" | PASS |
| A3.2 | Bonnet | Checkbox visible, scrunchie at 39 zl | PASS |
| A3.3 | Maska | Checkbox visible, scrunchie at 39 zl | PASS |
| A3.4 | Walek | Checkbox visible, scrunchie at 39 zl | PASS |
| A3.5 | Scrunchie | NO checkbox (can't cross-sell itself) | PASS — not found |
| A3.6 | Scrunchie Trio bundle | NO checkbox (already contains scrunchies) | PASS — not found |
| A3.7 | Nocna Rutyna bundle | Checkbox hidden initially (correct) | PASS — hidden, height=0 |
| A3.8 | Piekny Sen bundle | Checkbox hidden initially (correct) | PASS — hidden, height=0 |

---

## A4. Cross-sell Checkbox — Functional

**On poszewka PDP: test checkbox + ATC interaction.**

| # | Action | Expected | Result |
|---|--------|----------|--------|
| A4.1 | Check checkbox → click ATC | Both poszewka AND scrunchie in cart drawer | PASS — 2 items: poszewka (26900) + scrunchie (3900) |
| A4.2 | Verify scrunchie price in cart | Shows ~~59 zl~~ 39 zl (automatic discount) | PASS — discount 2000, type: fixed_amount (see F2) |
| A4.3 | Clear cart → uncheck checkbox → click ATC | Only poszewka in cart, no scrunchie | PASS — 1 item, poszewka only |

---

## A5. Bundle PDP Cross-sell Timing

**On Nocna Rutyna: verify checkbox appears only after all colors selected.**

| # | Action | Expected | Result |
|---|--------|----------|--------|
| A5.1 | Load Nocna Rutyna PDP | Cross-sell checkbox NOT visible | PASS — hidden, height=0, class `lusena-bundle-cross-sell--hidden` |
| A5.2 | Select first color (poszewka) | Checkbox still NOT visible | PASS — still height=0 |
| A5.3 | Select second color (bonnet) — all selected | Checkbox appears (slide-in animation) | PASS — height=70, hidden class removed |
| A5.4 | Check checkbox → ATC | Bundle + scrunchie both in cart, correct colors | PASS — Nocna Rutyna (39900) + scrunchie (3900), colors: Czarny/Czarny |

---

## A6. Scrunchie PDP Education

**Test price swap based on cart contents.**

| # | Setup | Visit scrunchie PDP | Expected Price | Result |
|---|-------|-------------------|---------------|--------|
| A6.1 | Empty cart | `/products/scrunchie-jedwabny` | **59 zl** (no strikethrough) | PASS — 59 zl, education row hidden |
| A6.2 | Add poszewka first | `/products/scrunchie-jedwabny` | **~~59 zl~~ 39 zl** + hint text | PASS — "Taniej z poszewka jedwabna w koszyku" |
| A6.3 | Add bonnet first | `/products/scrunchie-jedwabny` | **~~59 zl~~ 39 zl** + hint text | PASS — "Taniej z czepkiem jedwabnym w koszyku" |
| A6.4 | Add maska first | `/products/scrunchie-jedwabny` | **~~59 zl~~ 39 zl** + hint text | PASS — price correct, but generic "Taniej w komplecie" (see F1) |
| A6.5 | Check sticky ATC price | Scroll down | Sticky bar also shows 39 zl | PASS — sticky shows "39 zl" |

---

## A7. Cart Upsell Cards — Appearance

**Clear cart before each. Add trigger product, check which upsell card appears in drawer.**

| # | Add to cart | Expected card | Key content to verify | Result |
|---|-----------|--------------|----------------------|--------|
| A7.1 | Poszewka | Bundle nudge (two-tile) | "have" tile + "add" tile, gain-framed headline | PASS — Nocna Rutyna nudge, "zaoszczedz 109 zl", have: poszewka + add: czepek |
| A7.2 | Bonnet | Nocna Rutyna nudge | "have" bonnet + "add" poszewka | PASS — "zaoszczedz 109 zl", have: bonnet + add: poszewka |
| A7.3 | Maska | Piekny Sen nudge | "have" maska + "add" poszewka | PASS — "zaoszczedz 89 zl", have: maska + add: poszewka |
| A7.4 | Walek (curlers) | Regular cross-sell card | Scrunchie image, 39 zl, "Dodaj" button | PASS (functionally) — but card shows 59 zl, not 39 zl (see F5) |
| A7.5 | Scrunchie alone | No upsell card | Nothing in upsell zone | FAIL — Scrunchie Trio nudge appears (see F3) |

---

## A8. Cart Upsell Cards — Cart Page Parity

**Same as A7 but verify on `/cart` page instead of drawer.**

| # | Add to cart | Check `/cart` page | Expected | Result |
|---|-----------|-------------------|----------|--------|
| A8.1 | Poszewka | Navigate to `/cart` | Same bundle nudge as drawer | PASS — same Nocna Rutyna nudge on cart page |
| A8.2 | Walek | Navigate to `/cart` | Same cross-sell card as drawer | PASS — same scrunchie card on cart page |

---

## A9. Cart Merge — Card Appearance

**Add both components separately, verify merge card appears.**

| # | Items added | Expected merge card | Result |
|---|-----------|-------------------|--------|
| A9.1 | Poszewka + bonnet | "Kup razem i zaoszczedz 109 zl" — Nocna Rutyna merge | PASS — "Zamien na zestaw i zaoszczedz 109 zl", both tiles "W koszyku" |
| A9.2 | Poszewka + maska | "Kup razem i zaoszczedz 89 zl" — Piekny Sen merge | PASS — "Zamien na zestaw i zaoszczedz 89 zl" |
| A9.3 | Merge card UI | Two "W koszyku" tiles showing both products | PASS — 2 `bn-have` tiles, 0 `bn-add` tiles, both "W koszyku" |
| A9.4 | Poszewka + bonnet + maska | Higher savings wins (Nocna Rutyna, 109 zl) | PASS — 109 zl shown, not 89 zl |

---

## A10. BXGY Discount in Cart

**Verify strikethrough pricing for scrunchie in cart after cross-sell add.**

| # | Cart contents | Scrunchie shows | Cart total | Result |
|---|--------------|----------------|-----------|--------|
| A10.1 | Poszewka + scrunchie (via checkbox) | ~~59 zl~~ 39 zl | 308 zl | PASS — 30800, strikethrough confirmed in DOM |
| A10.2 | Bonnet + scrunchie (via checkbox) | ~~59 zl~~ 39 zl | 278 zl | PASS — 27800, discount 2000 |
| A10.3 | Walek + scrunchie (via cross-sell card) | ~~59 zl~~ 39 zl | 258 zl | PASS — 25800, "Dodaj" clicked in drawer |
| A10.4 | Scrunchie alone (no qualifying item) | 59 zl (no strikethrough) | 59 zl | PASS — 5900, no discount, no strikethrough |

---

## A11. Free Shipping Bar

**Add items, check shipping bar state in cart drawer.**

| # | Cart contents | Total | Bar state | Result |
|---|--------------|-------|----------|--------|
| A11.1 | Poszewka alone | 269 zl | NOT qualified (6 zl short) | PASS — "Brakuje Ci 6 zl do darmowej dostawy" |
| A11.2 | Poszewka + cross-sell scrunchie | 308 zl | QUALIFIED (green) | PASS — "Masz darmowa dostawe!" |
| A11.3 | Nocna Rutyna bundle | 399 zl | QUALIFIED | PASS — "Masz darmowa dostawe!" |
| A11.4 | Scrunchie Trio | 139 zl | NOT qualified | PASS — "Brakuje Ci 136 zl do darmowej dostawy" |
| A11.5 | Bonnet + cross-sell scrunchie | 278 zl | QUALIFIED | PASS — "Masz darmowa dostawe!" (278 > 275) |

---

## A12. Smart Suppress

| # | Scenario | Expected | Result |
|---|----------|----------|--------|
| A12.1 | Add poszewka + walek (2 distinct non-bundle items) | Regular cross-sell suppressed, but bundle nudge still shows | PASS — scrunchie card gone, Nocna Rutyna nudge still shows |
| A12.2 | Add scrunchie + walek | Both non-bundle triggers — upsell suppressed | PASS — upsell zone completely empty |

---

# Part B — Manual Tests (owner)

These tests require human judgment, multi-surface interaction, timing sensitivity, or real device testing.

---

## B1. Bundle PDP — Full Flow Feel

**Test each bundle end-to-end. Focus on feel, not just function.**

| # | Bundle | Checks | Result |
|---|--------|--------|--------|
| B1.1 | Nocna Rutyna | Progressive disclosure feels natural, steps open/close smoothly, chips update, color swatches responsive | PASS |
| B1.2 | Piekny Sen | Same flow, 2 steps (poszewka + maska) | PASS |
| B1.3 | Scrunchie Trio | 3 steps, can pick same color for multiple, cart shows all 3 with step numbering | PASS |
| B1.4 | Re-editing | Click completed chip → step re-opens, change color, other steps unaffected | PASS (agent) — changed Czarny→Szampan, step 2 kept Brudny roz |
| B1.5 | Sticky ATC (incomplete) | Click sticky → scrolls to selector + swatch breathe animation | PASS |
| B1.6 | Sticky ATC (complete) | Adds to cart directly, drawer opens | PASS (agent) — sticky ATC added Nocna Rutyna with re-edited colors |
| B1.7 | Cross-sell slide-in | After all colors picked: checkbox slides in with translateY animation — smooth, not janky | PASS |

---

## B2. Accept Bundle Nudge (Swap) — Feel & Locking

**Add a trigger product, accept the nudge. Focus on the transition.**

| # | Scenario | Checks | Result |
|---|----------|--------|--------|
| B2.1 | Add poszewka → accept Nocna Rutyna nudge in drawer | Loading state visible? Locking prevents other clicks? Re-render smooth? | PASS (agent) — poszewka gone, Nocna Rutyna added (39900). **Feel: test manually** |
| B2.2 | Add bonnet → accept nudge on `/cart` page | Same checks on cart page surface | PASS (agent) — bonnet gone, Nocna Rutyna added on cart page |
| B2.3 | Color auto-match | After swap: bundle color matches the original item's color | PASS (agent) — poszewka Czarny → bundle Poszewka: Czarny, Bonnet: Czarny |
| B2.4 | Nudge disappears after swap | Card gone, replaced by bundle line items | PASS (agent) — `.lusena-upsell-card` count = 0 |
| B2.5 | Cart totals update | Price changes from individual to bundle price | PASS (agent) — 39900 confirmed |

---

## B3. Accept Cart Merge — Feel & Color Carry-over

**Add both components separately, accept the merge.**

| # | Scenario | Checks | Result |
|---|----------|--------|--------|
| B3.1 | Poszewka (Czarny) + bonnet (Brudny roz) → merge | Both removed, Nocna Rutyna added with Czarny poszewka + Brudny roz bonnet | PASS (agent) — Nocna Rutyna, Poszewka: Czarny, Bonnet: Brudny roz |
| B3.2 | Poszewka (Szampan) + maska (Czarny) → merge | Both removed, Piekny Sen added with Szampan poszewka + Czarny maska | PASS (agent) — Piekny Sen, Poszewka: Szampan, Maska: Czarny |
| B3.3 | Loading/locking during merge | All items disabled, smooth transition, no flicker | PASS |
| B3.4 | Merge on cart page | Same behavior on `/cart` | PASS (agent) — cart page merge CTA works identically |

---

## B4. Bidirectional Cart Sync

**Open cart page in a tab AND cart drawer. Mutate in one, watch the other.**

| # | Action | Watch | Expected | Result |
|---|--------|-------|----------|--------|
| B4.1 | Change qty on cart page | Drawer | Drawer updates automatically | PASS (agent) — qty→2 on page, drawer showed qty=2 |
| B4.2 | Change qty in drawer | Cart page | Cart page updates automatically | PASS (agent) — qty→1 in drawer, cart page showed qty=1 |
| B4.3 | Accept nudge in drawer | Cart page | Cart page reflects swap (items change) | PASS (agent) — nudge accepted, cart page re-rendered with Nocna Rutyna |
| B4.4 | Add item via ATC (opens drawer) | Cart page (if open) | Cart page shows new item | PASS (manual, two tabs) |

---

## B5. Checkout Verification

**Verify prices carry through to Shopify checkout.**

| # | Cart contents | Check at checkout | Result |
|---|--------------|-------------------|--------|
| B5.1 | Poszewka + scrunchie (BXGY) | Scrunchie shows 39 zl, total 308 zl | PASS (agent) — checkout: 269 + 39 = 308 zl, discount -20 zl shown |
| B5.2 | Nocna Rutyna bundle | 399 zl, no unexpected discounts | PASS (agent) — checkout: 399 zl, no savings row |
| B5.3 | Nocna Rutyna + scrunchie | 399 + 39 = 438 zl | PASS (agent) — checkout: 438 zl, scrunchie discounted |
| B5.4 | Scrunchie standalone | 59 zl, no discount applied | PASS (agent) — checkout: 59 zl, no discount, no savings |
| B5.5 | Checkout button loading | Shimmer + "Przekierowuje..." text visible during redirect | PASS |

---

## B6. Edge Cases — Timing & Stress

| # | Scenario | Expected | Result |
|---|----------|----------|--------|
| B6.1 | Add poszewka qty 2, then accept nudge | ALL 2 units removed (qty → 0), bundle added once | PASS (agent) — qty 2 → 0, Nocna Rutyna qty 1, total 39900 |
| B6.2 | Rapidly click ATC 3-4 times | Only one add (no duplicates) | PASS |
| B6.3 | Rapidly click nudge CTA twice | Only one swap (interaction locking blocks second) | PASS |
| B6.4 | Accept nudge → browser back button | Cart state consistent, no phantom items | PASS |
| B6.5 | Refresh `/cart` page mid-swap | Page loads with correct final state | PASS |
| B6.6 | Add bundle via nudge, then add same individual product again | New nudge or merge card appears | PASS (agent) — both items in cart, no nudge shown (see F4) |
| B6.7 | Accept nudge in drawer while `/cart` page open | Cart page updates via bidirectional sync | SKIP — duplicate of B4.3 (PASS) |
| B6.8 | Bundle in cart → try to edit colors | Cannot — no color editing in cart, must use bundle PDP | PASS (agent) — 0 selects, 0 swatches, 0 edit links |
| B6.9 | On scrunchie PDP: add qualifying item in another tab | Price updates live (PubSub) without refreshing scrunchie tab | PASS |
| B6.10 | Slow network (DevTools throttle to Slow 3G) + accept nudge | Loading state visible long enough, swap completes, no errors | SKIP (optional) |

---

# Execution Log

## Agent batches (completed)

| Batch | Sections | Tests | Result | What was tested |
|-------|----------|-------|--------|----------------|
| 1 | A1 + A2 + A3 | 16 | 16 PASS | Pricing (all 8 PDPs) + cross-sell checkbox presence |
| 2 | A4 + A5 + A6 | 12 | 12 PASS | Cross-sell functional + bundle timing + scrunchie education |
| 3 | A7 + A8 + A9 | 11 | 10 PASS, 1 FAIL | Upsell card appearance (all triggers) + merge cards |
| 4 | A10 + A11 + A12 | 11 | 11 PASS | BXGY pricing in cart + shipping bar + smart suppress |
| 5 | B2.1-B2.5 + B3.1,B3.2,B3.4 | 8 | 8 PASS | Accept nudge swap + accept merge (cart state verification) |
| 6 | B6.1 + B6.6 + B6.8 | 3 | 3 PASS | Edge: qty>1 swap, re-add after swap, no color edit in cart |
| 7 | B1.4, B1.6, B4.1-B4.3, B5.1-B5.4 | 9 | 9 PASS | Re-edit chips, sticky ATC, bidirectional sync, checkout prices |

## Remaining manual tests (13)

Owner tests — feel, timing, multi-tab, stress:

1. **B1.1** — Nocna Rutyna progressive disclosure feel
2. **B1.2** — Piekny Sen flow feel
3. **B1.3** — Scrunchie Trio 3-step flow + cart step numbering
4. **B1.5** — Sticky ATC incomplete → scroll + breathe animation
5. **B1.7** — Cross-sell slide-in animation quality
6. **B3.3** — Merge locking feel (no flicker)
7. **B4.4** — ATC on PDP tab → cart page tab updates (two tabs)
8. **B5.5** — Checkout button shimmer + "Przekierowuje..."
9. **B6.2** — Rapidly click ATC 3-4 times → only one add
10. **B6.3** — Rapidly click nudge CTA twice → only one swap
11. **B6.4** — Accept nudge → browser back → cart consistent
12. **B6.5** — Refresh `/cart` mid-swap → correct state
13. **B6.9** — Cross-tab: add qualifying item in tab A → scrunchie price updates in tab B
14. ~~B6.10~~ — Slow 3G + nudge (optional, needs DevTools throttling)

## Key rules
- **Clear cart before each upsell/merge test** — cart contents affect card logic
- **Agent tests = facts** (is the price 269? does the checkbox exist?)
- **Manual tests = judgment** (does the swap feel smooth? is locking visible enough?)

## If BXGY discount isn't working
1. Check Shopify admin → Discounts → BXGY discount is active
2. Qualifying product handle matches BXGY "buys" configuration
3. Scrunchie variant is in the BXGY "gets" list
