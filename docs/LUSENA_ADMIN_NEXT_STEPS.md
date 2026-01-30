# LUSENA Shopify Admin — kolejne kroki (po stronie sklepu)

Ten plik zakłada, że kod motywu w repo `lusena-dawn` jest już dopasowany „po stronie theme” i dalsze prace robisz w **Shopify Admin / Theme Editor**.

## 1) Ustawienia sklepu (Shopify Admin)

- **Język sklepu:** PL jako domyślny (diakrytyka wszędzie).
- **Waluta:** PLN (format cen zależy od ustawień Shopify, nie od motywu).
- **Wysyłka (realny próg darmowej wysyłki):**
  - Ustaw progi w Shipping profiles.
  - Ten próg musi być spójny z motywem (patrz punkt 2).
- **Zwroty / gwarancja 60 dni:** dopnij prawnie w Policies (Return policy / Terms), żeby copy w motywie miało pokrycie.

## 2) Theme Editor → Theme settings → `LUSENA`

W motywie jest nowa grupa ustawień **LUSENA**, którą wypełniasz w Theme Editor:

- **Pasek do darmowej wysyłki**
  - `Pasek do darmowej wysyłki` → włącz/wyłącz.
  - `Próg darmowej wysyłki` → wpisz realny próg (musi zgadzać się z Shopify Shipping).
- **Tryb prezentowy (dedykacja w koszyku)**
  - włącz/wyłącz.
  - placeholder dedykacji (PL, krótko i spokojnie).
- **Upsell w koszyku**
  - wybierz produkt (np. scrunchie 5cm).
  - ustaw tekst upsell (np. „Dodaj pasującą scrunchie”).
- **CTA na PDP**
  - `Tekst przycisku „Dodaj do koszyka” (PDP)` – rekomendacja startowa:
    - „Dodaj do koszyka – wysyłka w 24 h”

## 3) Strony i szablony (Pages)

### 3.1 Strona „Nasza jakość”

- Utwórz stronę: **Pages → Add page**
  - Tytuł: `Nasza jakość`
  - Theme template: `page.nasza-jakosc`
- Uzupełnij sekcje w Theme Editor:
  - **HERO**: podaj konkret + CTA do PDF
  - **Suzhou / heritage**: dodaj zdjęcia (manufaktura / mapa)
  - **OEKO‑TEX**:
    - dodaj numer certyfikatu w treści
    - podłącz PDF (link w przycisku)
  - **Test ognia**: wstaw wideo (krótkie, porównawcze)

### 3.2 Dodatkowe strony (minimum)

- `O nas` (boilerplate z brandbooka: short/medium/long)
- `Kontakt`
- `FAQ / Pomoc` (jeśli nie chcesz trzymać wszystkiego na PDP)

## 4) Nawigacja (Online Store → Navigation)

- **Menu główne** (propozycja):
  - Poszewki
  - Maska na oczy
  - Akcesoria
  - Zestawy
  - Nasza jakość (`/pages/nasza-jakosc`)
- **Stopka**:
  - Dostawa i zwroty
  - Polityka prywatności
  - Regulamin
  - Kontakt

## 5) Produkty (Products) — dane, media, copy

- **Nazwy produktów (PL-first):** „LUSENA • [nazwa opisowa] …”
- **Claimy:** używaj „może / sprzyja / pomaga ograniczać”; bez medycznych obietnic.
- **Media (kolejność na PDP):**
  1) packshot
  2) krótkie video 10–15 s (muted)
  3) lifestyle
  4) makro splotu
  5) infografika „22 momme”
  6) UGC/opinie (gdy będą)
- **Alt tekst (wzorce):**
  - Packshot: „[Produkt] z jedwabiu 22 momme na jasnym tle…”
  - Makro: „Makro faktury jedwabiu, gładki połysk.”
  - Lifestyle: „[Produkt] używany w sypialni, naturalne światło.”

## 6) Kolekcje (Collections)

- Stwórz kolekcje docelowe (przykład):
  - `Poszewki`
  - `Akcesoria`
  - `Zestawy`
- Podłącz kolekcje do sekcji na Home (Bestsellery) i ewentualnie do kampanii.

## 7) Opinie / social proof (Apps)

- Wybierz aplikację opinii (Judge.me / Loox / Shopify Reviews).
- Upewnij się, że:
  - gwiazdki/rating pojawiają się na PLP (motyw ma to już włączone na collection/search),
  - na Home i PDP masz „proof bar” zgodnie z brandbookiem.

## 8) QA przed publikacją

- Przetestuj:
  - cart drawer: pasek darmowej wysyłki, upsell, tryb prezentowy (cart note)
  - cart page (`/cart`): to samo (w stopce koszyka)
  - PDP: CTA z tekstem „… wysyłka w 24 h” i brak wpływu na małe przyciski poza PDP
- Wydajność (quick win):
  - hero ≤ 300 KB (desktop), ≤ 200 KB (mobile)
  - zdjęcia PLP ≤ 160 KB
  - pierwsze 2–3 media na PDP ≤ 220 KB każde

