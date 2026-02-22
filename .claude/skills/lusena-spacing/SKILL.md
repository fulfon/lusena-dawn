---
name: lusena-spacing
description: Use when adjusting spacing in the LUSENA Shopify theme — both spacing between elements inside containers (content-flow) and spacing between sections (tier padding). Invoke for any spacing review, fix, or new section setup on any page. Keywords: spacing, padding, gap, margin, content-flow, tier, section padding, breathing room, vertical rhythm.
---

# LUSENA spacing — page review & adjustment skill

## Goal

Review any page in the LUSENA theme and ensure its spacing — both **between sections** and **inside containers** — delivers the best possible UI/UX for a premium e-commerce store. Every spacing decision must serve two purposes:

1. **Clean, aesthetic, premium feel** — generous breathing room, consistent rhythm across all pages
2. **Maximize conversion** — guide the customer's eye naturally toward trust signals and CTAs

## Core principle: use LUSENA spacing classes, never hardcode

All spacing MUST use the LUSENA spacing system classes defined in `assets/lusena-spacing.css`. **Never hardcode** spacing with Tailwind utility classes (`pt-4`, `mb-8`, `space-y-6`, `mt-12`, etc.) or raw CSS pixel values.

If the existing classes don't cover a spacing need you've identified during evaluation, **stop and ask the user for permission** to create a new class in `assets/lusena-spacing.css`. Explain:
- What spacing value you need and why
- What you'd name the class
- Which elements would use it

The user is open to new classes — just ask first.

---

## Architecture

All CSS lives in **`assets/lusena-spacing.css`** (standalone asset file loaded via `<link>` in `layout/theme.liquid`).

> **Never put spacing CSS in `{% stylesheet %}` blocks.** Shopify merges all `{% stylesheet %}` blocks into `compiled_assets/styles.css` which has a ~73KB size limit. Rules near the end get silently truncated.

### Key files

| File | Purpose |
|---|---|
| `assets/lusena-spacing.css` | **Source of truth** — all tokens, tiers, gap utilities, content-flow utilities |
| `snippets/lusena-section-gap-detector.liquid` | JS: detects adjacent same-background sections, adds `lusena-section-gap-same` class |
| `docs/theme-brandbook-uiux.md` (§3.3, §5.4) | Design documentation |

---

## Available spacing classes

### Section padding tiers (between sections)

One tier class per `<section>` element. Controls top/bottom padding.

| Class | Mobile | Desktop | When to use |
|---|---|---|---|
| `lusena-spacing--full-bleed` | 0 | 0 | Edge-to-edge images, video, maps |
| `lusena-spacing--compact` | 32px | 48px | Utility sections (announcement bars, thin banners) |
| `lusena-spacing--standard` | 40px | 64px | Informational / editorial content (FAQ, comparison tables, auxiliary info) |
| `lusena-spacing--spacious` | 48px | 80px | Trust-building, CTA, and primary showcase sections |
| `lusena-spacing--hero` | 64px | 96px | Hero / above-the-fold sections only |

#### Same-background section gap (`lusena-section-gap-same`)

Applied automatically by `lusena-section-gap-detector.liquid` when adjacent sections share the same `bg-*` color.

**Formula:** `padding-top: max(var(--lusena-section-gap-same), var(--lusena-tier-pt))`

This is a **floor**, not an additive bonus. It guarantees at least 40px (desktop) / 32px (mobile) of top padding on the second section, but does not inflate sections whose tier padding already exceeds that threshold. See Rule 12 for rationale.

#### Snug-top modifier

| Class | Mobile | Desktop | When to use |
|---|---|---|---|
| `lusena-spacing--snug-top` | 32px | 48px | Hero sections whose `bg-*` matches the site header (both `bg-brand-bg`). Reduces (not removes) top padding — uses compact-tier values for a "minimal entry, generous exit" rhythm. |

Combine with any tier class: `class="lusena-spacing--hero lusena-spacing--snug-top"`

**Why 32 / 48px (compact-tier values):**
- Reuses an existing spacing decision — keeps the scale coherent instead of inventing arbitrary values.
- 32px mobile ≈ 2× the header's own internal vertical spacing feel.
- 48px desktop gives enough room that the kicker reads as "section start" rather than "header continuation."
- Bottom padding stays at the section's own tier (e.g. hero = 64/96px).

**Design decision log:** Initially we tried `0px` (flush-top), but that made the kicker collide with the nav — no breathing room at all. Full hero-tier padding (64/96px) created a visible void since there's no color boundary. Compact-tier values (32/48px) are the sweet spot: clear separation without emptiness.

**When NOT to use:** If the hero has a different background than the header (e.g. `bg-white`, full-bleed image, gradient), the color boundary already provides visual separation — keep the normal tier padding.

**Currently applied to:** `lusena-quality-hero.liquid`, `lusena-returns-hero.liquid`.

**Note:** The section-gap-detector (`lusena-section-gap-detector.liquid`) only works between `<section>` elements — it cannot detect header→section same-bg. This modifier must be applied manually in Liquid.

