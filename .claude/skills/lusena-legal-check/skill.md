---
name: lusena-legal-check
description: "Legal compliance check for LUSENA product copy. Evaluates headlines, taglines, benefits, and any marketing claims against EU Regulation 655/2013, Polish UOKiK consumer protection rules, and the LUSENA brandbook's approved/forbidden claims list. Returns PASS or a list of specific issues with suggested fixes."
user_invocable: true
---

# LUSENA Legal Compliance Check

## Purpose

Verify that product copy (metafield values) complies with EU and Polish consumer protection law before publishing. This skill establishes the legal boundaries for creative copy — run it AFTER crafting copy but BEFORE customer persona validation.

## When to use

- After crafting creative copy for a new product (headline, tagline, benefits)
- After refining copy based on customer persona feedback (if new claims were introduced)
- When unsure whether a specific claim is legally safe
- As part of the creative session workflow (step 3 in `docs/product-metafields-reference.md`)

## Inputs

The user provides the product copy to check. At minimum:
- `pdp_emotional_headline`
- `pdp_tagline`
- `pdp_benefit_1`, `pdp_benefit_2`, `pdp_benefit_3`

Optionally:
- Feature highlight titles/descriptions
- Any other marketing claims being considered

If no copy is provided, ask the user to paste the values or point to the product file in `memory-bank/doc/products/`.

## Legal framework

Before evaluating, read these sources:

1. **LUSENA brandbook legal section** — `docs/LUSENA_BrandBook_v2.md` section 1.7 "Punkty dowodowe" — contains the approved/forbidden claims lists and proof point hierarchy.

2. **The rules below** (embedded for quick reference):

### Approved claim patterns (safe to use)

- "Sprzyja redukcji zagnieceń skóry" (helps reduce skin creases)
- "Pomaga zachować nawilżenie" (helps maintain moisture)
- "Może ograniczać tarcie włosów" (may reduce hair friction)
- Physical/mechanical claims: friction, creases, absorption (these describe textile properties, not medical effects)
- Factual specs with documentation: "22 momme", "Grade 6A", "OEKO-TEX Standard 100"
- Origin claims with supplier records: "jedwab z Suzhou"
- Comparative claims with evidence: "jedwab chłonie mniej wilgoci niż bawełna" (general textile science)

### Forbidden claim patterns (never use)

- Medical claims: "leczy trądzik" (cures acne), "usuwa zmarszczki" (removes wrinkles), "regeneruje skórę" (regenerates skin)
- Unqualified superlatives: "najlepszy na świecie" (best in the world), "jedyny taki" (only one like it) without proof
- Fabricated social proof: fake review counts, fake customer numbers, fake ratings
- Unsubstantiated percentages: "43% mniej tarcia" without owning the specific test documentation
- "Made in China" (use "jedwab z Suzhou" — region, not country)
- "Fabryka" (use "manufaktura" or "pracownia")
- Price war language: "taniej niż..." (cheaper than...)

### EU Regulation 655/2013 — six criteria (all must be met)

1. **Legal compliance** — no claims of official endorsement that doesn't exist
2. **Truthfulness** — features/ingredients must actually be present in meaningful quantities
3. **Evidential support** — all claims backed by studies, tests, or documentation
4. **Honesty** — no exaggerated expectations, no manipulative before/after
5. **Fairness** — comparative claims must not unfairly disparage competitors
6. **Informed decision-making** — claims must be clear and understandable to average consumer

### Polish UOKiK specifics

- Ustawa o przeciwdziałaniu nieuczciwym praktykom rynkowym (Act on Combating Unfair Market Practices)
- UOKiK can fine up to 10% of previous year's turnover
- Consumer-facing prices must include VAT
- "Bestseller" badge is acceptable only if the product is genuinely a top seller

### Note: silk pillowcases are TEXTILES, not cosmetics

EU Regulation 655/2013 technically applies to cosmetic products. Silk pillowcases are textiles, governed by general consumer protection law (Directive 2005/29/EC on unfair commercial practices). This means:
- You have slightly more flexibility than cosmetic brands
- But all claims must still be truthful, substantiable, and not misleading
- UOKiK applies the same consumer protection standards regardless of product category

## Evaluation process

For each piece of copy provided:

1. **Scan for forbidden patterns** — check against the forbidden list above
2. **Verify claims have evidence** — does each factual claim have documentation? (OEKO-TEX certificate, supplier COA, test reports)
3. **Check hedging language** — beauty effect claims must use "sprzyja/pomaga/może" not definitive language
4. **Check tone rules** — sentence case? No exclamation marks? No aggressive sales language?
5. **Check origin language** — "Suzhou" not "China"? "Manufaktura" not "fabryka"?
6. **Assess overall impression** — would a reasonable consumer be misled?

## Output format

```
## Legal compliance report

**Product:** {product name}
**Date:** {date}
**Verdict:** PASS / FAIL (N issues found)

### Items checked

| # | Copy element | Field | Verdict | Notes |
|---|---|---|---|---|
| 1 | "Obudź się bez zagnieceń..." | headline | ✅ PASS | Mechanical claim, safe |
| 2 | "43% mniej tarcia..." | benefit_1 | ⚠️ ISSUE | Needs test documentation |

### Issues requiring action (if any)

**Issue 1: [field name]**
- **Current copy:** "..."
- **Problem:** [specific legal concern]
- **Suggested fix:** "..." (legally safe alternative that preserves conversion intent)

### Summary

[1-2 sentences: overall compliance status and any patterns to watch]
```

## Important

- This skill checks LEGAL compliance only — not conversion quality or brand tone
- When suggesting fixes, preserve the conversion intent of the original copy as much as possible
- If a claim is borderline (could go either way), flag it as ⚠️ WARNING with explanation, not as a hard FAIL
- The owner makes the final decision on borderline cases
