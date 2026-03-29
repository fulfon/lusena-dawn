---
name: lusena-section-design-loop
description: Autonomous design iteration loop for LUSENA sections. Prototypes in the React draft shop (lusena-shop/), validates with a 5-agent Sonnet review panel (2 customer personas + UX designer + CRO specialist + Polish copywriter), iterates up to 5 rounds based on KPI scores, then hands off for Liquid migration.
---

# LUSENA Section Design Loop

## Overview

Redesign or create a LUSENA section through rapid iteration in the React draft shop, validated by simulated customer and expert reviewers. The loop produces a final React mockup approved by the owner, ready for Liquid migration via the `lusena-draftshop-fragment-parity` skill or direct migration.

## Prerequisites

Before starting, read:
- `memory-bank/doc/patterns/migration-lessons.md` — accumulated CSS, copy, and process gotchas
- `memory-bank/doc/patterns/brand-tokens.md` — design tokens
- `memory-bank/doc/brand/LUSENA_BrandBook_v2.md` — brand voice and positioning

## Workflow

### 1. Setup

1. Start the Vite dev server: `cd lusena-shop && npm run dev -- --port 5173 --host`
2. Create or modify the component in `lusena-shop/src/components/sections/`
3. Add it to the relevant page in `lusena-shop/src/pages/`
4. Verify it renders at `http://localhost:5173/`

### 2. Brand self-check (before every review round)

Verify every value in the component against `brand-tokens.md`:
- **Colors:** only Tailwind config tokens (`bg-brand-bg`, `text-accent-cta`, `text-accent-gold`, `text-primary`, `text-secondary`, `bg-surface-1/2`, `border-neutral-400`)
- **Fonts:** `font-serif` (Source Serif 4) for headings, `font-sans` (Inter) for body
- **Radius:** `rounded-brand` (6px)
- **No raw hex values** outside the token set

### 3. Review panel (5 Sonnet agents in parallel)

Spawn 5 agents with `model: "sonnet"`. Each receives a detailed text description of the section (copy, layout, visual treatment, context in the page flow).

**CRITICAL: Every reviewer prompt MUST include this line:**
> "DO NOT edit, write, or modify any files. Your job is to review and score only. Return your scores and commentary as text."

| # | Role | Evaluates |
|---|------|-----------|
| 1 | Customer: "Szuka jakosci na lata" (34, premium buyer) | Emotional pull, premium trust, skepticism |
| 2 | Customer: "Pielegnacja wlosow/skory" (26, skincare enthusiast) | Clarity, relevance, product desire |
| 3 | Senior UX designer (luxury e-commerce) | Visual hierarchy, whitespace, brand consistency, mobile layout |
| 4 | CRO specialist | Scan patterns, scroll momentum, conversion, information scent |
| 5 | Polish copywriter (premium brands) | Natural Polish, logical coherence, rhythm, brand voice |

### 4. KPI scoring

**Customers score (1-5):**
1. First impression
2. Scroll momentum
3. Premium perception
4. Clarity

**UX designer and CRO specialist:** Same 4 KPIs + specific actionable critique with concrete suggestions.

**Polish copywriter scores (1-5):**
1. Natural Polish
2. Logical coherence
3. Rhythm and flow
4. Brand voice
5. Overall copy quality

### 5. Synthesis (after each round)

Read all 5 responses. Identify:
- Lowest-scoring KPIs across reviewers (fix priority)
- Conflicting feedback (make a judgment call, favor customer reactions over expert theory)
- Specific suggestions worth adopting
- Whether to stop early (all KPIs 4+ across all reviewers AND copy quality 4+)

### 6. Iteration rules

- **Max 5 iterations.** After 5, pick the best version or mix the strongest elements.
- **Copy is in scope** unless the owner says otherwise.
- **All customer-facing text in Polish.**
- **Hyphens only, never em dashes** in all copy.
- **Feature card titles: max 28 characters.**
- After each iteration, present a score comparison table showing improvement/regression across versions.

### 7. Stop conditions

Stop iterating when:
- All 4 KPIs average 4.0+ across all reviewers AND copy quality is 4.0+
- OR 5 iterations reached (pick the best)
- OR the owner says stop

### 8. Owner approval gate

**NEVER modify Shopify theme files (Liquid, CSS, JSON templates) during the design loop.** All work stays in `lusena-shop/`. Present the final mockup URL to the owner and wait for explicit approval before any migration.

### 9. Handoff to migration

After owner approval:
- Summarize what changed (copy, layout, visual treatment)
- List all new schema fields needed
- Estimate CSS complexity (will it need a standalone file?)
- Either invoke `lusena-draftshop-fragment-parity` skill for complex migrations, or do a direct migration for simple sections
- During migration, the `.claude/rules/css-and-assets.md` rule auto-loads and enforces token compliance

## Lessons from previous iterations

Read `memory-bank/doc/patterns/migration-lessons.md` lessons 55-61 for specific gotchas discovered during the first use of this loop (benefit bridge redesign, 2026-03-29):

- **#55** `color-mix()` for opacity variants, never raw RGB
- **#56** Foundation type classes in Liquid, not custom font rules
- **#57** `lusena-icon-circle` + `lusena-icon-*` size classes
- **#58** `div:empty` trap on decorative elements
- **#59** Reviewer agents must never have write access
- **#60** Forward-reference problem with summary text on mobile
- **#61** Mobile cards merging into one visual block
