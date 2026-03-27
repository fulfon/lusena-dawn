---
name: lusena-page-audit
description: "Full UI/UX audit of any LUSENA page from the customer's perspective. Analyzes section order, copy, flow, conversion power, legal compliance, and visual rhythm. Rates each section, identifies structural problems, and produces an actionable improvement plan. Use for any page: homepage, PDP, collection, quality, about, returns, cart, search, blog, article, 404, contact."
user_invocable: true
---

# LUSENA Page Audit

## Purpose

Audit any LUSENA page from the customer's emotional journey perspective — what they think, feel, and do as they scroll from top to bottom. The goal is to maximize conversion (purchase, email signup, engagement) while maintaining LUSENA's premium brand feel.

## When to use

- Before launching a page or after a major content/structure change
- When conversion is underperforming and you need to diagnose why
- As part of the polish phase before go-live
- When the user asks to review/audit/improve any page's UI/UX

## Inputs

The user provides:
- **Page name** — which page to audit (e.g., "homepage", "PDP", "quality page")
- **Optional constraints** — things to ignore (placeholder images, dummy products, etc.)
- **Optional focus** — specific concerns (e.g., "is the section order optimal?", "is the copy converting?")

If no page is specified, ask which page to audit.

## Workflow

### Phase 1: Context Gathering (parallel reads)

Read these files to build understanding:

**Always read (brand context):**
1. `memory-bank/activeContext.md` — current project state, known issues
2. `memory-bank/projectbrief.md` — brand identity, positioning, tone, products, target segments
3. `memory-bank/productContext.md` — customer journey, UX goals, page purposes

**Page-specific reads:**
4. The page template JSON (e.g., `templates/index.json`, `templates/product.json`, `templates/page.nasza-jakosc.json`)
5. All section files referenced by the template — use an Explore agent to read ALL section files in full and extract: HTML structure, CSS approach, content/copy, mobile vs desktop behavior, CTAs, and rough edges

**On-demand (read when relevant to the page being audited):**
6. `memory-bank/doc/brand/LUSENA_BrandBook_v2.md` — for page-specific copy guidance, product tiers, hero specs
7. `memory-bank/doc/patterns/spacing-system.md` — for spacing/rhythm evaluation
8. `memory-bank/doc/patterns/brand-tokens.md` — for design tokens and component patterns

### Phase 2: Section-by-Section Analysis

For each section on the page, in order, evaluate:

#### 2a. Customer Perspective (the core of the audit)

Write what the customer **thinks and feels** at this point in the page. Consider:
- What question is the customer asking right now?
- Does this section answer that question?
- What emotion does the customer feel? (trust, curiosity, desire, confusion, boredom?)
- Is the customer closer to buying after reading this section?

#### 2b. Four-Dimension Rating (1-5 scale)

| Dimension | What it measures |
|-----------|-----------------|
| **First Impression** | Does it look/feel premium? Does it create the right emotion? Visual quality. |
| **Content Quality** | Is the copy compelling, clear, benefit-oriented? Is it in Polish? Is it accurate? |
| **Flow & Placement** | Does it belong here in the sequence? Does it build on what came before? |
| **Conversion Power** | Does it move the customer closer to the desired action (buy, sign up, explore)? |

#### 2c. Issues Checklist

For each section, check:

- [ ] **Language** — All customer-facing text in Polish? No English schema defaults leaking?
- [ ] **Social proof** — No fabricated counts, ratings, or reviews? (LUSENA rule: NEVER fabricate)
- [ ] **Legal compliance** — No unsubstantiated quantitative claims? (e.g., "30% trwalszy" without lab data)
- [ ] **CTA quality** — Is the CTA specific, action-oriented, and linked to the right destination?
- [ ] **CTA leaks** — Does the CTA send the customer AWAY from the purchase funnel?
- [ ] **Mobile behavior** — Does the section work well on mobile? Touch targets, readability, layout?
- [ ] **Content completeness** — Any placeholder text, missing images, empty settings?
- [ ] **Hardcoded content** — Are prices, savings, or product data hardcoded in the template JSON instead of pulled from Shopify products/collections? Hardcoded data goes stale silently.
- [ ] **Value anchors** — If the section shows prices, is there a per-night or per-unit anchor to make the price feel small? (Pattern: `price / 365 = X zł/noc`)
- [ ] **CTA competition** — Is this CTA competing with an adjacent section's CTA? Two CTAs back-to-back dilute both. Each CTA should feel like a clear, singular moment.
- [ ] **Consistency** — Does the section use LUSENA foundations classes, follow brand typography/spacing?
- [ ] **Accessibility** — Proper heading hierarchy? Color contrast? Focus states? aria attributes?
- [ ] **Animations** — Uses Dawn scroll-trigger pattern? Respects prefers-reduced-motion?

