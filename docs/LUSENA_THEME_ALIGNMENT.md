# LUSENA × Dawn (15.4.1) — plan dopasowania motywu (PL‑first)

Data: **2026-01-18**  
Repo: `lusena-dawn` (bazowo Shopify **Dawn 15.4.1**)  
Cel: spójne wdrożenie brandbooka LUSENA (UX/konwersja + premium look + PL‑first + WCAG 2.2 AA).

## Jak używać tego dokumentu

- To jest **checklista i mapa plików**: co zmienić, gdzie i w jakiej kolejności.
- Każdy krok ma: **(A)** szybkie “bez kodu” (Theme Editor / Shopify Admin) oraz **(B)** “w kodzie” (ten repozytorium), gdy warto to utrwalić w wersji motywu.
- Najpierw ustawiamy fundamenty (kolor/typografia/CTA), potem strony (Home/PDP/Cart), na końcu “Nasza Jakość” i optymalizacje.

---

## 0) Stan wyjściowy (audyt motywu)

### Co już masz w Dawn i można wykorzystać bez budowy od zera

- **Kolorystyka jako “color schemes”**: `config/settings_schema.json` → `color_scheme_group` + powiązane zmienne CSS w `layout/theme.liquid`.
- **Typografia jako font picker**: `config/settings_schema.json` → `type_header_font`, `type_body_font` (w `layout/theme.liquid` jest `font_face` + preload).
- **Moduły sekcji Home** (do złożenia układu bez kodu): `sections/image-banner.liquid`, `sections/featured-collection.liquid`, `sections/image-with-text.liquid`, `sections/multicolumn.liquid`, `sections/collapsible-content.liquid`, `sections/newsletter.liquid`, `sections/video.liquid`.
- **PDP (karta produktu)** ma rozbudowany system bloków: `sections/main-product.liquid` (m.in. `icon_with_text`, `rating`, `collapsible_tab`, `custom_liquid`, `complementary`).
- **Announcement bar** wspiera rotację wielu komunikatów: `sections/announcement-bar.liquid`.
- **Cart drawer** jest gotowy, ale trzeba go włączyć ustawieniem: `snippets/cart-drawer.liquid` + ustawienie `cart_type` w theme settings.

### Co jest “placeholderem” i wymaga podmiany

- Home: `templates/index.json` ma generyczne nagłówki (“Image banner”, “Talk about your brand”) i demo video.
- Header: `sections/header-group.json` ma “Welcome to our store”.
- Footer: `sections/footer-group.json` ma “Our mission” + generyczny opis.
- PDP: `templates/product.json` ma akordeony po angielsku (“Materials”, “Shipping & Returns”…).
- Preset wyglądu: `config/settings_data.json` ma domyślne schematy i font “Assistant”.

---

## 1) Decyzje startowe (muszą zapaść zanim dotkniesz UI)

1. **Route palety dla sklepu (UI):** używamy **Route A** (Porcelana + Atrament + Teal CTA).  
2. **Fonty:** Head = **Source Serif 4**, Body/UI = **Inter** (oba dostępne w font picker).  
3. **CTA copy (A/B):** wybieramy wariant startowy (rekomendacja na start: “Zamów teraz – wysyłka w 24 h”, bo jest prawdziwe zawsze; “wysyłka dzisiaj” wymaga reguł dni/godzin).  
4. **60 dni gwarancji:** czy to jest “marketingowo” (na stronie) + formalnie w politykach (regulamin/polityka zwrotów)?  
5. **Opinie/UGC:** jaka aplikacja (Judge.me / Loox / Shopify Reviews / Yotpo)? To determinuje, jak robimy “⭐ 4.9/5 z 127 opinii”.
6. **Pay‑later (PayPo/Klarna):** czy wdrażamy “payment terms” (Shopify) czy osobny widget app?

---

## 2) Fundamenty: Visual Identity → Theme settings (kolor, typografia, CTA)

