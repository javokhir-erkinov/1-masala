# Ajratuvchi qatlamlarning elastik suv berishi, suv o‘tkazuvchanlikning koordinatalarga bog‘liqligi va bosimsiz yuqori qatlam hisobga olingan uch qatlamli tizimda yer osti suvlari filtratsiyasining massani saqlovchi sonli modeli

Erkinov Javohir¹*, Ravshanov Normaxmad²

¹ Sharof Rashidov nomidagi Samarqand davlat universiteti, Samarqand, O‘zbekiston. ORCID 0009-0007-6580-7402
² Raqamli texnologiyalar va sun’iy intellektni rivojlantirish ilmiy-tadqiqot instituti, Toshkent, O‘zbekiston [Hydrology 2026, 13, 276 dagi yozuv bo‘yicha; aniqlashtiriladi]

\* Muallif bilan aloqa: erkinovj110@gmail.com

Qoralama v0.1, 21.11.2026. Inglizcha qoralamaning (`maqola/maqola1_qoralama.md`) o‘zbekcha matni. Barcha raqamlar `1-masala` repozitoriysidagi skriptlardan olingan, har bir jadvalda skript nomi ko‘rsatilgan.

## Annotatsiya

Uch qatlamli tizimda ikki ajratuvchi qatlam elastik suv zaxirasiga ega. Quduq ishlaganda bu zaxiradan suv ajraladi va qo‘shni suvli qatlamlarda napor pasayishini kechiktiradi. O‘zbekistonda yaratilgan ko‘p qatlamli sonli modellarda suvli qatlamlar orasidagi ajratuvchilar elastik suv berishi hisobga olinmagan oqib o‘tish chegarasi sifatida qaraladi. Ko‘p qatlamli analitik yechimlarda esa ajratuvchining elastik suv berishi bor, lekin qatlamlar bir jinsli, bosimli va oqim radial deb olinadi.

Maqolada har bir ajratuvchi qatlamda vertikal bir o‘lchamli elastik rejim tenglamasi yechiladigan model taklif etiladi. Ajratuvchining ikkala chegarasida napor va oqim uzluksiz. Suvli qatlamlarda filtratsiya koeffitsiyenti x, y koordinatalarga bog‘liq. Yuqori qatlam bosimsiz bo‘lib, unga infiltratsion ta’minot, sizot suvlari chuqurligiga bog‘liq bug‘lanish va quduqlar ta’sir qiladi.

Model markazlashgan chekli hajmlar usuli va oshkormas Eyler sxemasi bilan diskretlanadi. Har bir ajratuvchi ustunidagi noma’lumlar vektorlashgan progonka bilan yo‘qotiladi. Natijada har bir ustun uchun 2×2 o‘lchamli simmetrik almashinuv matritsasi va suvli qatlamlar naporlari uchun bitta simmetrik siyrak tizim qoladi. Sxema massani aniq saqlashi, energiya normasida absolyut turg‘unligi va diskret maksimum prinsipini qanoatlantirishi isbotlangan.

Dastur Teys va Xantush–Jakob yechimlarini hamda ajratuvchilarning elastik suv berishini hisobga olgan Laplas sohasidagi ko‘p qatlamli yechimni 0,7% aniqlikda takrorlaydi. Bir xil to‘rda MODFLOW 6 bilan farq 4·10⁻⁹ m dan oshmaydi. Sxema fazo bo‘yicha ikkinchi, vaqt bo‘yicha birinchi tartibda yaqinlashadi, suv balansi qoldig‘i 10⁻¹¹ dan kichik.

Hisoblashlar ajratuvchining elastik suv berishini hisobga olmaslik mumkinligini faqat t_c = b′S′/K′ xarakterli vaqti hal qilmasligini ko‘rsatdi. Ajratuvchi va suvli qatlamlar elastik suv berish koeffitsiyentlarining nisbati ε ham ahamiyatga ega: ε ≳ 1 bo‘lganda ikki model orasidagi farq t ≫ t_c da ham saqlanadi. Qalin gilli ajratuvchilar va geterogen filtratsiya maydoni bo‘lgan misolda elastik suv berishi quduqli qatlamda dastlabki napor pasayishini 18–30% ga o‘zgartiradi. Bir yildan keyin ham bosimsiz qatlamda sath pasayishi 14% kam bo‘ladi. Demak elastik suv berishi hisobga olinmagan model bug‘lanish va sho‘rlanishni belgilaydigan grunt suvlari sathining pasayishini oshirib baholaydi.

Kalit so‘zlar: ko‘p qatlamli suvli gorizont; ajratuvchi qatlamning elastik suv berishi; qatlamlararo oqib o‘tish; chekli hajmlar usuli; absolyut turg‘unlik; bosimsiz suvli qatlam

## Belgilar

| Belgi | Ma’nosi | Birligi |
|---|---|---|
| h_k | k-suvli qatlamdagi napor | m |
| u_j | j-ajratuvchi qatlamdagi napor | m |
| K_k, T_k | k-suvli qatlamning filtratsiya koeffitsiyenti va suv o‘tkazuvchanligi | m/sut, m²/sut |
| b_k | k-bosimli suvli qatlam qalinligi | m |
| S_k, μ | k-qatlamning elastik suv berish koeffitsiyenti, 1-qatlamning suv berish koeffitsiyenti | – |
| K′_j, b′_j | j-ajratuvchining vertikal filtratsiya koeffitsiyenti va qalinligi | m/sut, m |
| S′_{s,j}, S′_j | j-ajratuvchining solishtirma va to‘liq (S′_s b′) elastik suv berish koeffitsiyenti | 1/m, – |
| c | ajratuvchining gidravlik qarshiligi b′/K′ | sut |
| q⁺_j, q⁻_j | j-ajratuvchining yuqori va pastki chegarasi orqali solishtirma sarf, pastga musbat | m/sut |
| W, E | infiltratsion ta’minot va bug‘lanish jadalligi | m/sut |
| E₀, Δ, n | yer sathidagi bug‘lanish, bug‘lanish to‘xtaydigan chuqurlik, daraja ko‘rsatkichi | m/sut, m, – |
| z₀, z_s | 1-qatlam tubi va yer sathi belgisi | m |
| Q | quduq sarfi, suv olinganda musbat | m³/sut |
| t_c | ajratuvchining xarakterli vaqti b′²S′_s/K′ | sut |
| ε | elastik suv berish koeffitsiyentlari nisbati S′/ΣS_k | – |
| τ, δ, M | vaqt qadami, ajratuvchi qatlamchasi qalinligi, qatlamchalar soni | sut, m, – |
| C_PQ, A_P | yacheykalararo o‘tkazuvchanlik, yacheyka yuzasi | m²/sut, m² |

