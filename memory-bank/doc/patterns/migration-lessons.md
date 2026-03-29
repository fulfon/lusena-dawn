# CSS Foundations — Architecture Lessons

*Distilled from the Tailwind → foundations migration (completed 2026-03-04). Reference when adding new sections or modifying existing ones.*

## 1. CSS cascade: section stylesheets load BEFORE foundations

Shopify compiles `{% stylesheet %}` blocks into `compiled_assets/styles.css`, injected via `{{ content_for_header }}` (line 43 of `layout/theme.liquid`). The `lusena-foundations.css` loads at line 300 — **after** section stylesheets.

**Consequence:** At equal specificity (single class), foundations always wins over section CSS.

**Rule:** When a section needs to override a foundations class (e.g., white text on a dark hero overriding `.lusena-type-hero { color: var(--lusena-text-1) }`), bump the section selector to **0-2-0** by adding the parent class:

```css
/* BAD — 0-1-0, loses to foundations */
.lusena-hero__heading { color: #fff; }

/* GOOD — 0-2-0, beats foundations */
.lusena-hero .lusena-hero__heading { color: #fff; }
```

## 2. Dawn base.css resets you need to watch for

Dawn's `base.css` applies styles to bare HTML elements that can conflict with foundations components:

- `blockquote` — gets `border-left: 0.2rem solid; padding-left: 1rem` (caused double border on testimonials)
- `ul/ol` — default list styles and padding
- `button` — various resets
- `a` — color and text-decoration

**Rule:** When using semantic HTML in foundations components, check if Dawn's base.css applies conflicting styles. Reset them in foundations (not in the section), so the fix applies everywhere.

## 3. Reusable layout belongs in foundations, not section CSS

If you find yourself writing layout CSS that could apply to multiple sections, put it in foundations. Section stylesheets should only contain:

- Section-specific positioning (hero overlay, content positioning)
- Section-specific animations (hero fade-up, FAQ accordion states)
- Color/style variants unique to that section (white hero buttons, gold bullet colors)
- Section chrome (full-width borders on trust bar section element)

**Anti-pattern we fixed:** Trust bar layout was defined in section overrides fighting foundations. Once we moved the grid/flex layout into foundations, the component became instantly reusable on any page.

## 4. Don't fight foundations from section CSS — update foundations instead

If a section needs to override multiple foundations properties, that's a signal the foundations component definition is wrong. Fix it at the source.

**Anti-pattern we fixed:** Section had `ul.lusena-trust-bar { padding: 0; border: none; }` overriding foundations — then we had to re-add spacing elsewhere. Instead, we updated the foundations component to not have borders (moved to section level) and include the list reset.

## 5. Buttons: always use `var(--lusena-btn-radius)`

All section buttons must use `border-radius: var(--lusena-btn-radius)` — never hardcode `0` or `0.6rem`. This gives a single control point. Currently set to `0.6rem` (warm premium feel).

## 6. Borders that should span full viewport

If a border needs to go edge-to-edge, put it on the `<section>` element (or a data-attribute selector like `[data-lusena-trust-bar]`), NOT on an element inside `.lusena-container`. The container constrains width to `max-width: 120rem` with inline padding.

## 7. Verify with Playwright after every section migration

Don't guess at layout — screenshot both desktop (1280x800) and mobile (375x812) after changes. CSS cascade bugs are invisible in code review.

Specific things to check:
- Text color on dark backgrounds (cascade override issue)
- Border doubling from Dawn base.css on semantic elements
- Spacing above/below sections (padding stacking)
- Mobile single-column alignment (centered vs left-aligned)

## 8. Full page migration workflow (single pass)

The homepage used multiple phases because we were building the system. Now that foundations is stable, migrate each page in a **single pass**:

### Phase A: Plan
1. Read the page template JSON to identify all sections
2. Read each section's Liquid + `{% stylesheet %}` block
3. Map every Tailwind class → foundations equivalent (or section CSS)
4. Identify bugs (e.g., duplicate `class` attributes, invalid HTML)
5. Check if any section is already shared/migrated (e.g., `lusena-trust-bar`)
6. Note which section CSS needs 0-2-0 specificity for foundation overrides