### Phase 3: Structural Analysis

After analyzing all sections individually, evaluate the page as a whole:

#### 3a. Customer Journey Flow

Map the page to the AIDA framework:
- **Attention** — Does the opening grab the customer?
- **Interest** — Does education/proof build genuine interest?
- **Desire** — Do products/testimonials/bundles create desire?
- **Action** — Is there a clear, compelling call to action?

Identify flow breaks: places where the customer's momentum is interrupted, where they're sent away, or where the sequence doesn't build logically.

#### 3b. Proof-to-Product Ratio

Count:
- **Proof sections** (trust bars, heritage, quality evidence, testimonials, FAQ)
- **Product sections** (bestsellers, bundles, product grids, cross-sells)
- **Action sections** (CTAs, newsletter, buy boxes)

Flag imbalances: too much convincing before showing products, too many products without proof, missing final CTA.

#### 3c. Visual Rhythm

Map the background color of every section by reading the class attribute on the `<section>` tag:
```
Section 1: hero        → (image/overlay)
Section 2: trust bar   → surface-1  (#FFFFFF white)
Section 3: problem/sol → brand-bg   (#F7F5F2 warm porcelain)
Section 4: bestsellers → surface-1  (#FFFFFF white)
Section 5: testimonials→ surface-2  (#F0EEEB cream)
...
```

**Hard rule: every adjacent section transition must have a visible color change.** Two same-background sections in a row create a dead visual gap (their combined padding stacks: 96px + 96px = 192px of same-color space with no boundary). This looks like a single bloated section, not two distinct ones.

Available backgrounds: `surface-1` (white), `brand-bg` (warm porcelain), `surface-2` (cream), `bg-dark` (dark). Plan the sequence so colors alternate — no two adjacent sections share the same background class.

Flag issues: same-color adjacent sections, monotonous sequences (3+ similar tones in a row), background choices that don't match section purpose (e.g., conversion CTA on the same background as adjacent content sections instead of standing out).

#### 3d. Repetition Audit

Check if the same claims/information appear in multiple sections. Deliberate reinforcement (trust bar → PDP proof chips) is fine. Exact duplication (trust bar item = heritage tile with same text) is wasteful.

#### 3e. Content Integrity

Check every section for content that is hardcoded in template JSON instead of pulled from Shopify data:
- **Prices** — Are prices typed as text strings ("269 zł") instead of pulled from product objects (`{{ product.price | money }}`)?  Hardcoded prices go stale when real prices change and create maintenance debt.
- **Product names/descriptions** — Are product details typed manually instead of coming from the product catalog?
- **Savings/discount claims** — Are "Oszczędzasz 29 zł (10%)" style claims computed or hardcoded? Hardcoded savings become wrong when prices change.

Flag every instance. Recommendation: either pull from real Shopify data, or leave the field blank until real data is available.

#### 3f. CTA Competition

List all CTAs on the page in order and evaluate whether they compete or complement:
```
1. Hero CTA: "Zacznij swoją rutynę" → /collections/all  (conversion)
2. Problem/Solution CTA: "Sprawdź dowody jakości →" → /quality  (education)
3. Bestsellers: "Zobacz całą kolekcję" → /collections/all  (browse)
4. Final CTA: "Zacznij swoją rutynę" → /collections/all  (conversion)
```