### Content-flow utilities (inside containers)

One class on a parent container `<div>`. Sets uniform `margin-top` on all direct children except the first.

| Class | Mobile | Desktop | When to use |
|---|---|---|---|
| `lusena-content-flow--tight` | 12px | 16px | Section intros (kicker + heading pairs, heading + subheading pairs) |
| `lusena-content-flow` | 20px | 24px | **Default** — most containers |
| `lusena-content-flow--relaxed` | 28px | 32px | Visually heavy children (large images, card grids) |

#### Standard kicker+heading pattern

Every kicker → heading (and heading → subheading) pair **must** be wrapped in a `<div class="lusena-content-flow--tight lusena-gap-section-intro">`. This is the only sanctioned pattern:

```liquid
<div class="lusena-content-flow--tight lusena-gap-section-intro">
  <span class="text-secondary text-sm tracking-widest uppercase font-semibold">
    {{ kicker }}
  </span>
  <h2 class="text-3xl md:text-4xl font-serif text-primary">
    {{ heading }}
  </h2>
</div>
```

**Never** use individual `lusena-gap-kicker` / `lusena-gap-heading` on the kicker or heading elements directly — see Rule 9.

### Semantic gap classes (individual elements)

Apply `margin-bottom` to a specific element. Use when content-flow on the parent isn't appropriate.

> **Inline element warning:** `margin-top` / `margin-bottom` are **silently ignored** on inline elements (`<span>`, `<a>`, `<em>`, etc.). If you must use a gap class on a `<span>`, it **must** also have `display: block` (the CSS for `lusena-gap-kicker` includes this). But the preferred approach is to avoid individual gap classes on inline elements entirely — use a `lusena-content-flow--tight` wrapper instead (see standard kicker+heading pattern above).

| Class | Mobile | Desktop | Use case |
|---|---|---|---|
| `lusena-gap-kicker` | 12px | 12px | **Deprecated for kicker+heading pairs** — use `lusena-content-flow--tight` wrapper instead. Only for rare standalone kicker use outside a heading group. Has `display: block` built in. |
| `lusena-gap-heading` | 20px | 24px | Below a standalone heading when no content-flow parent is possible |
| `lusena-gap-body` | 20px | 24px | Below body text |
| `lusena-gap-cta` | 28px | 36px | Below content that precedes a CTA |
| `lusena-gap-section-intro` | 32px | 48px | Below a section intro, before the main content |

---

## How to evaluate a page

### Step 1: Read the page sections from the live server

```powershell
$html = (Invoke-WebRequest -Uri "http://127.0.0.1:9292/pages/PAGE" -UseBasicParsing).Content

# Section tiers
[regex]::Matches($html, 'class="[^"]*lusena-spacing--[^"]*"') | ForEach-Object { $_.Value }

# Content-flow containers
[regex]::Matches($html, 'class="[^"]*lusena-content-flow[^"]*"') | ForEach-Object { $_.Value }

# Hardcoded Tailwind spacing (should be zero — flag any you find)
[regex]::Matches($html, '\b(pt|pb|mt|mb|space-y)-(2|3|4|5|6|8|10|12|16)\b') | ForEach-Object { $_.Value } | Sort-Object -Unique
```

### Step 2: Read each section file

Read the Liquid source of every `lusena-*` section on the page. For each one, check:

1. **Section tier class** — does it match the section's conversion role?
2. **Container content-flow** — is it using a LUSENA content-flow class, or hardcoded Tailwind `space-y-*`?
3. **Individual element gaps** — are there hardcoded `mb-*`, `mt-*`, `pt-*` that should be LUSENA gap classes instead?

### Step 3: Evaluate for premium feel and conversion (desktop AND mobile)

For each section, answer:

**Section padding (the space around the section):**
- What is this section's job? Hero → `hero`. Trust/CTA → `spacious`. Info → `standard`. Utility → `compact`.
- Does the padding feel generous and premium, or cramped?
- **CTA/conversion sections must always be `spacious` or `hero`** — the final CTA is the climax, never `compact`.
- Does this section's padding feel consistent with other pages' equivalent sections?

**Content-flow (spacing between elements inside):**
- Is there a kicker+heading pair? → `lusena-content-flow--tight`
- Is it body content (heading → paragraphs → link)? → `lusena-content-flow`
- Are there visually heavy blocks? → consider `lusena-content-flow--relaxed`
- Does the internal rhythm let the customer scan comfortably, or does it feel rushed/disconnected?

**Cross-page consistency:**
- Does the same type of section (hero, FAQ, CTA) use the same tier on every page?
- Do section intros (kicker+heading) use the same content-flow variant everywhere?

### Step 4: Fix and verify

1. Replace any hardcoded Tailwind spacing with the appropriate LUSENA class
2. If no existing class fits, **ask the user** before creating a new one in `assets/lusena-spacing.css`
3. Verify on `http://127.0.0.1:9292/` — check both desktop and mobile viewports