### Phase B: Implement all sections
7. Replace Tailwind classes with foundations classes in HTML
8. Write section-specific CSS in `{% stylesheet %}` (only what foundations doesn't cover)
9. Replace hardcoded values with tokens (`var(--lusena-space-*)`, `var(--lusena-btn-radius)`, etc.)
10. Fix any HTML bugs found in planning
11. Update template JSON if new settings/sections were added

### Phase C: Validate
12. Run `validate_theme` on all changed files
13. Verify zero Tailwind classes remain (grep for `text-`, `bg-`, `font-`, `grid-`, `gap-`, `p-`, `m-`, `h-[`, `w-`, `flex`, `items-`, `justify-`, `rounded-`, `leading-`, `tracking-`, `uppercase`, `relative`, `absolute`, `inset-`, `overflow-`, `container`, `max-w-`)
14. Run `shopify theme check` — no new warnings beyond known baseline

### Phase D: Visual verification + UX audit (Playwright CLI)
15. Desktop (1280x800) — screenshot each section, check layout, spacing, typography
16. Mobile (375x812) — screenshot each section, check stacking, readability
17. Measure alignment programmatically if anything looks off (bounding box checks)

### Phase E: UX audit — conversion-focused proposals
After migration is visually correct, audit the page for **conversion optimization**:

18. **Dead ends:** Does every section have a path forward? Hero needs a CTA, page needs a final CTA
19. **Text readability:** Is body text large enough? Is contrast sufficient on colored backgrounds? Compare foundations type class sizes against original Tailwind sizes — foundations may be smaller
20. **Visual balance:** Are grids with incomplete rows centered? Are elements properly aligned?
21. **Mobile proportions:** Are fixed-height elements (images, containers) reasonable on small screens?
22. **Customer journey:** Does the page flow build toward a purchase decision? Brand story → proof → values → CTA
23. **Reusable sections:** Can new sections (like final CTA) be generic for reuse on other pages?

Propose changes, get approval, implement, and re-verify.

## 9. Trust bar is fully reusable now

The trust bar section can be dropped into any page template via the theme editor. Layout lives in foundations (2x2 grid mobile, flex space-evenly desktop). No additional CSS needed.

## 10. Spacing tier reference for section wrappers

| Use case | Class | Mobile | Desktop |
|----------|-------|--------|---------|
| Edge-to-edge media | `lusena-spacing--full-bleed` | 0 | 0 |
| Compact utility strips | No class + custom padding | varies | varies |
| Informational content | `lusena-spacing--standard` | 48px | 64px |
| Trust-building, CTAs | `lusena-spacing--spacious` | 64px | 96px |
| Hero sections | `lusena-spacing--hero` | 80px | 128px |

---

## Lessons from About page migration (2026-03-01)

## 11. Kicker pattern: size depends on context

`.lusena-kicker` is a **modifier** (uppercase, letter-spacing, weight) with NO font-size. Pair it with a type class to control size:

| Context | Classes | Result |
|---------|---------|--------|
| Hero section (big heading) | `lusena-kicker` alone | Inherits ~1.6rem — proportional to hero heading |
| Standard section (h1/h2 heading) | `lusena-type-caption lusena-kicker` | 1.2rem — proportional to smaller heading |

**Rule:** Always pair kickers with `lusena-type-caption` except in hero sections where the larger inherited size is intentional.

## 12. `margin-inline: auto` needs 0-2-0 specificity

`.lusena-type-body` in foundations sets `margin: 0`, which kills `margin-inline: auto` on child elements at equal specificity. Any section element that needs centering via `margin-inline: auto` must use 0-2-0:

```css
/* BAD — margin: 0 from .lusena-type-body wins */
.lusena-about-story__body { margin-inline: auto; }

/* GOOD — 0-2-0 beats foundations */
.lusena-about-story .lusena-about-story__body { margin-inline: auto; }
```

## 13. Check type class sizes against original Tailwind

Foundations type classes may be **smaller** than the Tailwind equivalents they replace. Always compare:

| Foundations class | Size (mobile → desktop) | Common Tailwind equivalent |
|-------------------|------------------------|---------------------------|
| `lusena-type-hero` | 4.8/5.6 → 6.4/7.2rem | `text-5xl md:text-7xl` (~4.8 → 7.2rem) ≈ match |
| `lusena-type-h1` | 3.2/4.0 → 4.0/4.8rem | `text-3xl md:text-5xl` (~3.0 → 4.8rem) ≈ match |
| `lusena-type-h2` | 2.0/2.4 → 2.4/3.2rem | `text-3xl md:text-4xl` (~3.0 → 3.6rem) **smaller** |
| `lusena-type-body` | 1.6/2.4rem | `text-lg` (~1.8rem) close |
| `lusena-type-caption` | 1.2/1.6rem | `text-sm` (~1.4rem) **smaller** |

If the size difference hurts readability, consider using the next size up (e.g., `lusena-type-h1` instead of `lusena-type-h2` for a section heading, `lusena-type-body` instead of `lusena-type-caption` for card text).

## 14. Flexbox for grids with incomplete rows, CSS Grid otherwise

- **CSS Grid** — clean and simple when all rows are complete (e.g., 6 items in a 3-col grid)
- **Flexbox with `justify-content: center`** — when the last row may have fewer items and they should be centered (e.g., 5 items in a 3-col grid → bottom 2 centered)

```css
/* Flexbox approach with token-based sizing */
.my-grid { display: flex; flex-wrap: wrap; gap: var(--lusena-space-4); justify-content: center; }
.my-grid-item { width: 100%; }
@media (min-width: 768px) { .my-grid-item { flex: 0 0 calc(50% - var(--lusena-space-4) / 2); } }
@media (min-width: 1024px) { .my-grid-item { flex: 0 0 calc(33.333% - var(--lusena-space-4) * 2 / 3); } }
```

## 15. Duplicate `class` attributes — common Liquid bug

Watch for this pattern where animation classes are added as a second `class` attribute:
```html
<!-- BUG: second class attribute is silently ignored by browsers -->
<div class="my-class" {% if settings.animations %}class="scroll-trigger"{% endif %}>

<!-- FIX: merge into single class attribute -->
<div class="my-class{% if settings.animations %} scroll-trigger{% endif %}">
```

## 16. Generic reusable sections > page-specific copies

When creating a section that could apply to multiple pages, make it generic:
- `lusena-final-cta.liquid` (reusable) instead of `lusena-quality-final-cta.liquid` + `lusena-returns-final-cta.liquid` + `lusena-about-final-cta.liquid`
- Page-specific versions (`lusena-quality-final-cta`, `lusena-returns-final-cta`) were replaced and deleted in Phase 3 (2026-03-04)

## 17. Template JSON must be updated alongside section changes

When adding new schema settings or new sections, the template JSON needs corresponding updates:
- New settings with defaults work without JSON changes (schema defaults apply)
- New settings **without** defaults (like `url` type) need explicit values in the JSON
- New sections must be added to both the `sections` object and the `order` array

## 18. Story/narrative text on cream backgrounds: use `--lusena-text-1`

`lusena-type-body` defaults to `--lusena-text-2` (secondary/muted). On cream backgrounds (`lusena-bg-brand`), this creates low contrast for the most important brand narrative. Override to `--lusena-text-1` in section CSS for readability:

```css
.lusena-about-story .lusena-type-body { color: var(--lusena-text-1); }
```

Apply this pattern to any section where body text carries the core brand message and sits on a non-white background.

---

## Lessons from Quality page migration (2026-03-02)

## 19. ALL section color overrides need 0-2-0 — no exceptions

Lesson #1 says "when a section needs to override a foundations class", but in practice it's easy to forget when the override seems unrelated. **Every `color:` declaration in section CSS must use 0-2-0**, because foundations sets colors on `.lusena-type-caption`, `.lusena-type-body`, etc.

Bug found: The about-values kicker used 0-1-0 (`.lusena-about-values__kicker { color: var(--lusena-accent-2) }`), which was overridden by foundations' `.lusena-type-caption { color: var(--lusena-text-2) }` at equal specificity. Result: kicker appeared gray instead of gold.

**Rule:** When writing ANY property in section CSS that competes with a foundations type class (`color`, `font-size`, `font-weight`, `margin`, etc.), always use the parent+child pattern:

```css
/* ALWAYS do this in section CSS */
.lusena-my-section .lusena-my-section__element { color: var(--lusena-accent-2); }
```

## 20. Shared components belong in foundations, not section CSS

If two or more sections need the same UI pattern (truth table, comparison grid, card layout), extract it into `lusena-foundations.css` as a shared component. Section `{% stylesheet %}` blocks should contain only section-specific overrides.

**Bug found:** The quality page comparison table had ~100 lines of section CSS for a table layout. The PDP had a separate ~200 lines for a similar truth table. Both were inconsistent (different spacing, colors, mobile behavior). Extracting `.lusena-truth-table` into foundations eliminated all duplication and guaranteed visual consistency.

**Checklist before writing section CSS:**
1. Could another section need this pattern? → foundations
2. Is this a layout primitive (grid, table, card)? → foundations
3. Is this only about color/position unique to this section? → section CSS

## 21. Section transitions: adjacent same-background sections need contrast

When two adjacent sections share the same background color, they visually merge into one blob. Always audit the section order in the template JSON and ensure visual breaks:

- **Alternate backgrounds:** cream (`lusena-bg-brand`) / white (`lusena-bg-surface-1`)
- **Hairline border:** `border-top: 1px solid var(--lusena-color-n200)` on the section element
- **Spacing tier change:** different `lusena-spacing--*` tier

**Bug found:** Quality page "Pochodzenie" (white) → "Dlaczego 22 momme?" (white) had no visual transition. Fixed by changing Momme section to `lusena-bg-brand` (cream).

## 22. Avoid duplicate CTAs in the page flow

Audit the full page flow for redundant calls-to-action. If a CTA section (e.g., `lusena-final-cta`) follows shortly after an inline CTA (e.g., button under a comparison table), the repetition feels pushy and dilutes urgency.

**Bug found:** Quality page had "Zobacz kolekcję" under the comparison table AND again in the final CTA section two sections later. Removed the table CTA.

**Rule:** One primary CTA per page "chapter" (roughly 3–4 sections). The final CTA section at the bottom is the page closer — don't compete with it.

## 23. Card grids need explicit equal-height setup

CSS Grid's `align-items: stretch` is not the default for all grid contexts, and cards with varying content lengths will have uneven heights unless explicitly handled:

```css
.my-grid { display: grid; align-items: stretch; }
.my-card { height: 100%; display: flex; flex-direction: column; }
```

**Bug found:** QC cards had uneven heights on desktop because `align-items: stretch` was missing from the grid and `height: 100%` was missing from the cards.

## 24. Spacing tiers: trust `--standard` as the default, use `--spacious` sparingly

`lusena-spacing--spacious` adds significantly more whitespace (64px mobile / 96px desktop vs 48px/64px for standard). Only use it for sections that genuinely need breathing room (hero, final CTA). For most content sections — including tables, FAQs, and info blocks — `lusena-spacing--standard` is correct.

**Bug found:** Comparison table used `--spacious`, creating too much gap between the table and the FAQ section below it. Changed to `--standard`.

## 25. Hero CTA hierarchy: primary action = purchase path

On every page, the hero's primary CTA should lead toward purchase (collection link, product page). Secondary actions (PDF downloads, certificate links, anchor scrolls) should be visually demoted to text links or outline buttons.

**Bug found:** Quality page hero had "Pobierz certyfikat OEKO-TEX (PDF)" as a prominent button alongside "Zobacz kolekcję". The PDF download is a supporting proof point, not the primary conversion action. Demoted to a text link.

## 26. Truth table column headers: 1.4rem minimum for readability

Uppercase tracked labels at 1.2rem (12px) are too small for table column headers, especially next to 1.7rem serif metric names. The hierarchy gap is too large and the headers feel fragile.

**Standard:** All `.lusena-truth-table` column headers and card labels use `1.4rem` with `letter-spacing: 0.08em` and `text-transform: uppercase`.

## 27. Responsive truth table: table desktop, cards mobile

The `.lusena-truth-table` component in foundations implements a proven responsive pattern:

| Breakpoint | Layout | Component |
|---|---|---|
| < 768px | 1-column card stack | `.lusena-truth-table__cards` |
| 768–1023px | 2-column card grid | `.lusena-truth-table__cards` (2-col) |
| ≥ 1024px | Semantic `<table>` | `.lusena-truth-table__table-wrap` |

Key features:
- LUSENA column gets subtle teal wash via `color-mix(in srgb, var(--lusena-accent-cta) 3%, transparent)`
- Serif metric names (`--lusena-font-brand`, 1.7rem, weight 600)
- Teal check icons for LUSENA, muted gray X for others
- Mobile cards repeat the teal highlight on the LUSENA line
- `<table>` uses `border-collapse: separate` for rounded corners + subtle `box-shadow`

Sections using this component need zero section CSS — only the outer `<section>` wrapper (background, spacing) and intro heading are section-controlled.

---

## Lessons from Phase 3 — Tailwind removal (2026-03-05)

## 28. Removing Tailwind exposes missing preflight resets

Tailwind's preflight CSS includes many element resets that are invisible until removed. When deleting a Tailwind file, add equivalent resets to foundations:

| Element | What Tailwind reset | What breaks without it |
|---------|-------------------|----------------------|
| `button` | `padding: 0; background: transparent; border: 0; cursor: pointer; font: inherit; color: inherit;` | Accordion triggers get 6px browser padding, buttons look wrong |
| `a` | `color: inherit; text-decoration: inherit;` | All link-based buttons show underlines |
| `img, video` | `max-width: 100%; height: auto; display: block;` | Images overflow containers, break layouts |

**Rule:** When removing any CSS framework, audit its preflight/reset file and port any resets your theme depends on.

## 29. SVG must NOT get `max-width: 100%` globally

Unlike `<img>`, SVGs used as icons typically have no intrinsic width/height — they rely on explicit sizing from their containing class. Adding `max-width: 100%` to SVGs causes them to expand and fill their flex/grid container.

**Rule:** Only apply `max-width: 100%` to `img` and `video`. SVG dimensions should always be set explicitly by the component class (e.g., `.lusena-trust-bar__icon-svg { width: 2rem; height: 2rem; }`).

## 30. compiled_assets truncation is silent and cumulative

Shopify compiles ALL `{% stylesheet %}` blocks into one `compiled_assets/styles.css` file. The file **silently truncates at ~73KB** — no error, no warning, CSS just stops mid-rule. The sections whose CSS gets cut off depend on compilation order, which you don't control.

**Symptoms:** Random sections lose styling (often the ones added most recently or alphabetically last). The bug is intermittent-looking because different pages may compile in different orders.

**Fix:** Extract large `{% stylesheet %}` blocks (>50 lines) into standalone `assets/lusena-*.css` files. After adding any section CSS, check compiled_assets size in DevTools Network tab — must stay under 55KB.

**Full pattern and extraction steps:** `memory-bank/doc/patterns/css-architecture.md`

## 31. Browser interactions: `/playwright-cli` skill is the only tool

This is a **general project rule** (documented in `CLAUDE.md` under "Browser Interactions"), not migration-specific. But it's critical during migration Phase D (visual verification): always use the `/playwright-cli` skill for ALL browser tasks. Never use Playwright MCP tools directly. **Always use `-s=<name>`** (e.g., `-s=migrate`) to isolate your browser from other concurrent Claude Code instances.

---

## Lessons from Cart page migration (2026-03-05)

## 32. `:has()` selector and Shopify section wrappers

Shopify wraps every section in a `<div class="shopify-section">` (or `<section class="shopify-section">`). This means sections are NOT direct children of `<main>`. When using `:has()` to style `<main>` based on a section's web component:

```css
/* BAD — won't match, cart-items is inside .shopify-section, not direct child */
main:has(> cart-items) { ... }

/* GOOD — descendant selector matches through wrapper */
main:has(cart-items) { ... }
```

When the `.shopify-section` wrapper also needs styling (e.g., `flex: 1`), target it explicitly:
```css
main:has(cart-items) > .shopify-section:has(cart-items) {
  flex: 1; display: flex; flex-direction: column;
}
```

## 33. Viewport-fill with `min-height: 100dvh` — `<main>` padding matters

Dawn's `<main>` has `padding-top` matching the sticky header height (76px). Since padding is INSIDE the element, `min-height: 100dvh` is correct (not `calc(100dvh - header)`). The padding pushes content down within the 100dvh box.

## 34. Flex chain for height propagation — every wrapper needs flex

To push a child element (like upsell) to the bottom of a flex container that fills the viewport, EVERY intermediate wrapper element must participate in the flex chain: `display: flex; flex-direction: column; flex: 1`. Missing one link breaks the chain and the child won't reach the bottom.

Typical chain for cart: `main` → `.shopify-section` → `cart-items` → `.lusena-container` → `form` → `#main-cart-items` → `.js-contents` → upsell (`margin-top: auto`).

## 35. CSS source order: mobile overrides must come AFTER base rules

When two selectors have the same specificity, the one appearing later in the stylesheet wins. A mobile `@media` override placed early in the file will be overridden by a base rule that appears later:

```css
/* BUG: this mobile override... */
@media (max-width: 767px) { .my-class { border: none; } }  /* line 220 */

/* ...is overridden by this base rule at same specificity */
.my-class { border: 1px solid gray; }  /* line 310 */
```

**Rule:** Place mobile overrides AFTER the base rules they override, or increase specificity.

## 36. Desktop vs mobile flex strategies for viewport-fill

Different screens need different approaches:
- **Mobile:** Flex chain with `flex: 1` on cart-items section, `margin-top: auto` on upsell — fills viewport, upsell sticks to footer
- **Desktop:** NO flex-grow on cart-items — content stays compact at top, remaining space is empty background. Site footer pushed below fold by `<main>` min-height.

Making the flex chain global causes a gap between items and footer on desktop (content stretches to fill). Making it mobile-only keeps desktop compact.

## 37. Redundant borders at section boundaries

When a section has a full-bleed tinted background (like the upsell zone), the background edge already provides visual separation from the next section. Adding a `border-top` on the next section creates a double-separator effect with mismatched widths (full-bleed bg vs container-width border).

**Rule:** Audit border/line sources at section transitions. If a tinted background already creates the break, remove redundant borders on adjacent sections.

---

## Lessons from Batch 4 — Customer account pages (2026-03-05)

## 38. Verify Shopify account system before migrating customer pages

Shopify deprecated legacy/classic customer accounts in **February 2026**. Stores created after this date (or stores that never explicitly opted into legacy) use the **new customer accounts** system, which is entirely hosted on `shopify.com/authentication/...`. This means:

- **Liquid templates for `customers/*` are completely bypassed** — login, register, activate, reset password, account, order, addresses
- **`shopify theme dev` cannot test customer pages** — authentication redirects to Shopify's hosted login (GitHub issue #1055, open since 2023)
- **Customization options:** Only Shopify admin branding settings (logo, colors, typography) or building a custom Shopify app with customer account UI extensions (JavaScript/React + Polaris)

**Rule:** Before starting ANY customer page migration, check which account system the store uses: Shopify admin → Settings → Customer accounts. If "New customer accounts" is active, skip ALL `customers/*` template migrations — they are dead code.

## 39. Research platform constraints before building

The Batch 4 migration built 3 full sections (~1100 lines), 5 icons, 8 CSS rules, and a pagination snippet before discovering the work was unusable. This cost could have been avoided by testing login access early or researching Shopify's account system deprecation timeline.

**Rule:** For any page that depends on a platform-managed flow (authentication, checkout, payments), verify the store's configuration first. Test the actual user flow before writing code.

---

## Lessons from Batch 5 — Search page (2026-03-05)

## 40. Viewport-fill: use `min-height: 100dvh` on `main`, not `flex: 1` on section

When a page has little content (e.g., empty search state), using `flex: 1` on the section makes it stretch and the footer fills the remaining space — ugly on mobile. Better pattern: `min-height: 100dvh` on `main` pushes the footer below the fold, while the section stays its natural size. Combine with `padding-top: 18vh` on the initial state for upper-third positioning (like Google search), leaving room for keyboard + predictive dropdown on mobile.

## 41. Dawn's `main-search.js` scrollIntoView must be disabled

Dawn's `MainSearch` class calls `this.scrollIntoView({ behavior: 'smooth' })` on input focus for screens < 750px. This causes jarring scroll when the field is already visible. Fix: override `scrollIntoView` on the `<main-search>` element instance (not the method — the bound listener can't be removed). Pattern: `customElements.whenDefined('main-search').then(() => { el.scrollIntoView = () => {}; });`

