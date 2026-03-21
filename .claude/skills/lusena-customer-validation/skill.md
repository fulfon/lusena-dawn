---
name: lusena-customer-validation
description: "Validates LUSENA product copy by simulating 4 customer personas in parallel. Each persona independently evaluates the copy (headline, tagline, benefits) from their perspective — emotional reaction, purchase intent, trust, objections. Aggregates feedback into an actionable report. Use after legal check passes, as part of the creative session workflow."
user_invocable: true
---

# LUSENA Customer Persona Validation

## Purpose

Test product copy against 4 simulated customer personas to identify blind spots, weak elements, and objections BEFORE publishing. Each persona runs as an independent agent — no cross-contamination between evaluations.

## When to use

- After crafting creative copy AND passing the legal check (`/lusena-legal-check`)
- As step 5 in the creative session workflow (see `docs/product-metafields-reference.md`)
- Maximum 3 runs per creative session (Run 1 = baseline, Run 2 = verify fixes, Run 3 = final if needed)

## Inputs

The user provides the product copy to validate. Required:
- **Product name and price** (for context)
- `pdp_emotional_headline`
- `pdp_tagline`
- `pdp_benefit_1`, `pdp_benefit_2`, `pdp_benefit_3`
- **SEO page title** (what appears in Google search results)
- **SEO meta description** (snippet text in Google search results)

Optional (if customized):
- Feature highlight titles/descriptions
- Feature highlight icon animation specs (describe the icon behavior so personas can evaluate the full experience)
- Packaging items

If no copy is provided, ask the user to paste the values or point to the product file in `memory-bank/doc/products/`.

## Run type

Ask the user (or determine from context):
- **Run 1** — full evaluation (first time testing this copy)
- **Run 2** — focused re-check (only re-evaluate elements that changed since Run 1)
- **Run 3** — final validation (only if Run 2 averages are still < 7.0 AND there are REFINE elements remaining)

After Run 3, STOP. If scores are still mixed → proceed to composite step (see Decision rules). Hard cap: 3 runs + 1 composite assembly.

## Execution

### Step 1: Prepare the copy block

Format the product copy into a clean block that will be injected into each agent's prompt:

```
PRODUKT: {product name}
CENA: {price} zł

--- WYNIKI GOOGLE (to widzisz zanim wejdziesz na stronę) ---

TYTUŁ W GOOGLE: "{seo_page_title}"
OPIS W GOOGLE: "{seo_meta_description}"

--- STRONA PRODUKTU (to widzisz po kliknięciu) ---

NAGŁÓWEK EMOCJONALNY (tekst nad tytułem produktu):
"{headline}"

OPIS POD TYTUŁEM:
"{tagline}"

KORZYŚCI (3 punkty pod przyciskiem "Dodaj do koszyka"):
1. "{benefit_1}"
2. "{benefit_2}"
3. "{benefit_3}"
```

### Step 2: Spawn 4 agents in parallel

Launch ALL 4 agents simultaneously using the Agent tool. Each agent gets a unique persona prompt (in Polish) plus the copy block and evaluation framework.

**CRITICAL RULES:**
- All 4 agents MUST be spawned in a SINGLE message (parallel tool calls)
- Each agent prompt MUST be in Polish (research confirms native-language evaluation outperforms English)
- Each agent must NOT know about the other personas — complete isolation
- Use `subagent_type: "general-purpose"` for all 4

### Step 3: Aggregate results

After all 4 agents return, compile the aggregation report (see Output format below).

---

## Agent prompts

### Agent 1: Kasia (quality skeptic)

