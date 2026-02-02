# LUSENA Theme — Sections by Page (Audit)

Wygenerowano: 2026-02-02 (na podstawie repozytorium `lusena-dawn`).

## Jak czytać ten raport

- **Co zawiera**: co realnie renderuje sekcja (UI + treść + dane).
- **Psychologia**: jaki „job” wykonuje w głowie klienta (zaufanie, redukcja ryzyka, pożądanie, klarowność).
- **Wpływ na zakup**: jakościowa ocena wpływu na konwersję.
- **Brandbook fit**: jak sekcja wspiera PL-first / premium / proof-first.

## Brandbook — zasady, do których się odnoszę

- PL-first: język, PLN, lokalne realia + obsługa po polsku.
- Premium feel: spokój, oddech w layoucie, limit akcentów, zero krzykliwych elementów.
- Proof-first: dowód przed obietnicą (OEKO‑TEX, 22 momme, pochodzenie Suzhou/Shengze, QC w PL, social proof, gwarancja 60 dni).
- Hierarchia komunikatu: benefit → dowód → CTA → uspokojenie (risk reversal) → pielęgnacja / detale.
- CTA: jeden Primary CTA na ekran, spójny kolor (accent‑cta) i wysoki kontrast (WCAG AA).

## Globalne sekcje (layout/theme.liquid)

Na wszystkich stronach (poza password layoutem) renderowane są grupy sekcji:

- Header group: `sections/header-group.json` → `lusena-header`
- Footer group: `sections/footer-group.json` → `lusena-footer`

Password layout (`layout/password.liquid`) ma dodatkowo:

- `main-password-header`
- `main-password-footer`

---

# 1) Strony (templates) → kolejność sekcji

## Strona główna (Home)

Template: `templates/index.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `lusena-hero` | Natychmiastowe „first impression” (premium) + obietnica beauty/snu | Bardzo wysoki | block:heading.heading: <p>Beauty Happens<br>at Night.</p><br>block:subheading.text: Obudź się piękniejsza. Jedwab 22 momme z Suzhou, który chroni Twoją sk |
| 2 | `lusena-trust-bar` | Zamienia „czy to legit?” w „OK, mają dowody” (redukcja ryzyka) | Wysoki | block:item.title: 4.9/5 Rating<br>block:item.title: OEKO-TEX® Certified |
| 3 | `lusena-problem-solution` | Agitacja problemu → ulga: użytkownik rozpoznaje siebie i dostaje prostą narrację | Wysoki | problem_heading: Cotton absorbs. Friction & Dryness.<br>solution_heading: Silk preserves. Hydration & Smoothness.<br>block:problem_item.title: Friction creates wrinkles<br>block:problem_item.title: Absorbs your skincare |
| 4 | `lusena-bestsellers` | Social proof przez selekcję („najczęściej wybierane”) | Wysoki | heading: Our Bestsellers<br>subheading: Loved by over 12,000 sleepers. |
| 5 | `lusena-heritage` | Buduje autorytet (pochodzenie/heritage) i poczucie „marki, a nie listingów” | Średni | heading: Born in Suzhou.<br>kicker: Our Heritage |
| 6 | `lusena-testimonials` | Dowód społeczny (redukcja ryzyka: „inni kupili i działa”) | Wysoki | heading: Sleepers Love Us<br>subheading: Rated 4.9/5 by over 12,000 customers.<br>block:review.quote: I never thought a pillowcase could change my skin. My face cream actua<br>block:review.quote: The quality is unmatched. I've tried cheaper silk before, but LUSENA f |
| 7 | `lusena-bundles` | Włącza segment „Prezent doskonały” (JTBD: bezbłędne pierwsze wrażenie) | Średni–wysoki | heading: The Perfect Gift, Wrapped in Luxury.<br>kicker: Gift Ready<br>block:benefit.text: Save up to 20% on sets<br>block:benefit.text: Signature gift box included |
| 8 | `lusena-faq` | Obsługuje obiekcje (prawdziwy jedwab, pranie, zwroty, wysyłka) | Wysoki | heading: Common Questions<br>subheading: Everything you need to know about sleeping on silk.<br>block:item.question: Is it real mulberry silk?<br>block:item.question: How do I wash it? |

## Kolekcja / Sklep

Template: `templates/collection.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `lusena-main-collection` | Ułatwia skanowanie oferty i porównanie wariantów (redukcja wysiłku) | Wysoki | — |

## Produkt (PDP)

Template: `templates/product.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `lusena-main-product` | Strona decyzyjna: minimalizuje tarcie i niepewność w kluczowym momencie | Krytyczny | tagline: The ultimate anti-aging tool for your skin and hair.<br>add_to_cart_label: Add to Cart - Ships Today<br>block:benefit.text: Reduces sleep wrinkles and morning creases<br>block:benefit.text: Keeps skin hydrated (doesn't absorb cream) |

## Koszyk

Template: `templates/cart.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-cart-items` | Urealnia zakup: klient widzi „co dokładnie kupuję” | Krytyczny | — |
| 2 | `main-cart-footer` | Zmniejsza niepewność ceny („ile zapłacę finalnie?”) | Krytyczny | — |

## Wyszukiwarka

Template: `templates/search.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-search` | Pomaga osobom z intencją („wiem czego chcę”) szybko znaleźć produkt | Średni–wysoki | — |

## Strona: nasza-jakosc

Template: `templates/page.nasza-jakosc.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `lusena-quality-hero` | Ustawia ramę: „nie wierz – sprawdź” (proof-first) | Średni–wysoki | hero_kicker: Nasza Jakość<br>hero_heading: Nie wierz nam na słowo. Sprawdź. |
| 2 | `lusena-quality-momme` | Racjonalny dowód parametru (momme) → uzasadnienie ceny | Średni | momme_heading: Dlaczego 22 momme?<br>block:momme_benefit.text: Wyższą trwałość — znosi pranie znacznie lepiej niż cieńsze odpowiednik<br>block:momme_benefit.text: Gładszą fakturę — mniejsze tarcie dla Twojej skóry i włosów. |
| 3 | `lusena-quality-fire-test` | Konfrontuje „czy to poliester?” – bardzo szybki proof autentyczności | Średni | — |
| 4 | `lusena-quality-origin` | Autorytet i „weryfikowalne pochodzenie” (brandbook poziom 2) | Średni | — |
| 5 | `lusena-quality-qc` | Redukuje ryzyko: „ktoś to sprawdza”, a nie anonimowy import | Średni–wysoki | block:qc_step.title: Produkcja<br>block:qc_step.title: Kontrola w Polsce |
| 6 | `lusena-quality-certificates` | Najsilniejszy dowód (brandbook poziom 1): zewnętrzna instytucja | Wysoki | cert_heading: Certyfikaty Bezpieczeństwa |
| 7 | `lusena-trust-bar` | Zamienia „czy to legit?” w „OK, mają dowody” (redukcja ryzyka) | Wysoki | block:item.title: 4.9/5 Rating<br>block:item.title: OEKO-TEX® Certified |