## 42. Polish quotation marks in JSON locale files need Unicode escapes

Polish uses `„..."` (U+201E opening, U+201D closing) for quotation marks. In JSON string values, these MUST be actual Unicode characters, not ASCII `"` (U+0022) which breaks the JSON string delimiter. When editing `en.default.json`, never use ASCII quotes for inner Polish quotes — use real Unicode characters `„` and `"`. If an edit tool converts them to ASCII, the JSON will be invalid.

## 43. Translating a PL-first store: override `en.default.json`, not `pl.json`

If the store's default locale is English but all customer-facing text should be Polish, translate strings directly in `en.default.json` (the active locale). The `pl.json` file exists but is only used if Polish is set as a published language in Shopify admin. Overriding `en.default.json` is simpler and works immediately without admin changes.

---

## Lessons from Batch 6 — Blog + Article (2026-03-06)

## 44. Polish dates: `time_tag` outputs English when store locale is English

Shopify's `time_tag` filter uses the store's primary locale for formatting. If the store is set to English (even though customer-facing text is Polish), dates render as "March 5, 2026". Fix: create `snippets/lusena-date-pl.liquid` that manually maps month numbers to Polish genitive forms (stycznia, lutego, marca...) using a `case` statement. Usage: `{% render 'lusena-date-pl', date: article.published_at %}`. The `{date}` param type is not valid in Shopify's `{% doc %}` block — use `{string}` instead.

