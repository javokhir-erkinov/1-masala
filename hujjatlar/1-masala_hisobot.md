# 1-masala bo‘yicha hisobot

Davr: 20.11.2026 – 21.11.2026. Dastur va natijalar: GitHub, `javokhir-erkinov/1-masala`, `claude/project-thread-15xs9v` tarmog‘i (oxirgi holat audit va hisobot bilan).

## 1. Masala va uning maqsadi

Masala Ravshanov ilmiy maktabining uch qatlamli modellarini davom ettiradi. Uch suvli qatlam ikki ajratuvchi orqali bog‘langan. Har bir ajratuvchida elastik suv berishi vertikal bir o‘lchamli tenglama bilan hisobga olinadi, ajratuvchi chegaralarida napor va oqim uzluksiz. Qolgan shartlar:

- barcha qatlamlarda filtratsiya koeffitsiyenti $x$, $y$ koordinatalarga bog‘liq;
- yuqori qatlam bosimsiz, unga infiltratsiya, S.F. Averyanov qonuni bo‘yicha bug‘lanish va quduqlar ta’sir qiladi;
- sxema bitta va massani saqlaydi, turg‘unligi va maksimum prinsipi isbotlanadi;
- ajratuvchining elastik suv berishini qachon hisobga olmaslik mumkinligi uchun mezon izlanadi.

Amaliy maqsad: chuqur qatlamdan suv olinganda grunt suvlari sathining o‘zgarishini, ya’ni bug‘lanish va sho‘rlanishga ta’sir qiluvchi kattalikni to‘g‘ri baholash.

## 2. Manbalar: qayerdan olindi va qanday o‘qildi

### Ravshanov maktabi ishlari (masala shulardan boshlanadi)

| Manba | Qayerdan olindi | O‘qilish darajasi | Masala uchun nima olindi |
|---|---|---|---|
| Ravshanov N., Shadmanov I. va boshq., Hydrology 2026, 13, 276 | MDPI ochiq maqola, bulutdagi tahlil `adabiyotlar/maqolalar_tahlili/hydrology-13-00276.md` | to‘liq matn | uch qatlam, ikki ajratuvchi, $K(x,y)$, massani saqlovchi almashinuv, garmonik o‘rtacha; ajratuvchida elastik suv berishi, bosimsiz qatlam, quduq, bug‘lanish va turg‘unlik isboti yo‘qligi aniqlandi |
| Ravshanov N., Shadmanova K., Shadmanov I., Hydrology 2026, 13, 181 | MDPI ochiq maqola, tahlil `hydrology-13-00181.md` | to‘liq matn | to‘rt qatlamli nochiziqli model; maktabning eng so‘nggi ko‘p qatlamli ishi sifatida |
| Qodirov K.R., PhD dissertatsiya, 2023 | kompyuterdagi Ravshanov materiallari papkasi, bulut nusxasi `Qodirov_dissertatsiya.txt` | to‘liq matn | ikki elastik ajratuvchi orasidagi bitta suvli qatlam (Hantush 1960 joylashuvi), analitik yechimlar, parametrlar o‘zgarmas; uchta bog‘langan qatlam yo‘q |
| Ravshanov N., Kodirov K. va boshq., PCAM 2017, 1(7), 47–53 | Qodirov dissertatsiyasidagi havola | faqat havola | Qodirov modelining birinchi nashri sifatida keltirildi |
| Karimov M. va boshq., Proc. SPIE 13662, 2025; Mukhamadiyev A., Karimov M. va boshq., Mathematics 2026, 14, 256 | foydalanuvchi yuklagan PDF lar (`dissertatsiyalar/karimov/`) | to‘liq matn, formulalar sahifa rasmidan | bosimsiz qatlam, $T(x,y)$, bug‘lanish va elastik rejimdagi qatlam bor, lekin bu qatlam eng pastda va tubi suv o‘tkazmaydi; ikki suvli qatlamni bog‘lamaydi |
| Kayumov va boshq., J. Phys.: Conf. Ser. 2697, 2024 | to‘liq matn topilmadi | faqat PVPM 2025 sharhi orqali | bir o‘lchamli, bitta suvli qatlam va ostidagi elastik qatlam; maqolaga kiritilmadi |
| Aminov S.M., PhD, 2023 | kompyuterdagi dissertatsiyalar papkasi | faqat avtoreferat | neft-gaz masalasi; maqolaga kiritilmadi |

### Xalqaro ishlar (yangilik chegarasini aniqlash va tekshiruv uchun)