## Strona: o-nas

Template: `templates/page.o-nas.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `lusena-about-hero` | Humanizuje markę; przenosi z „produkt” na „kto stoi za jakością” | Średni | — |
| 2 | `lusena-about-story` | Narracja: „dlaczego” + różnica vs rynek kompromisów | Niski–średni | — |
| 3 | `lusena-about-values` | Ułatwia identyfikację: „ta marka myśli jak ja” (estetyka minimalizmu) | Niski–średni | block:value.title: Jakość bez kompromisów<br>block:value.title: Szczerość |

## Strona: zwroty

Template: `templates/page.zwroty.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `lusena-returns-hero` | Risk reversal: zabiera strach „a jak nie zadziała?” | Wysoki | — |
| 2 | `lusena-returns-steps` | Redukuje niepewność: „wiem co zrobić” (kontrola) | Średni | block:step.title: Kupujesz i Testujesz<br>block:step.title: Piszesz do nas |
| 3 | `lusena-returns-faq` | Domyka obiekcje: koszty zwrotu, stan produktu, terminy | Średni–wysoki | block:faq.question: Kto pokrywa koszt wysyłki zwrotnej?<br>block:faq.question: Czy muszę mieć oryginalne pudełko? |

## Strona: contact

Template: `templates/page.contact.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-page` | Kanał dla polityk/edukacji (redukcja ryzyka) lub historii marki (zaufanie) | Zależne od treści | — |
| 2 | `contact-form` | Redukuje ryzyko: „jak coś, mogę zapytać / ktoś odpowie” | Średni | — |

## Strona: json

Template: `templates/page.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-page` | Kanał dla polityk/edukacji (redukcja ryzyka) lub historii marki (zaufanie) | Zależne od treści | — |

## Blog

Template: `templates/blog.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-blog` | Top‑of‑funnel: edukacja i budowanie autorytetu | Niski–średni | — |

## Artykuł

Template: `templates/article.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-article` | Edukacja → redukcja sceptycyzmu → „OK, rozumiem, czemu to działa” | Niski–średni | — |

## Lista kolekcji

Template: `templates/list-collections.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-list-collections` | Porządkuje ofertę i daje poczucie kontroli | Średni | — |

## 404

Template: `templates/404.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-404` | Minimalizuje frustrację i pomaga wrócić do zakupów | Niski | — |

## Password (storefront locked)

Template: `templates/password.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `email-signup-banner` | Konwertuje osoby „nie teraz” na lead (retencja + domknięcie później) | Średni | block:heading.heading: Opening soon<br>block:paragraph.text: <p>Be the first to know when we launch.</p> |

## Gift card

Template: `templates/gift_card.liquid`

Brak sekcji (template liquid lub nietypowa logika).

## Customer: login

Template: `templates/customers/login.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-login` | Daje kontrolę i ciągłość zakupów po zakupie | Niski–średni | — |

## Customer: register

Template: `templates/customers/register.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-register` | Obniża tarcie w kolejnych zakupach (retencja) | Niski | — |

## Customer: account

Template: `templates/customers/account.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-account` | Buduje zaufanie po zakupie: „mam kontrolę, sklep jest profesjonalny” | Niski | — |

## Customer: order

Template: `templates/customers/order.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-order` | Uspokaja po zakupie: „wszystko jest jasne” | Niski | — |

## Customer: addresses

Template: `templates/customers/addresses.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-addresses` | Wygoda i kontrola dla powracających | Niski | — |

## Customer: reset_password

Template: `templates/customers/reset_password.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-reset-password` | Minimalizuje frustrację i odblokowuje dostęp do konta | Niski | — |

## Customer: activate_account

Template: `templates/customers/activate_account.json`

| Kolejność | Sekcja (type) | Krótko: po co tu jest | Wpływ na zakup | Aktualna konfiguracja (skrócona) |
|---:|---|---|---|---|
| 1 | `main-activate-account` | Ułatwia start konta | Niski | — |

---

# 2) Katalog sekcji (co zawiera + psychologia + brandbook)

## `contact-form`

Plik: `sections/contact-form.liquid`

Użyte na: `templates/page.contact.json`

**Co zawiera**

- Formularz kontaktowy + ewentualne prefill z konta klienta.
- Ustawienia (ID): `heading`, `heading_size`, `color_scheme`, `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Redukuje ryzyko: „jak coś, mogę zapytać / ktoś odpowie”.

**Wpływ na zakup**

- Średni — Nie sprzedaje bezpośrednio, ale ratuje konwersję osób z obiekcjami.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: obsługa i copy po PL, jasne SLA odpowiedzi.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj obok formularza 2–3 proofy (24h wysyłka, 60 dni, OEKO‑TEX) + email/telefon.