### 2.1 Kolory (Route A) — mapowanie na Dawn “color schemes”

Brandbook (tokeny):
- `--brand-bg-0`: `#F7F5F2`
- `--surface-1`: `#FFFFFF`
- `--surface-2`: `#F0EEEB`
- `--text-1`: `#111111`
- `--accent-cta`: `#0E5E5A`
- `--accent-2`: `#8C6A3C`

Jak to działa w Dawn:
- `scheme.settings.background` → `--color-background`
- `scheme.settings.text` → `--color-foreground`
- `scheme.settings.button` → `--color-button` (Primary CTA)
- `scheme.settings.button_label` → `--color-button-text`
- `scheme.settings.secondary_button_label` → `--color-secondary-button-text` **i** `--color-link`

Rekomendowane schematy (minimum):
- **scheme‑1 (Base / Porcelana):** tło `#F7F5F2`, tekst `#111111`, button `#0E5E5A`, button_label `#FFFFFF`, secondary_button_label `#0E5E5A`
- **scheme‑2 (Surface‑2):** tło `#F0EEEB`, tekst `#111111`, button `#0E5E5A`, button_label `#FFFFFF`, secondary_button_label `#0E5E5A`
- **scheme‑3 (Dark / Ads‑like / inverted sections):** tło `#2E2D2B` albo `#111111`, tekst `#FFFFFF`, button `#FFFFFF`, button_label `#111111`, secondary_button_label `#FFFFFF`
- **scheme‑5 (Accent‑2 / badge‑like):** tło `#F0EEEB`, tekst `#8C6A3C` (subtelny akcent do badge’y i highlightów)

Gdzie ustawić:
- (A) Theme Editor → **Theme settings → Colors** (zaktualizuj schematy).
- (B) Kod: `config/settings_data.json` → `presets.Default.color_schemes` (ustaw jako domyślne w repo).

### 2.2 Typografia

Wymagania brandbook:
- Nagłówki: **Source Serif 4**
- Tekst/UI: **Inter**
- Skala: H1 40/48 • H2 28/36 • H3 20/28 • Body 16/24 • Caption 14/20

Gdzie ustawić:
- (A) Theme Editor → **Theme settings → Typography**
  - `type_header_font` = Source Serif 4
  - `type_body_font` = Inter
  - dopasuj `heading_scale`/`body_scale` tak, żeby wizualnie zbliżyć się do skali (Dawn skaluje globalnie).
- (B) Kod: `config/settings_data.json` → `type_header_font`, `type_body_font`, `heading_scale`, `body_scale`.

Notatka “italic”:
- Primary tagline (“Urodę Tworzysz w Nocy.”) ma być w italic. W Dawn najprościej:
  - użyć `<em>` w polu `inline_richtext` (np. w hero), albo
  - dodać klasę + CSS (jeśli chcesz 100% kontroli).

### 2.3 Przyciski, focus, promień

Brandbook:
- CTA: 44–48 px wysokości, radius 6–8 px, hover: +8–12% jasności, focus ring 2 px, bez agresywnych cieni.

Gdzie ustawić:
- (A) Theme Editor → **Theme settings → Buttons**
  - `buttons_radius`: **6–8**
  - `buttons_border_thickness`: 1 (albo 0 jeśli wygląd ma być super clean)
  - `buttons_shadow_opacity`: 0
- (B) Kod: `config/settings_data.json` → sekcja buttons.

---

## 3) PL‑first i mikrocopy (Verbal Identity)

### 3.1 Język i waluta

- Język sklepu: **polski** (`locales/pl.json` już istnieje).
- Waluta: PLN w Shopify Admin.
- Rozważ wyłączenie `currency_code_enabled` (żeby nie pokazywać “PLN” przy cenie, jeśli wolisz “zł”):
  - (A) Theme Editor → Theme settings → Currency format
  - (B) Kod: `config/settings_data.json` → `currency_code_enabled`

