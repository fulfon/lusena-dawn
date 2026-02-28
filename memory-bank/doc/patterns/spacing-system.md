# LUSENA Spacing System (Quick Reference)

> Full specification: `.claude/skills/lusena-spacing/SKILL.md`
> CSS source of truth: `assets/lusena-spacing.css`

## Tier selection cheat-sheet

| Section role | Recommended tier |
|-------------|-----------------|
| Hero / banner | `lusena-spacing--hero` |
| Trust bar / utility bar | `lusena-spacing--compact` |
| Content / info sections | `lusena-spacing--standard` |
| CTA / conversion sections | `lusena-spacing--spacious` |
| Full-width media | `lusena-spacing--full-bleed` |

## Content-flow selection

| Class | Gap (mob/desk) | When to use |
|-------|---------------|-------------|
| `lusena-content-flow--tight` | 12/16px | Kicker + heading pairs, section intros |
| `lusena-content-flow` | 20/24px | Standard containers, body text flow |
| `lusena-content-flow--relaxed` | 28/32px | Hero text columns, editorial blocks |

## Gap classes

| Class | Gap (mob/desk) | Usage |
|-------|---------------|-------|
| `lusena-gap-kicker` | 12/12px | Below kicker text |
| `lusena-gap-heading` | 20/24px | Below headings |
| `lusena-gap-body` | 20/24px | Below body text |
| `lusena-gap-cta` | 28/36px | Below CTA buttons |
| `lusena-gap-cta-top` | 28/36px | Above CTA buttons |
| `lusena-gap-section-intro` | 32/48px | Below section intro block |
| `lusena-gap-subsection` | 48/80px | Between major content breaks |

## Key rules (abbreviated)

1. **Always use LUSENA classes** — never hardcode Tailwind spacing (`py-8`, `mb-6`, etc.)
2. **When in doubt, go one tier up** — premium feel means generous spacing
3. **Prefer content-flow on parent** over individual gap classes on children
4. **Kicker+heading pattern:** always wrap in `<div class="lusena-content-flow--tight lusena-gap-section-intro">`
5. **Same-bg section gap** is a floor (max formula), not additive — detector handles automatically
6. **Snug-top modifier** (`lusena-spacing--snug-top`): use when hero has same bg as header
7. **CTA visibility:** use `lusena-gap-cta-top` for conditionally visible CTA elements
8. **FAQ/accordion first-item:** first-item spacing fix removes extra top padding in stacked groups