## 45. Back-to-back conversion sections create decision fatigue

On the article page, having newsletter signup + shop CTA as two separate sections felt like a "pushy exit gauntlet" and broke the calm editorial feel. Solution: merge into one section by adding optional `secondary_label`/`secondary_link` fields to the newsletter. This respects brandbook's "max 2 CTAs per section" (1 primary form + 1 text link) and keeps newsletter as the terminal section (matching homepage pattern). Default empty = no change on other pages.

## 46. Blog empty state needs viewport fill (same pattern as search)

An empty blog page with just "no articles" text makes the footer dominate the viewport. Apply the same `min-height: 100dvh` pattern used on search: `main:has(.lusena-blog) { display: flex; flex-direction: column; min-height: 100dvh; }` + flex children. Combine with a rich empty state (icon + heading + subtext + CTA button) to fill the space intentionally.

---

## Lessons from Batch 2 — System pages: 404, generic page, contact (2026-03-06)

## 47. Animations: always use `animate--slide-in`, wrap form content

Use `scroll-trigger animate--slide-in` for ALL content blocks — headings, text, forms. Do NOT use `animate--fade-in` (too subtle, inconsistent with other pages).

When adding animation to a `{% form %}` tag, put the class on the form element itself (via a Liquid variable), not on a wrapper div inside it. A wrapper div becomes the form's only flex child, breaking `gap` between form fields:

