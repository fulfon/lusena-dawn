# Re-evaluate single product copy — autonomous flow

Paste this prompt into a new session. Replace `{PRODUCT_HANDLE}` with one of:
`poszewka-jedwabna`, `silk-scrunchie`, `silk-bonnet`, `jedwabna-maska-3d`, `heatless-curlers`

---

Task: Autonomous re-evaluation of LUSENA product copy — {PRODUCT_HANDLE}

IMPORTANT: Run this ENTIRE flow autonomously without asking the owner for input.
Make all decisions yourself. Present ONLY the final result at the very end.
Do NOT pause for confirmation at any intermediate step.
Do NOT stop after the legal check — continue through validation and the final report.

This product's creative session was done BEFORE the orchestrator + Polish e-commerce
copywriter architecture was introduced. The goal: run the existing copy through the
upgraded flow to catch unnatural Polish, rule violations added after the original
session, and missed improvements. If the copy is strong — confirm it as-is. If it
needs changes — make them, validate them, and present the final result.

## Step 0: Read context (mandatory, in this order)

1. `memory-bank/activeContext.md` — current state
2. `memory-bank/progress.md` — what's done
3. `docs/product-metafields-reference.md` — the FULL creative process including:
   - Orchestrator + Polish copywriter architecture (steps 1-9)
   - Information architecture guard + exclusion list (added 2026-03-21)
   - Tagline/benefits rendering context (tagline = desktop, benefits = mobile alternative)
   - BUYBOX-LEVEL EXCLUSION (added 2026-03-22)
   - Feature card description length rule (150-210 chars)
   - Feature card title length rule (max 28 chars)
4. `docs/LUSENA_BrandBook_v2.md` — sections 1.3, 1.7, 2.1
5. The product file: `memory-bank/doc/products/{PRODUCT_HANDLE}.md`
6. Read at least ONE completed product file done with the new flow for tone reference:
   - `memory-bank/doc/products/scrunchie-trio.md` (latest, best example of the new flow)
   - `memory-bank/doc/products/piekny-sen.md` (also done with new flow)

## Step 1: AUDIT (orchestrator)

Read the product file and check EVERY creative field against ALL current rules.
For each field, systematically check:

**Buybox (headline, tagline, 3 benefits):**
- [ ] Exclusion list: Does it mention 22 momme, OEKO-TEX, silk vs polyester, gift
      packaging, Grade 6A, or Suzhou origin? (These were NOT excluded in the original
      sessions — check carefully)
- [ ] Buybox UI exclusion: Does any benefit repeat the guarantee box (60 dni),
      delivery row (1-2 dni robocze, 60 dni na zwrot), or care accordion content?
- [ ] Benefit-to-benefit overlap: Do the 3 benefits each cover a DIFFERENT angle?
      No two benefits may cover the same angle.
- [ ] Hyphens only: Any em dashes (—) instead of hyphens (-)?
- [ ] Sentence case, no exclamation marks?
- [ ] Experiential: Are benefits about what the customer FEELS, not material specs?

**IMPORTANT — Tagline ↔ Benefits is NOT overlap:**
The tagline renders on DESKTOP as a short product description. The 3 benefit bullets
render on MOBILE as an alternative to the tagline. The customer sees ONE OR THE OTHER,
never both at the same time. Therefore, similar or even identical content between
tagline and benefits is EXPECTED and CORRECT — the tagline is the benefits reformulated
as flowing prose for desktop. Do NOT flag tagline ≈ benefits as an overlap violation.

**Feature cards 1 and 3 (per-product):**
- [ ] Title: max 28 characters? Count them.
- [ ] Description: 150-210 characters? Count them.
- [ ] No overlap with universal cards 2/4/5/6?
- [ ] No overlap with buybox benefits?

**SEO:**
- [ ] Page title: max 70 chars?
- [ ] Meta description: max 160 chars?

Record the audit as a table: field | current value | char count | rule check | issues.

## Step 2: POLISH COPYWRITER REVIEW

Spawn a Polish e-commerce copywriter agent to review ALL existing creative copy.
The copywriter reviews for NATURAL POLISH QUALITY regardless of whether the audit
found issues. The brief:

"You are a senior Polish e-commerce copywriter specializing in premium beauty and
lifestyle brands. You write in Polish natively and have a perfect ear for natural,
elegant Polish phrasing.

Review the following existing copy for a LUSENA product. DO NOT rewrite everything —
only flag elements where:
1. The Polish sounds translated, awkward, or unnatural (wrong prepositions,
   unnatural collocations, wrong register for premium calm tone)
2. A phrase could be more natural/conversational while keeping the same meaning
3. The rhythm or flow feels off when read aloud

For each flagged element, provide:
- The current text
- What sounds unnatural and why (be specific about the Polish issue)
- A proposed minimal fix (same meaning, better Polish)

If the text sounds good and natural — say so EXPLICITLY for each field.
At the end, give an overall verdict: 'POTWIERDZONE' (no changes needed) or
'POPRAWKI' (list of specific fixes).