---

## Rules

1. **Always use LUSENA spacing classes.** Never hardcode `pt-4`, `mb-8`, `space-y-6`, `mt-12`, or any raw Tailwind spacing utility for vertical rhythm between content blocks or sections.

2. **When in doubt, go one tier up.** Cramped sections feel cheap. Generous padding signals quality.

3. **Prefer content-flow on the parent** over individual gap classes on children. Only use `lusena-gap-*` when the parent can't have content-flow (e.g. a grid with its own `gap-*`).

4. **Never mix content-flow with individual gap classes on the same container.** Content-flow sets `margin-top` on all children — adding `lusena-gap-heading` (`margin-bottom`) on a child creates double spacing.

5. **Standard content-flow (24px) is the default for 90% of containers.** Don't overuse `--relaxed` — it makes text feel disconnected.

6. **Consistency across pages is mandatory.** If hero sections use `lusena-spacing--hero` on one page, they must use it on all pages. If section intros use `lusena-content-flow--tight`, they must do so everywhere.

7. **If existing classes don't fit → ask, don't hack.** Tell the user what value you need, propose a class name, and wait for approval before adding it to `assets/lusena-spacing.css`.

8. **Never add spacing CSS to `{% stylesheet %}` blocks.** Always edit `assets/lusena-spacing.css` directly.

9. **Kicker+heading = `lusena-content-flow--tight` wrapper, always.** Never apply `lusena-gap-kicker` or `lusena-gap-heading` directly to kicker/heading elements in a kicker→heading pair. Wrap both in `<div class="lusena-content-flow--tight lusena-gap-section-intro">` instead. This avoids the inline-element margin bug (`<span>` ignores `margin-bottom`) and ensures all section intros are architecturally identical across all pages.

10. **Snug-top for same-bg heroes.** When a hero section shares the same background color as the site header (typically `bg-brand-bg`), add `lusena-spacing--snug-top` alongside the tier class to reduce top padding to compact-tier values (32/48px). Full hero-tier padding creates a visible void (no color boundary), while zero padding makes the kicker collide with the nav. Compact-tier values are the sweet spot. See the "Snug-top modifier" table above.

11. **Never apply `margin-bottom` / `margin-top` gap classes to inline elements** (`<span>`, `<a>`, `<em>`) without ensuring `display: block`. Browsers silently ignore vertical margins on inline elements — the spacing will look correct in some conditions but fail in others. Prefer wrapping in a content-flow container instead.

12. **Same-background adjacent sections: gap-same is a floor, not a bonus.** The `lusena-section-gap-same` class (applied by the JS gap-detector) uses `max(gap-same, tier-pt)` — it ensures *at least* `--lusena-section-gap-same` (40px desktop / 32px mobile) of top padding, but never inflates sections that already carry generous tier padding. This prevents an empty void between same-bg sections whose own tiers already provide sufficient separation.

    **How it works:** `padding-top: max(var(--lusena-section-gap-same), var(--lusena-tier-pt))`. For `full-bleed` (0px tier) → gap-same kicks in (40px). For `standard` (64px tier) → tier already exceeds gap-same, so no change.

    **Why not additive:** An earlier version used `calc(gap-same + tier-pt)`, which inflated every same-bg pair: e.g. `spacious` (80px) + 40px = 120px bottom + 120px top = 240px void — far too much for a premium store. Premium spacing should feel *intentional*, not *vacant*.

13. **Choose the right tier for the section's role, not its perceived importance.** A comparison table or editorial block is `standard` — it presents information, not a hero moment. Reserve `spacious` for primary trust-building / CTA sections and `hero` for above-the-fold entries only. When adjacent same-bg sections feel too far apart, first check whether a section is *over-tiered* before touching the gap-same system.

    **Tier cheat-sheet by section type:**

    | Section type | Correct tier | Examples |
    |---|---|---|
    | Hero / above-the-fold | `hero` | `lusena-quality-hero`, `lusena-returns-hero` |
    | Trust-building / CTA | `spacious` | `lusena-heritage`, `lusena-returns-final-cta`, `lusena-returns-steps` |
    | Informational / editorial | `standard` | `lusena-returns-editorial`, `lusena-returns-faq`, `lusena-faq` |
    | Utility / thin | `compact` | `lusena-trust-bar`, `lusena-pdp-details` |
    | Edge-to-edge media | `full-bleed` | Full-bleed images, video, maps |

14. **Audit same-bg pairs before shipping.** When creating or reordering sections on a page, check whether any adjacent pair shares the same `bg-*` class. If they do, calculate the total visual gap:

    `total = section_A bottom padding + max(gap-same, section_B top padding)`

    Target ranges for same-bg pairs:
    - **Desktop:** 100–140px total (below 100 feels cramped; above 150 feels vacant)
    - **Mobile:** 64–90px total

    If the total exceeds these ranges, the likely fix is to *lower the tier* on one or both sections — not to tweak the gap-same token.