```liquid
{%- liquid
  assign form_class = 'lusena-form'
  if settings.animations_reveal_on_scroll
    assign form_class = form_class | append: ' scroll-trigger animate--slide-in'
  endif
-%}
{%- form 'contact', id: 'ContactForm', class: form_class -%}
```

## 48. Viewport-fill: grow the PAGE section, not the reusable section

When a page uses viewport-fill (`min-height: 100dvh` on `main`) and has a reusable section at the bottom (e.g., newsletter), the extra space must be absorbed by the page-specific section — not the reusable one. Stretching a shared section changes its height across pages, breaking visual consistency.

Target the page section's `.shopify-section` wrapper specifically:
```css
main:has(.lusena-contact-form) > .shopify-section:has(.lusena-contact-form) {
  flex: 1;
  display: flex;
  flex-direction: column;
}
.lusena-contact-form { flex: 1; }
```

---

## Lessons from Homepage UX Audit + Cross-site Polish (2026-03-08 / 2026-03-09)

## 49. Em-dash to hyphen standardization in JSON content

Polish typographic convention uses em-dashes (—) for parenthetical dashes. However, Shopify JSON template values render the em-dash literally, creating inconsistency when some content uses hyphens and some uses em-dashes. Standardize all template JSON content to use a regular hyphen (-) surrounded by spaces.

