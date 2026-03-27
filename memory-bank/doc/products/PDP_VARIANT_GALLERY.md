# PDP — galeria zależna od koloru (warianty) + zdjęcia współdzielone

W LUSENA używamy galerii, która zmienia zestaw zdjęć po zmianie wariantu **Kolor/Color/Colour**.

Założenie: na produkt przypada zwykle **3–5 kolorów**, **3–4 zdjęcia na kolor** oraz **2–4 zdjęcia współdzielone** (np. opakowanie, certyfikaty) widoczne **na końcu** galerii.

## Jak przypisać zdjęcia do koloru (Shopify Admin)

Shopify pozwala przypisać tylko **1 zdjęcie** bezpośrednio do wariantu, ale w LUSENA grupujemy zdjęcia po kolorze przez **alt text**.

### Format alt text (wymagany)

Zawsze dodaj tag na końcu po separatorze `|`:

- Zdjęcie przypisane do koloru:
  - `Maska do spania — przód | [color=Blue]`
  - `Maska do spania — detal | [color=Blue]`
  - `Maska do spania — na modelce | [color=White]`
- Zdjęcie współdzielone (dla wszystkich kolorów):
  - `Opakowanie | [shared]`
  - `Certyfikat OEKO‑TEX | [shared]`

Ważne:
- Wartość w `[color=…]` musi odpowiadać **dokładnie** (bez względu na wielkość liter) wartości wariantu, np. wariant `Blue` ↔ `[color=Blue]`.
- Tag zawsze na końcu (po ostatnim `|`). Treść po lewej stronie `|` jest używana jako realny `alt` w `<img>` (tag nie „przecieka” do dostępności/SEO).

## Zachowanie galerii na PDP

- Galeria pokazuje:
  1) zdjęcia przypisane do wybranego koloru (w kolejności z „Media”),
  2) potem zdjęcia współdzielone (`[shared]` oraz nieotagowane, jeśli produkt używa tagów).
- Po zmianie koloru:
  - jeśli klient był na zdjęciu kolorowym → zostaje na tym samym indeksie (jeśli nowy kolor ma mniej zdjęć, indeks jest ograniczony),
  - jeśli klient był na zdjęciu współdzielonym → galeria przeskakuje na pierwsze zdjęcie nowego koloru.

## Szybki check, gdy „nie działa”

1) Czy wariant nazywa się `Kolor`/`Color`/`Colour` i ma wartości (np. `Blue`, `White`)?
2) Czy alt text ma dokładny format `Opis | [color=Wartość]` lub `Opis | [shared]`?
3) Czy w `[color=…]` jest identyczna wartość jak w wariancie (np. `Ice` ≠ `Blue`)?