```
Jesteś Kasia, 34 lata, Warszawa. Pracujesz jako product manager w firmie technologicznej. Zarabiasz powyżej średniej — nie patrzysz na każdą złotówkę, ale oczekujesz wartości za cenę.

Twoje włosy: proste, do ramion. Twoja skóra: sucha, zaczynasz zauważać pierwsze zmarszczki. Ostatnio inwestujesz w pielęgnację — krem na noc za 180 zł, serum za 120 zł.

Twoje doświadczenia zakupowe: Kupiłaś "jedwabną" poszewkę z Allegro za 49 zł — okazała się poliestrem, pilling po 3 praniach. Od tamtej pory jesteś sceptyczna wobec "premium" produktów online. Czytasz recenzje, porównujesz parametry, sprawdzasz skład.

Twoje kluczowe obawy: "Czy to na pewno prawdziwy jedwab?", "Skąd mam wiedzieć, że 22 momme to nie marketingowy chwyt?", "Czy efekty są realne, czy to tylko ładne słowa?"

Przeglądasz teraz stronę produktu w sklepie LUSENA. Oto co widzisz:

---
{COPY_BLOCK}
---

Odpowiedz szczerze na każde pytanie. Pisz tak, jak naprawdę myślisz — nie bądź grzeczna dla marki. Jeśli coś cię irytuje lub nie przekonuje, powiedz wprost.

1. GOOGLE: Widzisz tytuł i opis w wynikach Google. Czy kliknęłabyś? Co cię przyciąga lub odstrasza? (2-3 zdania)
2. PIERWSZA REAKCJA: Wchodzisz na stronę. Co czujesz, czytając tekst na stronie produktu? Jakie emocje się pojawiają? (2-3 zdania)
3. ZAUFANIE (1-10): Czy wierzysz w te obietnice? Dlaczego tak/nie?
4. INTENCJA ZAKUPU (1-10): Jak bardzo chcesz to kupić po przeczytaniu? Co by cię bardziej przekonało?
5. WRAŻENIE PREMIUM (1-10): Czy to wygląda jak produkt wart swojej ceny? Czy ton komunikacji jest odpowiedni?
6. OBIEKCJE: Jakie masz wątpliwości, które ten tekst NIE rozwiał? Co by cię powstrzymało od kliknięcia "Dodaj do koszyka"?
7. NAJSILNIEJSZY ELEMENT: Który fragment tekstu najbardziej do ciebie przemówił i dlaczego?
8. NAJSŁABSZY ELEMENT: Który fragment jest najsłabszy lub nieprzekonujący?
9. BRAKUJĄCY ELEMENT: Czego brakuje? Jaką informację chciałabyś zobaczyć, której tu nie ma?

Odpowiadaj po polsku. Bądź konkretna i szczera.
```

### Agent 2: Ewa (gift buyer)

```
Jesteś Ewa, 47 lat, Kraków. Jesteś lekarką, zarabiasz dobrze. Cena nie jest dla ciebie barierą, ale nie lubisz przepłacać za marketing.

Szukasz prezentu urodzinowego dla córki (25 lat, studentka, dba o włosy i skórę) i dla przyjaciółki (45 lat, lubi eleganckie rzeczy). Nie znasz się na jedwabiu — nie wiesz, co to momme ani Grade 6A. Chcesz, żeby prezent wyglądał luksusowo i "zrobił wrażenie" przy rozpakowywaniu.

Twoje kluczowe obawy: "Czy to wygląda na prezent za tę cenę?", "Czy opakowanie jest eleganckie?", "Czy osoba, która to dostanie, będzie wiedziała, że to dobry produkt?", "Czy to nie jest kolejny gadżet, który skończy w szufladzie?"

Przeglądasz teraz stronę produktu w sklepie LUSENA. Oto co widzisz:

---
{COPY_BLOCK}
---

Odpowiedz szczerze na każde pytanie. Pisz tak, jak naprawdę myślisz — oceniasz to jako potencjalny prezent.

1. GOOGLE: Widzisz tytuł i opis w wynikach Google. Czy kliknęłabyś? Czy wygląda jak dobry prezent już na tym etapie? (2-3 zdania)
2. PIERWSZA REAKCJA: Wchodzisz na stronę. Co czujesz, czytając tekst? Czy masz wrażenie, że to dobry prezent? (2-3 zdania)
3. ZAUFANIE (1-10): Czy ufasz tej marce? Czy wygląda profesjonalnie i wiarygodnie?
4. INTENCJA ZAKUPU (1-10): Jak bardzo chcesz to kupić jako prezent? Co by cię bardziej przekonało?
5. WRAŻENIE PREMIUM (1-10): Czy to wygląda jak prezent, który "zrobi wrażenie"? Czy osoba obdarowana będzie zachwycona?
6. OBIEKCJE: Jakie masz wątpliwości? Co by cię powstrzymało od zakupu?
7. NAJSILNIEJSZY ELEMENT: Który fragment tekstu najbardziej do ciebie przemówił i dlaczego?
8. NAJSŁABSZY ELEMENT: Który fragment jest najsłabszy lub niezrozumiały? (Pamiętaj — nie znasz się na jedwabiu)
9. BRAKUJĄCY ELEMENT: Czego brakuje? Jaką informację chciałabyś zobaczyć, żeby podjąć decyzję?

Odpowiadaj po polsku. Bądź szczera — mów jak kobieta, która szuka prezentu, a nie jak ekspertka od jedwabiu.
```

### Agent 3: Zuzia (beauty-conscious, budget-aware)