### 3.2 Mikrocopy: kluczowe miejsca do podmiany

Największy wpływ na konwersję:
- CTA: “Dodaj do koszyka – wysyłka w 24 h” (lub wariant A/B z brandbooka)
- Komunikaty błędów w koszyku
- Komunikaty “uspokajające” (dostawa/zwroty) w PDP i Cart

Gdzie to siedzi:
- Globalne tłumaczenia: `locales/pl.json`
  - `products.product.add_to_cart` (domyślnie: “Dodaj do koszyka”)
  - `sections.cart.cart_error` (domyślnie: “Wystąpił błąd…”)
- Teksty sekcji w JSON template: `templates/*.json` i `sections/*-group.json` (np. nagłówki akordeonów na PDP).

Rekomendacja implementacyjna (żeby nie “spalić” innych miejsc):
- Szybko: zmiana tłumaczeń w `locales/pl.json`.
- Docelowo: dodać ustawienie motywu “LUSENA CTA label override” i użyć go w:
  - `snippets/buy-buttons.liquid`
  - quick add / inne formularze produktu

---

## 4) Header + Announcement bar + Footer (globalne elementy)

### 4.1 Announcement bar (komunikaty dowodowe)

Cel: uspokoić i zbudować zaufanie **nad zgięciem**.

Wdrożenie:
- Plik: `sections/header-group.json` → sekcja `announcement-bar`
- Sekcja renderująca: `sections/announcement-bar.liquid`

Proponowane rotujące komunikaty (max 2–3):
1. “Wysyłka z Polski w 24 h (dni robocze).”
2. “60 dni testu i zwrotu — nawet używanego produktu.”
3. “Certyfikat OEKO‑TEX Standard 100.”

Ustawienia:
- `auto_rotate`: opcjonalnie ON (5–7 s), ale tylko jeśli nie rozprasza.
- `color_scheme`: **scheme‑1** (jasne, premium) lub scheme‑2 (delikatne tło).

### 4.2 Header (nawigacja, brak “szumu”)

Plik: `sections/header-group.json` → sekcja `header`

Rekomendacje:
- Wyłącz country selector jeśli nie robisz multi‑market na start (PL‑first).
- Wyłącz language selector jeśli sklep jest tylko po polsku (zmniejsza rozpraszanie).
- Sticky: “on-scroll-up” jest OK (mniej agresywne niż “always”).

### 4.3 Footer (boilerplate + zaufanie)

Plik: `sections/footer-group.json` + `sections/footer.liquid`

Co wstawić:
- Boilerplate (medium) z brandbooka (krótko, bez ściany tekstu).
- Linki: “Nasza jakość”, “Dostawa i zwroty”, “Kontakt”, “Regulamin”, “Polityka prywatności”.
- Widoczne proof points: “OEKO‑TEX”, “22 momme”, “24h wysyłka”, “60 dni gwarancji”.

Newsletter:
- zmień heading z “Subscribe…” na “Dołącz do LUSENA Circle”.

---

## 5) Home (strona główna) — docelowy układ LUSENA (bez kodu + opcja custom)

Plik startowy: `templates/index.json`

### 5.1 Docelowa sekwencja sekcji (zgodnie z brandbookiem)

1. **Hero** (`image-banner`)
   - H1: “Urodę Tworzysz w Nocy.”
   - Sub: “Jedwab 22 momme, który chroni Twoją skórę, gdy śpisz.”
   - CTA: “Zobacz poszewki”
   - overlay 60% (scrim)
2. **Social proof bar / proof points** (najlepiej jako 4 kolumny)
   - bezpośrednio pod hero, tło `scheme‑2`
3. **Problem → rozwiązanie** (`image-with-text` albo `multirow`)
   - “Bawełna chłonie. Jedwab chroni.”
4. **Bestsellery** (`featured-collection`)
   - 2–3 karty na start, spójne ratio 4:5
