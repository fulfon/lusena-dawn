---
name: lusena-preview-check
description: "Delegates browser testing to a subagent to save main conversation context. Use when you need to verify rendering, measure spacing/styles, test interactions, take screenshots, or debug CSS on the LUSENA dev store preview. The subagent handles all Playwright mechanics and returns concise findings. Keywords: preview, browser, check, verify, screenshot, measure, render, visual, test, debug CSS, layout, interaction, navigate."
user_invocable: true
---

# LUSENA Preview Check

## Purpose

Delegate browser testing to a **general-purpose subagent** instead of running Playwright in the main conversation. All browser interaction noise (snapshots, accessibility trees, navigation steps) stays in the subagent's context. The main conversation receives only concise, structured findings.

**Context savings:** A typical browser check generates 200-500 lines of snapshot/interaction data. With this skill, the main conversation receives ~10-20 lines of findings instead.

## When to use

- Verifying that a code change renders correctly
- Measuring CSS values (spacing, colors, fonts, dimensions)
- Testing interactions (clicks, form fills, cart operations)
- Taking reference screenshots for the owner
- Debugging layout or CSS issues
- Any time you need to see or interact with the live dev store

## Pre-flight checklist

Before dispatching the subagent, YOU (the main Claude) must:

### 1. Push your changes (worktrees only)

The subagent tests what is on the Shopify server, not local files. If you edited any theme files, push first:

```bash
shopify theme push --theme <THEME_ID> --store lusena-dev.myshopify.com --nodelete
```

### 2. Determine your preview URL

**Worktree:** Read your slot number from your cwd (e.g., `lusena-worktrees/lusena-1` = slot 1). Look up the theme ID from `config/worktree-themes.json`. The preview URL is:
```
https://lusena-dev.myshopify.com{path}?preview_theme_id=<THEME_ID>
```

**Main repo:** Use theme ID `144618684603`:
```
https://lusena-dev.myshopify.com{path}?preview_theme_id=144618684603
```

### 3. Pick a unique session name

Choose a descriptive session name for the `-s=` flag based on what you are checking. Examples: `check-pdp-spacing`, `verify-hero-mobile`, `test-cart-add`. Never use generic names like `test`, `check`, or `audit` - another concurrent instance may pick the same name.

## How to dispatch

Use the **Agent tool** with these parameters:

| Parameter | Value |
|-----------|-------|
| `subagent_type` | `general-purpose` |
| `model` | `sonnet` |
| `description` | Short label, e.g. "Check homepage hero spacing" |
| `run_in_background` | `true` if you have other work to do; `false` if you need results before continuing |

Fill in the subagent prompt template below, replacing all `{PLACEHOLDER}` values.

## Subagent prompt template

Copy the template below, fill in the placeholders, and pass it as the `prompt` parameter to the Agent tool.

---

BEGIN TEMPLATE

```
You are a browser testing agent for the LUSENA Shopify dev store (a premium Polish silk e-commerce site).

## Your environment

- Preview URL base: https://lusena-dev.myshopify.com
- Theme ID: {THEME_ID}
- Append `?preview_theme_id={THEME_ID}` to every URL
- Store password: paufro
- Browser session name: {SESSION_NAME} (use `-s={SESSION_NAME}` in EVERY playwright-cli command)
- Working directory: {CWD}

## URL reference

### Products
| Name | Path |
|------|------|
| Pillowcase (Poszewka) | /products/poszewka-jedwabna |
| Bonnet (Czepek) | /products/silk-bonnet |
| Scrunchie | /products/silk-scrunchie |
| Eye mask (Maska 3D) | /products/jedwabna-maska-3d |
| Curlers (Walek) | /products/heatless-curlers |
| Bundle: Nocna Rutyna | /products/nocna-rutyna |
| Bundle: Piekny Sen | /products/piekny-sen |
| Bundle: Scrunchie Trio | /products/scrunchie-trio |

### Pages
| Name | Path |
|------|------|
| Homepage | / |
| Collection | /collections/all |
| Cart | /cart |
| Quality (Nasza jakosc) | /pages/nasza-jakosc |
| About (O nas) | /pages/o-nas |
| Returns (Zwroty) | /pages/zwroty |
| Contact | /pages/kontakt |
| Search | /search |
| Blog | /blogs/blog |

## Rules

### 1. Use playwright-cli via Bash only

Run all browser commands through `playwright-cli` using the Bash tool. NEVER use Playwright MCP tools directly (browser_navigate, browser_snapshot, browser_evaluate, etc.).

### 2. Always include the session flag

Every single playwright-cli command must include `-s={SESSION_NAME}`. No exceptions.

```bash
# Correct:
playwright-cli -s={SESSION_NAME} open https://lusena-dev.myshopify.com/?preview_theme_id={THEME_ID}
playwright-cli -s={SESSION_NAME} resize 1440 900
playwright-cli -s={SESSION_NAME} eval "document.title"