## `email-signup-banner`

Plik: `sections/email-signup-banner.liquid`

Użyte na: `templates/password.json`

**Co zawiera**

- Banner z obrazem + email form (newsletter)
- Ustawienia (ID): `show_background_image`, `image`, `image_overlay_opacity`, `image_height`, `desktop_content_position`, `desktop_content_alignment`, `show_text_box`, `color_scheme`, `mobile_content_alignment`, `show_text_below`
- Typy bloków: `heading`, `paragraph`, `email_form`

**Psychologiczny cel**

- Konwertuje osoby „nie teraz” na lead (retencja + domknięcie później).

**Wpływ na zakup**

- Średni — Wspiera sprzedaż w czasie (email), szczególnie przy wysokiej cenie.

**Brandbook fit (PL-first / premium / proof-first)**

- Brandbook: 1 CTA na ekran (w tym wypadku 1 akcja: zapis).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Użyj obietnicy newslettera zgodnej z brandbook (np. early access, porady pielęgnacji, nowe kolory).

## `lusena-about-hero`

Plik: `sections/lusena-about-hero.liquid`

Użyte na: `templates/page.o-nas.json`

**Co zawiera**

- Kicker + dwulinijkowy nagłówek (2. linia italic) + body + obraz
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `hero_kicker`, `hero_heading_line_1`, `hero_heading_line_2`, `hero_body`, `hero_image`, `hero_image_placeholder`

**Psychologiczny cel**

- Humanizuje markę; przenosi z „produkt” na „kto stoi za jakością”.

**Wpływ na zakup**

- Średni — Pomaga sceptykom, ale zwykle jest poza główną ścieżką.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: domyślnie po PL (dobrze). Premium: estetyka spójna.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj 1–2 proof points w hero (Suzhou, 22 momme, QC w PL).

## `lusena-about-story`

Plik: `sections/lusena-about-story.liquid`

Użyte na: `templates/page.o-nas.json`

**Co zawiera**

- Nagłówek + richtext „Nasza historia”
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `story_heading`, `story_body`

**Psychologiczny cel**

- Narracja: „dlaczego” + różnica vs rynek kompromisów.

**Wpływ na zakup**

- Niski–średni — Nie sprzedaje bezpośrednio, ale buduje wiarygodność.

**Brandbook fit (PL-first / premium / proof-first)**

- Zgodne z pozycjonowaniem i „uczciwością w obietnicach”.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodać konkretne dowody (bez ogólników): 22 momme, OEKO‑TEX, 24h, 60 dni.

## `lusena-about-values`

Plik: `sections/lusena-about-values.liquid`

Użyte na: `templates/page.o-nas.json`

**Co zawiera**

- Grid wartości (bloki: tytuł + opis)
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `values_kicker`, `values_heading`
- Typy bloków: `value`

**Psychologiczny cel**

- Ułatwia identyfikację: „ta marka myśli jak ja” (estetyka minimalizmu).

**Wpływ na zakup**

- Niski–średni — Wspiera, ale rzadko jest jedynym powodem zakupu.

**Brandbook fit (PL-first / premium / proof-first)**

- Bardzo zgodne z brandbook „Wartości” (prostota, szczerość, lokalność).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Pilnuj, by wartości nie obiecywały medycznych efektów.

## `lusena-bestsellers`

Plik: `sections/lusena-bestsellers.liquid`

Użyte na: `templates/index.json`

**Co zawiera**

- Nagłówek + subhead
- Grid produktowy (z wybranej kolekcji)
- CTA „View all products” (desktop + mobile)
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `heading`, `subheading`, `collection`, `products_to_show`, `view_all_label`, `view_all_mobile_label`

**Psychologiczny cel**

- Social proof przez selekcję („najczęściej wybierane”).
- Skraca drogę do produktu – przejście z inspiracji do wyboru.

**Wpływ na zakup**

- Wysoki — To pierwszy moment „klikam produkt” na stronie głównej.

**Brandbook fit (PL-first / premium / proof-first)**

- Proof-first: OK, jeśli oznaczenia bestseller/new są prawdziwe i konsekwentne.
- PL-first: dopracować etykiety (część UI jest po EN).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Ujednolić język na PL (nagłówki, CTA, pluralizacja).
- Jeśli masz 1 flagowy produkt, rozważ 2 kolumny na mobile + mocny badge “Bestseller”.

## `lusena-bundles`

Plik: `sections/lusena-bundles.liquid`

Użyte na: `templates/index.json`

**Co zawiera**

- Sekcja „gift ready” z obrazem pudełka
- Lista benefitów (bloki), CTA do kolekcji/zestawów
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `kicker`, `heading`, `body`, `image`, `image_placeholder`, `button_label`, `button_link`
- Typy bloków: `benefit`

**Psychologiczny cel**

- Włącza segment „Prezent doskonały” (JTBD: bezbłędne pierwsze wrażenie).
- Podnosi AOV: pokazuje sens zestawu/bonusów.

**Wpływ na zakup**

- Średni–wysoki — Dla części ruchu (prezent) to kluczowy powód zakupu.

**Brandbook fit (PL-first / premium / proof-first)**

- Brandbook: bardzo zgodne z wątkiem „prezentowości” i premium packaging.
- PL-first: dopracować copy (obecnie defaulty po EN).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj konkretny proof prezentowości: zdjęcie unboxing + opis materiałów opakowania.

## `lusena-faq`

Plik: `sections/lusena-faq.liquid`

Użyte na: `templates/index.json`

**Co zawiera**

- Accordion FAQ (bloki pytanie/odpowiedź)
- Animowane otwieranie z `prefers-reduced-motion`
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `heading`, `subheading`
- Typy bloków: `item`

**Psychologiczny cel**