Rules: hyphens only (never em dashes), no exclamation marks, sentence case,
premium calm tone, everyday language.

Product: [paste product info]
Price: [paste price]
Target customer: [paste from brandbook]

CREATIVE FIELDS TO REVIEW:
[paste all creative fields: headline, tagline, benefits, card 1 title+desc,
card 3 title+desc, SEO title, SEO meta description]"

## Step 3: DECISION (make this autonomously — do NOT ask the owner)

Based on the audit + copywriter review, determine the severity:

**NO ISSUES (audit clean + copywriter says POTWIERDZONE):**
- Skip to Step 6. No changes needed.
- Record in the product file: "Re-evaluated {DATE} using orchestrator + Polish
  copywriter flow. No changes needed. Copy confirmed."

**MINOR ISSUES (1-3 small fixes: awkward phrasing, small char limit overage):**
- Apply the copywriter's minimal fixes directly.
- Quick legal re-check on changed elements only (invoke /lusena-legal-check).
- Do NOT run customer validation for minor wording fixes.
- Update the product file with the new values.
- Continue to Step 6.

**MAJOR ISSUES (exclusion list violations, significant overlap between benefits,
headline/tagline rewrite, 4+ elements changed):**
- Have the copywriter rewrite affected fields.
- Run legal check on all changed elements (Step 4).
- Run customer validation — 1 focused run on changed elements only (Step 5).
  Include buybox UI context: "W sekcji zakupowej, OBOK korzyści, klientka widzi:
  cenę produktu, box gwarancji '60 dni gwarancji spokojnego snu' z linkiem
  'Jak to działa?', wiersz dostawy '1-2 dni robocze' + '60 dni na zwrot'."
- If validation scores are all ≥ 7.0 → accept changes.
- If mixed → pick the higher-scoring version per element (original vs new).
- Update the product file with final values.
- Continue to Step 6.

## Step 4: Legal check (if changes made)

Invoke `/lusena-legal-check` on changed elements only.
If PASS → continue to Step 5 (or Step 6 if MINOR). If issues → have copywriter fix and re-check.

Do NOT stop here. Continue autonomously.

## Step 5: Customer validation (only if MAJOR changes)

Invoke `/lusena-customer-validation`. Max 1 run for re-evaluations.
Compare scores against the ORIGINAL validation scores in the product file.
If new scores are LOWER than original → revert to original copy for those elements.
The principle: do no harm.

Do NOT stop here. Continue autonomously to Step 6.

## Step 6: FINAL REPORT (present to owner)

This is the ONLY point where you communicate with the owner. Present EVERYTHING
in one message — the full report followed by the simple summary.

### Re-evaluation report: {PRODUCT_NAME}

**a. AUDIT RESULTS**
Table of all creative fields with rule check status (PASS/FAIL per rule).

**b. POLISH QUALITY VERDICT**
Copywriter's assessment: POTWIERDZONE or POPRAWKI with specifics.

**c. CHANGES MADE** (if any)
For each changed field:
| Field | Original | Updated | Reason |
Show the old and new values side by side.

If NO changes were made, state: "All fields confirmed as-is. No changes needed."

**d. VALIDATION SCORES** (if re-validated)
Show original scores vs new scores. Highlight any regressions.

**e. LEGAL STATUS**
PASS/FAIL for any changed elements.

**f. OVERALL VERDICT**
One of:
- "CONFIRMED — copy is strong, natural Polish, compliant with all current rules."
- "UPDATED — N fields adjusted for [reason]. Product file updated."
- "REVERTED — attempted changes scored lower than original. Original copy retained."

**g. PRODUCT FILE STATUS**
State whether the product file has been updated or left unchanged.

### Simple summary (MANDATORY — always include at the very end)

After the detailed report, always close with a plain-language summary:

- If nothing changed: state "No changes. Copy confirmed as-is." and briefly list
  what was checked and why it all passed.
- If something changed: for each changed field, show the old value, the new value,
  why it was changed, and why the new version was accepted (scores, praise, etc.).
- If something was changed and then reverted: explain what was tried, why it scored
  lower, and why the original was kept.

Keep it short — 5-15 lines. The owner should be able to read just this summary
and understand the full outcome without reading the detailed report.

## Reminders

- FULLY AUTONOMOUS — do not ask the owner anything until the final report
- Do NOT stop after intermediate steps (legal check, validation) — always continue
  to the final report
- This is quality assurance, not reinvention — minimize changes
- The orchestrator NEVER writes Polish text directly — all Polish comes from the
  copywriter agent
- Universal fields (cards 2/4/5/6, specs, care) are LOCKED — do not review them
- Hyphens only, never em dashes
- Tagline ≈ benefits is NOT overlap (they are desktop/mobile alternative views)
- DO NO HARM: if changes score lower than the original, revert
- Update the product file with results (re-evaluation date + verdict)
- Do NOT commit to git — the owner will decide when to commit
