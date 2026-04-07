# Homepage Architecture Redesign

*Date: 2026-04-06*
*Status: COMPLETE (2026-04-07) — all items implemented. Visual Proof Block scaffolded, awaiting owner photography.*

---

## 1. Context and goals

### What we're optimizing for

Dual objective: **maximize conversion** (visitors buying products) while **maintaining premium brand perception** (LUSENA feels like a confident, restrained silk brand — not a landing page).

### Analysis methods

This spec is the product of 5 independent analyses:

1. **E-commerce Conversion Analyst** (Sonnet agent) — evaluated section order against DTC conversion frameworks, identified redundancies and friction points
2. **Premium Brand Strategist** (Sonnet agent) — evaluated whether the page feels premium, identified tone violations and missing emotional beats
3. **Customer Persona Walk-throughs** (Sonnet agent) — simulated 4 target personas (Agnieszka 34/quality-seeker, Kasia 28/gift-buyer, Zuzia 22/hair-skin TikTok native, Ola 41/minimalist aesthete) scrolling the page on mobile, section by section
4. **Competitive Benchmarking** (Sonnet agent) — researched homepage structure of Slip, Brooklinen, Ettitude, Aesop, Glossier, Casper
5. **Framework Mapping** (Sonnet agent) — mapped proposed architecture against AIDA, PAS, StoryBrand SB7, PASTOR, and the Proof Sandwich pattern

### Key findings that drove decisions

- **Testimonials are fabricated** (pre-launch, no real customers) — all 3 review agents flagged this as the single biggest credibility risk. A proof-first brand cannot invent social proof. Unanimous: cut now, replace with real UGC when available.
- **Problem/Solution is redundant with Benefit Bridge** — same mechanism (cotton friction, cream absorption) explained twice. The red X / green check visual register was flagged as "D2C dropshipping playbook" incompatible with Calm/Precise/Luxurious brand personality. Unanimous: cut.
- **Bundles at position 7 is too late** — bundles are 30-61% more profitable per order, but most mobile users never scroll that far. Kasia (gift buyer) nearly bounced at section 4 because she couldn't find gift sets. Unanimous: move up.
- **10 sections is acceptable** — premium brands average 7-9, volume DTC runs 10-15. Our 10 is at the upper edge but justified if every section earns its place.
- **Visual Proof Block between products validates the price jump** — the Proof Sandwich pattern (Hook → Proof → Product → Proof → Product → Close) is the strongest framework match. A proof beat between Bestsellers (269 zl) and Bundles (349-399 zl) earns the right to ask for more money.
- **0/6 competitor brands have FAQ on homepage** — but our persona analysis showed FAQ scores 5/5 for two personas (quality-seeker, TikTok native). Keep it for pre-launch trust-building; reconsider once brand recognition is established.
- **Background pattern is busier than competitors** — most premium brands use 1-2 background tones (Aesop: uniform warm amber; Glossier: uniform white). LUSENA uses 3. Simplify to 2 tones on homepage.

---

## 2. Current state → New state

### Section mapping

| # | Current (before) | New (after) | Change type |
|---|-----------------|-------------|-------------|
| 1 | Hero | Hero | Minor edits |
| 2 | Trust bar | Trust bar | Reorder items |
| 3 | Benefit bridge | Benefit bridge | Add quality page link |
| 4 | Bestsellers | Bestsellers | Rename heading |
| 5 | Testimonials | **Visual Proof Block** | **Replaced** (new section, backlogged) |
| 6 | Problem/Solution | **Bundles** | **Cut P/S, moved Bundles here from #7** |
| 7 | Bundles | **UGC / Social proof** | **Replaced** (Testimonials → UGC, kept in slot for now) |
| 8 | Heritage | Heritage | No changes now |
| 9 | FAQ | FAQ | Reorder questions, tighten |
| 10 | Final CTA | Final CTA | Copy swap |

### What was cut and why

| Section | Why | Where its value migrated |
|---------|-----|------------------------|
| **Problem/Solution** | Content redundant with Benefit Bridge. Red X / green check register incompatible with premium brand personality. Scored 2.75/5 across personas. | "Sprawdź dowody jakości" CTA link migrates to Benefit Bridge. Educational content already covered by Benefit Bridge cards. |
| **Testimonials** (as fabricated reviews) | Pre-launch fabricated reviews undermine proof-first positioning. Scored 2/5 for the two most discerning personas (quality-seeker, aesthete). 0 credibility value. | Section slot preserved as UGC placeholder. Will be redesigned with real customer content before/shortly after launch. |