**Scope:** All template JSON files (`index.json`, `product.json`, `page.nasza-jakosc.json`, `page.o-nas.json`, `page.zwroty.json`). Search pattern: ` — ` (space-emdash-space) → ` - `.

## 50. FAQ JS: use `var`/`function` for broadest compatibility

Shopify's `{% javascript %}` blocks compile into a shared bundle where arrow functions and `const`/`let` can conflict with older browsers or strict concatenation. When JS is moved from `{% javascript %}` to inline `<script>`, use `var` and `function` declarations for maximum compatibility.

**Applied:** `lusena-faq.liquid` JS rewrite (arrow functions → function expressions, `const`/`let` → `var`, optional chaining removed).

## 51. Icon system: prefer lusena-icon over inline SVG and emoji

When sections use inline SVG for check/x/social icons or emoji for decorative icons, centralize them in `snippets/lusena-icon.liquid`. Benefits: single source of truth, consistent sizing/stroke, easy theme-wide icon updates. Use a `known_icons` allowlist with emoji fallback for merchant-configured icon fields.

**Applied:** `lusena-pdp-truth-table` (circle-check, circle-x), `lusena-quality-qc` (icon name with fallback), `lusena-footer` (instagram, facebook).

## 52. Trust bar copy: sentence case and canonical across pages