## 1. Kirish

Markaziy Osiyoning sug‘oriladigan tekisliklarida qumli suvli qatlamlar gil va qumoq qatlamlar bilan ajralgan. Chuqurroq qatlamdan suv olinganda ajratuvchilar orqali yuqoridagi bosimsiz qatlamda ham sath pasayadi. Sath o‘zgarishi bug‘lanishni va ildiz qatlamidagi tuz balansini o‘zgartiradi. Shu sababli yuqori qatlamdagi o‘zgarishni oldindan baholash uchun suvli qatlamlarni ajratuvchilar orqali fizik jihatdan to‘g‘ri bog‘laydigan model kerak.

N. Ravshanov ilmiy maktabida bunday tizimlar uchun kvaziuch o‘lchamli modellar ketma-ket ishlab chiqilgan. Ravshanov va boshq. (2026a) ikki ajratuvchi bilan bog‘langan uchta geterogen suvli qatlam masalasini ADI sxemasi, yacheykalararo koeffitsiyentning o‘rta garmonik qiymati va massani saqlovchi almashinuv hadi bilan yechgan; modelga zarrachalar ko‘chishi va kolmatatsiya ham kiritilgan. Ravshanov va boshq. (2026b) filtratsiya koeffitsiyenti naporga bog‘liq bo‘lgan to‘rt qatlamli tizimni ko‘rgan. Karimov va boshq. (2025) va Mukhamadiyev va boshq. (2026) bitta uch qatlamli modelni bayon qilgan: unda yuqori qatlam bosimsiz, suv o‘tkazuvchanlik koordinatalarga bog‘liq, bug‘lanish bor va kam o‘tkazuvchan qatlam elastik rejimda. Ammo bu kam o‘tkazuvchan qatlam tizimning eng pastida joylashgan va tubi suv o‘tkazmaydi, ya’ni u ikki suvli qatlamni bog‘lamaydi. Qodirov (2024) ajratuvchilarning elastik suv zaxirasi bo‘lgan uchta bir jinsli qatlam uchun analitik yechimlar olgan. Ko‘rsatilgan sonli modellarning birortasida suvli qatlamlar orasidagi ajratuvchining elastik suv berishi yo‘q, bog‘langan sxemaning turg‘unligi ham isbotlanmagan.

Xalqaro adabiyotda ajratuvchining elastik suv berishi uzoq vaqtdan beri o‘rganiladi. Hantush (1960) hamda Neuman va Witherspoon (1969) ajratuvchi zaxirasidan ajralgan suv dastlabki napor pasayishini o‘zgartirishini ko‘rsatgan. Hemker (1985) va Hemker, Maas (1987) barcha ajratuvchilarida elastik suv berishi bo‘lgan n qatlamli masalani Laplas sohasida yechgan. Cihan va boshq. (2011) bu yondashuvni ko‘p sonli suvli qatlam va germetik bo‘lmagan quduqlar uchun kengaytirgan. Herrera va Yates (1977) ajratuvchi ta’sirini xotira integrali orqali yozgan. MODFLOW dasturida ajratuvchining elastik suv berishi TLK1 paketi (Leake va boshq. 1994) va CSUB paketidagi kechikuvchi qatlamchalar (Hughes va boshq. 2022) orqali hisobga olinadi. Ajratuvchini bir necha yupqa model qatlami bilan tasvirlash ham mumkin. Demak ajratuvchining elastik suv berishi o‘z-o‘zidan yangi masala emas.

Sug‘oriladigan tekisliklar masalasi uchun quyidagilarning birgalikda bo‘lishi kerak, mavjud vositalarda esa ular birga uchramaydi:

1. suvli qatlamlar orasidagi har bir ajratuvchida elastik suv berishi;
2. har bir suvli qatlam va ajratuvchida filtratsiya koeffitsiyentining x, y koordinatalarga bog‘liqligi;
3. infiltratsion ta’minot va chuqurlikka bog‘liq bug‘lanish ta’sir qiladigan nochiziqli bosimsiz yuqori qatlam;
4. massaning saqlanishi, turg‘unlik va monotonlik sinab ko‘rilgan emas, balki isbotlangan bitta diskret sxema.

Analitik yechimlar 2- va 3-shartni qanoatlantirmaydi. Ajratuvchini MODFLOW qatlamlari bilan diskretlash bizning sxemamiz bilan bir xil diskret masalani beradi (5-bo‘lim), lekin uch o‘lchamli noma’lumlar sonini bir necha marta oshiradi va bog‘langan tizim turg‘unligi tahlil qilinmaydi.

Maqolada quyidagi natijalar keltiriladi.

1. Har bir ajratuvchida vertikal elastik rejim tenglamasi, ajratuvchi chegaralarida napor va oqim uzluksizligi, barcha qatlamlarda K(x,y), infiltratsion ta’minot, S.F. Averyanov bug‘lanish qonuni va quduqlar bo‘lgan bosimsiz yuqori qatlamli uch qatlamli model (2-bo‘lim).
2. Ajratuvchi ustunlari progonka bilan aniq yo‘qotiladigan chekli hajmlar sxemasi. Diskret massa saqlanishi, almashinuv matritsasining simmetrikligi va musbat yarim aniqligi, energiya normasida absolyut turg‘unlik va diskret maksimum prinsipi isbotlangan (3- va 4-bo‘limlar).
3. Klassik yechimlar, ajratuvchining elastik suv berishini hisobga olgan Laplas sohasidagi ko‘p qatlamli yechim, Hemker–Maas (1987) va MLU dasturining chop etilgan misollari, MODFLOW 6 va Dalem tajriba ma’lumotlari bilan tekshiruv (5-bo‘lim).
4. Ajratuvchining elastik suv berishini hisobga olmaslik mumkinligi t/t_c va ε = S′/ΣS parametrlariga bog‘liqligini ko‘rsatuvchi hisoblashlar. Geterogen maydonda elastik suv berishining grunt suvlari sathiga ta’siri miqdoriy baholangan (6-bo‘lim).