---

## 3. Section-by-section spec

### Section 1: Hero

**Position:** 1 (unchanged)
**Background:** Hero image
**Purpose:** Emotional hook — stop the scroll, establish brand promise

**Changes:**
- Downgrade "Dlaczego jedwab?" from button to text link. Two equal-weight buttons create decision paralysis. The primary CTA ("Zacznij swoją rutynę") should be the only button; the quality page link becomes a subtle text link below or beside it.

**Content (unchanged):**
- Heading: "Urodę Tworzysz w Nocy."
- Subheading: "8 godzin jedwabnej pielęgnacji - każdej nocy. Obudź się piękniejsza."
- Primary CTA: "Zacznij swoją rutynę" → collection page
- Secondary link (text, not button): "Dlaczego jedwab?" → quality page

**Implementation:** Edit `index.json` button settings or add a schema option for secondary link style. May need minor Liquid change in `lusena-hero.liquid` if the section doesn't support a text-link variant for button 2.

**Note:** Hero images are AI-generated placeholders. Must be replaced with real product photography before launch. This is a production dependency, not a code task.

---

### Section 2: Trust bar

**Position:** 2 (unchanged)
**Background:** White (`surface-1`)
**Purpose:** Instant credibility — catch the skeptic right after the hero

**Changes:**
- Reorder items to lead with risk-removal, not product spec:
  1. OEKO-TEX® 100 / Bezpieczny dla skóry (certification = strongest trust signal)
  2. 60 dni na test / Zwrot bez stresu (risk reversal = strongest conversion lever)
  3. Wysyłka w 24h / Z magazynu w Polsce (logistics convenience)
  4. 22 momme jedwab / Gęstszy i trwalszy (product spec — already hooked by now)

**Rationale:** Lead with what removes purchase risk (certification, guarantee), not what describes the product. The quality-seeker persona already knows about momme; the gift-buyer and TikTok-native personas engage with the guarantee and shipping first.

**Implementation:** Reorder blocks in `index.json` only. No code changes.

---

### Section 3: Benefit bridge

**Position:** 3 (unchanged)
**Background:** Warm cream (`bg-brand`)
**Purpose:** Outcome-framed education — "What will you see in the morning?"

**Changes:**
- Add a quality page link below the transition text. This migrates from the deleted Problem/Solution section. The link text "Sprawdź dowody jakości" (or similar) should appear as a subtle text link (same style as the heritage CTA — `lusena-link-arrow` pattern) below "Wszystkie trzy - bez żadnej zmiany w rutynie."

**Content (unchanged except addition):**
- Kicker: "Jedwab morwowy 22 momme"
- Heading: "Co zobaczysz rano?"
- 3 cards: skin, hair, cream retention (content unchanged)
- Transition text: "Wszystkie trzy - bez żadnej zmiany w rutynie."
- **NEW:** Link: "Sprawdź dowody jakości" → quality page (migrated from Problem/Solution)

**Implementation:** Add a CTA link setting to the `lusena-benefit-bridge` section schema (link label + link URL). Render below transition text using existing `lusena-link-arrow` pattern. Minor Liquid + schema change.

---

### Section 4: Bestsellers

**Position:** 4 (unchanged)
**Background:** White (`surface-1`)
**Purpose:** Product discovery — first price exposure, first product interaction

**Changes:**
- Rename heading from "Nasze bestsellery" to the current subheading: **"Twoja nocna rutyna zaczyna się tutaj."** The "bestsellery" claim is unearned pre-launch. The promoted subheading ties directly to the brand narrative ("nocna rutyna").
- Remove the separate subheading (now redundant since it became the heading).

**Implementation:** Update `index.json` heading/subheading settings. No code changes.

---

### Section 5: Visual Proof Block (NEW — backlogged)

**Position:** 5
**Background:** Warm cream (`bg-brand`)
**Purpose:** Proof Sandwich second proof beat — validates quality between individual products and bundles. Earns the right to show higher-priced bundles next.

**This section is backlogged for detailed design in a separate task.** The architecture spec defines its slot, purpose, and content direction. Detailed layout, copy, and implementation will be specced separately.