5. **Suzhou heritage** (`image-with-text` / `multicolumn`)
6. **UGC / opinie** (zależne od app; tymczasowo multicolumn z obrazami)
7. **Zestawy** (`featured-collection` na kolekcję “Zestawy” albo osobna strona)
8. **FAQ skrócone** (`collapsible-content`)
9. **Newsletter** (`newsletter` / `email-signup-banner`)

### 5.2 Co wymaga custom sekcji (jeśli chcesz “premium + szybkie” bez kompromisów)

Rekomendowane 2 małe custom sekcje (do zrobienia w kodzie później):
- `lusena-proof-bar.liquid`: 3–4 proof points z ikonami 24 px i stałą typografią (zamiast kombinowania multicolumn).
- `lusena-ugc-grid.liquid`: siatka UGC z “safe area” i overlay `--scrim-80` pod tekstem.

---

## 6) PDP (karta produktu) — konwersja + proof points (Twoje “money page”)

Pliki:
- Template: `templates/product.json`
- Sekcja: `sections/main-product.liquid`
- CTA: `snippets/buy-buttons.liquid`

### 6.1 Above the fold — wymagany układ bloków (Dawn blocks)

W `templates/product.json` przestaw blokowanie w `main` (kolejność):
1. Headline/benefit (custom): np. block `text` nad tytułem
2. `title`
3. `rating` (jeśli app/Shopify reviews)
4. `price`
5. **Kotwica cenowa** (“0,68 zł / noc…”)
   - szybko: `text` / `custom_liquid`
   - docelowo: custom block liczący na podstawie ceny
6. `variant_picker`
7. `buy_buttons` (Primary CTA)
8. **Risk reversal box** (60 dni) — widoczny, nie w FAQ
   - szybko: `custom_liquid` pod CTA
   - docelowo: custom block z ustawieniami
9. **Trust bar** (OEKO‑TEX / 24h / 60 dni)
   - użyj bloku `icon_with_text` (w `main-product` istnieje)

### 6.2 Akordeony (below the fold)

Zostaw akordeony, ale zmień nagłówki na PL i wypełnij treścią:
- “Materiał (22 momme, 6A)”
- “Dostawa i zwroty (24h PL + 60 dni)”
- “Wymiary i dopasowanie”
- “Pielęgnacja (PL)”

Ważne: claimy beauty tylko jako “może/sprzyja/pomaga” (bez medycznych obietnic).

### 6.3 Wideo jako 2 slajd w galerii

W Dawn kolejność mediów jest z Shopify Admin (media w produkcie).  
Instrukcja: w każdym bestsellerze ustaw kolejność:
1) packshot, 2) krótkie video 10–15 s, 3) lifestyle, 4) makro splotu, 5) infografika 22 momme, 6) UGC.

---

## 7) PLP (lista produktów) + karty produktów

Pliki:
- `templates/collection.json`
- `sections/main-collection-product-grid.liquid`
- `snippets/card-product.liquid`

Ustawienia:
- Ratio zdjęć: **4:5** (w sekcji grid: `image_ratio`)
- Hover = drugi kadr: `show_secondary_image: true` (jeśli używasz 2 zdjęć)
- 1 badge max na kartę (premium spokój)

Custom (opcjonalnie):
- logika badge “Bestseller / Gotowe na prezent” na podstawie tagu lub metafield (w `card-product.liquid`).

---

## 8) Cart drawer / koszyk — uspokojenie + AOV

### 8.1 Włącz cart drawer

Gdzie:
- (A) Theme Editor → Theme settings → Cart → `cart_type = drawer`
- (B) Kod: `config/settings_data.json` → `cart_type`

Pliki:
- `snippets/cart-drawer.liquid`
- `assets/cart-drawer.js`
- `assets/component-cart-drawer.css`

### 8.2 Must‑have elementy w cart drawer

