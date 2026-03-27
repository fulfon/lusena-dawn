# [Fragment Name] Parity Plan (Draft shop -> Shopify theme)

Created: YYYY-MM-DD  
Status: Planned  
Owner: [Name]

## Goal

[Describe the exact fragment to migrate and what "parity" means for this fragment.]

## Scope

### In scope
- [List what must be matched exactly: layout, typography, spacing, states, interactions, breakpoints.]
- [List dynamic behavior that must be preserved.]

### Out of scope
- [List related areas that are explicitly not part of this migration.]
- [List postponed items for later phases.]

## Source of truth (Draft shop)

- [Exact source file path]
- [Exact source file path]
- [Any constants/styles/config files used by the fragment]

## Target in theme (Shopify)

- [Exact target file path]
- [Exact target file path]
- [Template/section/snippet path that is actually rendered]

## Decisions (final) - YYYY-MM-DD

1. [Decision + rationale]
2. [Decision + rationale]
3. [Decision + rationale]

## Open questions / unresolved assumptions

- [Question or assumption]
- [Question or assumption]
- If none: `None.`

## Data sources & content model

- [What comes from Shopify objects (product, cart, section settings, metafields, metaobjects, locales).]
- [Fallback behavior if data is missing.]
- [Translation strategy for user-facing text.]

## Target UX spec (Desktop + Mobile)

### Desktop (~1280px)
- [Expected hierarchy and layout behavior]
- [Key spacing/typography expectations]
- [Interaction expectations]

### Mobile (~390px)
- [Expected hierarchy and layout behavior]
- [Key spacing/typography expectations]
- [Interaction expectations]

### Accessibility
- [Keyboard behavior]
- [Focus behavior]
- [ARIA/semantic requirements]

## Theme capability & conflict audit

| Capability / token | Draft source | Resolved draft value | Exists in theme? | Conflict detected? | Planned implementation path | Target file |
|---|---|---|---|---|---|---|
| [Example: `text-base`] | [file:line] | [16px/24px] | [Yes/No] | [No/Yes] | [Reuse / scoped CSS / utility backfill] | [path] |
| [Example: `h-14`] | [file:line] | [56px] | [Yes/No] | [No/Yes] | [Reuse / scoped CSS / utility backfill] | [path] |
| [Example: icon stroke] | [file:line] | [2] | [Yes/No] | [No/Yes] | [Reuse / component update] | [path] |

Audit rules:
- Resolve merged utility output before porting to Liquid.
- Do not carry conflicting utility classes into the final markup.
- Prefer semantic, scoped fragment CSS over global utility expansion.
- Add utility backfills only when justified and reusable.

### Spacing audit (mandatory — see `lusena-spacing` skill)

Map every draft Tailwind spacing value to a LUSENA spacing class. **Never carry over Tailwind spacing utilities** (`pt-*`, `mb-*`, `space-y-*`, `py-*`, `gap-*`) into Liquid.

| Draft spacing | Draft value | LUSENA class | Notes |
|---|---|---|---|
| Section padding | [e.g. `py-16` = 64px] | [e.g. `lusena-spacing--standard`] | [Tier chosen by section role — see cheat-sheet in spacing skill] |
| Container vertical rhythm | [e.g. `space-y-6` = 24px] | [e.g. `lusena-content-flow`] | [Parent-level class] |
| Kicker → heading gap | [e.g. `space-y-3` = 12px] | `lusena-content-flow--tight` + `lusena-gap-section-intro` | [Standard kicker+heading wrapper] |
| Element gap (CTA isolation) | [e.g. `mt-8` = 32px] | [e.g. `lusena-gap-cta`] | [Individual element] |
| [Add more rows as needed] | | | |

Same-background check (if adjacent sections share `bg-*`):
- Total gap = section A bottom padding + max(gap-same, section B top padding)
- Desktop target: 100–140px
- Mobile target: 64–90px
- If over target: lower the tier, do not hardcode pixels.

## Parity contract table

| Selector / element | Property | Draft value | Theme target value | State | Breakpoint | Tolerance |
|---|---|---|---|---|---|---|
| [e.g. `.fragment__title`] | `font-size` | [20px] | [20px] | default | all | exact |
| [e.g. `.fragment__cta`] | `height` | [56px] | [56px] | default | all | exact |
| [e.g. `.fragment__badge`] | `color` | [rgb(...)] | [rgb(...)] | active | desktop | exact |
| [e.g. `.fragment__row`] | `align-items` | [center] | [center] | default | all | exact |

## State fixture matrix

| State | Required fixture/data | Expected UI/UX |
|---|---|---|
| Empty | [Describe fixture] | [Expected behavior] |
| Populated | [Describe fixture] | [Expected behavior] |
| Active/Selected | [Describe fixture] | [Expected behavior] |
| Hover | [Describe fixture] | [Expected behavior] |
| Disabled | [Describe fixture] | [Expected behavior] |
| Loading | [Describe fixture] | [Expected behavior] |
| Error | [Describe fixture] | [Expected behavior] |
| Success | [Describe fixture] | [Expected behavior] |
| Long content | [Describe fixture] | [Expected behavior] |

## Implementation approach

1. [File-level plan item]
2. [File-level plan item]
3. [File-level plan item]

Implementation rules:
- Modify only the code path used by the live template.
- Keep JS hooks stable (`data-*` selectors).
- Preserve semantic HTML and accessibility behavior.
- Normalize inline numeric styles from Liquid math to CSS-safe format.
- **Spacing: use LUSENA spacing classes exclusively** — section tier for `<section>` padding, `lusena-content-flow*` for container rhythm, `lusena-gap-*` for individual elements. Never hardcode Tailwind spacing from draft source.

## Milestones / deliverables

1. Plan approved by user.
2. Fragment implementation complete in theme files.
3. Shopify `validate_theme` passes on touched files.
4. Parity checks completed for required states and breakpoints.

## Verification checklist (developer pre-check)

### Computed-style checks

Breakpoints:
- Mobile: ~390px
- Desktop: ~1280px

Check for critical selectors:
- font-size
- line-height
- spacing (margin/padding/gap)
- dimensions (width/height/min/max)
- alignment (text-align, align-items, justify-content)
- visibility/display in each state

### Behavior checks

- [Interaction 1]
- [Interaction 2]
- [State transition 1]
- [State transition 2]

## Verification checklist (user visual confirmation)

1. Compare draft vs theme at ~390px and ~1280px.
2. Confirm spacing/typography/colors match.
3. Confirm interactions and state transitions match.
4. Report mismatches with screenshot + viewport.

## Risks / edge cases

- [Risk]
- [Risk]
- [Mitigation]

## Validation and wrap-up

- Shopify Dev MCP `validate_theme`: [pending/pass]
- Files to include in summary:
  - [path]
  - [path]
- Optional after approval:
  - Update `docs/THEME_CHANGES.md`
  - Create commit