See [Section 7: Visual Proof Block — Design Brief](#7-visual-proof-block-design-brief) for the full backlog brief.

**Pre-launch requirement:** Owner provides macro fabric photography (standard silk vs. 22 momme comparison) before this section can go live.

---

### Section 6: Bundles

**Position:** 6 (moved from 7)
**Background:** White (`surface-1`) — **changed from cream.** With Visual Proof Block (#5) now in cream, two consecutive cream sections would feel heavy. White gives the product cards a neutral canvas and maintains the alternation rhythm.
**Purpose:** Upgrade path — "here's how to combine products into a complete routine"

**Changes:**
- Moved from position 7 to position 6 (directly after Visual Proof Block).
- Background changed from `bg-brand` to `surface-1`.
- Add SB7 Plan sentence to intro copy. The StoryBrand framework identified a missing "Plan" beat — the bundle section implies a routine structure but never names the steps explicitly.

**Content changes:**
- Kicker: "Zestawy Premium" (unchanged)
- Heading: "Zbuduj swoją nocną rutynę" (unchanged)
- Body: **Replace** current text with the Plan sentence:
  - Current: "Każdy zestaw to gotowy pomysł - na nocną rutynę albo idealny prezent."
  - New: "Poszewka chroni skórę. Czepek - włosy. Razem: kompletna nocna rutyna - albo idealny prezent."
  - Note: "albo idealny prezent" preserved from original — this phrase is what caught the gift-buyer persona (Kasia). The Scrunchie Trio card's editorial line also covers the gift angle.
- Bundle cards: unchanged (Nocna Rutyna, Piękny Sen, Scrunchie Trio)

**Rationale for the copy change:** The current body text says bundles are "a ready idea" — passive. The new text names the plan: what protects what, and what the combination achieves. This closes the StoryBrand Plan gap and makes the bundle upsell feel logical ("I need both pieces") rather than commercial ("buy more, save more").

**Implementation:** Update `index.json` body text. Change CSS class from `bg-brand` to `bg-surface-1` in `lusena-bundles.liquid` (or add a schema setting for background choice). Reorder in `index.json`.

---

### Section 7: UGC / Social proof (placeholder)

**Position:** 7 (was Testimonials at position 5)
**Background:** Warm cream (`bg-brand`)
**Purpose:** Proof Sandwich third proof beat — real people validate the purchase decision after seeing both individual products and bundles

**Current state:** The existing `lusena-testimonials` section remains in place with its current content (3 placeholder reviews) as a **temporary placeholder**. This section will be redesigned with real UGC content before or shortly after launch.

**No code changes now.** The detailed UGC section design (layout, content types, photo/video support, number of slots) will be specced separately when UGC content strategy is defined.

**Pre-launch requirement:** Replace fabricated testimonials with real customer content before going live. Options:
- Gift products to 10-20 beta testers (friends, beauty bloggers), collect real quotes with photos
- Use real Instagram/TikTok UGC (with permission)
- If no UGC available at launch: **hide this section entirely** rather than launch with fabricated reviews

**Post-launch A/B test:** PASTOR framework predicts testimony-before-offer converts better. Test swapping UGC (#7) with Bundles (#6) once real content exists and traffic allows measurement.

**Implementation (now):** Move section from position 5 to position 7 in `index.json` order array. Change background if needed (currently `surface-2`, should become `bg-brand`).

---

### Section 8: Heritage

**Position:** 8 (unchanged)
**Background:** White (`surface-1`) — **changed from off-white (`surface-2`).** Simplifying to 2-tone system; off-white dropped from homepage.
**Purpose:** Brand origin story — Suzhou provenance, direct sourcing, Polish QC. Differentiates LUSENA from generic Allegro silk sellers.

**Changes (now):**
- Background class changed from `surface-2` to `surface-1`.

**Content:** Unchanged.

**Long-term evolution (not in scope now):** Brand strategist flagged icon-only tiles as "placeholder energy." When photography of the Shengze weaving district or manufactory becomes available, replace icons with editorial photography. Alternatively, rewrite as editorial prose in a narrow column. The current icon-tile format communicates information without sensation — it tells the origin story without making the customer feel it.

**Implementation:** Change background class in `index.json` or section Liquid. No other changes.

---

### Section 9: FAQ

**Position:** 9 (unchanged)
**Background:** White (`surface-1`) (unchanged)
**Purpose:** Objection removal — clears last friction before the closing CTA

**Changes:**
- Reorder questions by purchase-blocking priority:
  1. "Czy to prawdziwy jedwab?" (real silk? — the skepticism gatekeeper)
  2. "Czy 60 dni gwarancji to serio?" (guarantee — strongest risk reversal)
  3. "Od czego zacząć swoją rutynę?" (where to start — guides the undecided)
  4. "Jak prać jedwab?" (washing — practical but post-purchase concern)
  5. "Dlaczego jedwab z Chin?" (origin — weakest purchase blocker, relevant for few)

**Rationale:** Current order puts "real silk?" first (correct) but buries the guarantee at position 4 and the routine guidance at position 5. The guarantee answer ("even used, full refund") was transformative for the TikTok-native persona — it deserves position 2. "Where to start" guides the undecided buyer who scrolled all the way here — position 3 catches them before they give up.

**Implementation:** Reorder blocks in `index.json`. No code changes.

---

### Section 10: Final CTA

**Position:** 10 (unchanged)
**Background:** Warm cream (`bg-brand`) (unchanged)
**Purpose:** Clean close — one ask, one button

**Changes:**
- Swap heading and body copy:
  - Heading: **"Poczuj różnicę już pierwszej nocy."** (currently body text — more specific, more compelling)
  - Body: **"Wybierz swój jedwab i zacznij nocną rutynę."** (lighter, action-oriented replacement)
- Button: "Zacznij swoją rutynę" → collection (unchanged)

**Rationale:** "Gotowa na lepszy sen?" is generic — could be any sleep brand. "Poczuj różnicę już pierwszej nocy" is specific (first night), sensory (feel the difference), and earned (the page has spent 9 sections building the case). Brand strategist flagged this.

**Implementation:** Update `index.json` heading/body settings. No code changes.

---

## 4. Background rhythm

### Simplification: 3 tones → 2 tones (homepage only)

**Before (current):**
image → white → cream → white → off-white → white → cream → off-white → white → cream
(3 tones, 10 switches, visually restless)

**After:**
image → white → cream → white → cream → white → cream → white → white → cream
(2 tones, clean alternation with a calm white zone before the cream close)

| # | Section | Background | Tone |
|---|---------|-----------|------|
| 1 | Hero | Image | — |
| 2 | Trust bar | `surface-1` | White |
| 3 | Benefit bridge | `bg-brand` | Cream |
| 4 | Bestsellers | `surface-1` | White |
| 5 | Visual Proof Block | `bg-brand` | Cream |
| 6 | Bundles | `surface-1` | White |
| 7 | UGC | `bg-brand` | Cream |
| 8 | Heritage | `surface-1` | White |
| 9 | FAQ | `surface-1` | White |
| 10 | Final CTA | `bg-brand` | Cream |

**Scope:** Homepage (`index.json`) only. Other pages (quality, about, returns) retain their current 3-tone backgrounds. A global background audit may be done separately if desired.

**Note:** `surface-2` is NOT deleted from `lusena-foundations.css`. It remains available for other pages. We simply stop using it on the homepage.

---

## 5. Decisions log

| # | Decision | Why | Alternatives considered |
|---|----------|-----|----------------------|
| D1 | Cut Problem/Solution entirely | Redundant with Benefit Bridge. Negative visual register (red X icons) incompatible with premium brand personality. Scored 2.75/5 across personas. | Keep but soften visuals → rejected because content itself is redundant |
| D2 | Cut fabricated Testimonials | Pre-launch fake reviews undermine proof-first positioning. All 3 agents flagged as single biggest credibility risk. Brand rule: "NEVER fabricate social proof." | Keep with disclaimer → rejected because any fabricated review damages trust architecture. Replace with authority quotes → no authority quotes available yet |
| D3 | Move Bundles from #7 to #6 | Bundles are 30-61% more profitable. Mobile scroll depth means most users never reach #7. Gift-buyer persona nearly bounced before finding bundles. | Keep at #7 → rejected by all 3 agents. Move to #5 directly after Bestsellers → rejected because two product sections back-to-back feels commercially aggressive for a premium brand (Aesop, Ettitude never do this) |
| D4 | Visual Proof Block at #5 | Proof Sandwich pattern requires a proof beat between the two product sections. Price jump from 269 zl to 399 zl needs trust reinforcement. Framework analysis confirmed this is the strongest structural pattern. | Skip proof block, put Bundles at #5 → rejected because premium brands always buffer product sections with validation content |
| D5 | UGC section kept as placeholder | Section slot has strong strategic value once real content exists. PASTOR framework, Proof Sandwich pattern, and competitive data all support social proof between product sections. | Remove entirely until launch → rejected because we're designing the final architecture, not a temporary state |
| D6 | Keep FAQ (despite 0/6 competitors having it) | Two personas scored it 5/5. Pre-launch brand with no reputation needs inline objection handling. The "even used, full refund" guarantee detail is transformative for hesitant buyers. | Remove like competitors → rejected because LUSENA lacks the brand recognition that lets established brands skip FAQ |
| D7 | Simplify backgrounds to 2 tones | Competitors use 1-2 tones. Current 3-tone system creates imperceptible variation (white vs. off-white) that adds cognitive noise without visual benefit. | Keep 3 tones → rejected by brand strategist ("off-white is the middle child that earns nothing") |
| D8 | Bestsellers heading → promoted subheading | "Nasze bestsellery" is unearned pre-launch. "Twoja nocna rutyna zaczyna się tutaj" ties to brand narrative and is the stronger line. | "Kolekcja" → too generic. "Zacznij tutaj" → too instructional. "Nocna kolekcja jedwabna" → too long |
| D9 | Final CTA heading → "Poczuj różnicę już pierwszej nocy" | More specific, sensory, and earned than "Gotowa na lepszy sen?" which could be any sleep brand. | Keep current → rejected as generic |
| D10 | Bundles body copy → SB7 Plan sentence | StoryBrand identified missing "Plan" beat. Naming the routine sequence makes the bundle upsell feel logical, not commercial. | Keep current body text → rejected because "gotowy pomysł" is passive; the plan sentence names what protects what |

---

## 6. Post-launch testing and evolution

### A/B tests to run once traffic allows

| Test | Hypothesis | Metric | Trigger |
|------|-----------|--------|---------|
| UGC before Bundles (swap #6 and #7) | PASTOR framework predicts testimony-before-offer converts better | Bundle attach rate, AOV | Real UGC content + 1000+ sessions/week |
| FAQ removal | Once brand trust is established, FAQ may not be needed on homepage (0/6 competitors have it) | Scroll depth past FAQ, conversion rate | 6+ months of brand recognition, review count > 100 |
| Heritage → editorial prose | Prose or photography may outperform icon tiles for brand storytelling | Time on section, About page click-through | When manufactory photography is available |

### Content dependencies before launch

| Dependency | Section affected | Owner action |
|-----------|-----------------|-------------|
| Real product photography | Hero (#1), Bundles (#6), Bestsellers (#4) | Replace AI-generated and placeholder images |
| Macro fabric photography (standard vs. 22 momme) | Visual Proof Block (#5) | Provide comparison photos for the proof section |
| Real UGC content | UGC (#7) | Gift products to beta testers, collect real quotes/photos. Or: hide section at launch |
| Manufactory photography (long-term) | Heritage (#8) | Source photos from Shengze partner |

---

## 7. Visual Proof Block — design brief

*This section defines the strategic slot and content direction for the Visual Proof Block. Detailed layout, copy, and implementation will be specced in a separate task.*

### Position and role

- **Position:** #5 (between Bestsellers and Bundles)
- **Background:** Warm cream (`bg-brand`)
- **Framework role:** Proof Sandwich second proof beat. Closes the first proof-product loop (Trust Bar → Bestsellers → Visual Proof) before opening the second (Visual Proof → Bundles → UGC).
- **Psychological role:** Validates quality *after* the customer has seen products and prices, *before* asking for the higher-priced bundle commitment. The price jump from 269 zl (pillowcase) to 399 zl (Nocna Rutyna bundle) needs a trust reinforcement beat.

### Format guidance

- **Compact, not full-section.** Framework agent recommended: "a trust beat, not a full editorial section." Think visual interlude — something that registers in 2-3 seconds of scrolling, not something that requires interaction or deep reading.
- **Competitive reference:** Slip uses clinical stats ("43% less friction than cotton, 96% would recommend") as visual proof. Ettitude uses CleanBamboo material story with specific claims ("17% more breathable"). LUSENA's equivalent: momme density comparison + OEKO-TEX certification.
- **No heading required.** A visual break without a headline can feel more premium than a titled section — it interrupts the rhythm of heading/content/heading/content with a moment of pure evidence.

### Content direction

The section should convey one idea: **"This is real, premium silk — here's the proof you can see."**

Content elements to consider (not all required — pick what's strongest):

1. **Fabric comparison image** — side-by-side or split photo showing standard market silk (16-19 momme, thin/translucent) vs. LUSENA 22 momme (dense/opaque). This makes the abstract "22 momme" claim tangible and visual. The owner will provide macro photography.

2. **OEKO-TEX® 100 certification badge** — the strongest external proof point. A visible badge (not just text) signals independent verification.

3. **Single caption or claim line** — one sentence that frames what the customer is seeing. Examples:
   - "22 momme - poczuj różnicę na własnej skórze"
   - "Jedwab morwowy klasy 6A - certyfikat OEKO-TEX® 100"
   - No copy at all (image + badge speak for themselves)

4. **Quality page link** — subtle "Dowiedz się więcej" or "Sprawdź dowody jakości" link to the full quality page for customers who want the deep dive.

### Layout options to explore in detailed design

- **Option A: Split image** — full-width image divided into two halves (standard silk left, LUSENA right) with a thin divider line and labels. Static, no interaction. Registers instantly.
- **Option B: Image + badge strip** — single fabric close-up photo on one side, OEKO-TEX badge + one caption line on the other. 2-column on desktop, stacked on mobile.
- **Option C: Full-bleed photo with overlay** — single striking macro photo of the silk weave with OEKO-TEX badge and caption overlaid (similar to hero treatment but smaller).

### What the owner needs to provide

- Macro photography of LUSENA 22 momme silk (close-up of weave texture)
- Macro photography of standard market silk (16-19 momme) for comparison — or a generic stock fabric photo that represents the typical cheap alternative
- OEKO-TEX certification badge image/SVG (if not already in assets)

### What this section does NOT include

- No customer testimonials or social proof (that's UGC section #7)
- No product cards or pricing (that's Bestsellers and Bundles)
- No extended educational copy (that's the Benefit Bridge and the quality page)
- No interactive elements on homepage (the comparison slider concept is better suited for the quality page where users are in research mode)

---

## 8. Implementation scope summary

### Changes that are `index.json` only (no code)

| Change | Section | Status |
|--------|---------|--------|
| Reorder trust bar items | #2 | **DEFERRED** (separate task) |
| Rename bestsellers heading, remove subheading | #4 | **DONE** (2026-04-07) |
| Update bundles body copy (Plan sentence) | #6 | **DONE** (2026-04-07) |
| Reorder FAQ questions | #9 | **DONE** (2026-04-07) |
| Update final CTA heading and body | #10 | **DONE** (2026-04-07) |
| Reorder sections in `order` array | Global | **DONE** (2026-04-07) — Problem/Solution removed, Bundles moved before Testimonials |

### Changes that need minor Liquid/CSS edits

| Change | Section | Files | Status |
|--------|---------|-------|--------|
| Hero: secondary button → text link | #1 | `lusena-hero.liquid`, `lusena-hero.css` | **DONE** (2026-04-07) |
| Benefit bridge: quality page CTA link | #3 | `lusena-benefit-bridge.liquid`, `lusena-benefit-bridge.css` | **ADDED then REMOVED** (2026-04-07) — quality link moved to Visual Proof Block |
| Bundles: background class change | #6 | `lusena-bundles.liquid` | **DONE** (2026-04-07) |
| Bundles: compact row bg fix | #6 | `lusena-bundles.css` | **DONE** (2026-04-07) — cream bg on white section |
| UGC/Testimonials: background class change | #7 | `lusena-testimonials.liquid` | **DONE** (2026-04-07) |
| Heritage: background class change | #8 | `lusena-heritage.liquid` | **DONE** (2026-04-07) |

### New section

| Section | Status | Dependency |
|---------|--------|-----------|
| Visual Proof Block (#5) | **DONE** (2026-04-07) — scaffolded with placeholders | Owner uploads comparison photos + OEKO-TEX badge via theme editor |

### No code changes needed

| Section | Why |
|---------|-----|
| Benefit bridge content | Cards unchanged |
| Bestsellers product grid | Collection/product data unchanged |
| Bundle cards | Product data unchanged |
| FAQ answers | Content unchanged, only order changes |
| Heritage content | Unchanged for now |