# Wrong (no session flag):
playwright-cli open https://...
```

### 3. Password page handling

On first navigation, you will land on a password page. Handle it:

1. Open the URL
2. Take a snapshot to find the password input field
3. Fill the password field with: paufro
4. Press Enter or click the submit button
5. Wait for redirect to the actual page
6. Take a snapshot to confirm you are on the correct page
7. Then proceed with your task

### 4. Measure with code, not screenshots

For ANY quantitative check (spacing, colors, fonts, dimensions, visibility), use `playwright-cli eval` with JavaScript. This gives exact, deterministic values.

**Spacing and dimensions:**
```bash
playwright-cli -s={SESSION_NAME} eval "JSON.stringify(document.querySelector('.lusena-hero').getBoundingClientRect())"
```

**Gap between two elements:**
```bash
playwright-cli -s={SESSION_NAME} eval "(() => { const a = document.querySelector('.section-a').getBoundingClientRect(); const b = document.querySelector('.section-b').getBoundingClientRect(); return JSON.stringify({ gap: b.top - a.bottom, aBottom: a.bottom, bTop: b.top }) })()"
```

**Computed CSS values (padding, margin, color, font):**
```bash
playwright-cli -s={SESSION_NAME} eval "((el) => { const s = getComputedStyle(el); return JSON.stringify({ padding: s.padding, margin: s.margin, color: s.color, backgroundColor: s.backgroundColor, fontSize: s.fontSize, fontWeight: s.fontWeight, lineHeight: s.lineHeight, gap: s.gap }) })(document.querySelector('.your-selector'))"
```

**Element visibility:**
```bash
playwright-cli -s={SESSION_NAME} eval "((el) => { const r = el.getBoundingClientRect(); return { visible: r.width > 0 && r.height > 0, width: r.width, height: r.height } })(document.querySelector('.your-selector'))"
```

**Element count:**
```bash
playwright-cli -s={SESSION_NAME} eval "document.querySelectorAll('.product-card').length"
```

**Only take screenshots when:**
- Explicitly asked for a visual reference
- Checking general layout sanity ("does this look broken?")
- The owner wants to see something

**Never use screenshots to measure** pixel values, colors, or font sizes.

### 5. Viewport presets

When the task involves measurement, resize BEFORE navigating (some CSS evaluates on page load):

| Preset | Command |
|--------|---------|
| Mobile | `playwright-cli -s={SESSION_NAME} resize 375 812` |
| Tablet | `playwright-cli -s={SESSION_NAME} resize 768 1024` |
| Desktop | `playwright-cli -s={SESSION_NAME} resize 1440 900` |

**Important:** Resize first, then navigate (or reload). Do NOT just resize after the page has loaded - you may get hybrid measurements from CSS that evaluated at the old viewport width.

**Which viewports to test:**
- Measurement tasks (spacing, sizing): Mobile + Desktop. Add Tablet only if the task mentions breakpoint behavior.
- Visual sanity checks: Desktop, unless specified otherwise.
- Functional tests (clicks, forms): Desktop, unless specified otherwise.
- Responsive layout checks: All three (Mobile + Tablet + Desktop).

### 6. Close the session when done

Always close the browser session at the end:
```bash
playwright-cli -s={SESSION_NAME} close
```

## Output format

Return your findings in this structured format:

```
## Preview Check Results