- Obsługuje obiekcje (prawdziwy jedwab, pranie, zwroty, wysyłka).
- Zmniejsza lęk przed zakupem: „mam odpowiedzi zanim zapytam”.

**Wpływ na zakup**

- Wysoki — FAQ często domyka decyzję przy drogich produktach.

**Brandbook fit (PL-first / premium / proof-first)**

- Tone: dopilnuj ostrożnych claimów („może/pomaga ograniczać”) zgodnie z brandbook.
- Proof-first: idealne miejsce na parametry (22 momme, OEKO‑TEX, pochodzenie, 60 dni).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- FAQ powinno być w 100% po PL dla PL-first.
- Używaj odpowiedzi z dowodem (link do certyfikatu, polityka zwrotów).

## `lusena-footer`

Plik: `sections/lusena-footer.liquid`

Użyte na: `sections/footer-group.json`

**Co zawiera**

- Stopka: brand blurb, 2 menu, newsletter
- Ustawienia (ID): `brand_heading`, `brand_text`, `shop_heading`, `shop_menu`, `help_heading`, `help_menu`, `newsletter_heading`, `newsletter_text`, `newsletter_button_label`

**Psychologiczny cel**

- Uspokojenie + weryfikacja (dane, linki, polityki).

**Wpływ na zakup**

- Średni — Nie sprzedaje bezpośrednio, ale buduje zaufanie i zbiera leady.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: ustaw treści i menu po PL. Brandbook: stopka ma czytelne dane firmy.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj dane firmy, regulaminy, polityki (RODO), kontakt.

## `lusena-header`

Plik: `sections/lusena-header.liquid`

Użyte na: `sections/header-group.json`

**Co zawiera**

- Stały header: logo + menu + search/account/cart + mobile menu
- Ustawienia (ID): `logo_image`, `logo_svg_inline`, `logo_width`, `logo_color`, `logo_text_fallback`, `about_page`, `silk_page`, `menu`, `show_additional_menu`, `enable_search`, `enable_account`, `enable_cart`, `auto_hide_on_scroll_mobile`, `auto_hide_on_scroll_desktop`

**Psychologiczny cel**

- Orientacja i poczucie bezpieczeństwa („normalny sklep, nie landing scam”).

**Wpływ na zakup**

- Wysoki — Nawigacja i dostęp do koszyka wpływają na konwersję.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: menu jest po PL (OK). Premium: czysto, bez krzyku.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj w header linki do proof pages (Nasza jakość, Zwroty).

## `lusena-heritage`

Plik: `sections/lusena-heritage.liquid`

Użyte na: `templates/index.json`

**Co zawiera**

- Kicker + H2 + richtext body
- CTA do strony „O nas”
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `kicker`, `heading`, `body`, `button_label`, `button_link`

**Psychologiczny cel**

- Buduje autorytet (pochodzenie/heritage) i poczucie „marki, a nie listingów”.
- Uspokaja: premium ma historię, parametry i standardy.

**Wpływ na zakup**

- Średni — Mniej bezpośrednio sprzedaje, ale wzmacnia zaufanie i usprawiedliwia cenę.

**Brandbook fit (PL-first / premium / proof-first)**

- Proof-first: OK jako „pochodzenie weryfikowalne” (Suzhou/Shengze).
- PL-first: w tym pliku defaulty są po EN – do przepisania pod PL.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dołącz 1 konkretny dowód: mapa, zdjęcie manufaktury, link do „Nasza jakość”.

## `lusena-hero`

Plik: `sections/lusena-hero.liquid`

Użyte na: `templates/index.json`

**Co zawiera**

- Hero obraz (desktop/mobile) + overlay
- H1 (blok: heading), 1 akapit (blok: subheading)
- Do 2 CTA (blok: buttons)
- Ustawienia (ID): `image`, `image_desktop`, `image_mobile`, `mobile_max_height_px`, `overlay_opacity`, `button_height_mobile_px`, `button_text_size_mobile_px`, `buttons_offset_y_mobile_px`, `buttons_offset_y_mobile_vh`, `content_position_mobile`, `content_offset_y_mobile`, `content_offset_y_mobile_vh`, `content_position_desktop`, `content_offset_y_desktop`
- Typy bloków: `heading`, `subheading`, `buttons`

**Psychologiczny cel**

- Natychmiastowe „first impression” (premium) + obietnica beauty/snu.
- Redukuje wysiłek poznawczy: jasny next step (CTA) w 3–5 sekund.

**Wpływ na zakup**

- Bardzo wysoki — To główna brama do całego sklepu i pierwszy filtr „czy to dla mnie?”.

**Brandbook fit (PL-first / premium / proof-first)**

- Proof-first: OK jeśli w treści/CTA jest 22 momme/OEKO‑TEX/24h/60 dni (u Ciebie część jest w kolejnych sekcjach).
- Premium feel: mocne (serif, spokojny layout, mało elementów).
- PL-first: do dopracowania jeśli przyciski/copy są po EN (w `templates/index.json` CTA są po EN).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Primary CTA zgodnie z brandbook: tło `--accent-cta`, tekst biały (obecnie primary jest biały z tekstem accent-cta).
- Zostaw max 2 CTA (jest OK) i dopilnuj, żeby Secondary nie wyglądał „ważniej” niż Primary.
- Dodaj 1 proof w hero (np. badge: OEKO‑TEX / 22 momme) albo kotwicę do trust bar.

## `lusena-main-collection`

Plik: `sections/lusena-main-collection.liquid`

Użyte na: `templates/collection.json`

**Co zawiera**

- H1 kolekcji + opis (fallback w ustawieniach)
- Grid produktów + „Load more” (link do następnej strony paginacji)
- Placeholder przycisku Filter & Sort (bez logiki)
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `products_per_page`, `show_secondary_image`, `default_description`

**Psychologiczny cel**

- Ułatwia skanowanie oferty i porównanie wariantów (redukcja wysiłku).
- Porządek i spójność budują „premium” (brak chaosu).