**Rules:**
- Two conversion CTAs back-to-back dilute both. Separate them with content.
- Each CTA should have a distinct purpose in the funnel (educate → browse → buy → subscribe).
- The final CTA on the page should be the strongest — it catches anyone who scrolled all the way down.
- Newsletter/email capture duplicated in both a section AND the footer is redundant. Pick one location.

#### 3g. Brandbook Compliance

Cross-reference the page structure and copy against `memory-bank/doc/brand/LUSENA_BrandBook_v2.md`:
- Does the page follow the brandbook's recommended section structure?
- Are the right products featured in the right order?
- Does the copy follow tone of voice rules (no exclamation marks in headings, sentence case, no medical claims)?
- Are value anchors present where the brandbook calls for them?

### Phase 4: Output Format

Present the audit in this structure:

```
# [Page Name] Audit — Customer Journey Analysis

## Rating Scale
(explain the 4 dimensions)

## Section 1: [Name]
**"[Actual heading text]"**
| Dimension | Score | Notes |
Customer thinks: "..."
Issues: (bulleted list)
Score: X.X / 5

## Section 2: [Name]
(repeat)

...

## Overall Score: X.X / 5

## The [N] Biggest Problems (ordered by conversion impact)
### 1. [Problem title]
(explanation + recommended fix)

## Recommended Section Order
(current vs proposed, if reordering is needed)

## Additional Concerns
| Issue | Impact | Effort |
(table of smaller issues)

## What Would Make This a 10/10?
(numbered list of improvements)

## Implementation Priority
| Priority | Change | Effort | Impact |
(table ordered by impact/effort ratio)
```

### Phase 5: Discussion & Alignment

After presenting the audit:
- Wait for the user's feedback on each section
- Discuss alternatives for contested decisions
- Align on final changes before creating an implementation plan
- Address user's constraints (placeholder images, missing products, etc.)

Do NOT start implementing changes until the user explicitly approves the plan.

### Phase 6: Implementation (only after user approval)

Once aligned:
1. Make content/order changes to the template JSON
2. Make any section file changes (if structural changes needed)
3. Create new sections/CSS if needed (follow compiled_assets truncation guard)
4. Update memory bank with completed work and new to-do items
5. Offer visual verification with Playwright

## Key Principles

1. **Customer-first, always.** Every recommendation must be justified by what the customer thinks/feels/does. Never optimize for developer convenience or technical elegance at the expense of UX.

2. **Benefit over feature.** Customers care about smooth skin and shiny hair, not "22 momme density." Features belong in deep-proof sections; benefits belong in hero and CTA sections.

3. **Proof near products.** Social proof (testimonials, reviews, certifications) is most powerful when placed immediately after product displays. Don't front-load all proof before showing any products.

4. **Every section earns its place.** If a section doesn't move the customer closer to the desired action, it should be moved, merged, or removed.

5. **No fabrication.** LUSENA has a hard rule: never fabricate social proof (customer counts, ratings, reviews). If real data doesn't exist yet, use neutral alternatives or placeholder copy that's clearly marked.

6. **Legal safety.** All quantitative claims must be substantiated. "30% more durable" requires lab testing. "Denser and more durable" (qualitative) is safe. When in doubt, go qualitative.

7. **Polish-first.** All customer-facing copy must be in Polish. Schema defaults may be in English, but the actual content in the template JSON must be Polish. Flag any English leaking through.

8. **Premium feel = restraint.** Premium isn't about adding more — it's about generous spacing, clean typography, and letting content breathe. Over-decorated pages feel cheap.

## Target Segments (for customer perspective analysis)

When writing "Customer thinks:" sections, consider LUSENA's four target segments:

1. **"Seeks quality for years"** (25-45) — values durability, material quality, wants proof
2. **"Perfect gift"** (22-55) — wants impressive presentation, easy buying, gift-ready packaging
3. **"Hair/skin care"** (18-40) — wants visible results, reduced friction, before/after proof
4. **"Minimalist aesthete"** (20-50) — values refined design, no clutter, timeless look

The audit should consider which segments each section serves and whether high-priority segments are well-covered.