| Manba | Qayerdan olindi | O‘qilish darajasi | Nima uchun kerak bo‘ldi |
|---|---|---|---|
| Kruseman, de Ridder 1990, ILRI 47 | bulutdagi skanerlangan PDF | kerakli boblari sahifa rasmlaridan (75–76, 83–84, 97–98-betlar) | Dalem tajribasi ma’lumotlari va Neuman–Witherspoon nisbatlar usuli natijasi |
| Olsthoorn 2003 (C. Maas ustuni), Stromingen 9(3) | kompyuterdagi PDF; parametrlar va jadval `maqola1/etalon_parametrlar/etalonlar.md` ga ko‘chirilgan | 48–50-betlar to‘liq | Hemker–Maas 1987 bilan bir xil deyilgan 36 qiymatli jadval, etalon tekshiruvi |
| Hemker, Randall 2010, MLU qo‘llanmasi | kompyuterdagi PDF; o‘sha `etalonlar.md` | "Two-aquifers" misoli (38–41-betlar) | parametrlar va bosilgan natija bilan solishtirish |
| Leake va boshq. 1994 (TLK1), Hughes va boshq. 2022 (CSUB), Langevin va boshq. 2017 (MODFLOW 6) | USGS sahifalari | hujjat sahifalari | MODFLOW da ajratuvchining elastik suv berishi qanday hisobga olinishi; MODFLOW 6 bilan hisob |
| Hantush 1960; Hantush, Jacob 1955; Theis 1935; Neuman, Witherspoon 1969; Hemker 1985; Hemker, Maas 1987; Cihan va boshq. 2011; Herrera, Yates 1977; Herrera, Figueroa 1969 | Crossref yozuvlari, annotatsiyalar, Kruseman 1990 va AQTESOLV dagi bayonlar | asl matnlar o‘qilmagan (pullik), formulalar ikkilamchi manbalardan va o‘zimiz keltirib chiqargan | ajratuvchining elastik suv berishi analitik yechimlarda bor ekanini ko‘rsatish; Laplas sohasidagi etalon shu yondashuvda qurildi |
| Forsyth, Sammon 1988; Stehfest 1970 | Crossref yozuvlari | asl matn o‘qilmagan | markazlashgan to‘rda ikkinchi tartib; Laplas teskari almashtirishi algoritmi |

Barcha 18 DOI 21.11.2026 da Crossref bo‘yicha tekshirildi (`maqola/mdpi/audit_hisobot.md`).

## 3. Masala qaysi tomonlardan o‘rganildi

**Yangilik chegarasi.** Maktab ishlari va xalqaro ishlar uchun "modelda bor / yo‘q" jadvali tuzildi. Ajratuvchining elastik suv berishi o‘zi yangilik emasligi (Hantush, Neuman–Witherspoon, Hemker, MODFLOW TLK1 va CSUB) ochiq yozildi. Qo‘shiladigan qism shu tarzda belgilandi: barcha shartlarni birga hisobga olgan bitta massani saqlovchi sonli sxema va uning isbotlangan xossalari.

**Matematik model.** Suvli qatlamlar va ajratuvchi tenglamalari massa saqlanishi va Darsi qonunidan keltirib chiqarildi, tenglamalar (1)–(14). Tutashuv shartlari, global suv balansi, $t_c=b'S'/K'$ xarakterli vaqti va $\varepsilon=S'/\sum S$ nisbati olingan. $S'_s\to0$ da maktab modelidagi almashinuv hadi kelib chiqishi ko‘rsatilgan.

**Sonli usul.** Markazlashgan chekli hajmlar, o‘rta garmonik o‘tkazuvchanlik va oshkormas Eyler sxemasi qo‘llandi. Har bir ajratuvchi ustuni progonka bilan aniq yo‘qotiladi, natijada $2\times2$ almashinuv matritsasi hosil bo‘ladi. Nochiziqlilik Pikar iteratsiyasi va bug‘lanishni chiziqlashtirish orqali hisobga olinadi, tenglamalar (15)–(22).

**Nazariy xossalar.** Quyidagilar isbotlandi:
- diskret suv balansi aniq bajariladi (1-lemma);
- almashinuv matritsasi simmetrik va musbat yarim aniqlangan (2-lemma);
- sxema ixtiyoriy $\tau$ da energiya normasida turg‘un (1-teorema);
- diskret maksimum prinsipi bajariladi (2-teorema).

**Tekshiruv.** Natijalar besh xil manba bilan solishtirildi:

| Tekshiruv | Natija |
|---|---|
| Theis va Hantush–Jacob yechimlari | farq $10^{-5}$ va $10^{-4}$ |
| Laplas sohasidagi uch qatlamli etalon (ikkala ajratuvchida elastik suv berishi) | eng katta farq 0,74% |
| MODFLOW 6 (ajratuvchi 20 qatlam sifatida, GitHub Actions da) | farq $4\cdot10^{-9}$ m |
| Olsthoorn 2003 / Hemker–Maas 1987 jadvali va MLU "Two-aquifers" | etalon 36 qiymatning hammasini 4 xonagacha takrorlaydi; MLU qiymati 0,29826 m aynan |
| Dalem dala tajribasi | o‘rtacha kvadratik farq 5,80 mm, $S'=1{,}1\cdot10^{-3}$ Kruseman–de Ridder natijasi bilan mos |
| To‘r va vaqt qadami bo‘yicha yaqinlashish | fazo bo‘yicha 2,07–2,32, vaqt bo‘yicha 1,02–1,05 |
| Suv balansi | qoldiq $10^{-12}$ tartibida |