1. **Progress do darmowej wysyłki** (jeśli masz próg)  
2. **Upsell niskiego oporu** (scrunchie / maska)  
3. **Gift mode** (checkbox + pole na dedykację)
   - Technicznie: można wykorzystać `cart.note` (Dawn już ma `settings.show_cart_note`).
   - “Ukryj ceny na dokumencie” to nie temat motywu — to temat szablonu packing slip / fulfillment.
4. Mikrocopy błędów (uspokajające, PL)

---

## 9) Strony dedykowane (brand + zaufanie)

### 9.1 /nasza-jakosc (must‑have)

Podejście:
- Utwórz nowy template JSON: `templates/page.nasza-jakosc.json` (do zrobienia później).
- Składaj z sekcji Dawn + 1 custom dla tabeli porównawczej.

Sekcje wg brandbooka:
1. Hero (“Nie wierz nam na słowo. Sprawdź.”) + CTA do pobrania certyfikatu (PDF)
2. Suzhou heritage (mapa + zdjęcia manufaktury)
3. “Co oznacza 22 momme?” (infografika)
4. OEKO‑TEX (logo + numer + link)
5. Test ognia (video)
6. Klasa 6A (infografika)
7. Kontrola w Polsce (zdjęcia)
8. Tabela porównawcza (custom)
9. FAQ (akordeony)
10. CTA do PDP

### 9.2 /zestawy (AOV)

Opcje:
- Kolekcja “Zestawy” + landing jako `page`/`collection` template.
- Minimalnie: sekcja na Home + link do kolekcji.

### 9.3 /circle (newsletter)

Docelowo: prosta strona z obietnicą (kod -10% + early access), 1 CTA.

---

## 10) Dane / “Proof Points” (żeby nie hardcodować)

Żeby zachować uczciwość claimów i łatwość utrzymania:
- Ustal źródła prawdy dla: momme, 6A, numer OEKO‑TEX, czas wysyłki, gwarancja 60 dni.

Rekomendacja:
- Metafields produktu (np. `lusena.momme`, `lusena.silk_grade`, `lusena.oekotex`…) albo metaobject “Proof pack”.
- Wtedy sekcje/akordeony i badge mogą czytać dane bez ręcznego wklejania w opis każdego produktu.

---

## 11) QA: dostępność, performance, zgodność claimów

### 11.1 WCAG 2.2 AA

- Kontrast CTA (biały na `#0E5E5A`) musi przejść AA.
- Focus visible wszędzie (Dawn ma, ale sprawdzamy po zmianie kolorów).
- Tap targets 44×44 na mobile (variant pills, filtry, przyciski).
- Reduce motion: bez agresywnych animacji.

### 11.2 Performance (budżety z brandbooka)

- Hero: ≤300 KB (desktop), ≤200 KB (mobile)
- PLP zdjęcie: ≤160 KB
- PDP first 2–3 media: ≤220 KB każdy
- Wideo: krótki clip + poster, bez autoplay z dźwiękiem

### 11.3 Theme Check

Uruchamiaj `shopify theme check`, ale ignoruj “known baseline warnings” z `AGENTS.md`.

---

## 12) Lista plików, które prawie na pewno będziemy edytować w tej serii wdrożeń

- `config/settings_data.json` (domyślne kolory/fonty/CTA/cart drawer)
- `templates/index.json` (Home układ + copy)
- `templates/product.json` (PDP blokowanie + copy)
- `templates/cart.json` (koszyk + sekcje uspokajające/upsell)
- `sections/header-group.json` (announcement bar + header settings)
- `sections/footer-group.json` (footer content + newsletter heading)
- `locales/pl.json` (mikrocopy: CTA, błędy, etykiety)
- (opcjonalnie) `snippets/buy-buttons.liquid` (CTA override, “wysyłka 24h” przy CTA)
- (opcjonalnie) `snippets/cart-drawer.liquid` (free shipping progress, gift mode, upsell)
- (nowe) `templates/page.nasza-jakosc.json` + ewentualne custom sections dla tabeli porównawczej

