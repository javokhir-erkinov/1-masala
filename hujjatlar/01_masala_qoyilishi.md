# 1-masala. Uch qatlamli muhitda ajratuvchilarning elastik suv zaxirasini hisobga olgan holda suv filtratsiyasi

Loyiha matni, 20.11.2026. Dastur: `masala1` (shu repozitoriy).

## 1. Asos bo'ladigan ishlar va qo'shiladigan qism

Masala Ravshanov ilmiy maktabining uch qatlamli modellarining davomi.

| Ish | Modelda bor | Modelda yo'q |
|---|---|---|
| Ravshanov, Shadmanov va boshq., Hydrology 2026, 13, 276 | uch suvli qatlam, ikki ajratuvchi; qatlam ichida K(x,y); massani saqlovchi almashinuv; garmonik o'rtacha; ADI va Pikar | ajratuvchining elastik suv berishi; bosimsiz qatlam; quduq; infiltratsiya va bug'lanish; turg'unlik isboti; qatlamlararo almashinuvning analitik tekshiruvi |
| Mukhamadiyev, Karimov, SPIE 2025 va Mathematics 2026, 14, 256 (bitta model) | bosimsiz yuqori qatlam; T(x,y); bug'lanish; elastik rejimdagi kam o'tkazuvchan qatlam | elastik rejimdagi qatlam pastda va tubi suv o'tkazmaydi, ikki suvli qatlam orasida emas; tutashuv sharti to'liq emas; turg'unlik isboti yo'q |
| Kayumov va boshq., J. Phys.: Conf. Ser. 2024, 2697, 012042 | bitta suvli qatlam (1D, x bo'yicha) va ostidagi kam o'tkazuvchan qatlamda vertikal elastik rejim tenglamasi; 13 ta nochiziqli filtratsiya qonuni | ikkinchi suvli qatlam yo'q, ostki chegara suv o'tkazmaydi; tutashuv sharti (napor uzluksizligi) yozilmagan; K(x,y) yo'q; turg'unlik isboti va tekshiruv yo'q |
| Aminov S.M., 2023, PhD (neft-gaz) | ikki qatlam va ko'prikda diffuziya tenglamasi | boshqa jarayon (neft-gaz); faqat avtoreferat o'qilgan |
| Qodirov K.R., 2023, PhD dissertatsiya (Ravshanov va boshq. 2017, PCAM 1(7) maqolasi bilan) | elastik rejimdagi ikki ajratuvchi orasidagi asosiy suvli qatlam (Hantush 1960 joylashuvi), tashqarida napor berilgan yoki suv o'tkazmaydigan asos; ustida grunt suvlari va bug'lanish bo'lgan chiziqlashtirilgan tizim; galereya va quduqlar batareyasi | uchta bog'langan suvli qatlam yo'q; parametrlar o'zgarmas; yechim analitik (Laplas, Xankel) |

Xalqaro ishlarda ajratuvchining elastik suv zaxirasi analitik (Neuman, Witherspoon 1969; Hemker 1985; Hemker, Maas 1987; Cihan va boshq. 2011) va MODFLOW paketlarida (TLK1, Leake va boshq. 1994; CSUB, Hughes va boshq. 2022) hisobga olingan. Shuning uchun ajratuvchining elastik suv berishini hisobga olishning o'zi yangilik emas.

Qo'shiladigan qism quyidagilarning birgalikdagi sonli yechimi:

1. har bir ajratuvchida vertikal bir o'lchamli elastik rejim tenglamasi, tutashuv chegaralarida napor va oqim uzluksizligi bilan;
2. har bir suvli qatlamda K(x,y), ajratuvchilarda K′(x,y), b′(x,y), S′_s(x,y);
3. bosimsiz nochiziqli yuqori qatlam, infiltratsiya, bug'lanish, quduqlar, ixtiyoriy shakldagi soha;
4. bitta massani saqlovchi sxema, uning turg'unligi va maksimum prinsipining isboti;
5. t_c = b′S′/K′ mezoni bo'yicha ajratuvchining elastik suv berishi hisobga olingan va olinmagan modellarni solishtirish.

## 2. Farazlar

1. Suvli qatlamlarda oqim gorizontal (Dyupyui farazi), ajratuvchilarda vertikal (Hantush farazi). Ajratuvchida gorizontal oqim hisobga olinmaydi, chunki K′ ≪ K_k.
2. Suv va skelet elastik siqiladi; bosimli qatlamlar va ajratuvchilarda zaxira chiziqli (S_k, S′_s o'zgarmas).
3. 1-qatlam bosimsiz, uning to'yingan qalinligi h₁ − z₀; suv berish koeffitsiyenti μ. 2- va 3-qatlam doimo bosimli.
4. Bug'lanish sizot suvlari chuqurligiga bog'liq (S.F. Averyanov qonuni).
5. Quduqlar bitta qatlamda filtrga ega, sarfi berilgan.
6. Muhit izotrop: har bir nuqtada K bitta son, lekin x, y ga bog'liq.

## 3. Matematik model

Soha Ω ⊂ ℝ² (ixtiyoriy shakl), chegarasi Γ = Γ_D ∪ Γ_N. Qatlamlar yuqoridan pastga k = 1, 2, 3; j-ajratuvchi (j = 1, 2) j- va (j+1)-qatlam orasida. ζ ∈ [0, b′_j] ajratuvchi shipidan pastga yo'nalgan vertikal koordinata.

### Suvli qatlamlar

$$\mu\frac{\partial h_1}{\partial t}=\nabla\cdot\big(K_1(h_1-z_0)\nabla h_1\big)+W-E(h_1)-q^{+}_1-\sum_i Q_{1i}\,\delta(\mathbf x-\mathbf x_i),\tag{1}$$

$$S_2\frac{\partial h_2}{\partial t}=\nabla\cdot(T_2\nabla h_2)+q^{-}_1-q^{+}_2-\sum_i Q_{2i}\,\delta(\mathbf x-\mathbf x_i),\tag{2}$$

$$S_3\frac{\partial h_3}{\partial t}=\nabla\cdot(T_3\nabla h_3)+q^{-}_2-\sum_i Q_{3i}\,\delta(\mathbf x-\mathbf x_i),\tag{3}$$

bu yerda T_k = K_k(x,y) b_k(x,y).

### Ajratuvchilar

$$S'_{s,j}\frac{\partial u_j}{\partial t}=K'_j\frac{\partial^2 u_j}{\partial\zeta^2},\qquad 0<\zeta<b'_j,\tag{4}$$

$$u_j\big|_{\zeta=0}=h_j,\qquad u_j\big|_{\zeta=b'_j}=h_{j+1},\tag{5}$$

$$q^{+}_j=-K'_j\frac{\partial u_j}{\partial\zeta}\Big|_{\zeta=0},\qquad q^{-}_j=-K'_j\frac{\partial u_j}{\partial\zeta}\Big|_{\zeta=b'_j}.\tag{6}$$

q⁺_j j-qatlamdan ajratuvchiga, q⁻_j ajratuvchidan (j+1)-qatlamga o'tgan solishtirma sarf (pastga musbat). (5) napor uzluksizligi, (6) oqim uzluksizligi. (4) ni ζ bo'yicha integrallasak:

$$\frac{d}{dt}\int_0^{b'_j}S'_{s,j}u_j\,d\zeta=q^{+}_j-q^{-}_j,\tag{7}$$

ya'ni ajratuvchiga kirgan va undan chiqqan suv farqi uning elastik suv zaxirasi o'zgarishiga teng. S′_s = 0 bo'lsa q⁺_j = q⁻_j = K′_j(h_j − h_{j+1})/b′_j (Hydrology 2026, 13, 276 dagi ajratuvchining elastik suv berishi hisobga olinmagan almashinuv).

### Bug'lanish

$$E(h_1)=E_0\Big(1-\frac{z_s-h_1}{\Delta}\Big)^{n},\quad 0\le z_s-h_1\le\Delta;\qquad E=0,\quad z_s-h_1>\Delta,\tag{8}$$

z_s yer sathi, Δ bug'lanish to'xtaydigan chuqurlik, n ko'rsatkich.

### Boshlang'ich va chegaraviy shartlar

$$h_k(\mathbf x,0)=h_k^0(\mathbf x),\qquad u_j(\mathbf x,\zeta,0)=u_j^0(\mathbf x,\zeta),\tag{9}$$

$$h_k=g_k\ \text{(}\Gamma_{D,k}\text{ da)},\qquad T_k\frac{\partial h_k}{\partial n}=0\ \text{(}\Gamma_{N,k}\text{ da)}.\tag{10}$$

Odatda boshlang'ich holat sifatida quduqlarsiz statsionar holat olinadi; unda u_j⁰ chiziqli.

### Global suv balansi

(1)–(3) ni Ω bo'yicha integrallab, (7) ni qo'shsak, almashinuv hadlari qisqaradi:

$$\frac{d}{dt}\Big[\int_\Omega\big(\mu h_1+S_2h_2+S_3h_3\big)d\mathbf x+\sum_{j}\int_\Omega\!\int_0^{b'_j}S'_{s,j}u_j\,d\zeta\,d\mathbf x\Big]=\int_\Omega(W-E)\,d\mathbf x-\sum Q+\sum_k\oint_{\Gamma_{D,k}}T_k\frac{\partial h_k}{\partial n}ds.\tag{11}$$

### Xarakterli vaqt

(4) ni o'lchamsizlantirsak, ajratuvchi uchun xarakterli vaqt

$$t_{c,j}=\frac{b'^2_jS'_{s,j}}{K'_j}=\frac{b'_jS'_j}{K'_j},\qquad S'_j=S'_{s,j}b'_j.\tag{12}$$

t ≫ t_c da ajratuvchidagi napor taqsimoti chiziqliga yaqin va elastik suv berishi hisobga olinmagan almashinuv yetarli; t ≲ t_c da elastik suv zaxirasi hisobga olinishi kerak. Herrera, Figueroa (1970) dagi "xotira vaqti" 3S′b′/(π²K′) ≈ 0,30 t_c.

## 4. Sonli sxema

### Fazoviy diskretizatsiya

Ω to'g'ri burchakli (notekis) to'r bilan qoplanadi; Ω dan tashqaridagi yacheykalar hisobdan chiqariladi. P yacheyka va uning qo'shnisi Q orasidagi yuz o'tkazuvchanligi ketma-ket qarshiliklar bo'yicha:

$$C_{PQ}=\ell_{PQ}\Big(\frac{d_P}{2T_P}+\frac{d_Q}{2T_Q}\Big)^{-1},\tag{13}$$

ℓ_PQ yuz uzunligi, d_P, d_Q yacheyka o'lchamlari. 1-qatlamda T₁ = K₁ max(h₁ − z₀, b_min).

Har bir ajratuvchi M ta qatlamchaga bo'linadi, δ = b′/M, tugunlar qatlamcha markazida:

$$\frac{S'_s\delta}{\tau}(u_m^{n+1}-u_m^n)=c_{m-1/2}(u^{n+1}_{m-1}-u^{n+1}_m)+c_{m+1/2}(u^{n+1}_{m+1}-u^{n+1}_m),\quad m=1..M,\tag{14}$$

u₀ = h_j, u_{M+1} = h_{j+1}; ichki c = K′/δ, chetki c_{1/2} = c_{M+1/2} = 2K′/δ. Oqimlar q⁺ = c_{1/2}(h_j − u₁), q⁻ = c_{M+1/2}(u_M − h_{j+1}).

### Vaqt bo'yicha diskretizatsiya

Oshkormas Eyler sxemasi. P yacheyka uchun (A_P yuza):

$$\frac{S_PA_P}{\tau}(h_P^{n+1}-h_P^n)+\sum_Q C_{PQ}(h_P^{n+1}-h_Q^{n+1})+A_P\big(q^{+}_P-q^{-}_P\big)^{n+1}=A_P\big(W-E\big)_P^{n+1}-Q_P.\tag{15}$$

### Ajratuvchini yo'qotish (statik kondensatsiya)

(14) har bir ustunda uch diagonalli simmetrik tizim: 𝔗u = s uⁿ + c_{1/2}e₁h_j + c_{M+1/2}e_Mh_{j+1}, s = S′_sδ/τ. Uni progonka bilan uch o'ng tomon uchun yechamiz:

$$u=a+\alpha h_j+\beta h_{j+1},\qquad \mathfrak T a=s\,u^n,\quad \mathfrak T\alpha=c_{1/2}e_1,\quad\mathfrak T\beta=c_{M+1/2}e_M.\tag{16}$$

Natijada oqimlar qo'shni naporlarning chiziqli funksiyasi:

$$\begin{pmatrix}q^{+}\\-q^{-}\end{pmatrix}=\Lambda\begin{pmatrix}h_j\\h_{j+1}\end{pmatrix}-\begin{pmatrix}c\,a_1\\c\,a_M\end{pmatrix},\qquad \Lambda=c\begin{pmatrix}1-\alpha_1&-\beta_1\\-\alpha_M&1-\beta_M\end{pmatrix}.\tag{17}$$

Bu Λ ni (15) ga qo'yib, faqat suvli qatlamlar naporlari uchun bitta siyrak tizim olinadi. Yechimdan keyin ajratuvchi naporlari (16) dan tiklanadi. M = 0 bo'lsa Λ = (K′/b′)[[1, −1], [−1, 1]].

### Nochiziqlilik

1-qatlamda T₁(h₁) va E(h₁) Pikar iteratsiyasi bilan aniqlanadi: r-iteratsiyada T₁ = T₁(h^{(r)}), E esa h^{(r)} atrofida chiziqlashtiriladi:

$$E(h^{(r+1)})\approx E(h^{(r)})+E'(h^{(r)})\,(h^{(r+1)}-h^{(r)}),\qquad E'\ge0.\tag{18}$$

E′ ≥ 0 bo'lgani uchun bu had matritsa diagonalini oshiradi. Iteratsiya max|h^{(r+1)} − h^{(r)}| < ε bo'lganda to'xtaydi.

### Algoritm

1. Boshlang'ich holat: statsionar masala yechiladi, u_j⁰ chiziqli.
2. Har bir vaqt qadamida: (16) har bir ajratuvchi ustunida progonka bilan yechiladi (h ga bog'liq emas, qadamda bir marta).
3. Pikar sikli: T₁ va E chiziqlashtiriladi, (15) yig'iladi va simmetrik siyrak tizim yechiladi.
4. u_j (16) dan tiklanadi, suv balansi hisoblanadi.

## 5. Sxema xossalari

Quyida 𝔸 = D/τ + 𝕃 ajratuvchi noma'lumlari bilan birga yozilgan to'liq tizim matritsasi (D: S_PA_P va S′_sδA_P diagonal, 𝕃: gorizontal va vertikal o'tkazuvchanliklar).

### 1-lemma (diskret balans)

(15) ni barcha erkin yacheykalar bo'yicha, (14) ni barcha ustun va qatlamchalar bo'yicha yig'sak, ichki oqimlar juft-jufti bilan qisqaradi va (11) ning diskret ko'rinishi aniq bajariladi:

$$\Delta V_{\text{qatlam}}+\Delta V_{\text{ajratuvchi}}=\tau\Big(\sum(W-E_{\text{lin}})A-\sum Q+B_D\Big),\tag{19}$$

B_D berilgan napor yacheykalaridan kelgan oqim. Isbot: C_PQ simmetrik, (17) dagi q⁺ va q⁻ (14) ning chetki oqimlari bilan bir xil. Dasturda qoldiq 10⁻¹³ tartibida.

### 2-lemma (kondensatsiya xossalari)

𝔗 diagonal ustunligi qat'iy bo'lgan M-matritsa, shuning uchun 𝔗⁻¹ ≥ 0 va α, β ≥ 0. 𝔗 simmetrik bo'lgani uchun c α_M = c β₁, ya'ni Λ simmetrik. 𝔗·𝟙 = s𝟙 + c e₁ + c e_M dan

$$1-\alpha_m-\beta_m=\big(\mathfrak T^{-1}s\mathbb 1\big)_m\ge0,\tag{20}$$

demak Λ ning diagonal elementlari manfiy emas, diagonaldan tashqari elementlari musbat emas va qatorlar yig'indisi manfiy emas. Λ diagonal ustunlikka ega simmetrik matritsa, ya'ni musbat yarim aniq. Kondensatsiyadan keyingi matritsa ham simmetrik M-matritsa bo'lib qoladi (Shur to'ldiruvchisi).

### 1-teorema (turg'unlik)

Chiziqli holatda (bosimli qatlamlar, E = 0) va g_k = 0 da ixtiyoriy τ > 0, M, to'r va K, K′, S, S′_s ning ixtiyoriy musbat qiymatlarida

$$\|h^{n+1}\|_D\le\|h^n\|_D+\tau\,\|D^{-1}F^{n+1}\|_D,\qquad \|v\|_D^2=v^{\top}Dv.\tag{21}$$

Isbot: (15) va (14) ni h^{n+1} ga skalyar ko'paytiramiz. 𝕃 simmetrik musbat yarim aniq, shuning uchun (h^{n+1})ᵀ𝕃h^{n+1} ≥ 0. Qolgan qism (h^{n+1} − hⁿ)ᵀD h^{n+1} ≥ ‖h^{n+1}‖²_D − ‖hⁿ‖_D‖h^{n+1}‖_D va Koshi–Bunyakovskiy tengsizligidan kelib chiqadi. Sxema absolyut turg'un; ajratuvchi zaxirasi D normasiga kiradi, ya'ni baho ajratuvchilardagi naporlarni ham chegaralaydi.

### 2-teorema (maksimum prinsipi)

𝔸 ning diagonali musbat, diagonaldan tashqari elementlari musbat emas, erkin yacheykalar qatorlari yig'indisi musbat (D/τ > 0). Demak 𝔸 M-matritsa va manbalar bo'lmaganda

$$\min\big(\min h^n,\ \min g\big)\le h^{n+1}\le\max\big(\max h^n,\ \max g\big)\tag{22}$$

(suvli qatlam va ajratuvchi naporlari uchun). Sxema monoton: τ qanchalik katta bo'lmasin, parametrlar keskin o'zgaradigan joylarda tebranish hosil bo'lmaydi. Krank–Nikolson sxemasida bu xossa faqat τ cheklangan bo'lsa bajariladi. Nochiziqli holatda har bir Pikar iteratsiyasi matritsasi ham M-matritsa (T₁ ≥ K₁b_min > 0, E′ ≥ 0), shuning uchun har bir iteratsiya bir qiymatli yechimga ega.

### Yaqinlashish

Approksimatsiya xatosi silliq yechimda O(τ + h² + δ²). 1-teorema va Laks teoremasi bo'yicha chiziqli holatda yechim D normada shu tartibda yaqinlashadi. Notekis to'rda katakcha markazli sxemaning lokal xatosi kamroq, lekin global ikkinchi tartib saqlanadi (superyaqinlashish); bu sonli tekshiriladi. Pikar iteratsiyasining yaqinlashishi umumiy holda isbotlanmagan; uning bajarilishi har qadamda nazorat qilinadi.

## 6. Tekshiruv rejasi

| № | Tekshiruv | Holati |
|---|---|---|
| 1 | Laplas sohasidagi ko'p qatlamli radial yechim (Hemker 1985 yondashuvi, Stehfest) ↔ Teys, Xantush–Jakob | bajarildi: 10⁻⁵, 10⁻⁴ |
| 2 | Sonli yechim ↔ 1-etalon (uch qatlam, ikkala ajratuvchida elastik suv berishi, o'rta qatlamda quduq) | bajarildi: ≤ 0,7% |
| 3 | Ajratuvchi ustuni ↔ aniq qator yechim; δ va τ bo'yicha tartib | bajarildi: 2 va 1 |
| 4 | Diskret balans (19), murakkab masala | bajarildi: < 10⁻¹⁰ |
| 5 | S′_s → 0 da elastik suv berishi hisobga olinmagan modelga o'tish | bajarildi |
| 6 | MODFLOW 6 (ajratuvchi alohida qatlamlar sifatida) | bajarildi (10-bo'lim) |
| 7 | Maas–Olsthoorn 2003 (Hemker–Maas 1987) jadvali, MLU "Two-aquifers" | bajarildi (12-bo'lim); Veling–Maas da faqat zarracha trayektoriyalari bor, ishlatilmadi |
| 8 | Dalem ma'lumotlari (Kruseman, de Ridder 1990, 4.2-jadval) | bajarildi (8-bo'lim) |
| 9 | t/t_c bo'yicha elastik suv berishi hisobga olingan va olinmagan modellar farqi | bajarildi (7-bo'lim) |
| 10 | Uch qatlamli bog'langan sxemaning to'r va vaqt qadami bo'yicha yaqinlashishi | bajarildi (13-bo'lim): 2 va 1 |

## 7. Dastlabki natija: t_c mezoni yetarli emas

`tajribalar/t2_tc_mezoni.py`, rasm `tajribalar/t2_tc_mezoni.png`. Bir jinsli uch qatlam, o'rta qatlamda quduq (Q = 500 m³/sut, r = 30 m), K′ = 10⁻³ m/sut, b′ = 5 m, S′_s = 10⁻⁴ 1/m (t_c = 2,5 sut). Suvli qatlamlarning elastik suv berish koeffitsiyentlari ko'paytuvchi bilan o'zgartirildi, ε = S′/ΣS_k.

| ε | Quduqli qatlamda farq 5% dan katta bo'lgan oxirgi t/t_c | t/t_c = 10³ dagi farq |
|---|---|---|
| 0,083 | 0,25 | 0,4% |
| 0,83 | 0,79 | 2,3% |
| 8,3 | 10³ dan katta | 6,6% |
| 83 | 10³ dan katta | 12% |

Xulosa:

1. Farq ikki o'lchamsiz parametrga bog'liq: t/t_c va ε. Bir xil ε da t/t_c bo'yicha egri chiziqlar ustma-ust tushadi (S va S′_s ni birga o'zgartirib tekshirildi).
2. ε ≲ 0,1 da t > t_c dan keyin ajratuvchining elastik suv berishi hisobga olinmagan model quduqli qatlamda yetarli (farq < 5%).
3. ε ≳ 1 da farq t ≫ t_c da ham yo'qolmaydi: yopiq tizimda ajratuvchi zaxirasi umumiy elastik suv zaxirasiga qo'shiladi. Demak faqat t_c bo'yicha baholash noto'g'ri xulosaga olib keladi.
4. Qo'shni qatlamlarda farq ancha katta (1-qatlamda ε = 0,83 da t = 10³t_c da ham 10%).

Neuman, Witherspoon (1969) va Hantush (1960) da ham elastik suv berish koeffitsiyentlari nisbati S′/S parametr sifatida qatnashadi; bu natija ularga zid emas. Maqolada uni K(x,y) va bosimsiz qatlam bo'lgan holatda sonli model bilan tekshirish kerak.

## 8. Dalem ma'lumotlari

`tajribalar/t4_dalem.py`, `malumotlar/dalem.csv` (Kruseman, de Ridder 1990, 4.2-jadval, 84-bet; Q = 761 m³/sut, to'rt pyezometr 30, 60, 90, 120 m). Ustki qatlam napori o'zgarmas deb olindi; parametrlar eng kichik kvadratlar usuli bilan topildi.

| Talqin | KD, m²/sut | S | c, sut | S′ | RMSE, mm |
|---|---|---|---|---|---|
| Kruseman–de Ridder (Walton usuli) | 1731 | 1,9·10⁻³ | 468 | | 6,9 |
| Sig'imsiz ajratuvchi | 1674 | 1,77·10⁻³ | 325 | | 5,87 |
| Sig'imli ajratuvchi | 1670 | 1,52·10⁻³ | 370 | 1,1·10⁻³ | 5,80 |

Ajratuvchining elastik suv berishini hisobga olgan talqin xatoni deyarli kamaytirmaydi, S′ ning ishonch oralig'i keng (lg S′ ning standart chetlanishi 0,41). Kuzatuv 0,015–0,33 sut oralig'ida, t_c ≈ 0,4 sut; ma'lumotlar ajratuvchining elastik suv berishini aniqlash uchun yetarli emas. Bu natija maqolada cheklov sifatida ochiq yoziladi: Dalem tajribasi modelni tekshiradi, lekin ajratuvchining elastik suv berishi ta'sirini tasdiqlamaydi.

## 9. K(x,y), bosimsiz qatlam, bug'lanish va quduqlar

`tajribalar/t5_geterogen.py`. Soha 2000×1000 m, 80×40 yacheyka; 1-qatlam bosimsiz (K₁ da linza va kanal), 2-qatlamda K₂(x,y), 3-qatlamda ikki zona; 1-ajratuvchida gidrogeologik oyna (K′ 20 marta katta). Infiltratsiya mavsumiy, bug'lanish Averyanov qonuni bo'yicha. 2-qatlamda uchta (800, 800, 600 m³/sut), 3-qatlamda bitta (1000 m³/sut) quduq; boshlang'ich holat quduqlarsiz statsionar holat; 365 sutka.

| Holat | 2-qatlamda eng katta pasayish, m | 1-qatlamda eng katta pasayish, m | Quduq suvining ajratuvchi zaxirasidan ulushi |
|---|---|---|---|
| elastik suv berishi bilan, geterogen | 10,54 | 0,67 | 0,64% |
| elastik suv berishisiz, geterogen | 10,54 | 0,68 | 0 |
| elastik suv berishi bilan, bir jinsli | 5,65 | 0,05 | 0,63% |
| elastik suv berishisiz, bir jinsli | 5,64 | 0,06 | 0 |

Har bir holatda balans qoldig'i ≤ 3·10⁻¹² (nisbiy), Pikar iteratsiyalari ≤ 4. Bu misolda t_c = 10,8 va 25,6 sut, hisob vaqti esa 365 sut, chegaralarda napor berilgan; shuning uchun ajratuvchining elastik suv berishi ta'siri kichik. Geterogenlik esa pasayishni ikki baravar oshiradi va oyna orqali 1-qatlamga o'tadi. Sig'im muhim bo'lgan holatni ko'rsatish uchun keyingi tajribada t ≲ t_c davr (quduqni ishga tushirish, sarfni o'zgartirish) va ε ≳ 1 olinadi.

## 10. MODFLOW 6 bilan solishtirish

`tajribalar/t3_modflow.py`, GitHub Actions (`.github/workflows/tekshiruv.yml`). 1-tajribadagi masala: har bir ajratuvchi MODFLOW da 20 ta qatlam (K33 = K′, SS = S′_s), suvli qatlamlar K33 = 10⁶ m/sut; jami 43 qatlam, 105×105 notekis to'r, 175 vaqt qadami (ko'paytuvchi 1,05), 10 sutka.

| Qatlam | masala1 va MODFLOW 6 orasidagi eng katta farq, m | MODFLOW 6 ning Laplas etalonidan nisbiy farqi | masala1 ning etalondan nisbiy farqi |
|---|---|---|---|
| 1 | 4·10⁻¹⁰ | 0,22% | 0,22% |
| 2 (quduqli) | 4·10⁻⁹ | 0,68–0,74% | 0,68–0,74% |
| 3 | 3·10⁻¹⁰ | 0,33% | 0,33% |

Ikki dastur bir xil to'r va vaqt qadamlarida mashina aniqligigacha (10⁻⁹ m) mos keladi, chunki diskret tenglamalar bir xil. Etalondan farq ikkalasida bir xil va vaqt bo'yicha birinchi tartibli xatodan kelib chiqadi (1-tajriba). Farq shundaki, masala1 da ajratuvchi noma'lumlari ustun bo'yicha progonka bilan yo'qotiladi va siyrak tizim faqat suvli qatlamlar uchun yechiladi (3 qatlam o'rniga 43 qatlam emas).

## 11. Qalin gilli ajratuvchilar

`tajribalar/t6_qalin_ajratuvchi.py`, rasm `tajribalar/t6_qalin_ajratuvchi.png`. 5-tajribadagi soha va quduqlar; ajratuvchilar b′ = 15 va 20 m, K′ = 10⁻⁴ va 5·10⁻⁵ m/sut (oyna va x bo'yicha o'zgarish saqlangan), S′_s = 4·10⁻⁴ 1/m; t_c = 900 va 3200 sut, ya'ni hisob vaqti (365 sut) t_c dan kichik. Infiltratsiya o'zgarmas, shuning uchun o'zgarishlar faqat quduqlardan.

| Nuqta | 365 sutkada pasayish (elastik suv berishi bilan), m | 365 sutkada pasayish (elastik suv berishisiz), m | Butun davrdagi eng katta nisbiy farq |
|---|---|---|---|
| 2-qatlam, quduq yonida | 7,237 | 7,260 | 18% |
| 2-qatlam, markaz | 5,416 | 5,442 | 30% |
| 1-qatlam (bosimsiz), markaz | 0,051 | 0,060 | 14% (365 sutkada) |
| 3-qatlam, quduq yonida | 2,297 | 2,302 | 1,2% |

Quduq suvining manbalari (elastik suv berishi hisobga olingan model, rasmning b qismi): birinchi soatlarda suv asosan suvli qatlamlar zaxirasidan olinadi. Taxminan 1 sutkada ajratuvchilar zaxirasining ulushi 26% ga yetadi, keyin kamayadi. 365 sutkada suv asosan chegaralar orqali keladi, bug'lanish ham kamayadi. Butun davrda ajratuvchilardan olingan suv 2,9% ni tashkil etadi. Balans qoldig'i ≤ 4·10⁻¹².

Xulosa: berilgan napor chegaralari yaqin bo'lgan bu sohada ajratuvchining elastik suv berishi quduqli qatlamda birinchi kunlardagi napor pasayishini 18–30% ga sekinlashtiradi. 365 sutkada farq 0,5% dan kam. Bosimsiz qatlamda esa uning ta'siri bir yildan keyin ham saqlanadi: napor pasayishi 14% kam. Demak ajratuvchining elastik suv berishi hisobga olinmagan model yuqori qatlamdagi sath pasayishini oshirib baholaydi. Bu esa bug'lanish va sho'rlanish masalalari uchun muhim.

## 12. Maas–Olsthoorn 2003 va MLU "Two-aquifers" misollari

Parametrlar: `/mnt/project-files/maqola1/etalon_parametrlar/etalonlar.md`. Skript: `tajribalar/t7_maas_mlu.py`, testlar: `testlar/test_masala1.py`.

1. Maas–Olsthoorn 2003 (manbada Hemker–Maas 1987 bilan aynan mos deyilgan): ikki suvli qatlam (kD = 100, S = 10⁻⁴), elastik suv berishi bo'lgan uchta ajratuvchi (c = 100, S′ = 0,0016), tizim ustida va ostida pasayish nol, r = 10. Laplas etaloni tashqi ajratuvchilar bilan kengaytirildi va jadvaldagi 36 qiymatning hammasi bilan bosilgan 4 xonagacha mos keldi. Sonli yechim (tashqi naporlar berilgan ikki qo'shimcha qatlam, M = 20) to'rning eng yaqin nuqtasida (r = 10,69) etalondan quduqli qatlamda t ≥ 10⁻³ da ko'pi bilan 0,31%, ikkinchi qatlamda t ≥ 0,1 da ko'pi bilan 1,1% farq qiladi (audit 21.11.2026).
2. MLU "Two-aquifers" (Hemker, Randall 2010; 6 qatlamli tasvir, Q = 180 m³/sut): etalon 1 minutda 5,01 m da 0,29826 m beradi (MLU dagi bilan bir xil), 15,85 m da 0,0496 m beradi (MLU da 0,050). Sonli yechim etalondan 0,04% va 0,3% farq qiladi.
3. Veling–Maas 2009 da napor yoki pasayish jadvali yo'q, faqat zarracha trayektoriyalari bor, shuning uchun u etalon sifatida ishlatilmadi.

## 13. Bog'langan sxemaning yaqinlashishi

`tajribalar/t8_yaqinlashish.py`, natija `tajribalar/t8_yaqinlashish.json`. Soha 1000×1000 m, chegarada oqim nol; K₁, K₂ va 1-ajratuvchidagi K′ x, y koordinatalarga bog'liq; ikkala ajratuvchida elastik suv berishi (b′ = 4 m, S′_s = 2·10⁻³ 1/m); 1-qatlamda 1 m balandlikdagi Gauss do'ngligi; t = 5 sut. Xato: uchta qatlam naporlarining o'rtacha kvadratik chetlanishi.

| n×n, M | xato, m | tartib | τ, sut | xato, m | tartib |
|---|---|---|---|---|---|
| 20×20, 4 | 1,49·10⁻⁴ | | 0,5 | 8,0·10⁻⁴ | |
| 40×40, 8 | 3,55·10⁻⁵ | 2,07 | 0,25 | 3,95·10⁻⁴ | 1,02 |
| 80×80, 16 | 7,10·10⁻⁶ | 2,32 | 0,125 | 1,94·10⁻⁴ | 1,03 |
| | | | 0,0625 | 9,39·10⁻⁵ | 1,05 |

Fazo bo'yicha etalon 160×160, M = 32, τ = 1/64; vaqt bo'yicha 40×40, M = 8, τ = 1/256. Tartiblar O(h² + δ² + τ) ni tasdiqlaydi.