**Wpływ na zakup**

- Wysoki — Dla części ruchu to główna ścieżka do PDP.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: obecnie są teksty po EN (Load More, Filter & Sort, Product(s)).
- Premium: filtr/sort bez działania może obniżać zaufanie.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Albo wdrożyć realne filtrowanie/sortowanie (Dawn patterns), albo ukryć przycisk.
- Lokalizować mikrocopy (PL + poprawna pluralizacja).

## `lusena-main-product`

Plik: `sections/lusena-main-product.liquid`

Użyte na: `templates/product.json`

**Co zawiera**

- Galeria + miniatury + placeholder video
- Rating + trust mini‑bar (shipping + OEKO)
- Cena + „price per night”
- Warianty (kolor) + CTA add-to-cart + sticky bar
- Sekcje: benefity, gwarancja 60 dni, akordeony, cross-sell, mini‑opinie (bloki)
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `emotional_headline`, `reviews_label`, `reviews_link`, `trust_shipping`, `trust_oeko`, `tagline`, `price_per_night_prefix`, `price_per_night_suffix`, `add_to_cart_label`, `sticky_add_to_cart_label`, `in_stock_label`, `out_of_stock_label`, `guarantee_heading`, `guarantee_body`, `video_placeholder`, `cross_sell_heading`, `pdp_reviews_heading`, `pdp_reviews_button_label`, `pdp_reviews_button_link`
- Typy bloków: `benefit`, `accordion`, `cross_sell`, `pdp_review`

**Psychologiczny cel**

- Strona decyzyjna: minimalizuje tarcie i niepewność w kluczowym momencie.
- Risk reversal + proof w pobliżu CTA zwiększają gotowość do kliknięcia.

**Wpływ na zakup**

- Krytyczny — To najważniejsza sekcja dla przychodu (PDP → ATC).

**Brandbook fit (PL-first / premium / proof-first)**

- Proof-first: obecne (rating, shipping, OEKO, gwarancja).
- PL-first: część defaultów po EN (tagline, guarantee) – do lokalizacji.
- Brandbook: „risk reversal widoczny pod CTA” – ta sekcja ma pole na to (guarantee).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Przepisz „tagline” na claim dozwolony (unikaj „anti-aging tool” jako twardej obietnicy).
- Dodaj do akordeonów konkretne proofy: 22 momme, certyfikat, pochodzenie, instrukcja prania, polityka zwrotów.
- Ujednolić język (PL) i nazwy kolorów.

## `lusena-problem-solution`

Plik: `sections/lusena-problem-solution.liquid`

Użyte na: `templates/index.json`

**Co zawiera**

- Kolumna „Problem” + lista problemów (bloki `problem_item`)
- Kolumna „Solution” + lista rozwiązań (bloki `solution_item`)
- Link CTA do edukacji (np. /nasza-jakosc)
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `problem_label`, `problem_heading`, `solution_label`, `solution_heading`, `cta_label`, `cta_link`
- Typy bloków: `problem_item`, `solution_item`

**Psychologiczny cel**

- Agitacja problemu → ulga: użytkownik rozpoznaje siebie i dostaje prostą narrację.
- Buduje racjonalne uzasadnienie ceny (premium = mniej kompromisów).

**Wpływ na zakup**

- Wysoki — To „dlaczego w ogóle jedwab” – bez tego część ludzi nie rozumie wartości.

**Brandbook fit (PL-first / premium / proof-first)**

- Proof-first: dobrze, jeśli problem/solution mają mierzalne parametry lub odsyłają do proof page.
- Tone: uważaj na zbyt mocne claimy zdrowotne; brandbook preferuje „może/sprzyja/pomaga”.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Przepisz copy na PL-first (w schema defaulty są po EN).
- Zamień ogólne zdania na konkret: tarcie, absorpcja kremu, zagniecenia – ale bez medycznych obietnic.

## `lusena-quality-certificates`

Plik: `sections/lusena-quality-certificates.liquid`

Użyte na: `templates/page.nasza-jakosc.json`

**Co zawiera**

- Opis certyfikatu + przycisk PDF z metafielda + logotypy
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `cert_heading`, `cert_body`, `cert_button_label`, `cert_button_link`, `cert_logo_1`, `cert_logo_1_placeholder`, `cert_logo_2`, `cert_logo_2_placeholder`

**Psychologiczny cel**

- Najsilniejszy dowód (brandbook poziom 1): zewnętrzna instytucja.

**Wpływ na zakup**

- Wysoki — Certyfikat mocno podnosi zaufanie do produktu dotykającego skóry.

**Brandbook fit (PL-first / premium / proof-first)**

- Idealne dopasowanie do proof-first.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Upewnić się, że metafield `lusena.oeko_tex_certificate` jest ustawiony i publiczny.

## `lusena-quality-fire-test`

Plik: `sections/lusena-quality-fire-test.liquid`

Użyte na: `templates/page.nasza-jakosc.json`

**Co zawiera**

- Wideo (lub placeholder) + opis testu ognia
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `fire_heading`, `fire_video`, `fire_video_placeholder`, `fire_body`

**Psychologiczny cel**

- Konfrontuje „czy to poliester?” – bardzo szybki proof autentyczności.

**Wpływ na zakup**

- Średni — Świetne na edukację, ale nie każdy potrzebuje.

**Brandbook fit (PL-first / premium / proof-first)**

- Proof-first: mocne, tylko zachowaj spokojny ton (bez agresji).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Wstawić realne wideo i krótką instrukcję „jak rozpoznać jedwab”.

## `lusena-quality-hero`

Plik: `sections/lusena-quality-hero.liquid`

Użyte na: `templates/page.nasza-jakosc.json`

**Co zawiera**

- Kicker + H1 + opis (strona „Nasza jakość”)
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `hero_kicker`, `hero_heading`, `hero_body`

