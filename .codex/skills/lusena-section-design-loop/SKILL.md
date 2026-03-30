---
name: lusena-section-design-loop
description: Autonomous design iteration loop for LUSENA sections. Edits sections directly in the Shopify theme (worktree), pushes to the worktree's dedicated theme, validates with browser capture via lusena-preview-check, then scores with a 5-agent Sonnet review panel (2 customer personas + UX designer + CRO specialist + Polish copywriter). Iterates up to 5 rounds based on KPI scores. No migration step — the section is production-ready in the theme.
---

# LUSENA Section Design Loop

## Overview

Redesign or create a LUSENA section through rapid iteration directly in the Shopify theme. Each iteration is pushed to the worktree's dedicated theme, visually captured via Playwright, and scored by a 5-agent review panel. The loop produces a final, production-ready section — no migration step needed.

## Prerequisites

Before starting, read:
- `memory-bank/doc/patterns/migration-lessons.md` — accumulated CSS, copy, and process gotchas
- `memory-bank/doc/patterns/brand-tokens.md` — design tokens
- `memory-bank/doc/patterns/spacing-system.md` — spacing tiers and content-flow system
- `memory-bank/doc/brand/LUSENA_BrandBook_v2.md` — brand voice and positioning

## Workflow

### 1. Setup

1. Confirm you are in a worktree (`lusena-worktrees/lusena-N/`) on a feature branch
2. Look up your theme ID from `config/worktree-themes.json` (key = your slot number N)
3. Identify the target section file(s) in `sections/` and any related snippets/CSS
4. If creating a new section, use `/lusena-new-section` to scaffold it first
5. Call `learn_shopify_api` with `api: "liquid"` before editing Liquid files

### 2. Implement the initial version

Create or edit the section directly in the Shopify theme:
- Follow LUSENA CSS architecture (`assets/lusena-foundations.css` classes, spacing tiers, brand tokens)
- Use existing snippets (`lusena-icon.liquid`, `lusena-icon-animated.liquid`, `lusena-button-system.liquid`, etc.)
- All customer-facing text in Polish
- Hyphens only (-), never em dashes
- Feature card titles: max 28 characters
- Sentence case everywhere

### 3. Push and capture

1. Push changes to the worktree theme:
   ```bash
   shopify theme push --theme <THEME_ID> --store lusena-dev.myshopify.com --nodelete
   ```

2. Use `/lusena-preview-check` to capture the rendered result at desktop (1440px) and mobile (375px). The subagent should:
   - Take screenshots of the section
   - Measure key spacing values (section padding, content-flow gaps, element spacing)
   - Check computed styles (fonts, colors, backgrounds)
   - Report any visual issues (overflow, misalignment, missing content)

3. Prepare a **section description** for the review panel based on the captured data:
   - Copy/text content (verbatim Polish)
   - Layout description (grid, flex, columns — desktop and mobile)
   - Visual treatment (backgrounds, borders, shadows, icons)
   - Spacing (tier class, content-flow variant, key gaps in px)
   - Context in the page flow (what section comes before/after, what the customer has already seen)
   - Screenshots or key measurements from Playwright

### 4. Brand self-check (before every review round)

Verify every value against `memory-bank/doc/patterns/brand-tokens.md`:
- **Colors:** only LUSENA token values (`--accent-cta`, `--accent-gold`, `--primary`, `--text-secondary`, `--surface-1/2`, `--brand-bg`)
- **Fonts:** `var(--font-heading-family)` (Source Serif 4) for headings, body font (Inter) for text
- **Radius:** `var(--lusena-radius-brand)` (6px)
- **Spacing:** LUSENA spacing tier classes, content-flow classes, gap classes — never hardcoded px values
- **No raw hex values** outside the token set

### 5. Review panel (5 Sonnet agents in parallel)

Spawn 5 agents with `model: "sonnet"`. Each receives the section description from step 3.

**CRITICAL: Every reviewer prompt MUST include this line:**
> "DO NOT edit, write, or modify any files. Your job is to review and score only. Return your scores and commentary as text."

| # | Role | Evaluates |
|---|------|-----------|
| 1 | Customer: "Szuka jakosci na lata" (34, premium buyer) | Emotional pull, premium trust, skepticism |
| 2 | Customer: "Pielegnacja wlosow/skory" (26, skincare enthusiast) | Clarity, relevance, product desire |
| 3 | Senior UX designer (luxury e-commerce) | Visual hierarchy, whitespace, brand consistency, mobile layout |
| 4 | CRO specialist | Scan patterns, scroll momentum, conversion, information scent |
| 5 | Polish copywriter (premium brands) | Natural Polish, logical coherence, rhythm, brand voice |

### 6. KPI scoring

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

### 7. Synthesis (after each round)

Read all 5 responses. Identify:
- Lowest-scoring KPIs across reviewers (fix priority)
- Conflicting feedback (make a judgment call, favor customer reactions over expert theory)
- Specific suggestions worth adopting
- Whether to stop early (all KPIs 4+ across all reviewers AND copy quality 4+)

Present a score comparison table showing improvement/regression across versions.

### 8. Iteration rules

- **Max 5 iterations.** After 5, pick the best version or mix the strongest elements.
- **Copy is in scope** unless the owner says otherwise.
- **All customer-facing text in Polish.**
- **Hyphens only, never em dashes** in all copy.
- **Feature card titles: max 28 characters.**
- After each iteration: edit files -> push -> capture via Playwright -> re-score.

### 9. Stop conditions

Stop iterating when:
- All 4 KPIs average 4.0+ across all reviewers AND copy quality is 4.0+
- OR 5 iterations reached (pick the best)
- OR the owner says stop

### 10. Owner approval gate

After the review panel approves (or max iterations reached), present the final result to the owner:
- Summary of what changed across iterations
- Final scores vs initial scores
- Screenshots at desktop and mobile
- Wait for explicit approval before considering the work done

## Lessons from previous iterations

Read `memory-bank/doc/patterns/migration-lessons.md` lessons 55-61 for specific gotchas discovered during the benefit bridge redesign (2026-03-29):

- **#55** `color-mix()` for opacity variants, never raw RGB
- **#56** Foundation type classes in Liquid, not custom font rules
- **#57** `lusena-icon-circle` + `lusena-icon-*` size classes
- **#58** `div:empty` trap on decorative elements
- **#59** Reviewer agents must never have write access
- **#60** Forward-reference problem with summary text on mobile
- **#61** Mobile cards merging into one visual block