**Parametrik tadqiqot.** Ajratuvchining elastik suv berishini qachon hisobga olmaslik mumkinligi o‘rganildi. Natija: buni faqat $t/t_c$ hal qilmaydi, $\varepsilon$ ham kerak. $\varepsilon\gtrsim1$ da farq $t=10^3\,t_c$ da ham 6–12% bo‘lib qoladi.

**Amaliy misol.** Geterogen maydon, bosimsiz qatlam, bug‘lanish va to‘rtta quduq bilan hisob qilindi. Qalin gilli ajratuvchilar ($t_c=900$ va 3200 sut) uchun natijalar:
- elastik suv berishi quduqli qatlamda dastlabki pasayishni 18–30% ga sekinlashtiradi;
- taxminan 1 sutkada quduqlar suvining 26% i ajratuvchilardan keladi;
- bir yildan keyin bosimsiz qatlamdagi sath pasayishi 14% ga kam bo‘ladi (0,051 m va 0,060 m).

## 4. Bajarilgan ishlar ketma-ketligi

1. Asos ishlar tahlili va masalaning qo‘yilishi (`hujjatlar/01_masala_qoyilishi.md`).
2. `masala1` dasturi tuzildi: to‘r, model, yechuvchi, Laplas etaloni (Python, 1100 qator). Unga 10 ta avtomatik test yozildi.
3. Tajribalar t1–t8 o‘tkazildi: etalon, $t_c$ mezoni, MODFLOW 6, Dalem, geterogen maydon, qalin ajratuvchi, Maas–MLU, yaqinlashish.
4. MODFLOW 6 bilan solishtirish GitHub Actions orqali bajarildi, chunki bulutdan MODFLOW yuklab bo‘lmaydi.
5. Inglizcha va o‘zbekcha maqola qoralamalari yozildi. Mualliflar: Ravshanov N., Erkinov J. Formulalarni keltirib chiqarish qo‘shildi, belgilar indeksli shaklga keltirildi.
6. II bobning 2.1-bo‘limi tayyorlandi (`bob2/II_bob_2_1_band_1-masala.docx`).
7. Jurnal tanlandi: Hydrology (MDPI). Maqola MDPI tartibiga o‘tkazildi, cover letter yozildi, SuSy profili to‘ldirildi.
8. Yuborishdan oldin audit qilindi: 4 ta raqam xatosi, 4 ta belgi to‘qnashuvi va 2 ta havola yozuvi tuzatildi.

## 5. Natija fayllari

| Fayl | Joyi |
|---|---|
| Maqola, inglizcha (Hydrology uchun) | `maqola1/hydrology/maqola1_hydrology.docx` |
| Maqola, o‘zbekcha nusxa | `maqola1/hydrology/maqola1_hydrology_uz.docx` |
| Cover letter, rasmlar Figure1–3 | `maqola1/hydrology/` |
| Audit hisoboti | `maqola1/hydrology/audit_hisobot.md` |
| Masalaning qo‘yilishi (to‘liq hujjat) | `maqola1/01_masala_qoyilishi.md` |
| II bob, 2.1-bo‘lim | `bob2/II_bob_2_1_band_1-masala.docx` |
| Dastur, testlar, tajribalar | GitHub `1-masala` |

## 6. Cheklovlar va ochiq qolgan masalalar

- 2- va 3-qatlamlar doimo bosimli deb olinadi, har bir quduqning filtri bitta qatlamda joylashgan.
- Ajratuvchida faqat vertikal oqim hisobga olinadi. MLU misolida bu farq −16% dan +1,3% gacha ta’sir qiladi.
- Pikar iteratsiyasining yaqinlashishi isbotlanmagan, faqat har bir hisobda kuzatiladi.
- Dala tekshiruvi bitta tajribaga tayanadi. Dalem ma’lumotlari ajratuvchining elastik suv berishini alohida tasdiqlay olmaydi, buning uchun ajratuvchi ichida pyezometrli tajriba kerak.
- Hemker–Maas 1987, Cihan 2011, Cheng 1993 va Sindalovskiy 2014 ning asl matnlari o‘qilmagan (pullik).
- Yuborishdan oldin uchta ish qolgan: Ravshanov N. roziligi, GitHub repozitoriysini ochiq qilish va Word faylini ko‘zdan kechirish.