**Psychologiczny cel**

- Ustawia ramę: „nie wierz – sprawdź” (proof-first).

**Wpływ na zakup**

- Średni–wysoki — Dla sceptyków to klucz do zaufania, ale nie każdy tu trafia.

**Brandbook fit (PL-first / premium / proof-first)**

- Bardzo zgodne z proof-first i tonem brandbooka.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodać CTA/kotwice do sekcji: 22 momme, pochodzenie, certyfikaty.

## `lusena-quality-momme`

Plik: `sections/lusena-quality-momme.liquid`

Użyte na: `templates/page.nasza-jakosc.json`

**Co zawiera**

- Obraz porównawczy + opis 22 momme + lista benefitów
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `momme_image`, `momme_image_placeholder`, `momme_heading`, `momme_body`
- Typy bloków: `momme_benefit`

**Psychologiczny cel**

- Racjonalny dowód parametru (momme) → uzasadnienie ceny.

**Wpływ na zakup**

- Średni — Wspiera decyzję po obejrzeniu produktu/reklamy.

**Brandbook fit (PL-first / premium / proof-first)**

- Zgodne z brandbook: „parametr mierzalny” jako proof point.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodać porównanie 19 vs 22 (wykres/zdjęcie), ale bez przesady w claimach.

## `lusena-quality-origin`

Plik: `sections/lusena-quality-origin.liquid`

Użyte na: `templates/page.nasza-jakosc.json`

**Co zawiera**

- Historia pochodzenia + obraz (mapa/manufaktura)
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `origin_kicker`, `origin_heading`, `origin_body`, `origin_image`, `origin_image_placeholder`

**Psychologiczny cel**

- Autorytet i „weryfikowalne pochodzenie” (brandbook poziom 2).

**Wpływ na zakup**

- Średni — Buduje zaufanie, szczególnie przy obiekcji „dlaczego z Chin?”.

**Brandbook fit (PL-first / premium / proof-first)**

- Zgodne (Suzhou/Shengze + narracja).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodać mapę i zdjęcia (brandbook: krytyczne do tej strony).

## `lusena-quality-qc`

Plik: `sections/lusena-quality-qc.liquid`

Użyte na: `templates/page.nasza-jakosc.json`

**Co zawiera**

- 3 karty procesu (CN produkcja → PL kontrola → wysyłka 24h)
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `qc_heading`, `qc_highlight_badge`
- Typy bloków: `qc_step`

**Psychologiczny cel**

- Redukuje ryzyko: „ktoś to sprawdza”, a nie anonimowy import.

**Wpływ na zakup**

- Średni–wysoki — To kluczowy proof dla polskiej marki (PL-first + zaufanie).

**Brandbook fit (PL-first / premium / proof-first)**

- Bardzo zgodne z PL-first i proof-first.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodać 1 konkret: co sprawdzacie (szwy, waga, zamek) + zdjęcie procesu.

## `lusena-returns-faq`

Plik: `sections/lusena-returns-faq.liquid`

Użyte na: `templates/page.zwroty.json`

**Co zawiera**

- FAQ zwrotów + CTA do kontaktu
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `faq_heading`, `contact_prompt`, `contact_button_label`, `contact_button_link`
- Typy bloków: `faq`

**Psychologiczny cel**

- Domyka obiekcje: koszty zwrotu, stan produktu, terminy.

**Wpływ na zakup**

- Średni–wysoki — Uważne osoby sprawdzają to przed zakupem.

**Brandbook fit (PL-first / premium / proof-first)**

- Zgodne z risk reversal i transparentnością.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Spójność z regulaminem i polityką zwrotów (unikaj rozjazdów).

## `lusena-returns-hero`

Plik: `sections/lusena-returns-hero.liquid`

Użyte na: `templates/page.zwroty.json`

**Co zawiera**

- Hero polityki zwrotów + badge „zwrot nawet używanego”
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `hero_kicker`, `hero_heading_line_1`, `hero_heading_line_2`, `hero_body`, `hero_badge`

**Psychologiczny cel**

- Risk reversal: zabiera strach „a jak nie zadziała?”.

**Wpływ na zakup**

- Wysoki — Gwarancja 60 dni jest jednym z najsilniejszych domykaczy zakupu.

**Brandbook fit (PL-first / premium / proof-first)**

- Zgodne z brandbook: risk reversal ma być widoczny, nie w stopce.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Upewnij się, że ten komunikat jest też na PDP pod CTA i w koszyku/checkout.

## `lusena-returns-steps`

Plik: `sections/lusena-returns-steps.liquid`

Użyte na: `templates/page.zwroty.json`

**Co zawiera**

- 3 kroki procesu zwrotu (bloki)
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `steps_heading`
- Typy bloków: `step`

**Psychologiczny cel**

- Redukuje niepewność: „wiem co zrobić” (kontrola).

**Wpływ na zakup**

- Średni — Wspiera decyzję, ale zwykle po tym jak ktoś już uwierzył.

**Brandbook fit (PL-first / premium / proof-first)**

- Zgodne z „szacunek dla czasu klienta”.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj realne SLA (np. 3–5 dni) i kanał kontaktu (email/telefon).

## `lusena-testimonials`

Plik: `sections/lusena-testimonials.liquid`

Użyte na: `templates/index.json`

**Co zawiera**