**Task:** [what was checked]
**URL:** [full URL tested]
**Viewport(s):** [sizes tested]

### Findings

[For measurements - use a table:]
| Element | Property | Mobile (375) | Desktop (1440) | Notes |
|---------|----------|--------------|----------------|-------|
| .lusena-hero | padding-top | 32px | 64px | Matches spacing tier |
| .lusena-hero | padding-bottom | 32px | 64px | Matches spacing tier |

[For visual checks - use a list:]
- Hero image loads correctly, fills viewport width
- CTA button is visible and properly styled
- No layout overflow on mobile

[For interaction tests - use numbered steps:]
1. Clicked "Dodaj do koszyka" -> cart drawer opened with product
2. Changed quantity to 2 -> price updated to 318,00 zl
3. Clicked "Przejdz do kasy" -> redirected to checkout

### Issues found
- [issue description, if any]
- None [if no issues]

### Screenshots
- [file path]: [description] (only if screenshots were taken)
```

## Your task

{TASK_DESCRIPTION}
```

END TEMPLATE

---

## Viewport reference

The LUSENA theme uses two CSS breakpoints:

| Breakpoint | Direction | Role |
|------------|-----------|------|
| **768px** | `min-width` | Canonical mobile/desktop flip (foundations, spacing, typography) |
| **1024px** | `min-width` | Secondary, large-desktop 3-column grids (6 sections only) |

The three presets (375 / 768 / 1440) test below, at, and above both breakpoints respectively.

## Batching guidance

- **Same page, multiple checks** -> one subagent (e.g., "check hero spacing + CTA color on homepage")
- **Different pages** -> separate subagents (e.g., homepage layout + cart interaction = two agents)
- **Same page, multiple viewports** -> one subagent (it resizes between checks)

## Example dispatches

### Example 1: Measurement task

You just changed hero section padding and pushed to Shopify. You want to verify.

```
Agent tool call:
  subagent_type: general-purpose
  model: sonnet
  description: "Check homepage hero spacing"
  prompt: |
    You are a browser testing agent for the LUSENA Shopify dev store...
    [full template with filled values]
    ...
    Your task:
    Navigate to the homepage. Measure the padding-top and padding-bottom
    of the .lusena-hero section at mobile (375px) and desktop (1440px).
    Expected values from the spacing tier system:
    - Mobile: 80px top, 80px bottom (hero tier)
    - Desktop: 128px top, 128px bottom (hero tier)
    Report PASS/FAIL for each measurement.
```

### Example 2: Visual sanity check

You changed the product card layout and want a general look.

```
Agent tool call:
  subagent_type: general-purpose
  model: sonnet
  description: "Visual check collection page"
  prompt: |
    You are a browser testing agent for the LUSENA Shopify dev store...
    [full template with filled values]
    ...
    Your task:
    Navigate to /collections/all at desktop (1440px).
    Take a screenshot of the full page.
    Check that product cards display in a grid, images load,
    and prices are visible. Report any visual issues.
```

### Example 3: Interaction test

You want to test the add-to-cart flow on a product page.

```
Agent tool call:
  subagent_type: general-purpose
  model: sonnet
  description: "Test ATC flow on pillowcase PDP"
  prompt: |
    You are a browser testing agent for the LUSENA Shopify dev store...
    [full template with filled values]
    ...
    Your task:
    Navigate to the pillowcase PDP (/products/poszewka-jedwabna) at desktop.
    1. Select the color variant "Szampanski"
    2. Click the "Dodaj do koszyka" button
    3. Verify the cart drawer opens and shows the correct product
    4. Report what happened at each step
```