Trust bar blocks appear on homepage, about, and quality pages. When updating copy (like fixing "30%"), update ALL instances in their respective template JSON files. Use sentence case for subtitles ("Gęstszy i trwalszy" not "30% gęstszy splot").

## 53. Returns deep-link: click `<summary>`, not set `.open` attribute

Setting `details.open = true` programmatically does not trigger the transition animation and can leave the `<details>` element in an inconsistent state. Instead, dispatch a click event on the `<summary>` element, which triggers the normal open/close flow including animations.

**Applied:** `lusena-pdp-scripts.liquid` returns link handler.

## 54. Dawn's `div:empty { display: none }` hides empty placeholder divs

Dawn's `base.css` (line 473) has a global rule: `a:empty, ul:empty, dl:empty, div:empty, section:empty, article:empty, p:empty, h1:empty, ... { display: none; }`. This silently hides ANY empty div — including image placeholder containers that intentionally have no `<img>` child (e.g., when a product has no featured image).

**Specificity trap:** `div:empty` has specificity `(0,1,1)` — one pseudo-class + one element. A single class selector like `.my-img-wrapper` has only `(0,1,0)` and LOSES. Adding `display: block` to the class rule doesn't work.

**Fix:** Use `.my-img-wrapper:empty { display: block; }` — specificity `(0,2,0)` beats `div:empty` `(0,1,1)`.