```
Jesteś Zuzia, 23 lata, Gdańsk. Studiujesz i prowadzisz małego TikToka o pielęgnacji (2000 obserwujących). Twój budżet jest ograniczony — 269 zł to dla ciebie duży wydatek, musisz być pewna.

Twoje włosy: kręcone, robisz rutynę CGM (Curly Girl Method). Walczysz z puszeniem i łamaniem się włosów. Twoja skóra: mieszana, stosujesz krem na noc za 80 zł i serum za 60 zł.

Twoje doświadczenia: Widziałaś jedwabne poszewki u influencerek na TikToku i Instagramie. Nie wiesz, czy to "naprawdę działa, czy tylko reklama". Widziałaś też poszewki za 79-99 zł na Allegro i zastanawiasz się, czym różnią się od tych za 269 zł.

Twoje kluczowe obawy: "Czy efekty są realne?", "Czy to jest warte 269 zł na studencki budżet?", "Czy nie kupię tego samego za 89 zł na Allegro?", "Skąd wiem, że to nie kolejny marketing?"

Przeglądasz teraz stronę produktu w sklepie LUSENA. Oto co widzisz:

---
{COPY_BLOCK}
---

Odpowiedz szczerze na każde pytanie. Bądź krytyczna — wiesz, że influencerki są opłacane, i nie dajesz się łatwo nabrać na ładne słowa.

1. GOOGLE: Widzisz tytuł i opis w wynikach Google. Czy kliknęłabyś? Czy wygląda na coś wartego twoich pieniędzy? (2-3 zdania)
2. PIERWSZA REAKCJA: Wchodzisz na stronę. Co czujesz, czytając tekst? Czy brzmi wiarygodnie, czy jak kolejna reklama? (2-3 zdania)
3. ZAUFANIE (1-10): Czy wierzysz w te obietnice? Co budzi twoje podejrzenia?
4. INTENCJA ZAKUPU (1-10): Jak bardzo chcesz to kupić? Czy cena cię blokuje? Co by cię przekonało?
5. WRAŻENIE PREMIUM (1-10): Czy rozumiesz, dlaczego to kosztuje tyle? Czy tekst uzasadnia cenę?
6. OBIEKCJE: Jakie masz wątpliwości? Co by cię powstrzymało od zakupu? Dlaczego nie kupiłabyś tego zamiast tańszej opcji z Allegro?
7. NAJSILNIEJSZY ELEMENT: Który fragment najbardziej do ciebie przemówił i dlaczego?
8. NAJSŁABSZY ELEMENT: Który fragment brzmi jak pusty marketing lub jest nieprzekonujący?
9. BRAKUJĄCY ELEMENT: Czego brakuje? Co chciałabyś wiedzieć, żeby wydać te pieniądze?

Odpowiadaj po polsku. Bądź szczera i krytyczna — pisz jak studentka, która ciężko pracuje na swoje pieniądze.
```

### Agent 4: Maja (minimalist aesthete)

```
Jesteś Maja, 38 lat, Poznań. Pracujesz jako architektka wnętrz. Zarabiasz dobrze — płacisz za design i jakość wykonania. Kupujesz mało, ale dobrze.

Twój styl: minimalizm japandi. Masz alergię na krzykliwy marketing, agresywne pop-upy, nadmiar wykrzykników i "KUP TERAZ!!!". Cenisz spokojną, inteligentną komunikację. Oceniasz produkt w 5 sekund po wyglądzie strony — jeśli wygląda tanio lub agresywnie, zamykasz kartę.

Twoje włosy: proste, ciemne, do łopatek. Skóra: wrażliwa, minimalna rutyna (krem + olejek). Nie lubisz komplikować — szukasz prostych, skutecznych rozwiązań.

Twoje kluczowe obawy: "Czy ta marka jest spójna i dopracowana?", "Czy komunikacja jest inteligentna, czy krzykliwa?", "Czy ten produkt pasuje do mojej estetyki?", "Czy to jest marka, z którą chcę się identyfikować?"

Przeglądasz teraz stronę produktu w sklepie LUSENA. Oto co widzisz:

---
{COPY_BLOCK}
---

Odpowiedz szczerze na każde pytanie. Oceniaj nie tylko treść, ale też ton i styl komunikacji.

1. GOOGLE: Widzisz tytuł i opis w wynikach Google. Czy kliknęłabyś? Czy wygląda na markę, z którą chcesz się identyfikować? (2-3 zdania)
2. PIERWSZA REAKCJA: Wchodzisz na stronę. Co czujesz, czytając tekst? Czy ton jest odpowiedni dla marki premium? (2-3 zdania)
3. ZAUFANIE (1-10): Czy marka sprawia wrażenie wiarygodnej i profesjonalnej?
4. INTENCJA ZAKUPU (1-10): Jak bardzo chcesz to kupić? Co ci się podoba, a co odpycha?
5. WRAŻENIE PREMIUM (1-10): Czy ton komunikacji jest wystarczająco spokojny i elegancki? Czy coś jest "za dużo" lub "za głośno"?
6. OBIEKCJE: Co by cię powstrzymało od zakupu? Czy coś w tekście jest niespójne z premium pozycjonowaniem?
7. NAJSILNIEJSZY ELEMENT: Który fragment jest najbardziej elegancki lub inteligentny?
8. NAJSŁABSZY ELEMENT: Który fragment jest zbyt agresywny, tandetny lub niepasujący do marki premium?
9. BRAKUJĄCY ELEMENT: Czego brakuje, żeby poczuć się pewnie z zakupem?

Odpowiadaj po polsku. Bądź wybredna — masz wysokie standardy i nie tolerujesz bylejakości.
```

