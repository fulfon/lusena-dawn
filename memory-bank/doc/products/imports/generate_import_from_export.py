"""
Generate Shopify import file from a fresh export.

Workflow:
1. Export all products from Shopify admin (Products > Export > CSV for Excel)
2. Save as: ../exports/products_export.csv
3. Run: cd imports && python generate_import_from_export.py
4. Import: imports/products_import_updated.csv into Shopify with "Overwrite" checked

This script reads the export, updates ONLY the copy/metafield columns (35-73)
and upsell text columns (74, 76) with current values from the MD product files,
and writes the result. Upsell product references (cols 75, 77) must be set
manually in Shopify admin (CSV can't set product_reference metafields).
All other columns (variants, prices, inventory, images) are preserved as-is.

Updated: 2026-03-28
"""
import csv
import io

# Read fresh export
with open('../exports/products_export.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = list(next(reader))
    rows = list(reader)

print(f'Read export: {len(header)} cols, {len(rows)} rows')

# Build updates: handle -> {col_index: value}
# We update cols 35-73 (SEO + all lusena.* metafields) + cols 74, 76 (upsell text fields)
# Col 38 (bundle_original_price) is skipped — kept from export
# Cols 75, 77 (upsell_primary, upsell_secondary) are product references — set manually in admin
updates = {}

# ============================================================
# POSZEWKA JEDWABNA (re-evaluated 2026-03-22)
# ============================================================
updates['poszewka-jedwabna'] = {
    35: 'Jedwabna poszewka 50\u00d760 na poduszk\u0119 - 22 momme \u00b7 LUSENA',
    36: '100% jedwab morwowy z Suzhou. 22 momme, certyfikat OEKO-TEX\u00ae. Mniej zmarszczek, g\u0142adsze w\u0142osy - od pierwszej nocy.',
    37: 'TRUE',
    39: 'Budzisz si\u0119 bez odcisk\u00f3w poduszki - jedwab nie gniecie sk\u00f3ry jak bawe\u0142na',
    40: 'Wch\u0142ania znacznie mniej krem\u00f3w i serum - piel\u0119gnacja zostaje na sk\u00f3rze, nie na poszewce',
    41: 'W\u0142osy bez spl\u0105ta\u0144 i puszenia - fryzura przetrwa noc bez wysi\u0142ku',
    43: 'Obud\u017a si\u0119 bez zagniece\u0144 - od pierwszej nocy.',
    44: 'Zmarszczki senne (sleep wrinkles) to efekt gniecenia sk\u00f3ry przez poduszk\u0119 - ka\u017cdej nocy, godzina po godzinie. G\u0142adki jedwab morwowy zmniejsza to tarcie. Efekt wida\u0107 rano w lustrze.',
    45: 'heart',
    46: 'Mniej tarcia, mniej odcisk\u00f3w',
    47: 'Momme to g\u0119sto\u015b\u0107 jedwabiu \u2013 im wy\u017csze, tym grubszy i trwalszy materia\u0142. Standard rynkowy to 16\u201319 momme. Nasze 22 momme to g\u0119stszy splot, kt\u00f3ry lepiej trzyma kszta\u0142t i d\u0142u\u017cej s\u0142u\u017cy.',
    48: 'layers', 49: 'Dlaczego 22 momme?',
    50: 'Jedwab pomaga naturalnie regulowa\u0107 temperatur\u0119 - w\u0142\u00f3kna jedwabiu odprowadzaj\u0105 wilgo\u0107 i oddychaj\u0105. Latem utrzymuje ch\u0142\u00f3d, zim\u0105 nie wych\u0142adza. Koniec z obracaniem poduszki w poszukiwaniu zimnej strony.',
    51: 'wind', 52: 'Ch\u0142odna strona - ca\u0142\u0105 noc',
    53: 'Satyna to nazwa splotu, nie materia\u0142u \u2013 najcz\u0119\u015bciej kryje si\u0119 za ni\u0105 poliester. LUSENA to 100% jedwab morwowy: naturalne w\u0142\u00f3kno bia\u0142kowe, kt\u00f3re oddycha i nie elektryzuje.',
    54: 'shield-check', 55: 'Jedwab, nie satyna z poliestru',
    56: 'Twoja twarz spoczywa na poszewce 8 godzin ka\u017cdej nocy. To powinien by\u0107 najczystszy materia\u0142 w Twojej sypialni - i jest. Jedwab morwowy to czyste bia\u0142ko, sama natura.',
    57: 'sparkles', 58: 'Czysty jedwab, czysta sk\u00f3ra',
    59: 'Ka\u017cda poszewka LUSENA przychodzi w eleganckim pude\u0142ku prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.',
    60: 'gift', 61: 'Gotowa do wr\u0119czenia',
    62: 'Jedwabna poszewka LUSENA\nEleganckie pude\u0142ko prezentowe LUSENA\nKarta z instrukcj\u0105 piel\u0119gnacji',
    63: 'TRUE',
    73: 'Budzisz si\u0119 bez odcisk\u00f3w poduszki - jedwab nie gniecie sk\u00f3ry jak bawe\u0142na. Wch\u0142ania znacznie mniej krem\u00f3w i serum, wi\u0119c piel\u0119gnacja zostaje na sk\u00f3rze, nie na poszewce. W\u0142osy bez spl\u0105ta\u0144 i puszenia - fryzura przetrwa noc bez wysi\u0142ku.',
    74: 'Jedwab na noc - obudź się bez zagnieceń',
    76: 'hero',
}

# ============================================================
# SILK BONNET (re-evaluated 2026-03-22)
# ============================================================
updates['silk-bonnet'] = {
    35: 'Jedwabny czepek do spania 22 momme - ochrona w\u0142os\u00f3w \u00b7 LUSENA',
    36: 'Jedwabny czepek z regulacj\u0105 obwodu - 22 momme, Grade 6A z Suzhou. \u015aci\u0105gacz pokryty jedwabiem chroni lini\u0119 w\u0142os\u00f3w. Mniej tarcia, mniej pl\u0105tania. OEKO-TEX\u00ae.',
    37: 'FALSE',
    39: 'Otula w\u0142osy g\u0142adkim jedwabiem ze wszystkich stron - mniej tarcia, pl\u0105tania i puszenia ni\u017c na bawe\u0142nie',
    40: 'Regulowany \u015bci\u0105gacz pokryty jedwabiem - dopasujesz go do swojej g\u0142owy, \u017cadne gumowe w\u0142\u00f3kno nie dotyka w\u0142os\u00f3w',
    41: 'Chroni fryzur\u0119 od wieczora do rana - loki, fale czy prostowanie przetrwaj\u0105 noc',
    43: 'Budzisz si\u0119 z fryzur\u0105 - nie z pl\u0105tanin\u0105.',
    44: 'Zwyk\u0142e czepki maj\u0105 ods\u0142oni\u0119t\u0105 gumk\u0119, kt\u00f3ra \u015bciska i ociera najdelikatniejsze pasma. W czepku LUSENA \u015bci\u0105gacz jest pokryty jedwabiem od wewn\u0105trz - g\u0142adkie w\u0142\u00f3kno zamiast twardej gumy.',
    45: 'heart', 46: 'Chroni lini\u0119 w\u0142os\u00f3w',
    47: 'Momme to g\u0119sto\u015b\u0107 jedwabiu \u2013 im wy\u017csze, tym grubszy i trwalszy materia\u0142. Standard rynkowy to 16\u201319 momme. Nasze 22 momme to g\u0119stszy splot, kt\u00f3ry lepiej trzyma kszta\u0142t i d\u0142u\u017cej s\u0142u\u017cy.',
    48: 'layers', 49: 'Dlaczego 22 momme?',
    50: 'Regulowany \u015bci\u0105gacz dopasujesz dok\u0142adnie do swojej g\u0142owy - ani za lu\u017ano, ani za ciasno. Jedwab morwowy oddycha i pomaga regulowa\u0107 temperatur\u0119. Budzisz si\u0119 w czepku, nie obok niego.',
    51: 'wind', 52: 'Trzyma pewnie ca\u0142\u0105 noc',
    53: 'Satyna to nazwa splotu, nie materia\u0142u \u2013 najcz\u0119\u015bciej kryje si\u0119 za ni\u0105 poliester. LUSENA to 100% jedwab morwowy: naturalne w\u0142\u00f3kno bia\u0142kowe, kt\u00f3re oddycha i nie elektryzuje.',
    54: 'shield-check', 55: 'Jedwab, nie satyna z poliestru',
    56: 'Nak\u0142adasz olejek albo mask\u0119 i zak\u0142adasz czepek - jedwab otacza w\u0142osy ze wszystkich stron, wi\u0119c kosmetyki pracuj\u0105 przez ca\u0142\u0105 noc zamiast wsi\u0105ka\u0107 w poduszk\u0119. Rano efekt jest na w\u0142osach, nie na po\u015bcieli.',
    57: 'droplets', 58: 'Olejek zostaje we w\u0142osach',
    59: 'Ka\u017cdy czepek LUSENA przychodzi w eleganckim pude\u0142ku prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.',
    60: 'gift', 61: 'Gotowa do wr\u0119czenia',
    62: 'Jedwabny czepek LUSENA\nEleganckie pude\u0142ko prezentowe LUSENA\nKarta z instrukcj\u0105 piel\u0119gnacji',
    63: 'TRUE',
    73: 'Otula w\u0142osy g\u0142adkim jedwabiem ze wszystkich stron - mniej tarcia, pl\u0105tania i puszenia ni\u017c na bawe\u0142nie. Regulowany \u015bci\u0105gacz pokryty jedwabiem dopasowuje si\u0119 do kszta\u0142tu g\u0142owy. Chroni fryzur\u0119 od wieczora do rana - loki, fale czy prostowanie przetrwaj\u0105 noc.',
    74: 'Kompletna ochrona w\u0142os\u00f3w na noc',
    76: 'hero',
}

# ============================================================
# JEDWABNA MASKA 3D (re-evaluated 2026-03-22 — no changes)
# ============================================================
updates['jedwabna-maska-3d'] = {
    35: 'Jedwabna maska 3D do spania - 22 momme \u00b7 LUSENA',
    36: 'Maska 3D z jedwabiu morwowego 22 momme. Nie uciska powiek, chroni rz\u0119sy, jedwab oddycha. Certyfikat OEKO-TEX\u00ae. Wysy\u0142ka z Polski.',
    37: 'FALSE',
    39: 'Wyprofilowane miseczki 3D nie dotykaj\u0105 powiek - oczy odpoczywaj\u0105 bez nacisku',
    40: 'Jedwab minimalizuje tarcie wok\u00f3\u0142 oczu - tam, gdzie sk\u00f3ra jest najcie\u0144sza na ca\u0142ym ciele',
    41: 'Profilowany mostek nosowy blokuje \u015bwiat\u0142o tam, gdzie p\u0142askie maski przepuszczaj\u0105',
    43: '\u015apisz w ciemno\u015bci - bez nacisku na powieki i rz\u0119sy.',
    44: 'Wyprofilowane miseczki tworz\u0105 przestrze\u0144 wok\u00f3\u0142 oczu - powieki i rz\u0119sy nie maj\u0105 kontaktu z materia\u0142em. Jedwab delikatnie przylega tylko wzd\u0142u\u017c kraw\u0119dzi. Swobodne mruganie, ochrona rz\u0119s - nawet doczepianych.',
    45: 'heart', 46: '3D - oczy nie czuj\u0105 nacisku',
    47: 'Momme to g\u0119sto\u015b\u0107 jedwabiu \u2013 im wy\u017csze, tym grubszy i trwalszy materia\u0142. Standard rynkowy to 16\u201319 momme. Nasze 22 momme to g\u0119stszy splot, kt\u00f3ry lepiej trzyma kszta\u0142t i d\u0142u\u017cej s\u0142u\u017cy.',
    48: 'layers', 49: 'Dlaczego 22 momme?',
    50: 'Maski z poliestru i pianki gromadz\u0105 ciep\u0142o wok\u00f3\u0142 oczu. Jedwab morwowy oddycha naturalnie - ogranicza przegrzewanie, nawet latem. Najcie\u0144sza sk\u00f3ra na ciele zas\u0142uguje na naturalny materia\u0142.',
    51: 'wind', 52: 'Jedwab oddycha - syntetyki nie',
    53: 'Satyna to nazwa splotu, nie materia\u0142u \u2013 najcz\u0119\u015bciej kryje si\u0119 za ni\u0105 poliester. LUSENA to 100% jedwab morwowy: naturalne w\u0142\u00f3kno bia\u0142kowe, kt\u00f3re oddycha i nie elektryzuje.',
    54: 'shield-check', 55: 'Jedwab, nie satyna z poliestru',
    56: 'Zwyk\u0142a gumka zostawia czerwone \u015blady na skroniach i ci\u0105gnie w\u0142osy. Tu jest pokryta jedwabiem - delikatnie przylega, nie wgniata si\u0119, nie ci\u0105gnie. Zapominasz, \u017ce j\u0105 masz.',
    57: 'feather', 58: 'Nawet gumka jest jedwabna',
    59: 'Ka\u017cda maska LUSENA przychodzi w eleganckim pude\u0142ku prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.',
    60: 'gift', 61: 'Gotowa do wr\u0119czenia',
    62: 'Jedwabna maska 3D do spania LUSENA\nEleganckie pude\u0142ko prezentowe LUSENA\nKarta z instrukcj\u0105 piel\u0119gnacji',
    63: 'TRUE',
    73: 'Wyprofilowane miseczki 3D nie dotykaj\u0105 powiek - oczy odpoczywaj\u0105 bez nacisku. Jedwab minimalizuje tarcie wok\u00f3\u0142 oczu, tam gdzie sk\u00f3ra jest najcie\u0144sza na ca\u0142ym ciele. Profilowany mostek nosowy blokuje \u015bwiat\u0142o bez szczelin.',
    74: 'Ciemno\u015b\u0107 bez nacisku na powieki',
}

# ============================================================
# SILK SCRUNCHIE (re-evaluated 2026-03-22)
# ============================================================
updates['silk-scrunchie'] = {
    35: 'Jedwabny scrunchie 22 momme - mniej \u0142amania w\u0142os\u00f3w \u00b7 LUSENA',
    36: 'Scrunchie z prawdziwego jedwabiu morwowego 22 momme. Mniej tarcia, mniej \u0142amania - w\u0142osy poczuj\u0105 r\u00f3\u017cnic\u0119. Certyfikat OEKO-TEX\u00ae Standard 100.',
    37: 'FALSE',
    39: 'Ogranicza tarcie i \u0142amanie - jedwab chroni w\u0142osy lepiej ni\u017c syntetyczne gumki',
    40: 'Nie traci formy po kilku u\u017cyciach - jedwab zachowuje spr\u0119\u017cysto\u015b\u0107 na d\u0142ugo',
    41: 'Wch\u0142ania znacznie mniej olejk\u00f3w i kosmetyk\u00f3w - to, co nak\u0142adasz, zostaje na w\u0142osach, nie na gumce',
    43: 'Zdejmujesz gumk\u0119 - w\u0142osy zostaj\u0105 na miejscu.',
    44: 'Jedwab morwowy ma naturalnie g\u0142adk\u0105 powierzchni\u0119 - ogranicza tarcie, kt\u00f3re prowadzi do \u0142amania i rozdwajania ko\u0144c\u00f3wek. Twoje w\u0142osy po prostu zsuwaj\u0105 si\u0119 z gumki, zamiast si\u0119 rwa\u0107.',
    45: 'heart', 46: 'Chroni struktur\u0119 w\u0142osa',
    47: 'Momme to g\u0119sto\u015b\u0107 jedwabiu \u2013 im wy\u017csze, tym grubszy i trwalszy materia\u0142. Standard rynkowy to 16\u201319 momme. Nasze 22 momme to g\u0119stszy splot, kt\u00f3ry lepiej trzyma kszta\u0142t i d\u0142u\u017cej s\u0142u\u017cy.',
    48: 'layers', 49: 'Dlaczego 22 momme?',
    50: 'Jedwab ogranicza elektryczno\u015b\u0107 statyczn\u0105, przez kt\u00f3r\u0105 w\u0142osy pusz\u0105 si\u0119 i stercz\u0105. Zdejmujesz gumk\u0119 - fryzura wygl\u0105da tak, jak j\u0105 zostawi\u0142a\u015b. Bez niespodzianek, kt\u00f3re znasz ze zwyk\u0142ych gumek.',
    51: 'wind', 52: 'Mniej puszenia w\u0142os\u00f3w',
    53: 'Satyna to nazwa splotu, nie materia\u0142u \u2013 najcz\u0119\u015bciej kryje si\u0119 za ni\u0105 poliester. LUSENA to 100% jedwab morwowy: naturalne w\u0142\u00f3kno bia\u0142kowe, kt\u00f3re oddycha i nie elektryzuje.',
    54: 'shield-check', 55: 'Jedwab, nie satyna z poliestru',
    56: 'Jedwab rozk\u0142ada nacisk r\u00f3wnomiernie na ca\u0142\u0105 szeroko\u015b\u0107 gumki - nie \u015bciska w jednej cienkiej linii. Po ca\u0142ym dniu, nawet po nocy - znacznie mniejszy \u015blad ni\u017c po zwyk\u0142ej gumce.',
    57: 'moon', 58: 'Bez \u015bladu po gumce',
    59: 'Ka\u017cda gumka LUSENA przychodzi w eleganckim pude\u0142ku prezentowym - idealny drobny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.',
    60: 'gift', 61: 'Gotowa do wr\u0119czenia',
    62: 'Jedwabna gumka LUSENA\nEleganckie pude\u0142ko prezentowe LUSENA\nKarta z instrukcj\u0105 piel\u0119gnacji',
    63: 'FALSE',
    73: 'Ogranicza tarcie i \u0142amanie - jedwab chroni w\u0142osy lepiej ni\u017c syntetyczne gumki. Zachowuje kszta\u0142t i spr\u0119\u017cysto\u015b\u0107 - dzie\u0144 po dniu. Wch\u0142ania znacznie mniej olejk\u00f3w i kosmetyk\u00f3w - to, co nak\u0142adasz, zostaje na w\u0142osach, nie na gumce.',
    74: 'Jedwab na dzie\u0144 - mniej tarcia, mniej \u0142amania',
}

# ============================================================
# HEATLESS CURLERS (re-evaluated 2026-03-22)
# ============================================================
updates['heatless-curlers'] = {
    35: 'Jedwabny wa\u0142ek do lok\u00f3w 22 momme - loki bez ciep\u0142a \u00b7 LUSENA',
    36: 'Jedwabny wa\u0142ek do lok\u00f3w LUSENA 22 momme. Owijasz wilgotne w\u0142osy na noc - rano gotowe loki. Jedwab ogranicza tarcie i chroni piel\u0119gnacj\u0119.',
    37: 'FALSE',
    39: 'Loki bez ciep\u0142a - w\u0142osy formuj\u0105 si\u0119 w nocy, bez ryzyka uszkodze\u0144 termicznych',
    40: 'Olejek i od\u017cywka zostaj\u0105 na w\u0142osach - jedwab wch\u0142ania znacznie mniej ni\u017c syntetyczne wa\u0142ki',
    41: 'G\u0142adka powierzchnia jedwabiu ogranicza tarcie - mniej szarpania i pl\u0105taniny przy zdejmowaniu',
    43: 'Zdejmujesz wa\u0142ek rano - loki gotowe.',
    44: 'Temperatura narz\u0119dzi do stylizacji mo\u017ce si\u0119ga\u0107 230\u00b0C - a bia\u0142ko keratynowe w\u0142osa zaczyna traci\u0107 struktur\u0119 ju\u017c powy\u017cej 180\u00b0C. Jedwabny wa\u0142ek formuje loki mechanicznie, w nocy, bez jednego stopnia ciep\u0142a.',
    45: 'wind', 46: 'Bez ciep\u0142a - bez uszkodze\u0144',
    47: 'Momme to g\u0119sto\u015b\u0107 jedwabiu \u2013 im wy\u017csze, tym grubszy i trwalszy materia\u0142. Standard rynkowy to 16\u201319 momme. Nasze 22 momme to g\u0119stszy splot, kt\u00f3ry lepiej trzyma kszta\u0142t i d\u0142u\u017cej s\u0142u\u017cy.',
    48: 'layers', 49: 'Dlaczego 22 momme?',
    50: 'Owijasz lekko wilgotne w\u0142osy wok\u00f3\u0142 wa\u0142ka, spinasz i k\u0142adziesz si\u0119 spa\u0107. Rano rozwijasz - fale lub loki gotowe. \u017badnego czekania z gor\u0105cym \u017celazkiem w r\u0119ku, \u017cadnego po\u015bpiechu przed wyj\u015bciem.',
    51: 'clock', 52: 'Owijasz na noc - rano loki',
    53: 'Satyna to nazwa splotu, nie materia\u0142u \u2013 najcz\u0119\u015bciej kryje si\u0119 za ni\u0105 poliester. LUSENA to 100% jedwab morwowy: naturalne w\u0142\u00f3kno bia\u0142kowe, kt\u00f3re oddycha i nie elektryzuje.',
    54: 'shield-check', 55: 'Jedwab, nie satyna z poliestru',
    56: 'Wiele wa\u0142k\u00f3w ma sztywny rdze\u0144 z pianki - taki, kt\u00f3ry czujesz przez ca\u0142\u0105 noc. Nasz ma woln\u0105 przestrze\u0144 na \u015brodku - nic nie uciska g\u00f3ry g\u0142owy i mo\u017cesz wygodnie spa\u0107. Mi\u0119kkie wype\u0142nienie jest tylko po bokach, tam gdzie formuj\u0105 si\u0119 loki.',
    57: 'heart', 58: 'Mi\u0119kki - nie uciska w nocy',
    59: 'Ka\u017cdy jedwabny wa\u0142ek LUSENA przychodzi w eleganckim pude\u0142ku prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.',
    60: 'gift', 61: 'Gotowa do wr\u0119czenia',
    63: 'FALSE',
    73: 'Loki bez ciep\u0142a - w\u0142osy formuj\u0105 si\u0119 w nocy, bez ryzyka uszkodze\u0144 termicznych. Jedwab wch\u0142ania znacznie mniej olejk\u00f3w i od\u017cywek, wi\u0119c piel\u0119gnacja zostaje na w\u0142osach. G\u0142adka powierzchnia ogranicza tarcie - mniej szarpania i pl\u0105taniny przy zdejmowaniu. Efekt zale\u017cy od typu i d\u0142ugo\u015bci w\u0142os\u00f3w.',
    74: 'Loki bez ciep\u0142a - jedwab formuje fale w nocy',
}

# ============================================================
# NOCNA RUTYNA bundle (re-evaluated 2026-03-22)
# ============================================================
updates['nocna-rutyna'] = {
    35: 'Nocna Rutyna - jedwabna poszewka i czepek w zestawie \u00b7 LUSENA',
    36: 'Jedwabna poszewka 50x60 + czepek do spania w jednym zestawie. Oszcz\u0119dzasz 109 z\u0142. Jedwab dla sk\u00f3ry i w\u0142os\u00f3w - na ca\u0142\u0105 noc. 22 momme, OEKO-TEX\u00ae.',
    37: 'TRUE',
    39: 'Zasypiasz w jedwabiu - twarz na g\u0142adkiej poszewce, w\u0142osy pod lekkim czepkiem',
    40: 'Jedwab wch\u0142ania znacznie mniej ni\u017c bawe\u0142na - krem zostaje na sk\u00f3rze, olejek na w\u0142osach',
    41: 'Mniej tarcia od pierwszej nocy - i na twarzy, i we w\u0142osach',
    43: 'Twarz bez zagniece\u0144, w\u0142osy bez pl\u0105taniny.',
    44: 'Poszewka k\u0142adzie g\u0142adk\u0105 powierzchni\u0119 pod twarz - mniej tarcia, mniej zagniece\u0144. Czepek otula w\u0142osy ze wszystkich stron - mniej pl\u0105tania, mniej puszenia. Dwa produkty, jeden materia\u0142, pe\u0142na rutyna.',
    45: 'heart', 46: 'Inna ochrona, ten sam jedwab',
    47: 'Momme to g\u0119sto\u015b\u0107 jedwabiu \u2013 im wy\u017csze, tym grubszy i trwalszy materia\u0142. Standard rynkowy to 16\u201319 momme. Nasze 22 momme to g\u0119stszy splot, kt\u00f3ry lepiej trzyma kszta\u0142t i d\u0142u\u017cej s\u0142u\u017cy.',
    48: 'layers', 49: 'Dlaczego 22 momme?',
    50: 'Zak\u0142adasz poszewk\u0119, naci\u0105gasz czepek - gotowe. Przez 8 godzin g\u0142adki jedwab ogranicza tarcie na twarzy i we w\u0142osach jednocze\u015bnie. Im d\u0142u\u017cej, tym lepiej wida\u0107 r\u00f3\u017cnic\u0119.',
    51: 'clock', 52: 'Rutyna na ka\u017cd\u0105 noc',
    53: 'Satyna to nazwa splotu, nie materia\u0142u \u2013 najcz\u0119\u015bciej kryje si\u0119 za ni\u0105 poliester. LUSENA to 100% jedwab morwowy: naturalne w\u0142\u00f3kno bia\u0142kowe, kt\u00f3re oddycha i nie elektryzuje.',
    54: 'shield-check', 55: 'Jedwab, nie satyna z poliestru',
    56: 'Sama poszewka nie ochroni w\u0142os\u00f3w. Sam czepek nie ochroni twarzy. Dopiero razem daj\u0105 Ci poranek, kt\u00f3ry zaczyna si\u0119 od kawy, nie od szczotki.',
    57: 'wind', 58: 'Poranek bez porannej rutyny',
    59: 'Ka\u017cdy zestaw LUSENA przychodzi w eleganckim opakowaniu prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.',
    60: 'gift', 61: 'Gotowe do wr\u0119czenia',
    63: 'FALSE',
    73: 'Poszewka chroni sk\u00f3r\u0119, ale w\u0142osy nadal maj\u0105 kontakt z poduszk\u0105 przez 8 godzin. Czepek zamyka t\u0119 luk\u0119 - razem masz pe\u0142n\u0105 rutyn\u0119 na noc.',
    74: 'Kompletna ochrona na noc - twarz i w\u0142osy',
    76: 'bundle',
}

# ============================================================
# PIEKNY SEN bundle (written with copywriter flow 2026-03-22)
# ============================================================
updates['piekny-sen'] = {
    35: 'Pi\u0119kny Sen - jedwabna poszewka i maska 3D w zestawie \u00b7 LUSENA',
    36: 'Jedwabna poszewka 50x60 + maska 3D do spania w jednym zestawie. Oszcz\u0119dzasz 89 z\u0142. Mniej tarcia na twarzy, ciemno\u015b\u0107 i spok\u00f3j dla oczu. OEKO-TEX\u00ae.',
    37: 'FALSE',
    39: 'Ciemno\u015b\u0107 pod mask\u0105 i g\u0142adko\u015b\u0107 poszewki - warunki, w kt\u00f3rych \u0142atwiej odpocz\u0105\u0107',
    40: 'Krem i serum pod oczy pracuj\u0105 do rana - jedwab wch\u0142ania znacznie mniej ni\u017c bawe\u0142na',
    41: 'Policzek na g\u0142adkim jedwabiu, oczy w pe\u0142nym mroku - czujesz r\u00f3\u017cnic\u0119 od pierwszej nocy',
    43: 'Pi\u0119kniejszy poranek zaczyna si\u0119 wieczorem.',
    44: 'Poszewka chroni sk\u00f3r\u0119 twarzy przed tarciem - policzki, czo\u0142o, brod\u0119. Maska 3D otula okolice oczu bez nacisku na powieki. Razem pokrywaj\u0105 ca\u0142\u0105 twarz - \u017cadna sk\u00f3ra nie zostaje bez ochrony.',
    45: 'moon', 46: 'Od policzka po powieki',
    47: 'Momme to g\u0119sto\u015b\u0107 jedwabiu \u2013 im wy\u017csze, tym grubszy i trwalszy materia\u0142. Standard rynkowy to 16\u201319 momme. Nasze 22 momme to g\u0119stszy splot, kt\u00f3ry lepiej trzyma kszta\u0142t i d\u0142u\u017cej s\u0142u\u017cy.',
    48: 'layers', 49: 'Dlaczego 22 momme?',
    50: 'Mniej zagniece\u0144 na policzku, okolice oczu odci\u0105\u017cone, twarz otulona jedwabiem przez osiem godzin. Poszewka ogranicza tarcie na sk\u00f3rze, maska daje oczom ciemno\u015b\u0107 i spok\u00f3j - efekt wida\u0107 rano w lustrze.',
    51: 'heart', 52: 'Ranek po pi\u0119knym \u015bnie',
    53: 'Satyna to nazwa splotu, nie materia\u0142u \u2013 najcz\u0119\u015bciej kryje si\u0119 za ni\u0105 poliester. LUSENA to 100% jedwab morwowy: naturalne w\u0142\u00f3kno bia\u0142kowe, kt\u00f3re oddycha i nie elektryzuje.',
    54: 'shield-check', 55: 'Jedwab, nie satyna z poliestru',
    56: 'Tw\u00f3j wiecz\u00f3r si\u0119 nie zmienia. Poszewka trafia na t\u0119 sam\u0105 poduszk\u0119. Mask\u0119 zak\u0142adasz w pi\u0119\u0107 sekund. Zmienia si\u0119 jedno - materia\u0142, kt\u00f3ry dotyka Twojej twarzy przez ca\u0142\u0105 noc.',
    57: 'clock', 58: 'Nic nowego w Twojej rutynie',
    59: 'Ka\u017cdy zestaw LUSENA przychodzi w eleganckim opakowaniu prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.',
    60: 'gift', 61: 'Gotowe do wr\u0119czenia',
    63: 'FALSE',
    73: 'Jedwabna poszewka chroni twarz przed tarciem przez ca\u0142\u0105 noc. Ale okolice oczu potrzebuj\u0105 czego\u015b innego - ciemno\u015bci i braku nacisku na powieki. Maska 3D zamyka t\u0119 luk\u0119 - ca\u0142a twarz w jedwabiu.',
    74: 'Jedwabna ochrona twarzy i oczu',
    76: 'bundle',
}

# ============================================================
# SCRUNCHIE TRIO bundle (written with copywriter flow 2026-03-22)
# ============================================================
updates['scrunchie-trio'] = {
    35: 'Scrunchie Trio - 3 jedwabne gumki w zestawie \u00b7 LUSENA',
    36: 'Trzy jedwabne scrunchie w zestawie za 139 z\u0142 (zamiast 177 z\u0142). Czarny, Brudny r\u00f3\u017c, Szampan - 22 momme, OEKO-TEX\u00ae. Idealny prezent.',
    37: 'FALSE',
    39: 'Czarna do pracy, r\u00f3\u017cowa na weekend, szampanowa na wyj\u015bcie - dobierasz do nastroju, nie do tego, co zosta\u0142o w szufladzie',
    40: 'Jedna w torebce, jedna w \u0142azience, jedna na nadgarstku - nie szukasz, nie po\u017cyczasz, nie si\u0119gasz po syntetyczn\u0105',
    41: 'Trzy w rotacji - ka\u017cda odpoczywa mi\u0119dzy u\u017cyciami, wi\u0119c jedwab d\u0142u\u017cej zachowuje spr\u0119\u017cysto\u015b\u0107 i kszta\u0142t',
    43: 'Trzy kolory jedwabiu - jeden na ka\u017cdy moment.',
    44: 'Czarny, brudny r\u00f3\u017c i szampan - trzy klasyki, kt\u00f3re pasuj\u0105 do siebie i do wszystkiego w szafie. Dobierasz do stroju, do nastroju albo po prostu si\u0119gasz po najbli\u017csz\u0105. Ka\u017cda opcja jest dobra.',
    45: 'droplets', 46: 'Kolor pod nastr\u00f3j',
    47: 'Momme to g\u0119sto\u015b\u0107 jedwabiu \u2013 im wy\u017csze, tym grubszy i trwalszy materia\u0142. Standard rynkowy to 16\u201319 momme. Nasze 22 momme to g\u0119stszy splot, kt\u00f3ry lepiej trzyma kszta\u0142t i d\u0142u\u017cej s\u0142u\u017cy.',
    48: 'layers', 49: 'Dlaczego 22 momme?',
    50: 'Rano w po\u015bpiechu, w trakcie treningu, wieczorem przed snem - moment, w kt\u00f3rym si\u0119gasz po gumk\u0119, jest przypadkowy. Kiedy ka\u017cda pod r\u0119k\u0105 jest jedwabna, nie musisz o tym my\u015ble\u0107.',
    51: 'wind', 52: 'Jedwab zawsze pod r\u0119k\u0105',
    53: 'Satyna to nazwa splotu, nie materia\u0142u \u2013 najcz\u0119\u015bciej kryje si\u0119 za ni\u0105 poliester. LUSENA to 100% jedwab morwowy: naturalne w\u0142\u00f3kno bia\u0142kowe, kt\u00f3re oddycha i nie elektryzuje.',
    54: 'shield-check', 55: 'Jedwab, nie satyna z poliestru',
    56: 'Jedna jedwabna gumka to przyjemny wyj\u0105tek. Kiedy masz trzy, nie zastanawiasz si\u0119, po kt\u00f3r\u0105 si\u0119gn\u0105\u0107 - ka\u017cda jest jedwabna. I w\u0142a\u015bnie tak wyj\u0105tek staje si\u0119 oczywisto\u015bci\u0105.',
    57: 'sparkles', 58: 'Po prostu jedwab',
    59: 'Ka\u017cdy zestaw LUSENA przychodzi w eleganckim opakowaniu prezentowym - idealny upominek, kt\u00f3ry robi wra\u017cenie. Bez dodatkowego pakowania.',
    60: 'gift', 61: 'Gotowe do wr\u0119czenia',
    63: 'FALSE',
    73: 'Jedna jedwabna gumka to mi\u0142y akcent. Trzy - i syntetyczna gumka po prostu przestaje mie\u0107 sens.',
    74: '3 kolory, 1 zestaw - idealny prezent',
}

# ============================================================
# Apply updates to export rows
# ============================================================
changes = 0
seen_handles = set()
for row in rows:
    handle = row[0]
    if handle in updates and handle not in seen_handles:
        seen_handles.add(handle)
        product_updates = updates[handle]
        for col_idx, new_val in product_updates.items():
            old_val = row[col_idx]
            if old_val != new_val:
                changes += 1
            row[col_idx] = new_val

print(f'Updated {len(seen_handles)} products, {changes} cell changes')

# Write to imports folder
filename = 'products_import_updated.csv'
output = io.StringIO()
writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
writer.writerow(header)
for row in rows:
    writer.writerow(row)
with open(filename, 'wb') as f:
    f.write(b'\xef\xbb\xbf')  # UTF-8 BOM for Excel
    f.write(output.getvalue().encode('utf-8'))
print(f'Written to imports/{filename} ({len(header)} cols, {len(rows)} rows)')