## 2. Matematik model

### Tizim va farazlar

Tizim yuqoridan pastga k = 1, 2, 3 tartibda raqamlangan uchta suvli qatlam va j = 1, 2 ikkita ajratuvchidan iborat. j-ajratuvchi j- va (j+1)-suvli qatlamlar orasida joylashgan. Gorizontal tekislikdagi soha Ω ⊂ ℝ² ixtiyoriy shaklda (1-rasm). Quyidagi farazlar qabul qilinadi:

- (A1) suvli qatlamlarda oqim gorizontal (Dyupyui farazi), ajratuvchilarda vertikal (Hantush farazi), chunki K′ ≪ K_k;
- (A2) bosimli qatlamlar va ajratuvchilarda elastik suv zaxirasi naporga chiziqli bog‘liq;
- (A3) 1-qatlam bosimsiz, uning suvga to‘yingan qalinligi h₁ − z₀, suv berish koeffitsiyenti μ; 2- va 3-qatlamlar doimo bosimli;
- (A4) sizot suvlari sathidan bug‘lanish uning chuqurligiga bog‘liq;
- (A5) har bir quduqning filtri bitta suvli qatlamda joylashgan;
- (A6) har bir nuqtada muhit izotrop, filtratsiya koeffitsiyenti x, y koordinatalarga bog‘liq.

1-rasm. Uch qatlamli tizimning sxematik kesimi (`maqola/rasm1_sxema.png`).

### Asosiy tenglamalar

1-qatlam (bosimsiz):

$$\mu\frac{\partial h_1}{\partial t}=\nabla\cdot\big(K_1(h_1-z_0)\nabla h_1\big)+W-E(h_1)-q^{+}_1-\sum_i Q_{1i}\delta(\mathbf x-\mathbf x_i).\tag{1}$$

2- va 3-qatlamlar (bosimli, T_k = K_k b_k):

$$S_2\frac{\partial h_2}{\partial t}=\nabla\cdot(T_2\nabla h_2)+q^{-}_1-q^{+}_2-\sum_i Q_{2i}\delta(\mathbf x-\mathbf x_i),\tag{2}$$

$$S_3\frac{\partial h_3}{\partial t}=\nabla\cdot(T_3\nabla h_3)+q^{-}_2-\sum_i Q_{3i}\delta(\mathbf x-\mathbf x_i).\tag{3}$$

j-ajratuvchi uchun vertikal koordinata ζ ∈ [0, b′_j] ajratuvchining yuqori chegarasidan pastga yo‘nalgan:

$$S'_{s,j}\frac{\partial u_j}{\partial t}=K'_j\frac{\partial^2u_j}{\partial\zeta^2},\tag{4}$$

