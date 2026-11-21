# 1-maqola auditi (Hydrology, MDPI), 21.11.2026

Tekshirilgan fayllar: `maqola1_hydrology.md/.docx` (inglizcha), `maqola1_hydrology_uz.md/.docx` (o‘zbekcha), manba qoralamalar `maqola1_qoralama.md`, `maqola1_qoralama_uz.md`.

## 1. Adabiyotlar

23 ta manbaning 18 tasida DOI bor. Barcha 18 DOI Crossref'da tekshirildi: mualliflar, yil, sarlavha, jurnal, jild va sahifalar ro‘yxatdagi bilan mos.

| Topilgan | Tuzatish |
|---|---|
| Karimov va boshq. 2025 (SPIE): yozuvda konferensiya nomi yo‘q edi; Crossref sahifa sifatida "25" ni beradi, maqolaning o‘zida esa SPIE raqami 136620J | Konferensiya nomi (DTIEE 2025) qo‘shildi, maqoladagi 136620J raqami qoldirildi |
| Leake va boshq. 1994: sarlavhada vergul tushib qolgan ("Finite-Difference, Ground-Water") | Tuzatildi |
| Theis 1935 va Hantush–Jacob 1955: Crossref yozuvida muallif maydoni yo‘q | Mualliflar klassik ishlardan ma'lum, o‘zgarishsiz qoldi |
| Matnda De Ridder (1961) va Veling–Maas (2009) bor, ro‘yxatda yo‘q edi | Ikki jumla matndan olib tashlandi |

DOI'si yo‘q 5 manba: Qodirov 2023 (dissertatsiya), Ravshanov va boshq. 2017, Kruseman–de Ridder 1990 (kitob), Olsthoorn 2003, Hemker–Randall 2010 (MLU qo‘llanmasi). Ular dissertatsiya va qo‘llanma sifatida aniq ko‘rsatilgan.

## 2. Raqamlar (matn ↔ skript natijalari)

Matndagi har bir raqam `tajribalar/*.json` bilan solishtirildi. Dalem, t2, t5, t6, t8 jadvallari va matndagi qiymatlar mos. 2-, 3-rasmlar inglizcha yozuvlar bilan qayta hisoblandi, natija oldingisi bilan bir xil.

| Topilgan xato | To‘g‘risi |
|---|---|
| 3.3-bo‘lim: yupqa ajratuvchilarda $t_c=11$ va 32 sut | $t_c=b'^2S'_s/K'=8^2\cdot2\cdot10^{-4}/5\cdot10^{-4}=25{,}6\approx26$ sut |
| 3.1-bo‘lim, Olsthoorn misoli: sonli yechim $t\ge10^{-3}$ da etalondan "ko‘pi bilan 0,25%" farq qiladi | Quduqli qatlamda 0,31% gacha ($t=10^{-3}$), ikkinchi qatlamda $t\ge0{,}1$ da 1,1% gacha; jumla shunga ko‘ra o‘zgartirildi |
| Annotatsiya va 5-xulosa: elastik suv berishi hisobga olinmagan model sath pasayishini "14% ga oshirib baholaydi" | 0,060 m / 0,051 m = 16% oshirib baholash; 14% esa elastik suv berishi pasayishni kamaytiradigan ulush. Ifoda "14% ga kamaytiradi" qilib to‘g‘rilandi (II bob 2.1-bo‘limida ham) |
| Annotatsiya va 3-xulosa: "0,7% aniqlikda" | Jadvaldagi eng katta qiymat 0,74%, shu yozildi |

## 3. Matematika

Tenglamalar (1)–(22), Laplas sohasidagi oqimlar, 1–2-lemma, 1–2-teorema isbotlari qayta tekshirildi. Isbotlarda xato topilmadi: $\Lambda$ ning simmetriyasi ($\alpha_M=\beta_1$), satr yig‘indisi ($1-\alpha_m-\beta_m\ge0$), energiya bahosi va M-matritsa xossasi to‘g‘ri; $t_c$ ning ikki ko‘rinishi va Herrera–Figueroa xotira vaqti ($0{,}30\,t_c$) mos.

Bitta belgi bir nechta ma'noda ishlatilgan joylar (25 bandning 20-bandi) tuzatildi:

| Belgi | Avval | Endi |
|---|---|---|
| $Q$ | quduq sarfi va qo‘shni yacheyka | qo‘shni yacheyka $N$ ($C_{PN}$, $T_N$, $h_N$) |
| $h$ | napor va yacheyka o‘lchami | yacheyka o‘lchami $\Delta x$ |
| $s$ | napor pasayishi va $S'_s\delta/\tau$ | $\sigma=S'_s\delta/\tau$ |
| $KD$, $D'$ | Dalem jadvalida (Kruseman belgilari) | $T$, $b'$ (maqoladagi belgilar) |

Belgilar jadvaliga $\Delta x$ va $\sigma$ qo‘shildi.

## 4. Uslub

Taqiqlangan so‘zlar (25 band, 16-band) topilmadi. "First" so‘zi faqat "birinchi tartib", "birinchi qadam" ma'nosida. Tire faqat MDPI'ning standart "writing—original draft" iborasida. O‘zbekcha matnda taqiqlangan atamalar yo‘q. Muallif familiyalari o‘zbekcha matnda bir xil lotin yozuvida berildi (Teys, Xantush–Jakob → Theis, Hantush–Jacob; "Hemker, Maas" → "Hemker va Maas").

Inglizcha va o‘zbekcha matnlarda havolalar ketma-ketligi aynan bir xil ([1]…[23]), 22 ta raqamlangan formula, 4 jadval, 3 rasm.

## 5. Fayllar

DOCX metama'lumoti: muallif "Javokhir Erkinov", dastur izlari yo‘q. PNG fayllarda faqat dpi bor. DOCX → PDF: inglizcha 11, o‘zbekcha 12 bet. Formulalar Word formulalari (OMML), LibreOffice PDF'ida ko‘rinmaydi, Word'da ko‘rinadi.

Sun'iy intellektdan foydalanish haqidagi jumla Acknowledgments'da qoldirildi: bu MDPI'ning majburiy talabi.

## 6. Yuborishdan oldin sizda qolganlar

1. Ravshanov N. maqolani o‘qib, yuborishga rozilik berishi.
2. GitHub'dagi `1-masala` repozitoriysi ochiq (public) bo‘lishi, chunki Data Availability unga havola qiladi.
3. Word'da formulalar va rasmlar to‘g‘ri ko‘rinishini bir ko‘zdan kechirish.
