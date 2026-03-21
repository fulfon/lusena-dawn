"""
Generate Shopify product import CSV for 4 LUSENA products.
Source of truth: finalized MD product files in ../
Template: ../exports/products_export.csv (header row only).
Run from the imports/ directory: cd imports && python generate_import_csv.py

Fixes applied (2026-03-15):
- Shopify category metafields (cols 72-76) left empty — they differ per product category
  and cause "Owner subtype does not match" errors if set for the wrong category.
  Set them manually in Shopify admin after import.
- Product Category paths left empty — pick from Shopify UI to ensure exact taxonomy match.
- Variant Grams: 0.0 (not 0) to match Shopify format.
- Variant Weight Unit: kg (matching Shopify default export).
- Feature 2 uses en-dash (–) not hyphen (-) in "16–19 momme" to match Shopify export.
"""
import csv
import io

# Read header from existing export
with open('../exports/products_export.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)

num_cols = len(header)

def make_empty_row():
    return [''] * num_cols

# --- Universal feature cards (shared across all products) ---
# Note: en-dash (–) in "16–19" matches what Shopify stores
UNIVERSAL_FEATURE_2 = {
    'desc': 'Momme to g\u0119sto\u015b\u0107 jedwabiu \u2013 im wy\u017csze, tym grubszy i trwalszy materia\u0142. Standard rynkowy to 16\u201319 momme. Nasze 22 momme to g\u0119stszy splot, kt\u00f3ry lepiej trzyma kszta\u0142t i d\u0142u\u017cej s\u0142u\u017cy.',
    'icon': 'layers',
    'title': 'Dlaczego 22 momme?',
}
UNIVERSAL_FEATURE_4 = {
    'desc': 'Satyna to nazwa splotu, nie materia\u0142u \u2013 najcz\u0119\u015bciej kryje si\u0119 za ni\u0105 poliester. LUSENA to 100% jedwab morwowy: naturalne w\u0142\u00f3kno bia\u0142kowe, kt\u00f3re oddycha i nie elektryzuje.',
    'icon': 'shield-check',
    'title': 'Jedwab, nie satyna z poliestru',
}
UNIVERSAL_FEATURE_5 = {
    'desc': 'Niezale\u017cny certyfikat potwierdza, \u017ce nasz jedwab jest bezpieczny dla sk\u00f3ry i wolny od szkodliwych substancji. Pewno\u015b\u0107, kt\u00f3r\u0105 mo\u017cesz zweryfikowa\u0107.',
    'icon': 'sparkles',
    'title': 'Certyfikowany OEKO-TEX\u00ae 100',
}

# --- Common base for all products ---
def make_base_row():
    row = make_empty_row()
    row[2] = ''  # Body HTML empty
    row[3] = 'LUSENA'
    # Product Category (col 4) left empty — pick from Shopify UI to ensure exact match
    row[7] = 'false'  # Published
    row[8] = 'Title'  # Option1 Name (default single-variant)
    row[9] = 'Default Title'  # Option1 Value
    row[18] = '0.0'  # Variant Grams (matching Shopify export format)
    row[19] = 'shopify'  # Inventory Tracker
    row[20] = 'deny'  # Inventory Policy (don't sell when OOS)
    row[21] = 'manual'  # Fulfillment Service
    row[24] = 'true'  # Requires Shipping
    row[25] = 'true'  # Taxable
    row[34] = 'false'  # Gift Card
    # Universal feature cards 2, 4, 5
    row[46] = UNIVERSAL_FEATURE_2['desc']
    row[47] = UNIVERSAL_FEATURE_2['icon']
    row[48] = UNIVERSAL_FEATURE_2['title']
    row[52] = UNIVERSAL_FEATURE_4['desc']
    row[53] = UNIVERSAL_FEATURE_4['icon']
    row[54] = UNIVERSAL_FEATURE_4['title']
    row[55] = UNIVERSAL_FEATURE_5['desc']
    row[56] = UNIVERSAL_FEATURE_5['icon']
    row[57] = UNIVERSAL_FEATURE_5['title']
    # Shopify category metafields (cols 72-76) intentionally left empty.
    # These differ per product category and cause "Owner subtype" errors
    # if set for the wrong category. Set manually in Shopify admin after import.
    row[80] = 'kg'  # Variant Weight Unit (matching Shopify default)
    row[83] = 'draft'  # Status
    return row

# ============================================================
# Product 1: silk-bonnet
# ============================================================
bonnet = make_base_row()
bonnet[0] = 'silk-bonnet'
bonnet[1] = 'Jedwabny czepek do spania'
bonnet[5] = 'Czepek jedwabny'
bonnet[6] = 'jedwab, czepek, czepek-jedwabny, czepek-do-spania, bonnet, 22-momme, nocna-rutyna, hair-care, ochrona-wlosow'
bonnet[22] = '239.00'
bonnet[35] = 'Jedwabny czepek do spania 22 momme - ochrona w\u0142os\u00f3w \u00b7 LUSENA'
bonnet[36] = 'Jedwabny czepek z regulacj\u0105 obwodu - 22 momme, Grade 6A z Suzhou. \u015aci\u0105gacz pokryty jedwabiem chroni lini\u0119 w\u0142os\u00f3w. Mniej tarcia, mniej pl\u0105tania. OEKO-TEX\u00ae Standard 100.'
bonnet[37] = 'FALSE'
bonnet[38] = 'Otula w\u0142osy g\u0142adkim jedwabiem ze wszystkich stron - mniej tarcia, pl\u0105tania i puszenia ni\u017c na bawe\u0142nie'
bonnet[39] = 'Regulowany \u015bci\u0105gacz pokryty jedwabiem - dopasujesz obw\u00f3d do swojej g\u0142owy, \u017cadne gumowe w\u0142\u00f3kno nie dotyka w\u0142os\u00f3w'
bonnet[40] = 'Chroni fryzur\u0119 od wieczora do rana - loki, fale czy prostowanie przetrwaj\u0105 noc'
bonnet[41] = ''  # care_steps empty (theme defaults)
bonnet[42] = 'Budzisz si\u0119 z fryzur\u0105 - nie z pl\u0105tanin\u0105.'
# Feature 1 (product-specific)
bonnet[43] = 'Zwyk\u0142e czepki maj\u0105 ods\u0142oni\u0119t\u0105 gumk\u0119, kt\u00f3ra \u015bciska i ociera najdelikatniejsze pasma. W czepku LUSENA \u015bci\u0105gacz jest pokryty jedwabiem od wewn\u0105trz - g\u0142adkie w\u0142\u00f3kno zamiast twardej gumy.'
bonnet[44] = 'heart'
bonnet[45] = 'Chroni lini\u0119 w\u0142os\u00f3w'
# Feature 3 (product-specific)
bonnet[49] = 'Regulowany \u015bci\u0105gacz dopasujesz dok\u0142adnie do obwodu g\u0142owy - ani za lu\u017ano, ani za ciasno. Jedwab morwowy oddycha i pomaga regulowa\u0107 temperatur\u0119. Budzisz si\u0119 w czepku, nie obok niego.'
bonnet[50] = 'wind'
bonnet[51] = 'Trzyma pewnie ca\u0142\u0105 noc'
# Feature 6 (universal but product name swapped)
bonnet[58] = 'Ka\u017cdy czepek LUSENA przychodzi w eleganckim pude\u0142ku prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.'
bonnet[59] = 'gift'
bonnet[60] = 'Gotowa do wr\u0119czenia'
# Packaging
bonnet[61] = "Jedwabny czepek LUSENA\nEleganckie pude\u0142ko prezentowe LUSENA\nKarta z instrukcj\u0105 piel\u0119gnacji"
bonnet[62] = 'TRUE'  # show_price_per_night
# Specs
bonnet[63] = 'OEKO-TEX\u00ae Standard 100'
bonnet[64] = 'Regulowany \u015bci\u0105gacz pokryty jedwabiem'
bonnet[65] = 'Regulowany (\u015bci\u0105gacz z regulacj\u0105 obwodu)'
bonnet[66] = '6A (najwy\u017csza)'
bonnet[67] = '100% jedwab morwowy (Mulberry Silk)'
bonnet[68] = '22 momme'
bonnet[69] = 'Charmeuse (splot satynowy)'
bonnet[70] = ''  # weight PENDING
# Tagline (2026-03-17: benefit-oriented, removed redundant specs)
bonnet[71] = 'Otula w\u0142osy g\u0142adkim jedwabiem ze wszystkich stron - mniej tarcia, pl\u0105tania i puszenia ni\u017c na bawe\u0142nie. Regulowany \u015bci\u0105gacz pokryty jedwabiem dopasowuje si\u0119 do obwodu g\u0142owy. Chroni fryzur\u0119 od wieczora do rana - loki, fale czy prostowanie przetrwaj\u0105 noc.'

# ============================================================
# Product 2: silk-scrunchie
# ============================================================
scrunchie = make_base_row()
scrunchie[0] = 'silk-scrunchie'
scrunchie[1] = 'Scrunchie jedwabny'
scrunchie[5] = 'Gumka do w\u0142os\u00f3w'
scrunchie[6] = 'jedwab, scrunchie, gumka, w\u0142osy, 22-momme, ochrona-w\u0142os\u00f3w'
scrunchie[22] = '59.00'
scrunchie[35] = 'Jedwabny scrunchie 22 momme - mniej \u0142amania w\u0142os\u00f3w \u00b7 LUSENA'
scrunchie[36] = 'Scrunchie z prawdziwego jedwabiu morwowego 22 momme. Mniej tarcia, mniej \u0142amania - w\u0142osy poczuj\u0105 r\u00f3\u017cnic\u0119. Certyfikat OEKO-TEX\u00ae Standard 100.'
scrunchie[37] = 'FALSE'
scrunchie[38] = 'Ogranicza tarcie i \u0142amanie - jedwab chroni w\u0142osy lepiej ni\u017c syntetyczne gumki'
scrunchie[39] = 'Jedwab 22 momme nie traci kszta\u0142tu - wytrzymuje znacznie d\u0142u\u017cej ni\u017c ta\u0144sze gumki'
scrunchie[40] = 'Wch\u0142ania znacznie mniej olejk\u00f3w i kosmetyk\u00f3w - stylizacja zostaje na w\u0142osach, nie na gumce'
scrunchie[41] = ''  # care_steps empty
scrunchie[42] = 'Zdejmujesz gumk\u0119 - w\u0142osy zostaj\u0105 na miejscu.'
# Feature 1
scrunchie[43] = 'Jedwab morwowy ma naturalnie g\u0142adk\u0105 powierzchni\u0119 - ogranicza tarcie, kt\u00f3re prowadzi do \u0142amania i rozdwajania ko\u0144c\u00f3wek. Twoje w\u0142osy po prostu zsuwaj\u0105 si\u0119 z gumki, zamiast si\u0119 szarpa\u0107.'
scrunchie[44] = 'heart'
scrunchie[45] = 'Chroni struktur\u0119 w\u0142osa'
# Feature 3
scrunchie[49] = 'Jedwab naturalnie redukuje elektryczno\u015b\u0107 statyczn\u0105. Zdejmujesz gumk\u0119 - w\u0142osy nie stercz\u0105 i nie pusz\u0105 si\u0119 jak po syntetycznych gumkach.'
scrunchie[50] = 'wind'
scrunchie[51] = 'Mniej puszenia i elektryzowania'
# Feature 6
scrunchie[58] = 'Ka\u017cda gumka LUSENA przychodzi w eleganckim pude\u0142ku prezentowym - idealny drobny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.'
scrunchie[59] = 'gift'
scrunchie[60] = 'Gotowa do wr\u0119czenia'
# Packaging
scrunchie[61] = "Jedwabna gumka LUSENA\nEleganckie pude\u0142ko prezentowe LUSENA\nKarta z instrukcj\u0105 piel\u0119gnacji"
scrunchie[62] = 'FALSE'  # show_price_per_night (daytime product)
# Specs
scrunchie[63] = 'OEKO-TEX\u00ae Standard 100'
scrunchie[64] = ''  # closure N/A
scrunchie[65] = ''  # dimensions vary
scrunchie[66] = '6A (najwy\u017csza)'
scrunchie[67] = '100% jedwab morwowy (Mulberry Silk)'
scrunchie[68] = '22 momme'
scrunchie[69] = 'Charmeuse (splot satynowy)'
scrunchie[70] = ''  # weight PENDING
# Tagline (2026-03-17: benefit-oriented, no downward comparison)
scrunchie[71] = 'Ogranicza tarcie i \u0142amanie - jedwab chroni w\u0142osy lepiej ni\u017c syntetyczne gumki. Zachowuje kszta\u0142t i spr\u0119\u017cysto\u015b\u0107 - dzie\u0144 po dniu. Wch\u0142ania znacznie mniej olejk\u00f3w i kosmetyk\u00f3w - stylizacja zostaje na w\u0142osach, nie na gumce.'

# ============================================================
# Product 3: jedwabna-maska-3d
# ============================================================
mask = make_base_row()
mask[0] = 'jedwabna-maska-3d'
mask[1] = 'Jedwabna maska 3D do spania'
mask[5] = 'Maska do spania'
mask[6] = 'jedwab, maska-3d, maska-do-spania, 22-momme, nocna-rutyna, sen, konstrukcja-3d'
mask[22] = '169.00'
mask[35] = 'Jedwabna maska 3D do spania - 22 momme \u00b7 LUSENA'
mask[36] = 'Maska 3D z jedwabiu morwowego 22 momme. Nie uciska powiek, chroni rz\u0119sy, jedwab oddycha. Certyfikat OEKO-TEX\u00ae. Wysy\u0142ka z Polski.'
mask[37] = 'FALSE'
mask[38] = 'Wyprofilowane miseczki 3D nie dotykaj\u0105 powiek - oczy odpoczywaj\u0105 bez nacisku'
mask[39] = 'Jedwab minimalizuje tarcie wok\u00f3\u0142 oczu - tam, gdzie sk\u00f3ra jest najcie\u0144sza na ca\u0142ym ciele'
mask[40] = 'Profilowany mostek nosowy blokuje \u015bwiat\u0142o tam, gdzie p\u0142askie maski przepuszczaj\u0105'
mask[41] = ''  # care_steps empty
mask[42] = '\u015apisz w ciemno\u015bci - bez nacisku na powieki i rz\u0119sy.'
# Feature 1
mask[43] = 'Wyprofilowane miseczki tworz\u0105 przestrze\u0144 wok\u00f3\u0142 oczu - powieki i rz\u0119sy nie maj\u0105 kontaktu z materia\u0142em. Jedwab delikatnie przylega tylko wzd\u0142u\u017c kraw\u0119dzi. Swobodne mruganie, ochrona rz\u0119s - nawet doczepianych.'
mask[44] = 'heart'
mask[45] = '3D - oczy nie czuj\u0105 nacisku'
# Feature 3
mask[49] = 'Maski z poliestru i pianki gromadz\u0105 ciep\u0142o wok\u00f3\u0142 oczu. Jedwab morwowy oddycha naturalnie - ogranicza przegrzewanie, nawet latem. Najcie\u0144sza sk\u00f3ra na ciele zas\u0142uguje na naturalny materia\u0142.'
mask[50] = 'wind'
mask[51] = 'Jedwab oddycha - syntetyki nie'
# Feature 6
mask[58] = 'Ka\u017cda maska LUSENA przychodzi w eleganckim pude\u0142ku prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.'
mask[59] = 'gift'
mask[60] = 'Gotowa do wr\u0119czenia'
# Packaging
mask[61] = "Jedwabna maska 3D do spania LUSENA\nEleganckie pude\u0142ko prezentowe LUSENA\nKarta z instrukcj\u0105 piel\u0119gnacji"
mask[62] = 'TRUE'  # show_price_per_night
# Specs
mask[63] = 'OEKO-TEX\u00ae Standard 100'
mask[64] = 'Gumka pokryta jedwabiem'
mask[65] = ''  # dimensions PENDING
mask[66] = '6A (najwy\u017csza)'
mask[67] = '100% jedwab morwowy (Mulberry Silk)'
mask[68] = '22 momme'
mask[69] = 'Charmeuse (splot satynowy)'
mask[70] = ''  # weight PENDING
# Tagline (2026-03-17: benefit-oriented, self-referential mostek claim)
mask[71] = 'Wyprofilowane miseczki 3D nie dotykaj\u0105 powiek - oczy odpoczywaj\u0105 bez nacisku. Jedwab minimalizuje tarcie wok\u00f3\u0142 oczu, tam gdzie sk\u00f3ra jest najcie\u0144sza na ca\u0142ym ciele. Profilowany mostek nosowy blokuje \u015bwiat\u0142o bez szczelin.'

# ============================================================
# Product 4: heatless-curlers (most deviations)
# ============================================================
curlers = make_base_row()
curlers[0] = 'heatless-curlers'
curlers[1] = 'Jedwabny wa\u0142ek do lok\u00f3w'
curlers[5] = 'Wa\u0142ek do lok\u00f3w'
curlers[6] = 'jedwab, wa\u0142ek, loki, bez-ciep\u0142a, w\u0142osy, hair-care, heatless-curls'
curlers[22] = '219.00'
curlers[35] = 'Jedwabny wa\u0142ek do lok\u00f3w 22 momme - loki bez ciep\u0142a \u00b7 LUSENA'
curlers[36] = 'Jedwabny wa\u0142ek do lok\u00f3w LUSENA z jedwabiu morwowego 22 momme. Owijasz wilgotne w\u0142osy na noc - rano gotowe fale i loki. Jedwab ogranicza tarcie i wch\u0142ania znacznie mniej wilgoci z w\u0142os\u00f3w.'
curlers[37] = 'FALSE'
curlers[38] = 'Loki bez ciep\u0142a - w\u0142osy formuj\u0105 si\u0119 w nocy, bez ryzyka uszkodze\u0144 termicznych'
curlers[39] = 'Jedwab morwowy 22 momme wch\u0142ania znacznie mniej olejk\u00f3w i od\u017cywek - piel\u0119gnacja zostaje na w\u0142osach'
curlers[40] = 'G\u0142adka powierzchnia jedwabiu ogranicza tarcie - mniej szarpania i pl\u0105taniny przy zdejmowaniu'
# Custom care steps (PP cotton filling)
curlers[41] = "Przetrzyj jedwabn\u0105 powierzchni\u0119 wilgotn\u0105, mi\u0119kk\u0105 \u015bciereczk\u0105\nW razie potrzeby przepierz r\u0119cznie w letniej wodzie z delikatnym myd\u0142em\nNie pierz w pralce - wype\u0142nienie mo\u017ce si\u0119 odkszta\u0142ci\u0107\nSusz na p\u0142asko, z dala od bezpo\u015bredniego s\u0142o\u0144ca i \u017ar\u00f3de\u0142 ciep\u0142a\nPrzechowuj w pude\u0142ku LUSENA, \u017ceby zachowa\u0107 kszta\u0142t wa\u0142ka"
curlers[42] = 'Zdejmujesz wa\u0142ek rano - loki gotowe.'
# Feature 1 (product-specific — wind icon for "no heat")
curlers[43] = 'Temperatura narz\u0119dzi do stylizacji mo\u017ce si\u0119ga\u0107 230\u00b0C - a bia\u0142ko keratynowe w\u0142osa zaczyna traci\u0107 struktur\u0119 ju\u017c powy\u017cej 180\u00b0C. Jedwabny wa\u0142ek formuje loki mechanicznie, w nocy, bez jednego stopnia ciep\u0142a.'
curlers[44] = 'wind'
curlers[45] = 'Bez ciep\u0142a - bez uszkodze\u0144'
# Feature 3 (product-specific — clock icon for "overnight")
curlers[49] = 'Owijasz lekko wilgotne w\u0142osy wok\u00f3\u0142 wa\u0142ka, spinasz i k\u0142adziesz si\u0119 spa\u0107. Rano rozwijasz - fale lub loki gotowe. \u017badnego czekania z gor\u0105cym \u017celazkiem w r\u0119ku, \u017cadnego po\u015bpiechu przed wyj\u015bciem.'
curlers[50] = 'clock'
curlers[51] = 'Owijasz na noc - rano loki'
# Feature 6 (product name swapped)
curlers[58] = 'Ka\u017cdy jedwabny wa\u0142ek LUSENA przychodzi w eleganckim pude\u0142ku prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.'
curlers[59] = 'gift'
curlers[60] = 'Gotowa do wr\u0119czenia'
# Packaging (note: "użytkowania" not "pielęgnacji")
curlers[61] = "Jedwabny wa\u0142ek LUSENA\nEleganckie pude\u0142ko prezentowe LUSENA\nKarta z instrukcj\u0105 u\u017cytkowania"
curlers[62] = 'FALSE'  # show_price_per_night (not nightly product)
# Specs (custom material due to PP cotton filling)
curlers[63] = 'OEKO-TEX\u00ae Standard 100'
curlers[64] = ''  # closure N/A
curlers[65] = 'D\u0142ugo\u015b\u0107: 90 cm'
curlers[66] = '6A (najwy\u017csza)'
curlers[67] = 'Jedwab morwowy 22 momme + wype\u0142nienie z bawe\u0142ny PP'
curlers[68] = '22 momme'
curlers[69] = 'Charmeuse (splot satynowy)'
curlers[70] = ''  # weight PENDING
# Tagline (2026-03-17: benefit-oriented, kept disclaimer)
curlers[71] = 'Loki bez ciep\u0142a - w\u0142osy formuj\u0105 si\u0119 w nocy, bez ryzyka uszkodze\u0144 termicznych. Jedwab wch\u0142ania znacznie mniej olejk\u00f3w i od\u017cywek, wi\u0119c piel\u0119gnacja zostaje na w\u0142osach. G\u0142adka powierzchnia ogranicza tarcie - mniej szarpania i pl\u0105taniny przy zdejmowaniu. Efekt zale\u017cy od typu i d\u0142ugo\u015bci w\u0142os\u00f3w.'

# ============================================================
# Product 5: poszewka-jedwabna (flagship pillowcase)
# ============================================================
poszewka = make_base_row()
poszewka[0] = 'poszewka-jedwabna'
poszewka[1] = 'Poszewka jedwabna 50\u00d760'
poszewka[5] = 'Poszewka jedwabna'
poszewka[6] = 'jedwab, poszewka, 22-momme, nocna-rutyna, flagship'
poszewka[8] = 'Color'  # Multi-variant by color
poszewka[9] = 'zloty'  # Default variant
poszewka[10] = 'product.metafields.shopify.color-pattern'
poszewka[18] = '80.0'  # Variant Grams
poszewka[22] = '269.00'
poszewka[35] = 'Jedwabna poszewka 50\u00d760 na poduszk\u0119 - 22 momme \u00b7 LUSENA'
poszewka[36] = '100% jedwab morwowy z Suzhou. 22 momme, certyfikat OEKO-TEX\u00ae. Mniej zmarszczek, g\u0142adsze w\u0142osy - od pierwszej nocy.'
poszewka[37] = 'TRUE'  # badge_bestseller
poszewka[38] = 'Budzisz si\u0119 bez odcisk\u00f3w poduszki - jedwab nie gniecie sk\u00f3ry jak bawe\u0142na'
poszewka[39] = 'Wch\u0142ania znacznie mniej krem\u00f3w i serum - piel\u0119gnacja zostaje na sk\u00f3rze, nie na poszewce'
poszewka[40] = 'W\u0142osy bez pl\u0105taniny i puszenia - fryzura przetrwa noc bez wysi\u0142ku'
poszewka[41] = ''  # care_steps empty (theme defaults)
poszewka[42] = 'Obud\u017a si\u0119 bez zagniece\u0144 - od pierwszej nocy.'
# Feature 1 (product-specific)
poszewka[43] = 'Zmarszczki senne (sleep wrinkles) to efekt gniecenia sk\u00f3ry przez poduszk\u0119 - ka\u017cdej nocy, godzina po godzinie. G\u0142adki jedwab morwowy sprzyja redukcji tego tarcia. Efekt wida\u0107 rano w lustrze.'
poszewka[44] = 'heart'
poszewka[45] = 'Mniej tarcia, mniej odcisk\u00f3w'
# Feature 3 (product-specific)
poszewka[49] = 'Jedwab pomaga naturalnie regulowa\u0107 temperatur\u0119 - w\u0142\u00f3kna bia\u0142ka jedwabnego odprowadzaj\u0105 wilgo\u0107 i oddychaj\u0105. Latem utrzymuje ch\u0142\u00f3d, zim\u0105 nie wych\u0142adza. Koniec z obracaniem poduszki w poszukiwaniu zimnej strony.'
poszewka[50] = 'wind'
poszewka[51] = 'Ch\u0142odna strona - ca\u0142\u0105 noc'
# Feature 6 (universal but product name swapped)
poszewka[58] = 'Ka\u017cda poszewka LUSENA przychodzi w eleganckim pude\u0142ku prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.'
poszewka[59] = 'gift'
poszewka[60] = 'Gotowa do wr\u0119czenia'
# Packaging
poszewka[61] = "Jedwabna poszewka LUSENA\nEleganckie pude\u0142ko prezentowe LUSENA\nKarta z instrukcj\u0105 piel\u0119gnacji"
poszewka[62] = 'TRUE'  # show_price_per_night
# Specs
poszewka[63] = 'OEKO-TEX\u00ae Standard 100'
poszewka[64] = 'Koperta'
poszewka[65] = '50 \u00d7 60 cm'
poszewka[66] = '6A (najwy\u017csza)'
poszewka[67] = '100% jedwab morwowy (Mulberry Silk)'
poszewka[68] = '22 momme'
poszewka[69] = 'Charmeuse (splot satynowy)'
poszewka[70] = '80 g'
# Tagline (2026-03-17: benefit-oriented, removed redundant specs)
poszewka[71] = 'Budzisz si\u0119 bez odcisk\u00f3w poduszki - jedwab nie gniecie sk\u00f3ry jak bawe\u0142na. Wch\u0142ania znacznie mniej krem\u00f3w i serum, wi\u0119c piel\u0119gnacja zostaje na sk\u00f3rze zamiast na poszewce. W\u0142osy bez pl\u0105taniny i puszenia - fryzura przetrwa noc bez wysi\u0142ku.'

# Additional variant rows for poszewka (color variants)
poszewka_gray = make_empty_row()
poszewka_gray[0] = 'poszewka-jedwabna'
poszewka_gray[9] = 'gray'
poszewka_gray[18] = '80.0'
poszewka_gray[19] = 'shopify'
poszewka_gray[20] = 'continue'
poszewka_gray[21] = 'manual'
poszewka_gray[22] = '269.00'
poszewka_gray[24] = 'true'
poszewka_gray[25] = 'true'
poszewka_gray[80] = 'g'

poszewka_gold = make_empty_row()
poszewka_gold[0] = 'poszewka-jedwabna'
poszewka_gold[9] = 'gold'
poszewka_gold[18] = '80.0'
poszewka_gold[19] = 'shopify'
poszewka_gold[20] = 'continue'
poszewka_gold[21] = 'manual'
poszewka_gold[22] = '269.00'
poszewka_gold[24] = 'true'
poszewka_gold[25] = 'true'
poszewka_gold[80] = 'g'

poszewka_pink = make_empty_row()
poszewka_pink[0] = 'poszewka-jedwabna'
poszewka_pink[9] = 'pink'
poszewka_pink[18] = '80.0'
poszewka_pink[19] = 'shopify'
poszewka_pink[20] = 'continue'
poszewka_pink[21] = 'manual'
poszewka_pink[22] = '269.00'
poszewka_pink[24] = 'true'
poszewka_pink[25] = 'true'
poszewka_pink[80] = 'g'

# ============================================================
# Write separate CSV per product
# ============================================================
single_variant_products = [bonnet, scrunchie, mask, curlers]

for product in single_variant_products:
    handle = product[0]
    filename = f'{handle}_import.csv'
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(header)
    writer.writerow(product)
    with open(filename, 'wb') as f:
        f.write(b'\xef\xbb\xbf')  # UTF-8 BOM
        f.write(output.getvalue().encode('utf-8'))
    print(f"Generated {filename} ({len(product)} columns, price={product[22]})")

# Poszewka has multiple color variants — write all rows
filename = 'poszewka-jedwabna_import.csv'
output = io.StringIO()
writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
writer.writerow(header)
writer.writerow(poszewka)
writer.writerow(poszewka_gray)
writer.writerow(poszewka_gold)
writer.writerow(poszewka_pink)
with open(filename, 'wb') as f:
    f.write(b'\xef\xbb\xbf')  # UTF-8 BOM
    f.write(output.getvalue().encode('utf-8'))
print(f"Generated {filename} ({len(poszewka)} columns, price={poszewka[22]}, 4 variants)")