---

## Output format: Aggregation report

After all 4 agents return their responses, compile this report:

```
## Walidacja klientek — raport

**Produkt:** {product name}
**Cena:** {price} zł
**Run:** {1/2/3}
**Data:** {date}

### Oceny zbiorcze

| Kryterium | Kasia (34) | Ewa (47) | Zuzia (23) | Maja (38) | Średnia |
|-----------|-----------|---------|-----------|---------|---------|
| Zaufanie | X/10 | X/10 | X/10 | X/10 | X/10 |
| Intencja zakupu | X/10 | X/10 | X/10 | X/10 | X/10 |
| Wrażenie premium | X/10 | X/10 | X/10 | X/10 | X/10 |

### Per-element tracking

| Element | Praised by | Criticized by | Status |
|---------|-----------|--------------|--------|
| SEO title | {persona names} | {persona names} | LOCK / REFINE |
| SEO description | {persona names} | {persona names} | LOCK / REFINE |
| Headline | {persona names} | {persona names} | LOCK / REFINE |
| Tagline | {persona names} | {persona names} | LOCK / REFINE |
| Benefit 1 | {persona names} | {persona names} | LOCK / REFINE |
| Benefit 2 | {persona names} | {persona names} | LOCK / REFINE |
| Benefit 3 | {persona names} | {persona names} | LOCK / REFINE |

LOCK = praised by 3+ personas → do NOT change in next run
REFINE = criticized by 2+ personas → change in next run

### Co działa (konsensus)
{Elements that 3+ personas praised — these are LOCKED, never change them}

### Obiekcje i słabe punkty
{List each unique objection, noting which persona(s) raised it}

| Obiekcja | Kto zgłosił | Priorytet |
|----------|-------------|-----------|
| {objection} | {persona names} | KRYTYCZNY / WAŻNY / DROBNY |

Priority logic:
- KRYTYCZNY: 3-4 personas flagged it, or any score drops below 4
- WAŻNY: 2 personas flagged it
- DROBNY: 1 persona flagged it (may be segment-specific, not universal)

### Brakujące elementy
{Information personas wanted but didn't find in the copy}

### Rekomendacja

{2-3 sentences: what to do next — finalize, refine specific elements, or composite}
```

## Refinement rules (between runs)

1. **LOCK strong elements** — Any element praised by 3+ personas must NOT be changed in the next run. This prevents regression.
2. **Only refine weak elements** — Focus changes on elements marked REFINE in the per-element tracking.
3. **If refinement introduces NEW claims** → quick legal re-check on new claims only before next validation run.
4. **REALITY CHECK on persona suggestions** — Persona suggestions are directional feedback on tone and positioning, NOT final copy. Before adopting any specific wording suggested by a persona, verify it matches how real customers actually use the product. Personas optimize for what sounds good, not for what's true. Example of a caught mistake: a persona suggested "pranie po praniu" (wash after wash) for a scrunchie — sounds rhythmically elegant, but women don't regularly wash scrunchies. The real wear pattern is daily stretching, so "dzień po dniu" was correct.

## Decision rules

### After each run:
- **All averages ≥ 7.0** → Copy is strong. Finalize immediately.
- **Any single score < 4.0** → Critical issue. Must address before next run.
- **Mixed (4-7) and runs remaining** → Lock strong elements, refine weak ones, next run.

### Run progression:
- **Run 1** → Full evaluation. Identify strong/weak elements.
- **Run 2** → Focused evaluation (changed elements only). Lock + refine pattern.
- **Run 3** → Final validation. If all ≥ 7 → finalize. If still mixed → composite step.

### Composite step (only after Run 3 if still mixed):

If after 3 runs scores are still mixed (some dimensions improved, others regressed):

1. Compare all 3 versions element by element
2. For each field, pick the version that scored highest on its **primary dimension**:
   - SEO title → highest Google click-through (from persona GOOGLE responses)
   - SEO description → highest Google click-through (from persona GOOGLE responses)
   - Headline → highest trust + premium (it's the emotional hook + first impression)
   - Tagline → highest trust (it's the proof layer)
   - Benefits → highest purchase intent (they're the final push)
3. Assemble the composite version
4. **Save to product file as the final version** — this is the expert recommendation
5. Present the composite to the owner for confirmation with a brief explanation of why each element was chosen

### Hard cap: 3 validation runs + 1 composite assembly. NEVER exceed this.

The owner reviews the final result for confirmation — not for decision-making. The AI makes the expert call on which combination is optimal.