**Applied:** `.lusena-upsell-card__bn-add-img:empty`, `.lusena-upsell-card__xs-img:empty` in both `cart-drawer.liquid` and `lusena-cart-items.liquid`.

---

## Lessons from Benefit Bridge redesign (2026-03-29)

## 55. Never use raw RGB/hex for opacity variants — use `color-mix()`

When you need a token color at partial opacity, never hardcode the RGB channel values. Use `color-mix(in srgb, var(--token) N%, transparent)`. If the token changes in foundations, `color-mix()` updates automatically; raw RGB values become stale.

```css
/* BAD — raw RGB, breaks if token changes */
background: rgb(14 94 90 / 0.06);

/* GOOD — references token, auto-updates */
background: color-mix(in srgb, var(--lusena-accent-cta) 6%, transparent);
```

**Applied:** `assets/lusena-benefit-bridge.css` — all 6 opacity values converted.

## 56. Always use foundation type classes in Liquid, not custom font rules in CSS

Typography should use `lusena-type-h1`, `lusena-type-h2`, `lusena-type-body`, `lusena-type-caption` in the Liquid markup. Section CSS should only contain margin/spacing overrides on those classes, never redefine font-size/line-height/font-family.

**Bug found:** Benefit bridge CSS had 40 lines of custom typography (font-size, line-height, font-family, color for titles, body, featured variants) that duplicated what foundations already provides.

## 57. Always use `lusena-icon-circle` + `lusena-icon-*` size classes

Foundations provides `lusena-icon-circle` (4.8rem, border, transparent bg) and size classes `lusena-icon-xs` through `lusena-icon-xl`. Section CSS should only override bg/border/color on the circle, never define custom icon dimensions.

**Bug found:** Benefit bridge had custom icon circle (4rem/4.4rem) and custom icon SVG sizes (1.8rem/2rem) that diverged from the standard. Fixed to use `lusena-icon-circle` + `lusena-icon-lg`.

## 58. `div:empty` trap applies to decorative accent bars too

Empty divs used as decorative elements (accent bars, dividers) are caught by Dawn's `div:empty { display: none }` at specificity (0,1,1). A single-class selector like `.lusena-section__accent-bar { display: block }` at (0,1,0) silently loses.

**Fix:** Use 0-2-0: `.lusena-section .lusena-section__accent-bar { display: block; }`

**Applied:** `lusena-benefit-bridge__accent-bar` was invisible on desktop until specificity was bumped.

## 59. Reviewer agents must never have write access

When using AI agents as reviewers (personas, UX designer, CRO specialist, copywriter), their prompts must explicitly state "DO NOT edit, write, or modify any files. Your job is to review and score only." Without this restriction, general-purpose agents may read the actual codebase and implement changes directly — bypassing the review loop and modifying production files without approval.

**Bug found:** CRO specialist agent in the benefit bridge iteration loop read the Shopify Liquid files and implemented changes directly, modifying 17 theme files without authorization.

## 60. Transition line placement: forward-reference problem on mobile

A summary phrase that references "all items" (e.g., "Wszystkie trzy - bez żadnej zmiany w rutynie") cannot appear inside the first card on mobile, because the reader hasn't seen the other cards yet. On desktop where all cards are visible simultaneously, it works. Solution: place at section level below all cards on both viewports, or use responsive show/hide if desktop placement differs from mobile.

## 61. Mobile card treatment: avoid merging cards into one visual block

When stacking cards vertically on mobile with no gap (gap-0), white card backgrounds merge into one continuous block. Fix: either remove the white background on mobile (`background: transparent`) so cards blend into the page background, or add gap between cards. The teal left-border + bottom divider pattern provides structure without the white block effect.