$$u_j|_{\zeta=0}=h_j,\qquad u_j|_{\zeta=b'_j}=h_{j+1},\tag{5}$$

$$q^{+}_j=-K'_j\partial_\zeta u_j|_{\zeta=0},\qquad q^{-}_j=-K'_j\partial_\zeta u_j|_{\zeta=b'_j}.\tag{6}$$

K′_j, b′_j va S′_{s,j} ham x, y koordinatalarga bog‘liq bo‘lishi mumkin. (5) va (6) tutashuv shartlari bo‘lib, napor va oqimning uzluksizligini ifodalaydi. S′_s = 0 bo‘lganda ajratuvchi elastik suv berishi bo‘lmagan oqib o‘tish chegarasiga aylanadi va q⁺ = q⁻ = K′(h_j − h_{j+1})/b′ bo‘ladi. Ravshanov va boshq. (2026a) da aynan shu almashinuv ishlatilgan.

Bug‘lanish S.F. Averyanov qonuni bo‘yicha hisoblanadi:

$$E(h_1)=E_0\big(1-(z_s-h_1)/\Delta\big)^n,\quad 0\le z_s-h_1\le\Delta;\qquad E=0,\quad z_s-h_1>\Delta.\tag{7}$$

Boshlang‘ich naporlar h_k⁰ quduqlarsiz statsionar holatdan olinadi, bunda ajratuvchidagi napor u_j⁰ chiziqli taqsimlangan. Γ_D chegarada napor berilgan, Γ_N chegarada oqim nolga teng.

### Global balans va xarakterli vaqt

(4) ni ajratuvchi qalinligi bo‘yicha integrallasak, d/dt ∫S′_s u dζ = q⁺ − q⁻ hosil bo‘ladi: ajratuvchiga kirgan va undan chiqqan suv farqi uning elastik suv zaxirasi o‘zgarishiga teng. Bu tenglikni (1)–(3) ning integrallariga qo‘shsak, almashinuv hadlari qisqaradi. Suvli qatlamlar va ajratuvchilar zaxirasining o‘zgarishi infiltratsiya va bug‘lanish farqidan quduqlar sarfini ayirib, chegaradan kelgan oqimni qo‘shganiga teng bo‘ladi.

(4) ni o‘lchamsiz ko‘rinishga keltirish ajratuvchining xarakterli vaqtini beradi:

$$t_c=\frac{b'^2S'_s}{K'}=\frac{b'S'}{K'},\qquad S'=S'_sb'.\tag{8}$$

Herrera va Figueroa (1969) dagi xotira vaqti 3S′b′/(π²K′) ga teng, bu 0,30 t_c ni tashkil etadi. Ikkinchi o‘lchamsiz parametr elastik suv berish koeffitsiyentlari nisbati:

$$\varepsilon=S'/\textstyle\sum_kS_k.\tag{9}$$

Hantush (1960) hamda Neuman va Witherspoon (1969) yechimlarida bu rolni S′/S nisbati bajaradi.

## 3. Sonli usul

### Fazo bo‘yicha diskretlash

Ω soha qadamlari o‘zgaruvchan to‘g‘ri burchakli to‘r bilan qoplanadi, Ω dan tashqaridagi yacheykalar hisobga kirmaydi. Qo‘shni P va Q yacheykalar ketma-ket ulangan qarshiliklar orqali bog‘lanadi:

$$C_{PQ}=\ell_{PQ}\Big(\frac{d_P}{2T_P}+\frac{d_Q}{2T_Q}\Big)^{-1},\tag{10}$$

bu yerda ℓ_PQ yacheykalar orasidagi yon tomon uzunligi, d_P, d_Q yacheyka o‘lchamlari. Bu ifoda o‘rta garmonik qiymat bo‘lib, T bo‘lakli o‘zgarmas bo‘lganda aniq natija beradi. 1-qatlamda T₁ = K₁ max(h₁ − z₀, b_min) olinadi.

Har bir ajratuvchi ustuni qalinligi δ = b′/M bo‘lgan M ta qatlamchaga bo‘linadi, tugunlar qatlamchalar markazida joylashadi. Ichki o‘tkazuvchanlik c = K′/δ, chetki o‘tkazuvchanlik c_e = 2K′/δ.

### Vaqt bo‘yicha diskretlash

Barcha qatlamlar uchun oshkormas Eyler sxemasi qo‘llaniladi. Yuzasi A_P bo‘lgan P yacheyka uchun:

$$\frac{S_PA_P}{\tau}(h_P^{n+1}-h_P^n)+\sum_QC_{PQ}(h_P^{n+1}-h_Q^{n+1})+A_P(q^+_P-q^-_P)^{n+1}=A_P(W-E)_P^{n+1}-Q_P.\tag{11}$$

Ajratuvchining har bir m-qatlamchasi uchun:

$$\frac{S'_s\delta}{\tau}(u_m^{n+1}-u_m^n)=c_{m-1/2}(u_{m-1}^{n+1}-u_m^{n+1})+c_{m+1/2}(u_{m+1}^{n+1}-u_m^{n+1}),\tag{12}$$

bunda u₀ = h_j va u_{M+1} = h_{j+1}. Chegaralardagi oqimlar q⁺ = c_e(h_j − u₁) va q⁻ = c_e(u_M − h_{j+1}).

### Ajratuvchi noma’lumlarini yo‘qotish

Har bir ustunda (12) simmetrik uch diagonalli tizimni tashkil etadi: 𝔗u = s uⁿ + c_e e₁ h_j + c_e e_M h_{j+1}, bu yerda s = S′_sδ/τ. Uni uchta o‘ng tomon uchun yechib, quyidagini olamiz:

$$u=a+\alpha h_j+\beta h_{j+1},\qquad \mathfrak Ta=su^n,\ \mathfrak T\alpha=c_ee_1,\ \mathfrak T\beta=c_ee_M.\tag{13}$$

Shunda chegaralardagi oqimlar ikki qo‘shni suvli qatlam naporlariga chiziqli bog‘liq bo‘ladi:

$$\begin{pmatrix}q^+\\-q^-\end{pmatrix}=\Lambda\begin{pmatrix}h_j\\h_{j+1}\end{pmatrix}-c_e\begin{pmatrix}a_1\\a_M\end{pmatrix},\qquad\Lambda=c_e\begin{pmatrix}1-\alpha_1&-\beta_1\\-\alpha_M&1-\beta_M\end{pmatrix}.\tag{14}$$

Progonka barcha ustunlar uchun bir vaqtda (vektorlashgan holda) bajariladi. Uning natijasi faqat τ va uⁿ ga bog‘liq, shuning uchun u har bir qadamda bir marta hisoblanadi. (14) ni (11) ga qo‘yib, suvli qatlamlar naporlari uchun bitta siyrak simmetrik tizim olinadi. U yechilgandan keyin ajratuvchidagi naporlar (13) dan tiklanadi. M = 0 bo‘lganda Λ = (K′/b′)[[1, −1], [−1, 1]].

### Nochiziqlilik va algoritm

T₁(h₁) va E(h₁) Pikar iteratsiyasi bilan aniqlanadi. r-iteratsiyada T₁(h^{(r)}) olinadi, E esa h^{(r)} atrofida chiziqlashtiriladi:

$$E(h^{(r+1)})\approx E(h^{(r)})+E'(h^{(r)})(h^{(r+1)}-h^{(r)}).$$

E′ ≥ 0 bo‘lgani uchun hosilali had matritsa diagonaliga qo‘shiladi. Iteratsiya max|h^{(r+1)} − h^{(r)}| < 10⁻⁸ m bo‘lganda to‘xtatiladi.

1-algoritm (bitta vaqt qadami):

1. barcha ustunlarda (13) dan a, α, β topiladi;
2. yaqinlashguncha T₁ va chiziqlashtirilgan E bilan tizim yig‘iladi va yechiladi;
3. ajratuvchidagi naporlar (13) dan tiklanadi;
4. suv balansi hisoblanadi.

## 4. Sxemaning xossalari

Ajratuvchi noma’lumlari bilan birga yozilgan (11)–(12) to‘liq tizim matritsasini 𝔸 = D/τ + 𝕃 bilan belgilaymiz. D diagonal matritsa bo‘lib, uning elementlari S_PA_P va S′_sδA_P. 𝕃 gorizontal va vertikal o‘tkazuvchanliklardan tuzilgan.

### 1-lemma (diskret suv balansi)

(11) ni barcha erkin yacheykalar, (12) ni barcha qatlamchalar bo‘yicha yig‘sak,

$$\Delta V_{\rm qatlam}+\Delta V_{\rm ajratuvchi}=\tau\Big[\sum A(W-E_{\rm lin})-\sum Q+B_D\Big]$$

tenglik aniq bajariladi. Bu yerda B_D napor berilgan yacheykalardan kelgan oqim.

Isbot. C_PQ simmetrik, shuning uchun gorizontal oqimlar juft-jufti bilan qisqaradi. (14) dagi oqimlar (12) ning chetki oqimlari bilan bir xil, demak vertikal oqimlar ham qisqaradi. □

### 2-lemma (almashinuv matritsasi)

Λ simmetrik, uning diagonaldan tashqari elementlari musbat emas, qatorlar yig‘indisi manfiy emas. Demak Λ musbat yarim aniq, kondensatsiyadan keyingi matritsa esa simmetrik M-matritsa.

Isbot. 𝔗 qat’iy diagonal ustunlikka ega M-matritsa, shuning uchun 𝔗⁻¹ ≥ 0, demak α, β ≥ 0. 𝔗 simmetrik bo‘lgani uchun α_M = β₁. 𝔗𝟙 = s𝟙 + c_e e₁ + c_e e_M tenglikdan 1 − α_m − β_m = (𝔗⁻¹ s𝟙)_m ≥ 0 kelib chiqadi. □

### 1-teorema (absolyut turg‘unlik)

Bosimli qatlamlar, bug‘lanish bo‘lmagan holat va bir jinsli berilgan naporlar uchun ixtiyoriy τ > 0, ixtiyoriy M, ixtiyoriy to‘r va parametrlarning barcha musbat qiymatlarida

$$\|h^{n+1}\|_D\le\|h^n\|_D+\tau\|D^{-1}F^{n+1}\|_D$$

baho o‘rinli, bu yerda ‖v‖²_D = vᵀDv.

Isbot. 𝔸h^{n+1} = Dhⁿ/τ + F tenglikni h^{n+1} ga skalyar ko‘paytiramiz. (h^{n+1})ᵀ𝕃h^{n+1} ≥ 0 va Koshi–Bunyakovskiy tengsizligidan baho kelib chiqadi. □

D ajratuvchilar zaxirasini ham o‘z ichiga olgani uchun baho ajratuvchilardagi naporlarni ham chegaralaydi.

### 2-teorema (diskret maksimum prinsipi)

𝔸 M-matritsa. Manbalar bo‘lmaganda suvli qatlamlar va ajratuvchilardagi yangi naporlar eski naporlar va chegaradagi naporlarning eng kichik va eng katta qiymatlari orasida bo‘ladi.

Demak sxema ixtiyoriy τ da monoton. Xususan, K yoki K′ keskin o‘zgaradigan joylarda tebranish hosil bo‘lmaydi, Krank–Nikolson sxemasida esa bu xossa faqat qadam cheklanganda saqlanadi. Nochiziqli holatda T₁ ≥ K₁b_min > 0 va E′ ≥ 0 bo‘lgani uchun har bir Pikar iteratsiyasining matritsasi ham M-matritsa, shuning uchun har bir iteratsiya bir qiymatli aniqlanadi. Pikar iteratsiyasining yaqinlashishi umumiy holda isbotlanmagan, iteratsiyalar soni har bir hisobda ko‘rsatiladi.

### Yaqinlashish

Silliq yechimda approksimatsiya xatosi O(τ + h² + δ²). 1-teorema bilan birga bu chiziqli masalada D normada shu tartibdagi yaqinlashishni beradi. Notekis to‘rda markazlashgan sxemaning lokal approksimatsiya xatosi birinchi tartibli bo‘lsa ham, global aniqlik ikkinchi tartibda saqlanishi ma’lum (Forsyth va Sammon 1988). Tartiblar 5-bo‘limda sonli tekshiriladi.

## 5. Tekshiruv

### Analitik va yarim analitik etalonlar

Bir jinsli bosimli qatlamlar va sarfi o‘zgarmas quduq uchun (2)–(6) Laplas sohasiga o‘tkaziladi. U yerda (4) aniq yechiladi. λ = b′√(pS′_s/K′) belgilash bilan ajratuvchi chegaralaridagi oqimlar quyidagicha bo‘ladi:

$$\bar q^+=\frac{K'}{b'}\lambda\,(\coth\lambda\,\bar h_j-\operatorname{csch}\lambda\,\bar h_{j+1}),\qquad \bar q^-=\frac{K'}{b'}\lambda\,(\operatorname{csch}\lambda\,\bar h_j-\coth\lambda\,\bar h_{j+1}).$$

Suvli qatlamlar tizimi Hemker (1985) yondashuvi bo‘yicha simmetrik ko‘rinishda xos vektorlarga yoyiladi va K₀ modifikatsiyalangan Bessel funksiyalari orqali yechiladi. Vaqt sohasiga 12 hadli Stehfest (1970) algoritmi bilan qaytiladi. Bu etalon Teys (1935) yechimini 10⁻⁵ nisbiy farq bilan takrorlaydi. Xantush–Jakob (1955) yechimi ham 10⁻⁴ farq bilan olinadi: buning uchun yuqori qatlamga juda katta T va S, ajratuvchiga esa S′_s = 0 beriladi (`testlar/test_masala1.py`).

### Ikkala ajratuvchisida elastik suv berishi bo‘lgan uch qatlam

Test masala parametrlari: T = 200, 100, 300 m²/sut; S = 2, 1, 3 ·10⁻⁴; K′ = 2·10⁻³ va 10⁻³ m/sut; b′ = 5 va 8 m; S′_s = 10⁻⁴ 1/m. Quduq 2-qatlamdan 500 m³/sut suv oladi. To‘r 105×105 yacheykadan iborat: markazdagi yacheyka 2 m, keyingilari 1,15 marta kattalashib 20 km gacha boradi. Har bir ajratuvchi M = 20 qatlamchaga bo‘lingan. Vaqt qadami 10⁻⁴ sut dan boshlanib, har qadamda 1,05 marta oshadi va 10 sut dan oshmaydi. 10⁻³–10 sut oralig‘ida Laplas etalonidan eng katta nisbiy farq 1-qatlamda 0,22%, 2-qatlamda 0,68–0,74%, 3-qatlamda 0,33% (`tajribalar/t3_modflow.py`). Qadam ko‘paytuvchisi 1,2 bo‘lganda 1- va 3-qatlamlardagi farq 1,2–1,8% gacha oshadi. Demak farqning asosiy qismi vaqt bo‘yicha birinchi tartibli xatodan kelib chiqadi.

### MODFLOW 6 bilan solishtirish

Shu masala MODFLOW 6 da (Langevin va boshq. 2017) tuzildi: har bir ajratuvchi 20 ta model qatlami (K33 = K′, SS = S′_s), suvli qatlamlarda K33 = 10⁶ m/sut, jami 43 qatlam, vaqt qadamlari bir xil. To‘qqizta kuzatuv nuqtasida naporlar farqi 4·10⁻⁹ m dan oshmaydi. Ikkala dasturning Laplas etalonidan farqi ham bir xil. Ikkala dastur bir xil diskret tenglamalarni yechadi. Farq shundaki, bizning dasturda siyrak tizim 43 emas, 3 qatlam uchun tuziladi, ajratuvchilar esa alohida uch diagonalli tizimlar bilan hisoblanadi.

### Ajratuvchi bo‘yicha yaqinlashish va suv balansi

1-jadval. Ajratuvchi ustuni (K′ = 10⁻² m/sut, b′ = 2 m, S′_s = 10⁻² 1/m) yuqori chegarasida napor birlik qiymatga sakrab o‘zgargandan keyin t = 0,5 sut dagi chegara oqimi q⁺ ning qator ko‘rinishidagi aniq yechimdan nisbiy farqi, τ = 10⁻⁴ sut.

| M | q⁺ ning nisbiy xatosi | kuzatilgan tartib |
|---|---|---|
| 4 | 3,9·10⁻² | |
| 8 | 8,5·10⁻³ | 2,20 |
| 16 | 2,1·10⁻³ | 2,00 |
| 32 | 5,8·10⁻⁴ | 1,86 |

M = 32 da tartibning biroz pasayishi vaqt bo‘yicha xatodan kelib chiqadi: τ = 10⁻⁴ sut da u shu kattalikda.

2-jadvalda uch qatlamli bog‘langan sxema butunligicha tekshiriladi (`tajribalar/t8_yaqinlashish.py`). Soha 1000 × 1000 m, chegaralarda oqim nolga teng. K₁, K₂ va 1-ajratuvchidagi K′ x, y koordinatalarga bog‘liq ravishda silliq o‘zgaradi. Ikkala ajratuvchida elastik suv berishi bor (b′ = 4 m, S′_s = 2·10⁻³ 1/m). Boshlang‘ich holatda 1-qatlamda balandligi 1 m bo‘lgan Gauss shaklidagi do‘nglik olingan, yechimlar t = 5 sut da solishtiriladi. Fazo bo‘yicha yacheyka o‘lchami h va qatlamcha qalinligi δ birga ikki marta kichraytiriladi. Xato uchta suvli qatlam naporlarining 160 × 160, M = 32 yechimining yacheykalar bo‘yicha o‘rtacha qiymatlaridan o‘rtacha kvadratik chetlanishi sifatida hisoblanadi. Vaqt bo‘yicha 40 × 40, M = 8 to‘rda τ ikki marta kichraytiriladi, etalon τ = 1/256 sut.

2-jadval. Bog‘langan sxemaning to‘r va vaqt qadami bo‘yicha yaqinlashishi: t = 5 sut dagi naporning o‘rtacha kvadratik xatosi.

| n × n, M | xato, m | tartib | τ, sut | xato, m | tartib |
|---|---|---|---|---|---|
| 20 × 20, 4 | 1,49·10⁻⁴ | | 0,5 | 8,0·10⁻⁴ | |
| 40 × 40, 8 | 3,55·10⁻⁵ | 2,07 | 0,25 | 3,95·10⁻⁴ | 1,02 |
| 80 × 80, 16 | 7,10·10⁻⁶ | 2,32 | 0,125 | 1,94·10⁻⁴ | 1,03 |
| | | | 0,0625 | 9,39·10⁻⁵ | 1,05 |

Tartiblar O(h² + δ² + τ) bahoni tasdiqlaydi. Eng mayda to‘rdagi 2,32 qiymat biroz katta chiqqan, chunki bu to‘r etalondan faqat bir marta yirikroq.

Bitta ajratuvchi ustunida vaqt qadami maydalanganda ham tartib 1 ga teng. Barcha jarayonlar qatnashgan geterogen, murakkab shakldagi masalada suv balansi qoldig‘i har bir qadamda 10⁻¹⁰ dan kichik. S′_s → 0 da yechim elastik suv berishi hisobga olinmagan modelga yaqinlashadi (farq < 10⁻⁸ m).

### Dalem tajriba ma’lumotlari

Dalem tajribasi Kruseman va de Ridder (1990) kitobining 4.2-jadvalida De Ridder (1961) bo‘yicha keltirilgan. Quduq sarfi Q = 761 m³/sut, to‘rtta pyezometr quduqdan 30–120 m masofada. Ma’lumotlar yuqori qatlam napori o‘zgarmas deb olingan Laplas etaloni bilan moslashtirildi.

| Talqin | KD, m²/sut | S | c, sut | S′ | RMSE, mm |
|---|---|---|---|---|---|
| Walton usuli (Kruseman, de Ridder 1990) | 1731 | 1,9·10⁻³ | 468 | | 6,9 |
| ajratuvchining elastik suv berishisiz, eng kichik kvadratlar | 1674 | 1,77·10⁻³ | 325 | | 5,87 |
| ajratuvchining elastik suv berishi bilan, eng kichik kvadratlar | 1670 | 1,52·10⁻³ | 370 | 1,1·10⁻³ | 5,80 |

Ajratuvchining elastik suv berishini qo‘shish xatoni deyarli kamaytirmaydi, S′ esa ishonchli aniqlanmaydi: lg S′ ning standart chetlanishi 0,41. Kuzatuvlar 0,015–0,33 sut oralig‘ida, bu topilgan t_c ≈ 0,4 sut bilan bir tartibda. Demak bu ma’lumotlar modelni tasdiqlaydi, lekin faqat suvli qatlamdagi pasayish bo‘yicha ajratuvchining elastik suv berishini tasdiqlab bo‘lmaydi. Shunga qaramay topilgan S′ = 1,1·10⁻³ qiymat Kruseman va de Ridder (1990, 97–98-betlar) Neuman–Witherspoon nisbatlar usuli bilan olgan S′ = 1,1·10⁻³ bilan mos keladi. Ular ajratuvchi ichidagi qo‘shimcha pyezometrdan foydalangan (D′ = 8 m, K′D′/S′ = 126 m²/sut). Ularning o‘rtacha parametrlari: KD = 1800 m²/sut, S = 1,7·10⁻³, c = 450 sut. O‘lchangan pasayishlar chop etilishdan oldin quduqning to‘liq ochmaganligi va dengiz suvi ko‘tarilishi ta’siri bo‘yicha tuzatilgan, biz ularni shu ko‘rinishda ishlatdik.

### Chop etilgan ko‘p qatlamli misollar

Olsthoorn (2003) uchta ajratuvchi (c = 100, S′ = 0,0016) orasidagi ikki suvli qatlam (kD = 100, S = 10⁻⁴) uchun pasayishlarni keltiradi. Tizim ustida va ostida pasayish nolga teng, r = 10, t = 10⁻⁵–5. Maqolada bu qiymatlar Hemker va Maas (1987) natijalari bilan bir xil ekani aytilgan. Ikki tashqi ajratuvchi bilan kengaytirilgan Laplas etalonimiz jadvaldagi 36 qiymatning hammasini bosilgan to‘rt xonagacha takrorlaydi (`testlar/test_masala1.py`). Sonli modelda tashqi naporlar napori berilgan ikki qatlam bilan, har bir ajratuvchi M = 20 qatlamcha bilan tasvirlandi. To‘rning eng yaqin nuqtasida (r = 10,69) t ≥ 10⁻³ da etalondan farq 0,25% dan oshmaydi (`tajribalar/t7_maas_mlu.py`). Kattaroq farqlar faqat birinchi vaqt qadamlarida uchraydi.

MLU qo‘llanmasidagi "Two-aquifers" tekshiruv misoli (Hemker va Randall 2010) bosimsiz qatlam, 10 m qalinlikdagi ajratuvchi va quduqli qatlamdan (Q = 180 m³/sut) iborat. Unda ajratuvchining elastik suv berishi va gorizontal oqimi uchta yupqa qatlam bilan tasvirlangan, jami oltita qatlam. Laplas etalonimiz 1 minutdan keyin r = 5,01 m da 0,29826 m beradi, bu MLU qiymatining barcha bosilgan raqamlari bilan bir xil. 15,85 m da 0,0496 m olinadi, MLU da 0,050 m. Xuddi shu olti qatlamli tizim uchun sonli model etalondan to‘rning ikki eng yaqin nuqtasida 0,04% va 0,3% farq qiladi. Veling va Maas (2009) misolida faqat zarrachalar trayektoriyalari keltirilgani uchun u ishlatilmadi.

## 6. Natijalar

### Ajratuvchining elastik suv berishini qachon hisobga olmaslik mumkin?

5-bo‘limdagi tizim K′ = 10⁻³ m/sut va b′ = 5 m bilan olinadi, bunda t_c = 2,5 sut. Suvli qatlamlarning elastik suv berish koeffitsiyentlari ko‘paytuvchi bilan o‘zgartirilib, ε = 0,083–83 oraliq hosil qilindi. Ikki model r = 30 m da solishtirildi (2-rasm).

| ε | Quduqli qatlamda farq 5% dan katta bo‘lgan oxirgi t/t_c | t = 10³ t_c dagi farq |
|---|---|---|
| 0,083 | 0,25 | 0,4% |
| 0,83 | 0,79 | 2,3% |
| 8,3 | 10³ dan katta | 6,6% |
| 83 | 10³ dan katta | 12% |

ε o‘zgarmas bo‘lganda t/t_c bo‘yicha chizilgan egri chiziqlar ustma-ust tushadi. Kichik ε da t_c dan biroz keyin ajratuvchining elastik suv berishini hisobga olmaslik mumkin. ε ≳ 1 da esa bunday emas: yopiq tizimda ajratuvchidan ajralgan suv umumiy elastik suv zaxirasini oshirib turaveradi. Quduq bo‘lmagan qo‘shni qatlamda farq yana ham katta: ε = 0,83 da t = 10³ t_c da 10%. Faqat t_c ga asoslangan mezon bu holatlarda noto‘g‘ri xulosaga olib keladi.

### Bosimsiz yuqori qatlamli geterogen maydon

Soha 2000 × 1000 m, to‘r 80 × 40 yacheyka. 1-qatlam bosimsiz, unda filtratsiya koeffitsiyenti kichik linza va egri-bugri yo‘nalgan yuqori o‘tkazuvchan o‘zan bor. K₂(x,y) silliq o‘zgaradi va linzaga ega, K₃ ikki zonadan iborat. 1-ajratuvchida K′ 20 marta katta bo‘lgan gidrogeologik oyna bor. Infiltratsion ta’minot 6·10⁻⁴ m/sut; bug‘lanish parametrlari E₀ = 1,5·10⁻³ m/sut, Δ = 3 m, n = 1,5. Chap va o‘ng chegarada napor berilgan. To‘rtta quduq jami 3200 m³/sut suv oladi: uchtasining filtri 2-qatlamda, bittasiniki 3-qatlamda. Hisob statsionar holatdan boshlanadi.

Yupqa ajratuvchilarda (t_c = 11 va 32 sut) geterogenlik 2-qatlamdagi eng katta pasayishni bir jinsli maydonga nisbatan ikki baravar oshiradi (10,5 m va 5,6 m). Oyna orqali pasayish grunt suvlari sathiga ham o‘tadi (0,67 m va 0,05 m). Bir yil davomida quduqlar suvining 0,6% i ajratuvchilar zaxirasidan olinadi va elastik suv berishi pasayishni 0,5% dan kam o‘zgartiradi (`tajribalar/t5_geterogen.py`).

Qalin gilli ajratuvchilarda (b′ = 15 va 20 m, K′ = 10⁻⁴ va 5·10⁻⁵ m/sut, S′_s = 4·10⁻⁴ 1/m) t_c = 900 va 3200 sut, ya’ni hisoblangan bir yildan uzoq. Barcha o‘zgarishlar faqat quduqlardan kelishi uchun infiltratsion ta’minot o‘zgarmas olindi (3-rasm).

Elastik suv berishi 2-qatlamda dastlabki napor pasayishini 18–30% ga sekinlashtiradi. Taxminan t = 1 sut da quduqlar suvining 26% i ajratuvchilardan keladi. Keyinchalik asosiy manba napor berilgan chegaralar bo‘ladi, bir yildan keyin quduqli qatlamdagi farq 0,5% dan kam. Bosimsiz qatlamda esa holat boshqacha: bir yildan keyin grunt suvlari sathi elastik suv berishi hisobga olingan modelda 0,051 m ga, hisobga olinmagan modelda 0,060 m ga pasayadi. 14% lik bu farq hisob oxirigacha saqlanadi. Balans qoldig‘i 4·10⁻¹² dan kichik, Pikar iteratsiyalari har bir qadamda 4 tadan oshmaydi.

## 7. Muhokama

Natijalardan amaliy xulosa kelib chiqadi. Agar ε kichik bo‘lsa, t bir necha t_c dan oshgandan keyin quduqli qatlamda ajratuvchining elastik suv berishini hisobga olmaslik mumkin. Qalin gil qatlam ustidagi grunt suvlari qatlamida esa t_c dan kichik vaqtlarda bunday model sath pasayishini oshirib baholaydi, bug‘lanish va tuz to‘planishini esa aynan shu pasayish belgilaydi. Sug‘oriladigan tekisliklarga xos ajratuvchilarda (10–20 m qalinlikdagi gil va qumoq) t_c yillar bilan o‘lchanadi, shuning uchun elastik suv berishi modelda saqlanishi kerak.

Ajratuvchi ustunlarini yo‘qotish MODFLOW dagi qatlamli tasvirga teng kuchli. Natijalar mashina aniqligigacha mos keladi, lekin bizning tizim matritsasining o‘lchami faqat suvli qatlamlar masalasiga teng. 2-lemma bu yo‘qotish M-matritsa tuzilishini saqlashini ko‘rsatadi. Demak musbatlik va turg‘unlik testlarda kuzatilibgina qolmay, kondensatsiyalangan tizimga isbot orqali o‘tadi.

Modelning cheklovlari quyidagilar. 2- va 3-qatlamlar doimo bosimli deb olinadi, har bir quduqning filtri bitta qatlamda. Ajratuvchilarda faqat vertikal oqim hisobga olinadi. 5-bo‘limdagi MLU misolida uchta qatlamni uzluksiz (4) tenglama bilan almashtirish (b′ = 10 m, K′ = 0,1 m/sut, S′ = 0,004) quduqli qatlamda r = 5,01 m dagi pasayishni 1 minutda −7% ga, 7 sutkada +1,2% ga o‘zgartiradi; 15,85 m da bu farqlar −16% va +1,3%. Farqning bir qismi MLU tasviridagi vertikal yo‘nalishdagi yirik bo‘linishdan, bir qismi bizning modelda hisobga olinmagan ajratuvchidagi gorizontal oqimdan kelib chiqadi; bu ikki ta’sir alohida ajratilmadi. Vaqt bo‘yicha sxema birinchi tartibli. BDF2 kabi ikkinchi tartibli sxema qadam cheklanmasa M-matritsa xossasini yo‘qotadi, shuning uchun oshkormas Eyler sxemasi saqlandi va xato qadam o‘sishi bilan boshqariladi. Pikar iteratsiyasining yaqinlashishi isbotlanmagan, har qadamda nazorat qilinadi. Dala ma’lumotlari bilan tekshiruv bitta klassik tajribaga asoslangan va bu tajriba ajratuvchining elastik suv berishini aniqlay olmaydi. Buning uchun Dalemdagi kabi ajratuvchi ichida pyezometri bo‘lgan tajriba kerak.

## 8. Xulosalar

1. Har bir ajratuvchida elastik rejim tenglamasi, K(x,y), bosimsiz yuqori qatlam, infiltratsion ta’minot, bug‘lanish va quduqlar bo‘lgan uch qatlamli model tuzildi. U har bir ajratuvchi ustunini aniq yo‘qotadigan chekli hajmlar sxemasi bilan yechildi.
2. Sxema massani aniq saqlaydi, elastik suv zaxirasi bilan vaznlangan normada absolyut turg‘un va diskret maksimum prinsipini qanoatlantiradi. Kondensatsiyalangan almashinuv matritsasi simmetrik va musbat yarim aniq.
3. Dastur Teys, Xantush–Jakob va Laplas sohasidagi ko‘p qatlamli yechimlarni 0,7% aniqlikda takrorlaydi. MODFLOW 6 bilan farq 4·10⁻⁹ m. Yaqinlashish tartibi fazo bo‘yicha (suvli qatlamlar to‘ri va ajratuvchi qatlamchalari) ikki, vaqt bo‘yicha bir.
4. Ajratuvchining elastik suv berishini hisobga olmaslik mumkinligi t/t_c va ε = S′/ΣS ga bog‘liq. ε ≳ 1 da uning ta’siri t_c dan ancha keyin ham saqlanadi.
5. Qalin gilli ajratuvchilar va geterogen maydonda ajratuvchining elastik suv berishi hisobga olinmagan model bir yildan keyin bosimsiz qatlamdagi sath pasayishini taxminan 14% ga oshirib baholaydi.

Keyingi ish: ajratuvchi orqali tuzlar ko‘chishi bilan bog‘lash (dissertatsiyaning 2-masalasi) va ajratuvchida pyezometrlari bo‘lgan obyekt ma’lumotlari bo‘yicha kalibrlash.

## Sun’iy intellektdan foydalanish to‘g‘risida bayonot

Dastur kodini yozish va sinash, rasmlarni tayyorlash va maqola tilini tahrirlashda Claude (Anthropic) dan foydalanildi. Barcha tenglamalar, isbotlar, sonli natijalar va adabiyotlar mualliflar tomonidan tekshirilgan, mazmun uchun to‘liq javobgarlik mualliflarda. [matn jurnal talabiga moslashtiriladi]

## Ma’lumotlar va dastur

Har bir raqam va rasmni hosil qiluvchi dastur, kiruvchi ma’lumotlar va skriptlar https://github.com/javokhir-erkinov/1-masala manzilida (qabul qilingandan keyin DOI bilan arxivlanadi).

## Mualliflar hissasi

J. Erkinov: g‘oya, model, sonli usul, isbotlar, dastur, tekshiruv, matn. N. Ravshanov: ilmiy rahbarlik, masalaning qo‘yilishi, matnni ko‘rib chiqish va tahrirlash. [aniqlashtiriladi]

## Moliyalashtirish, manfaatlar to‘qnashuvi

[To‘ldiriladi.]

## Adabiyotlar

Adabiyotlar ro‘yxati inglizcha qoralamadagi bilan bir xil (DOI lar 20.11.2026 da Crossref bo‘yicha tekshirilgan) va jurnal talabiga ko‘ra lotin yozuvida beriladi.