- Heading + subheading
- 3‑kolumnowy grid opinii (bloki `review`), stałe 5 gwiazdek
- Link do pełnych opinii
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`, `heading`, `subheading`, `link_label`, `link_url`
- Typy bloków: `review`

**Psychologiczny cel**

- Dowód społeczny (redukcja ryzyka: „inni kupili i działa”).
- Ułatwia decyzję osobom niezdecydowanym.

**Wpływ na zakup**

- Wysoki — Social proof jest jednym z najsilniejszych lewarów na premium (brandbook: poziom 4).

**Brandbook fit (PL-first / premium / proof-first)**

- Proof-first: ok, ale tylko jeśli opinie są prawdziwe (unikaj placeholderów).
- Premium feel: pasuje (serif, spokojny card layout).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Jeśli masz rating z aplikacji, podłącz realne dane (gwiazdki + liczba opinii).
- Zadbaj o PL-first (obecne defaulty w ENG).

## `lusena-trust-bar`

Plik: `sections/lusena-trust-bar.liquid`

Użyte na: `templates/index.json`, `templates/page.nasza-jakosc.json`

**Co zawiera**

- Siatka 2×2 (mobile) / 4 kolumny (desktop)
- Ikona + tytuł + podtytuł per blok
- Domyślne proofy: rating, OEKO‑TEX, 24h, 60 dni
- Ustawienia (ID): `padding_top`, `padding_bottom`, `padding_top_mobile`, `padding_bottom_mobile`
- Typy bloków: `item`

**Psychologiczny cel**

- Zamienia „czy to legit?” w „OK, mają dowody” (redukcja ryzyka).
- Szybkie proof points bez scrollowania do długich opisów.

**Wpływ na zakup**

- Wysoki — Bez trust bar premium produkt traci na wiarygodności (szczególnie z reklam).

**Brandbook fit (PL-first / premium / proof-first)**

- Proof-first: bardzo mocne (zgodne z hierarchią dowodów w brandbook).
- Premium: prosto, bez krzykliwości.
- PL-first: wartości w blokach powinny być po PL na polskiej wersji sklepu.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Pilnuj, żeby tytuły były konkretne (liczby: „22 momme”, „OEKO‑TEX 100”, „Wysyłka 24h”, „60 dni”).
- Jeśli masz realny rating/UGC, podaj prawdziwe liczby (unikaj placeholderów typu 127 jeśli to nieprawda).

## `main-404`

Plik: `sections/main-404.liquid`

Użyte na: `templates/404.json`

**Co zawiera**

- Komunikat 404 + linki powrotu.

**Psychologiczny cel**

- Minimalizuje frustrację i pomaga wrócić do zakupów.

**Wpływ na zakup**

- Niski — Dotyczy tylko części ruchu, ale warto uratować użytkownika.

**Brandbook fit (PL-first / premium / proof-first)**

- Premium: spokojny, pomocny ton, bez „winienia” użytkownika.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj link do sklepu (kolekcja) i do bestsellerów.

## `main-account`

Plik: `sections/main-account.liquid`

Użyte na: `templates/customers/account.json`

**Co zawiera**

- Panel konta: zamówienia, dane.
- Ustawienia (ID): `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Buduje zaufanie po zakupie: „mam kontrolę, sklep jest profesjonalny”.

**Wpływ na zakup**

- Niski — Wpływa na LTV i NPS bardziej niż na pierwszą konwersję.

**Brandbook fit (PL-first / premium / proof-first)**

- Premium: czytelność, prostota.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj łatwy dostęp do zwrotów i kontaktu.

## `main-activate-account`

Plik: `sections/main-activate-account.liquid`

Użyte na: `templates/customers/activate_account.json`

**Co zawiera**

- Aktywacja konta klienta (invite).
- Ustawienia (ID): `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Ułatwia start konta.

**Wpływ na zakup**

- Niski — Rzadko dotyczy pierwszego zakupu.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: copy po PL.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Zachować prostotę.

## `main-addresses`

Plik: `sections/main-addresses.liquid`

Użyte na: `templates/customers/addresses.json`

**Co zawiera**

- Zarządzanie adresami klienta.
- Ustawienia (ID): `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Wygoda i kontrola dla powracających.

**Wpływ na zakup**

- Niski — Post‑purchase convenience.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: formatowanie adresów, copy.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Bez zmian krytycznych – ważna stabilność.

## `main-article`

Plik: `sections/main-article.liquid`

Użyte na: `templates/article.json`

**Co zawiera**

- Strona pojedynczego artykułu (treść, meta, komentarze jeśli włączone).
- Typy bloków: `@app`, `featured_image`, `title`, `content`, `share`

**Psychologiczny cel**

- Edukacja → redukcja sceptycyzmu → „OK, rozumiem, czemu to działa”.

**Wpływ na zakup**

- Niski–średni — Zależy od intencji ruchu i jakości CTA w treści.

**Brandbook fit (PL-first / premium / proof-first)**

- Tone: ostrożne claimy, spokój premium, dowody.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj sekcję „najczęstsze pytania” + link do „Nasza jakość” i Zwroty.

## `main-blog`

Plik: `sections/main-blog.liquid`

Użyte na: `templates/blog.json`

**Co zawiera**

- Lista artykułów bloga + paginacja.
- Ustawienia (ID): `layout`, `show_image`, `image_height`, `show_date`, `show_author`, `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Top‑of‑funnel: edukacja i budowanie autorytetu.

**Wpływ na zakup**

- Niski–średni — Rzadko domyka zakup natychmiast, ale poprawia zaufanie i SEO.

**Brandbook fit (PL-first / premium / proof-first)**

- Proof-first: artykuły powinny linkować do dowodów (certyfikaty, 22 momme).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- W każdym artykule dodaj 1 miękki CTA do produktu + 1 proof (bez agresji).

## `main-cart-footer`

Plik: `sections/main-cart-footer.liquid`

Użyte na: `templates/cart.json`

**Co zawiera**

- Podsumowanie (subtotal, shipping/taxes info), CTA do checkout, ewentualne notatki.
- Ustawienia (ID): `color_scheme`, `padding_top`, `padding_bottom`
- Typy bloków: `subtotal`, `buttons`, `@app`

**Psychologiczny cel**

- Zmniejsza niepewność ceny („ile zapłacę finalnie?”).
- Domyka decyzję: jasny next step (checkout).

**Wpływ na zakup**

- Krytyczny — To miejsce, gdzie użytkownik klika „checkout”.

**Brandbook fit (PL-first / premium / proof-first)**

- Brandbook: risk reversal powinien być widoczny (nie chowany w stopce).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodać pod CTA krótki proof + reassurance (OEKO‑TEX / 24h / 60 dni) zgodnie z zasadą „benefit → dowód → CTA → uspokojenie”.

## `main-cart-items`

Plik: `sections/main-cart-items.liquid`

Użyte na: `templates/cart.json`

**Co zawiera**

- Lista pozycji w koszyku (ilości, warianty, usuwanie, ceny).
- Komunikaty błędów/stanów koszyka.
- Ustawienia (ID): `color_scheme`, `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Urealnia zakup: klient widzi „co dokładnie kupuję”.
- Minimalizuje frustrację przy zmianie ilości/koloru → mniej porzuceń.

