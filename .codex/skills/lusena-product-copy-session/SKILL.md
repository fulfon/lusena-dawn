---
name: lusena-product-copy-session
description: Orchestrates the full LUSENA creative copy workflow - from product research through legal check, customer validation, and saving finalized copy
argument-hint: "<product-handle>"
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, Skill(lusena-legal-check), Skill(lusena-customer-validation)
---

# LUSENA Product Copy Session

End-to-end creative workflow for writing or refreshing product copy. Chains the legal check and customer validation skills automatically instead of requiring manual invocation.

## Step 1: Load product context

1. Read `memory-bank/doc/products/$ARGUMENTS.md` (the product file)
2. Read `memory-bank/doc/products/product-metafields-reference.md` (universal fields reference)
3. Identify which fields are marked **"REQUIRES CREATIVE SESSION"** in the product file — only these will be written

Typically creative-session fields are:
- `lusena.pdp_emotional_headline` — the #1 emotional hook (eyebrow text above title)
- `lusena.pdp_tagline` — desktop prose below title, PAS structure (Problem -> Agitate -> Solve)
- `lusena.pdp_benefit_1/2/3` — mobile bullets, each a different angle, experiential only
- `lusena.pdp_feature_1_icon/title/description` — product-specific feature card 1
- `lusena.pdp_feature_3_icon/title/description` — product-specific feature card 3
- `lusena.pdp_feature_5_icon/title/description` — product-specific feature card 5

**NEVER touch universal fields** (feature cards 2, 4, 6 and all `pdp_specs_*` base values). These are locked across all products.

## Step 2: Research and brief

1. Read `memory-bank/doc/brand/LUSENA_BrandBook_v2.md` sections on voice/tone and the specific product category claims
2. Check what category the product falls into for claim limits:
   - **Pillowcase:** skin care claims OK ("sprzyja redukcji zagniecen")
   - **Scrunchie/Bonnet:** protection claims only ("ogranicza tarcie i platanie")
   - **Curlers:** explicit expectation management ("moze pomoc", depends on hair type)
   - **Mask 3D:** comfort and darkness only, not beauty
   - **Bundles:** routine framing, never savings framing
3. Review the **buybox exclusion list** — these topics MUST NOT appear in headline/tagline/benefits:
   - "22 momme" / momme density (-> feature card 2)
   - "OEKO-TEX" / certification (-> quality evidence section + specs accordion)
   - Silk vs polyester/satin (-> feature card 4)
   - Gift packaging (-> feature card 6)
   - "Grade 6A" (-> specs accordion)
   - Origin "z Suzhou" (-> quality evidence section)
   - Guarantee, delivery, savings badge (-> already visible in buybox UI)

## Step 3: Write copy (Polish copywriter subagent)

Launch a subagent as a **Polish e-commerce copywriter** with these instructions:
- Write ALL copy in natural, fluent Polish
- Follow LUSENA voice: expert, calm, empathetic, precise
- Sentences max 18-22 words, one idea per paragraph
- Fewer adjectives, more proof
- Hyphens only (-), never em dashes
- No exclamation marks in headings or benefit bullets
- Sentence case everywhere
- Feature card titles: max 28 characters
- `pdp_tagline` uses PAS structure (Problem -> Agitate -> Solve), 2-3 sentences max
- `pdp_benefit_1/2/3` are experiential (what you feel/see), not specs, not delivery, not guarantee
- Benefits should each cover a different angle (no overlap between them)
- Approved hedging: "sprzyja redukcji", "pomaga zachowac", "moze ograniczac"

The subagent writes draft copy for all creative-session fields.

## Step 4: Legal check

Invoke `/lusena-legal-check` with the draft copy (headline, tagline, 3 benefits, feature card descriptions).

If issues are found, revise and re-check. Max 2 legal check rounds.

## Step 5: Customer validation

Invoke `/lusena-customer-validation` with the approved copy.

4 personas evaluate independently:
- Kasia (quality skeptic, 35, researcher)
- Ewa (gift buyer, 42, low engagement)
- Zuzia (budget student, 22, price sensitive)
- Maja (minimalist, 29, skeptical of marketing)

**Threshold:** All dimension averages must reach >= 7.0 (trust, intent, premium feel).

## Step 6: Iterate if needed

If validation scores are below threshold:
1. Review per-persona LOCK/REFINE table
2. Revise only REFINE-marked elements
3. Re-run legal check on changed elements
4. Re-run customer validation

**Hard cap:** 3 validation runs + 1 composite assembly. If after 3 rounds scores don't reach threshold, present the best version to the user with the scores and let them decide.

## Step 7: Save finalized copy

1. Update the product MD file (`memory-bank/doc/products/$ARGUMENTS.md`) with finalized metafield values
2. Mark the creative-session fields as completed (change "REQUIRES CREATIVE SESSION" to "COMPLETED — [date]")
3. Record validation scores in the product file
4. Remind the user: to push copy to Shopify, run the CSV import workflow (see `memory-bank/doc/products/README.md`)

## Summary output

Present a table of all written fields with their final values and validation scores.