**Wpływ na zakup**

- Krytyczny — Koszyk to wąskie gardło konwersji; tarcie tutaj = utrata sprzedaży.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: język, waluta, komunikaty systemowe muszą być po PL.
- Premium: czytelność, brak chaosu, mocne focus/kontrast (WCAG).

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj reassurance blisko zmian ilości (np. „60 dni na test”, „Wysyłka 24h”) – ale bez przesytu.
- Upewnij się, że CTA do checkout jest jedno i wyraźne.

## `main-list-collections`

Plik: `sections/main-list-collections.liquid`

Użyte na: `templates/list-collections.json`

**Co zawiera**

- Lista kolekcji (karty), nawigacja po ofercie.
- Ustawienia (ID): `title`, `sort`, `image_ratio`, `columns_desktop`, `columns_mobile`

**Psychologiczny cel**

- Porządkuje ofertę i daje poczucie kontroli.

**Wpływ na zakup**

- Średni — Ułatwia wybór ścieżki zakupowej, gdy ktoś nie wie co kliknąć.

**Brandbook fit (PL-first / premium / proof-first)**

- Premium: mało bodźców, czytelne karty.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Nazwy kolekcji po PL i zgodne z brandbook (bez krzykliwych tytułów).

## `main-login`

Plik: `sections/main-login.liquid`

Użyte na: `templates/customers/login.json`

**Co zawiera**

- Logowanie klienta + odzyskiwanie hasła.
- Ustawienia (ID): `enable_shop_login_button`, `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Daje kontrolę i ciągłość zakupów po zakupie.

**Wpływ na zakup**

- Niski–średni — Wpływa głównie na powracających klientów.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: komunikaty błędów i reset hasła po PL.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Upewnij się, że copy jest spokojne i pro‑klienckie.

## `main-order`

Plik: `sections/main-order.liquid`

Użyte na: `templates/customers/order.json`

**Co zawiera**

- Szczegóły zamówienia klienta.
- Ustawienia (ID): `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Uspokaja po zakupie: „wszystko jest jasne”.

**Wpływ na zakup**

- Niski — Wpływa na obsługę posprzedażową.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: daty, statusy, waluta PLN.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj link do instrukcji pielęgnacji jedwabiu (brand experience).

## `main-page`

Plik: `sections/main-page.liquid`

Użyte na: `templates/page.contact.json`, `templates/page.json`

**Co zawiera**

- Renderuje treść strony (page.content) + standardowe odstępy.
- Ustawienia (ID): `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Kanał dla polityk/edukacji (redukcja ryzyka) lub historii marki (zaufanie).

**Wpływ na zakup**

- Zależne od treści — Dla stron typu Zwroty/Jakość wpływ jest wysoki; dla ogólnych – niski.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: strony informacyjne powinny być w pełni po PL i spójne tonalnie.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Trzymaj strukturę brandbooka: benefit → dowód → CTA → uspokojenie.

## `main-register`

Plik: `sections/main-register.liquid`

Użyte na: `templates/customers/register.json`

**Co zawiera**

- Rejestracja konta klienta.
- Ustawienia (ID): `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Obniża tarcie w kolejnych zakupach (retencja).

**Wpływ na zakup**

- Niski — Dla pierwszego zakupu zwykle drugorzędne.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: jasne zgody/RODO.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Nie zmuszaj do konta przed zakupem; pokaż wartość (śledzenie zamówień itp.).

## `main-reset-password`

Plik: `sections/main-reset-password.liquid`

Użyte na: `templates/customers/reset_password.json`

**Co zawiera**

- Reset hasła klienta.
- Ustawienia (ID): `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Minimalizuje frustrację i odblokowuje dostęp do konta.

**Wpływ na zakup**

- Niski — Dotyczy wąskiej grupy, ale warto, żeby działało bez tarcia.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: komunikaty po PL.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Krótko, jasno, bez straszenia.

## `main-search`

Plik: `sections/main-search.liquid`

Użyte na: `templates/search.json`

**Co zawiera**

- Wyniki wyszukiwania + sortowanie/filtry (jeśli włączone).
- Karty produktów/artykułów.
- Ustawienia (ID): `columns_desktop`, `columns_mobile`, `image_ratio`, `image_shape`, `show_secondary_image`, `show_vendor`, `show_rating`, `enable_filtering`, `filter_type`, `enable_sorting`, `article_show_date`, `article_show_author`, `padding_top`, `padding_bottom`

**Psychologiczny cel**

- Pomaga osobom z intencją („wiem czego chcę”) szybko znaleźć produkt.

**Wpływ na zakup**

- Średni–wysoki — Dla ruchu z „search intent” to szybka ścieżka do PDP.

**Brandbook fit (PL-first / premium / proof-first)**

- PL-first: placeholdery, filtry i komunikaty „brak wyników” po PL.

**Rekomendacje (co poprawić, żeby mocniej sprzedawało)**

- Dodaj sugestie przy braku wyników (kolekcje, bestseller) – bez rozpraszania.
