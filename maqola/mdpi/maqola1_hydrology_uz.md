---
title: "Ajratuvchi qatlamlarning elastik suv berishi, suv o‘tkazuvchanlikning koordinatalarga bog‘liqligi va bosimsiz yuqori qatlam hisobga olingan uch qatlamli tizimda yer osti suvlari filtratsiyasining massani saqlovchi sonli modeli"
---

*Maqola (Hydrology jurnaliga yuboriladigan inglizcha matnning o‘zbekcha nusxasi)*

Ravshanov Normaxmad ^1^, Erkinov Javokhir ^2,\*^

^1^ Raqamli texnologiyalar va sun’iy intellektni rivojlantirish ilmiy-tadqiqot instituti, Buz-2, 17A, Toshkent, 100125, O‘zbekiston; ravshanzade-09@mail.ru

^2^ Sharof Rashidov nomidagi Samarqand davlat universiteti, Samarqand, 140104, O‘zbekiston; erkinovjavohir@samdu.uz

\* Muallif bilan aloqa: erkinovj110@gmail.com

**Annotatsiya:** Ko‘p qatlamli tizimlarda ajratuvchi qatlamlarning elastik suv zaxirasidan ajraladigan suv qo‘shni suvli qatlamlardagi napor pasayishini kechiktiradi, biroq sug‘oriladigan tekisliklar uchun tuzilgan sonli modellarda ajratuvchilar ko‘pincha elastik suv berishi hisobga olinmagan oqib o‘tish chegarasi sifatida qaraladi. Maqolada ikki ajratuvchi orqali bog‘langan uchta suvli qatlam modeli taklif etiladi; har bir ajratuvchida vertikal bir o‘lchamli elastik rejim tenglamasi yechiladi, ikkala chegarada napor va oqim uzluksiz. Barcha qatlamlarda filtratsiya koeffitsiyenti $x$, $y$ koordinatalarga bog‘liq, yuqori qatlam bosimsiz bo‘lib, unga infiltratsion ta’minot, sizot suvlari chuqurligiga bog‘liq bug‘lanish va quduqlar ta’sir qiladi. Model markazlashgan chekli hajmlar usuli va oshkormas Eyler sxemasi bilan diskretlanadi. Ajratuvchi noma’lumlari har bir ustunda yo‘qotiladi va suvli qatlamlar naporlari uchun bitta simmetrik siyrak tizim qoladi. Diskret massa saqlanishi, energiya normasida absolyut turg‘unlik va diskret maksimum prinsipi isbotlangan. Dastur Theis, Hantush–Jacob va ajratuvchining elastik suv berishini hisobga olgan Laplas sohasidagi ko‘p qatlamli yechimlarni 0,74% aniqlikda takrorlaydi, MODFLOW 6 bilan farq $4\cdot10^{-9}$ m. Hisoblashlar ajratuvchining elastik suv berishini hisobga olmaslik mumkinligini faqat $t_c$ xarakterli vaqti emas, elastik suv berish koeffitsiyentlari nisbati $\varepsilon$ ham belgilashini ko‘rsatdi. Qalin gilli ajratuvchilarda elastik suv berishi bir yildan keyin bosimsiz qatlamdagi sath pasayishini 14% ga kamaytiradi.

**Kalit so‘zlar:** ko‘p qatlamli suvli gorizont; ajratuvchining elastik suv berishi; oqib o‘tuvchi qatlam; chekli hajmlar usuli; absolyut turg‘unlik; bosimsiz qatlam; bug‘lanish

## 1. Kirish

Markaziy Osiyoning sug‘oriladigan tekisliklarida qumli suvli qatlamlar gil va qumoq qatlamlar bilan ajralgan. Chuqurroq qatlamdan suv olinganda ajratuvchilar orqali yuqoridagi bosimsiz qatlamda ham sath pasayadi. Sath o‘zgarishi bug‘lanishni va ildiz qatlamidagi tuz balansini o‘zgartiradi. Shu sababli yuqori qatlamdagi o‘zgarishni oldindan baholash uchun suvli qatlamlarni ajratuvchilar orqali fizik jihatdan to‘g‘ri bog‘laydigan model kerak.

N. Ravshanov ilmiy maktabida bunday tizimlar uchun kvaziuch o‘lchamli modellar ketma-ket ishlab chiqilgan. Ravshanov va boshq. [1] ikki ajratuvchi bilan bog‘langan uchta geterogen suvli qatlam masalasini ADI sxemasi, yacheykalararo koeffitsiyentning o‘rta garmonik qiymati va massani saqlovchi almashinuv hadi bilan yechgan; modelga zarrachalar ko‘chishi va kolmatatsiya ham kiritilgan. Ravshanov va boshq. [2] filtratsiya koeffitsiyenti naporga bog‘liq bo‘lgan to‘rt qatlamli tizimni ko‘rgan. Karimov va boshq. [3] va Mukhamadiyev va boshq. [4] bitta uch qatlamli modelni bayon qilgan: unda yuqori qatlam bosimsiz, suv o‘tkazuvchanlik koordinatalarga bog‘liq, bug‘lanish bor va kam o‘tkazuvchan qatlam elastik rejimda. Ammo bu kam o‘tkazuvchan qatlam tizimning eng pastida joylashgan va tubi suv o‘tkazmaydi, ya’ni u ikki suvli qatlamni bog‘lamaydi. Qodirov [5,6] ustidan va ostidan elastik rejimdagi kam o‘tkazuvchan qatlamlar bilan chegaralangan asosiy suvli qatlam uchun (Hantush [7] dagi joylashuv) analitik yechimlar olgan; ajratuvchilar tashqarisida napor pasayishi berilgan yoki asos suv o‘tkazmaydi. U shuningdek ustida grunt suvlari va bug‘lanish bo‘lgan chiziqlashtirilgan tizimni ko‘rgan. Bu ishlarda barcha parametrlar o‘zgarmas, ajratuvchining elastik suv berishi esa uchta bog‘langan suvli qatlam orasida emas, bitta "ajratuvchi – suvli qatlam – ajratuvchi" tizimida qaraladi. Ko‘rsatilgan sonli modellarning birortasida suvli qatlamlar orasidagi ajratuvchining elastik suv berishi yo‘q, bog‘langan sxemaning turg‘unligi ham isbotlanmagan.

Xalqaro adabiyotda ajratuvchining elastik suv berishi uzoq vaqtdan beri o‘rganiladi. Hantush [7] hamda Neuman va Witherspoon [8] ajratuvchi zaxirasidan ajralgan suv dastlabki napor pasayishini o‘zgartirishini ko‘rsatgan. Hemker [9] va Hemker va Maas [10] barcha ajratuvchilarida elastik suv berishi bo‘lgan $n$ qatlamli masalani Laplas sohasida yechgan. Cihan va boshq. [11] bu yondashuvni ko‘p sonli suvli qatlam va germetik bo‘lmagan quduqlar uchun kengaytirgan. Herrera va Yates [12] ajratuvchi ta’sirini xotira integrali orqali yozgan. MODFLOW dasturida ajratuvchining elastik suv berishi TLK1 paketi [13] va CSUB paketidagi kechikuvchi qatlamchalar [14] orqali hisobga olinadi. Ajratuvchini bir necha yupqa model qatlami bilan tasvirlash ham mumkin. Demak ajratuvchining elastik suv berishi o‘z-o‘zidan yangi masala emas.

Sug‘oriladigan tekisliklar masalasi uchun quyidagilarning birgalikda bo‘lishi kerak, mavjud vositalarda esa ular birga uchramaydi:

1. suvli qatlamlar orasidagi har bir ajratuvchida elastik suv berishi;
2. har bir suvli qatlam va ajratuvchida filtratsiya koeffitsiyentining $x$, $y$ koordinatalarga bog‘liqligi;
3. infiltratsion ta’minot va chuqurlikka bog‘liq bug‘lanish ta’sir qiladigan nochiziqli bosimsiz yuqori qatlam;
4. massaning saqlanishi, turg‘unlik va monotonlik sinab ko‘rilgan emas, balki isbotlangan bitta diskret sxema.

Analitik yechimlar 2- va 3-shartni qanoatlantirmaydi. Ajratuvchini MODFLOW qatlamlari bilan diskretlash bizning sxemamiz bilan bir xil diskret masalani beradi (3.1-bo‘lim), lekin uch o‘lchamli noma’lumlar sonini bir necha marta oshiradi va bog‘langan tizim turg‘unligi tahlil qilinmaydi.

Maqolada quyidagi natijalar keltiriladi.

1. Har bir ajratuvchida vertikal elastik rejim tenglamasi, ajratuvchi chegaralarida napor va oqim uzluksizligi, barcha qatlamlarda $K(x,y)$, infiltratsion ta’minot, S.F. Averyanov bug‘lanish qonuni va quduqlar bo‘lgan bosimsiz yuqori qatlamli uch qatlamli model (2.1-bo‘lim).
2. Ajratuvchi ustunlari progonka bilan aniq yo‘qotiladigan chekli hajmlar sxemasi. Diskret massa saqlanishi, almashinuv matritsasining simmetrikligi va musbat yarim aniqligi, energiya normasida absolyut turg‘unlik va diskret maksimum prinsipi isbotlangan (2.2- va 2.3-bo‘limlar).
3. Klassik yechimlar, ajratuvchining elastik suv berishini hisobga olgan Laplas sohasidagi ko‘p qatlamli yechim, Hemker–Maas [10] va MLU dasturining chop etilgan misollari, MODFLOW 6 va Dalem tajriba ma’lumotlari bilan tekshiruv (3.1-bo‘lim).
4. Ajratuvchining elastik suv berishini hisobga olmaslik mumkinligi $t/t_c$ va $\varepsilon=S'/\sum S$ parametrlariga bog‘liqligini ko‘rsatuvchi hisoblashlar. Geterogen maydonda elastik suv berishining grunt suvlari sathiga ta’siri miqdoriy baholangan (3.2- va 3.3-bo‘limlar).

## 2. Materiallar va usullar

### 2.1. Matematik model

**Tizim va farazlar**

Tizim yuqoridan pastga $k=1,2,3$ tartibda raqamlangan uchta suvli qatlam va $j=1,2$ ikkita ajratuvchidan iborat. $j$-ajratuvchi $j$- va $(j+1)$-suvli qatlamlar orasida joylashgan. Gorizontal tekislikdagi soha $\Omega\subset\mathbb R^2$ ixtiyoriy shaklda (1-rasm). Quyidagi farazlar qabul qilinadi:

- (A1) suvli qatlamlarda oqim gorizontal (Dyupyui farazi), ajratuvchilarda vertikal (Hantush farazi), chunki $K'\ll K_k$;
- (A2) bosimli qatlamlar va ajratuvchilarda elastik suv zaxirasi naporga chiziqli bog‘liq;
- (A3) 1-qatlam bosimsiz, uning suvga to‘yingan qalinligi $h_1-z_0$, suv berish koeffitsiyenti $\mu$; 2- va 3-qatlamlar doimo bosimli;
- (A4) sizot suvlari sathidan bug‘lanish uning chuqurligiga bog‘liq;
- (A5) har bir quduqning filtri bitta suvli qatlamda joylashgan;
- (A6) har bir nuqtada muhit izotrop, filtratsiya koeffitsiyenti $x$, $y$ koordinatalarga bog‘liq.

![](rasm1_sxema_uz.png){width=16cm}

**1-rasm.** Uch qatlamli tizimning sxematik kesimi: grunt suvlari sathi $h_1$, infiltratsion ta’minot $W$ va bug‘lanish $E(h_1)$ bo‘lgan bosimsiz 1-qatlam; bosimli 2- va 3-qatlamlar; vertikal koordinatasi $\zeta$ va chegaralardagi oqimlari $q^\pm_j$ bo‘lgan 1- va 2-ajratuvchilar; 2-qatlamdagi $Q_2$ quduq.

**Suvli qatlamlar tenglamalarini keltirib chiqarish**

$k$-suvli qatlamda asosi $dx\,dy$ bo‘lgan va suvga to‘yingan qalinlikni to‘liq egallagan vertikal prizmani qaraymiz. Suv prizmaga yon tomonlari, yuqori va pastki yuzalari hamda quduqlar orqali kiradi va chiqadi. Kam siqiluvchan suv va elastik skelet uchun massa saqlanish qonuni quyidagini beradi:

$$\frac{\partial V_k}{\partial t}=-\nabla\cdot\mathbf Q_k+(\text{vertikal kirish})-(\text{vertikal chiqish})-\sum_iQ_{ki}\,\delta(\mathbf x-\mathbf x_i),\tag{1}$$

bu yerda $V_k$ birlik yuzaga to‘g‘ri keladigan suv hajmi, $\mathbf Q_k$ birlik kenglik orqali gorizontal sarf. (A1) Dyupyui farazida napor qalinlik bo‘yicha o‘zgarmaydi, shuning uchun Darsi qonuni $\mathbf q=-K_k\nabla h_k$ ni to‘yingan qalinlik bo‘yicha integrallab quyidagini olamiz:

$$\mathbf Q_k=-K_k\,b_k\,\nabla h_k=-T_k\nabla h_k .\tag{2}$$

Bosimli qatlamda zaxira suv va skeletning siqilishi hisobiga o‘zgaradi: $\partial V_k/\partial t=S_{s,k}b_k\,\partial h_k/\partial t=S_k\,\partial h_k/\partial t$. Bosimsiz qatlamda to‘yingan qalinlik $h_1-z_0$ ga teng, shuning uchun (2) da $b_1$ o‘rniga $h_1-z_0$ yoziladi. Bu qatlamda zaxira asosan sath siljiganda g‘ovaklarning to‘lishi va bo‘shashi hisobiga o‘zgaradi: $\partial V_1/\partial t=\mu\,\partial h_1/\partial t$; to‘yingan qismning elastik suv berishi $\mu$ ga nisbatan kichik va hisobga olinmaydi. 1-qatlam yuqori yuzasiga infiltratsion ta’minot $W$ keladi va bug‘lanish $E$ ketadi. $j$-ajratuvchi bilan umumiy yuzadan $j$-qatlam pastga yo‘nalgan $q^+_j$ oqimni yo‘qotadi, $(j+1)$-qatlam esa $q^-_j$ oqimni oladi. Bu hadlarni (1) ga qo‘yib, quyidagi tenglamalarni olamiz:

$$\mu\frac{\partial h_1}{\partial t}=\nabla\cdot\big(K_1(h_1-z_0)\nabla h_1\big)+W-E(h_1)-q^{+}_1-\sum_i Q_{1i}\delta(\mathbf x-\mathbf x_i),\tag{3}$$

$$S_2\frac{\partial h_2}{\partial t}=\nabla\cdot(T_2\nabla h_2)+q^{-}_1-q^{+}_2-\sum_i Q_{2i}\delta(\mathbf x-\mathbf x_i),\tag{4}$$

$$S_3\frac{\partial h_3}{\partial t}=\nabla\cdot(T_3\nabla h_3)+q^{-}_2-\sum_i Q_{3i}\delta(\mathbf x-\mathbf x_i).\tag{5}$$

3-qatlamning tubi suv o‘tkazmaydi deb olinadi. Agar tubi orqali oqib o‘tish bo‘lsa, (5) ga $q^+_j$ ko‘rinishidagi had qo‘shiladi.

**Ajratuvchi tenglamasini keltirib chiqarish**

$\zeta\in[0,b'_j]$ orqali $j$-ajratuvchining yuqori chegarasidan pastga o‘lchanadigan chuqurlikni belgilaymiz. Ajratuvchining hajm elementida massa saqlanish qonuni $S'_{s,j}\,\partial u_j/\partial t=-\nabla\cdot\mathbf q'$ ko‘rinishda bo‘ladi, bu yerda Darsi qonuni bo‘yicha $\mathbf q'=-K'_j\nabla u_j$. $\nabla\cdot\mathbf q'$ ning gorizontal qismi vertikal qismiga $(b'/L)^2$ tartibda nisbatda bo‘ladi, $L$ napor gorizontal yo‘nalishda sezilarli o‘zgaradigan masofa. Qalinligi bir necha metr bo‘lgan ajratuvchi va o‘nlab, yuzlab metrli $L$ uchun bu nisbat kichik. Bundan tashqari, $K'\ll K$ bo‘lganda tok chiziqlari chegarada sinib, ajratuvchi ichida deyarli vertikal yo‘naladi [7]. Faqat vertikal qismni qoldirib, pastga musbat $q_z=-K'_j\,\partial u_j/\partial\zeta$ bilan quyidagini olamiz:

$$S'_{s,j}\frac{\partial u_j}{\partial t}=-\frac{\partial q_z}{\partial\zeta}=K'_j\frac{\partial^2u_j}{\partial\zeta^2},\qquad 0<\zeta<b'_j.\tag{6}$$

Har bir chegarada ajratuvchi va suvli qatlam napori bir xil, chunki napor sakrashi cheksiz katta oqimni talab qiladi. Chegaralardagi oqimlar ajratuvchidagi Darsi oqimining chegaradagi qiymatlariga teng:

$$u_j|_{\zeta=0}=h_j,\qquad u_j|_{\zeta=b'_j}=h_{j+1},\tag{7}$$

$$q^{+}_j=-K'_j\frac{\partial u_j}{\partial\zeta}\Big|_{\zeta=0},\qquad q^{-}_j=-K'_j\frac{\partial u_j}{\partial\zeta}\Big|_{\zeta=b'_j}.\tag{8}$$

$K'_j$, $b'_j$ va $S'_{s,j}$ ham $x$, $y$ koordinatalarga bog‘liq bo‘lishi mumkin. (7) va (8) tutashuv shartlari bo‘lib, napor va oqimning uzluksizligini ifodalaydi.

(6) ni ajratuvchi qalinligi bo‘yicha integrallab, (8) dan foydalansak,

$$\frac{d}{dt}\int_0^{b'_j}S'_{s,j}u_j\,d\zeta=q^+_j-q^-_j\tag{9}$$

hosil bo‘ladi: yuqoridan kirgan va pastdan chiqqan oqimlar farqi ajratuvchidagi elastik suv zaxirasining o‘zgarish tezligiga teng. $S'_s=0$ bo‘lsa, (6) ning o‘ng tomoni nolga teng, $u_j$ $\zeta$ ga chiziqli bog‘liq bo‘ladi va (8) quyidagi ko‘rinishga keladi:

$$q^+_j=q^-_j=\frac{K'_j}{b'_j}\,(h_j-h_{j+1}).\tag{10}$$

Ravshanov va boshq. [1] da aynan shu, ajratuvchining elastik suv berishi hisobga olinmagan almashinuv ishlatilgan. (3)–(8) model (10) ni $S'_s\to0$ dagi limit holat sifatida o‘z ichiga oladi.

Bug‘lanish S.F. Averyanov qonuni bo‘yicha hisoblanadi:

$$E(h_1)=E_0\Big(1-\frac{z_s-h_1}{\Delta}\Big)^n,\quad 0\le z_s-h_1\le\Delta;\qquad E=0,\quad z_s-h_1>\Delta.\tag{11}$$

Boshlang‘ich naporlar $h_k^0$ quduqlarsiz statsionar holatdan olinadi, bunda ajratuvchidagi boshlang‘ich napor $u_j^0$ $\zeta$ bo‘yicha chiziqli taqsimlangan. $\Gamma_{D,k}$ chegarada napor berilgan, $h_k=g_k$; $\Gamma_{N,k}$ chegarada oqim nolga teng, $T_k\,\partial h_k/\partial n=0$.

**Global balans va xarakterli vaqt**

(3)–(5) ni $\Omega$ bo‘yicha integrallab, ikkala ajratuvchi uchun $\Omega$ bo‘yicha integrallangan (9) ni qo‘shsak, $q^\pm_j$ almashinuv hadlari qisqaradi:

$$\frac{d}{dt}\Big[\int_\Omega(\mu h_1+S_2h_2+S_3h_3)\,d\mathbf x+\sum_j\int_\Omega\!\int_0^{b'_j}S'_{s,j}u_j\,d\zeta\,d\mathbf x\Big]=\int_\Omega(W-E)\,d\mathbf x-\sum Q+\sum_k\oint_{\Gamma_{D,k}}T_k\frac{\partial h_k}{\partial n}\,ds.\tag{12}$$

Suvli qatlamlar va ajratuvchilar zaxirasining o‘zgarishi infiltratsiya va bug‘lanish farqidan quduqlar sarfini ayirib, chegaradan kelgan oqimni qo‘shganiga teng. 2.2-bo‘limdagi diskret sxema (12) ni aniq bajaradi (1-lemma).

O‘lchamsiz chuqurlik $\xi=\zeta/b'$ va vaqt $\theta=t/t_c$ kiritilsa, (6) tenglama $\partial u/\partial\theta=\partial^2u/\partial\xi^2$ ko‘rinishga keladi, bu yerda

$$t_c=\frac{b'^2S'_s}{K'}=\frac{b'S'}{K'},\qquad S'=S'_sb'.\tag{13}$$

$t\ll t_c$ da ajratuvchi faqat chegaralari yaqinida javob beradi va zaxirasidan suv ajratadi; $t\gg t_c$ da undagi napor taqsimoti (10) dagi chiziqli taqsimotga yaqinlashadi. Herrera va Figueroa [15] dagi xotira vaqti $3S'b'/(\pi^2K')$ ga teng, bu $0{,}30\,t_c$ ni tashkil etadi. (13) xarakterli vaqt ajratuvchi qanchalik tez muvozanatga kelishini ko‘rsatadi, lekin u suvli qatlamlarga nisbatan qancha suv berishini ko‘rsatmaydi. Buni elastik suv berish koeffitsiyentlari nisbati o‘lchaydi:

$$\varepsilon=S'\Big/\sum_kS_k.\tag{14}$$

Hantush [7] hamda Neuman va Witherspoon [8] yechimlarida bu rolni $S'/S$ nisbati bajaradi.

### 2.2. Sonli usul

**Suvli qatlamlarni chekli hajmlar usulida diskretlash**

$\Omega$ soha qadamlari o‘zgaruvchan to‘g‘ri burchakli to‘r bilan qoplanadi, $\Omega$ dan tashqaridagi yacheykalar hisobga kirmaydi. (4) ni yuzasi $A_P$ bo‘lgan $P$ yacheyka va $[t^n,t^{n+1}]$ vaqt qadami bo‘yicha integrallab, oqim hadiga Gauss–Ostrogradskiy teoremasini qo‘llaymiz:

$$\int_{t^n}^{t^{n+1}}\!\!\int_{A_P}S\,\frac{\partial h}{\partial t}\,dA\,dt=\int_{t^n}^{t^{n+1}}\Big[\sum_{N}\int_{e_{PN}}T\,\frac{\partial h}{\partial n}\,d\ell+\int_{A_P}(q^--q^+)\,dA-Q_P\Big]dt ,\tag{15}$$

bu yerda $e_{PN}$ qo‘shni $N$ yacheyka bilan umumiy tomon. (15) uchta yaqinlashish bilan algebraik tenglamaga aylanadi: yacheykadagi napor uning markazidagi qiymat bilan almashtiriladi; vaqt bo‘yicha integrallar $t^{n+1}$ da hisoblanadi (oshkormas Eyler sxemasi); $e_{PN}$ orqali oqim ikki qo‘shni markazdagi qiymatlar orqali ifodalanadi.

Tomon orqali oqim quyidagicha keltirib chiqariladi. Har bir yacheykada $T_P$ va $T_N$ o‘zgarmas, $d_P$ va $d_N$ tomonga perpendikulyar yo‘nalishdagi yacheyka o‘lchamlari, $h_e$ tomondagi noma’lum napor bo‘lsin. Ikki yarim yacheykada Darsi qonuni birlik tomon uzunligi uchun bir xil oqimni beradi: $F=2T_P(h_P-h_e)/d_P=2T_N(h_e-h_Q)/d_N$. $h_e$ ni yo‘qotib, $F=(h_P-h_Q)\big/\big(d_P/2T_P+d_N/2T_N\big)$ ni olamiz, ya’ni yacheykalararo o‘tkazuvchanlik

$$C_{PN}=\ell_{PN}\Big(\frac{d_P}{2T_P}+\frac{d_N}{2T_N}\Big)^{-1}\tag{16}$$

ga teng, bu yerda $\ell_{PN}$ tomon uzunligi. Bu ikki suv o‘tkazuvchanlikning o‘rta garmonik qiymati. U $T$ uzilishga ega bo‘lgan joyda oqim uzluksizligini saqlaydi va $T$ bo‘lakli o‘zgarmas bo‘lganda aniq natija beradi. 1-qatlamda $T_1=K_1\max(h_1-z_0,b_{\min})$ olinadi, bu yerda $b_{\min}>0$ kichik son: suvsizlangan yacheyka tizimdan uzilib qolmaydi. Natijada $P$ yacheyka uchun quyidagi tenglama hosil bo‘ladi:

$$\frac{S_PA_P}{\tau}(h_P^{n+1}-h_P^n)+\sum_NC_{PN}(h_P^{n+1}-h_N^{n+1})+A_P(q^+_P-q^-_P)^{n+1}=A_P(W-E)_P^{n+1}-Q_P,\tag{17}$$

1-qatlamda $S_P=\mu$. Quduq o‘zi joylashgan yacheykada nuqtaviy yutilish sifatida qatnashadi.

**Ajratuvchi ustunlarini diskretlash**

Har bir yacheyka ostidagi ajratuvchi vertikal ustun sifatida qaraladi. Ustun qalinligi $\delta=b'/M$ bo‘lgan $M$ ta qatlamchaga bo‘linadi, tugunlar qatlamchalar markazida, $\zeta_m=(m-\tfrac12)\delta$. (6) ni $m$-qatlamcha va vaqt qadami bo‘yicha integrallab, quyidagini olamiz:

$$\frac{S'_s\delta}{\tau}(u_m^{n+1}-u_m^n)=c_{m-1/2}(u_{m-1}^{n+1}-u_m^{n+1})+c_{m+1/2}(u_{m+1}^{n+1}-u_m^{n+1}),\qquad m=1,\dots,M,\tag{18}$$

bunda $u_0=h_j$ va $u_{M+1}=h_{j+1}$. Ikki ichki tugun orasidagi masofa $\delta$, shuning uchun o‘tkazuvchanlik $c=K'/\delta$. Birinchi va oxirgi tugunlar chegaradan $\delta/2$ masofada, chegarada esa (7) bo‘yicha napor suvli qatlam naporiga teng; shuning uchun chetki o‘tkazuvchanlik $c_e=2K'/\delta$. (17) ga kiradigan chegara oqimlari (18) ning chetki oqimlari:

$$q^+=c_e(h_j-u_1),\qquad q^-=c_e(u_M-h_{j+1}).\tag{19}$$

(17) va (18) bir xil (19) oqimdan foydalangani uchun suvli qatlamdan chegara orqali chiqqan suv ajratuvchiga aynan kiradi. (18) ning approksimatsiya xatosi $O(\tau+\delta^2)$.

**Ajratuvchi noma’lumlarini yo‘qotish**

Har bir ustunda (18) simmetrik uch diagonalli tizimni tashkil etadi: $\mathfrak Tu=\sigma u^n+c_ee_1h_j+c_ee_Mh_{j+1}$, bu yerda $\sigma=S'_s\delta/\tau$, $e_1$ va $e_M$ birinchi va oxirgi birlik vektorlar. Tizim chiziqli, uning o‘ng tomoni ikki suvli qatlam naporlariga faqat oxirgi ikki had orqali bog‘liq. Superpozitsiya bo‘yicha yechim quyidagicha yoziladi:

$$u=a+\alpha\,h_j+\beta\,h_{j+1},\qquad \mathfrak Ta=\sigma u^n,\ \ \mathfrak T\alpha=c_ee_1,\ \ \mathfrak T\beta=c_ee_M.\tag{20}$$

$a$, $\alpha$, $\beta$ vektorlar uchta o‘ng tomon uchun bitta progonka bilan topiladi. (20) dagi $u_1$ va $u_M$ ni (19) ga qo‘ysak, chegaralardagi oqimlar ikki qo‘shni suvli qatlam naporlariga chiziqli bog‘liq bo‘ladi:

$$\begin{pmatrix}q^+\\-q^-\end{pmatrix}=\Lambda\begin{pmatrix}h_j\\h_{j+1}\end{pmatrix}-c_e\begin{pmatrix}a_1\\a_M\end{pmatrix},\qquad\Lambda=c_e\begin{pmatrix}1-\alpha_1&-\beta_1\\-\alpha_M&1-\beta_M\end{pmatrix}.\tag{21}$$

Progonka barcha ustunlar uchun bir vaqtda (vektorlashgan holda) bajariladi. Uning natijasi faqat $\tau$ va $u^n$ ga bog‘liq, shuning uchun u har bir qadamda bir marta hisoblanadi. (21) ni (17) ga qo‘yib, suvli qatlamlar naporlari uchun bitta siyrak simmetrik tizim olinadi. U yechilgandan keyin ajratuvchidagi naporlar (20) dan tiklanadi. $M=0$ bo‘lganda ustunda elastik suv zaxirasi yo‘q va $\Lambda=(K'/b')\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, bu (10) ning o‘zi.

**Nochiziqlilik va algoritm**

$T_1(h_1)$ va $E(h_1)$ Pikar iteratsiyasi bilan aniqlanadi. $r$-iteratsiyada $T_1(h^{(r)})$ olinadi, $E$ esa $h^{(r)}$ atrofida Teylor qatoriga yoyilib, chiziqli had qoldiriladi:

$$E(h^{(r+1)})\approx E(h^{(r)})+E'(h^{(r)})\,(h^{(r+1)}-h^{(r)}).\tag{22}$$

$d=z_s-h_1$ bo‘lganda hosila $E'=nE_0(1-d/\Delta)^{n-1}/\Delta$ manfiy emas, shuning uchun $A_PE'h^{(r+1)}$ had tenglamaning chap tomoniga o‘tadi va matritsa diagonalini oshiradi. Iteratsiya $\max|h^{(r+1)}-h^{(r)}|<10^{-8}$ m bo‘lganda to‘xtatiladi.

1-algoritm (bitta vaqt qadami):

1. barcha ustunlarda (20) dan $a$, $\alpha$, $\beta$ topiladi;
2. yaqinlashguncha $T_1$ va chiziqlashtirilgan $E$ bilan (17), (21) tizim yig‘iladi va yechiladi;
3. ajratuvchidagi naporlar (20) dan tiklanadi;
4. suv balansi hisoblanadi.

### 2.3. Sxemaning xossalari

Ajratuvchi noma’lumlari bilan birga yozilgan (17)–(18) to‘liq tizim matritsasini $\mathbb A=D/\tau+\mathbb L$ bilan belgilaymiz. $D$ diagonal matritsa bo‘lib, uning elementlari $S_PA_P$ va $S'_s\delta A_P$. $\mathbb L$ gorizontal va vertikal o‘tkazuvchanliklardan tuzilgan.

### 1-lemma (diskret suv balansi)

(17) ni barcha erkin yacheykalar, (18) ni barcha qatlamchalar bo‘yicha yig‘sak,

$$\Delta V_\mathrm{qatlam}+\Delta V_\mathrm{ajratuvchi}=\tau\Big[\sum A(W-E_\mathrm{lin})-\sum Q+B_D\Big]$$

tenglik aniq bajariladi. Bu yerda $B_D$ napor berilgan yacheykalardan kelgan oqim.

Isbot. $C_{PN}$ simmetrik, shuning uchun gorizontal oqimlar juft-jufti bilan qisqaradi. (21) dagi oqimlar (19) chetki oqimlar bilan bir xil, demak vertikal oqimlar ham qisqaradi. □

### 2-lemma (almashinuv matritsasi)

$\Lambda$ simmetrik, uning diagonaldan tashqari elementlari musbat emas, qatorlar yig‘indisi manfiy emas. Demak $\Lambda$ musbat yarim aniq, kondensatsiyadan keyingi matritsa esa simmetrik M-matritsa.

Isbot. $\mathfrak T$ qat’iy diagonal ustunlikka ega M-matritsa, shuning uchun $\mathfrak T^{-1}\ge0$, demak $\alpha,\beta\ge0$. $\mathfrak T$ simmetrik bo‘lgani uchun $\alpha_M=\beta_1$. $\mathfrak T\mathbb 1=\sigma\mathbb 1+c_ee_1+c_ee_M$ tenglikdan $1-\alpha_m-\beta_m=(\mathfrak T^{-1}\sigma\mathbb 1)_m\ge0$ kelib chiqadi. □

### 1-teorema (absolyut turg‘unlik)

Bosimli qatlamlar, bug‘lanish bo‘lmagan holat va bir jinsli berilgan naporlar uchun ixtiyoriy $\tau>0$, ixtiyoriy $M$, ixtiyoriy to‘r va parametrlarning barcha musbat qiymatlarida

$$\|h^{n+1}\|_D\le\|h^n\|_D+\tau\|D^{-1}F^{n+1}\|_D$$

baho o‘rinli, bu yerda $\|v\|^2_D=v^{\top}Dv$.

Isbot. $\mathbb Ah^{n+1}=Dh^n/\tau+F$ tenglikni $h^{n+1}$ ga skalyar ko‘paytiramiz. $(h^{n+1})^{\top}\mathbb Lh^{n+1}\ge0$ va Koshi–Bunyakovskiy tengsizligidan baho kelib chiqadi. □

$D$ ajratuvchilar zaxirasini ham o‘z ichiga olgani uchun baho ajratuvchilardagi naporlarni ham chegaralaydi.

### 2-teorema (diskret maksimum prinsipi)

$\mathbb A$ M-matritsa. Manbalar bo‘lmaganda suvli qatlamlar va ajratuvchilardagi yangi naporlar eski naporlar va chegaradagi naporlarning eng kichik va eng katta qiymatlari orasida bo‘ladi.

Demak sxema ixtiyoriy $\tau$ da monoton. Xususan, $K$ yoki $K'$ keskin o‘zgaradigan joylarda tebranish hosil bo‘lmaydi, Krank–Nikolson sxemasida esa bu xossa faqat qadam cheklanganda saqlanadi. Nochiziqli holatda $T_1\ge K_1b_{\min}>0$ va $E'\ge0$ bo‘lgani uchun har bir Pikar iteratsiyasining matritsasi ham M-matritsa, shuning uchun har bir iteratsiya bir qiymatli aniqlanadi. Pikar iteratsiyasining yaqinlashishi umumiy holda isbotlanmagan, iteratsiyalar soni har bir hisobda ko‘rsatiladi.

**Yaqinlashish**

Silliq yechimda approksimatsiya xatosi $O(\tau+\Delta x^2+\delta^2)$. 1-teorema bilan birga bu chiziqli masalada $D$ normada shu tartibdagi yaqinlashishni beradi. Notekis to‘rda markazlashgan sxemaning lokal approksimatsiya xatosi birinchi tartibli bo‘lsa ham, global aniqlik ikkinchi tartibda saqlanishi ma’lum [16]. Tartiblar 3.1-bo‘limda sonli tekshiriladi.

## 3. Natijalar

### 3.1. Tekshiruv

**Analitik va yarim analitik etalonlar**

Bir jinsli bosimli qatlamlar va sarfi o‘zgarmas quduq uchun (4)–(8) Laplas sohasiga o‘tkaziladi. U yerda (6) aniq yechiladi. $\lambda=b'\sqrt{pS'_s/K'}$ belgilash bilan ajratuvchi chegaralaridagi oqimlar quyidagicha bo‘ladi:

$$\bar q^+=\frac{K'}{b'}\lambda\,(\coth\lambda\,\bar h_j-\operatorname{csch}\lambda\,\bar h_{j+1}),\qquad \bar q^-=\frac{K'}{b'}\lambda\,(\operatorname{csch}\lambda\,\bar h_j-\coth\lambda\,\bar h_{j+1}).$$

Suvli qatlamlar tizimi Hemker [9] yondashuvi bo‘yicha simmetrik ko‘rinishda xos vektorlarga yoyiladi va $K_0$ modifikatsiyalangan Bessel funksiyalari orqali yechiladi. Vaqt sohasiga 12 hadli Stehfest [17] algoritmi bilan qaytiladi. Bu etalon Theis [18] yechimini $10^{-5}$ nisbiy farq bilan takrorlaydi. Hantush–Jacob [19] yechimi ham $10^{-4}$ farq bilan olinadi: buning uchun yuqori qatlamga juda katta $T$ va $S$, ajratuvchiga esa $S'_s=0$ beriladi (`testlar/test_masala1.py`).

**Ikkala ajratuvchisida elastik suv berishi bo‘lgan uch qatlam**

Test masala parametrlari: $T=200$, 100, 300 m²/sut; $S=2$, 1, $3\cdot10^{-4}$; $K'=2\cdot10^{-3}$ va $10^{-3}$ m/sut; $b'=5$ va 8 m; $S'_s=10^{-4}$ 1/m. Quduq 2-qatlamdan 500 m³/sut suv oladi. To‘r 105×105 yacheykadan iborat: markazdagi yacheyka 2 m, keyingilari 1,15 marta kattalashib 20 km gacha boradi. Har bir ajratuvchi $M=20$ qatlamchaga bo‘lingan. Vaqt qadami $10^{-4}$ sut dan boshlanib, har qadamda 1,05 marta oshadi va 10 sut dan oshmaydi. $10^{-3}$–10 sut oralig‘ida Laplas etalonidan eng katta nisbiy farq 1-qatlamda 0,22%, 2-qatlamda 0,68–0,74%, 3-qatlamda 0,33% (`tajribalar/t3_modflow.py`). Qadam ko‘paytuvchisi 1,2 bo‘lganda 1- va 3-qatlamlardagi farq 1,2–1,8% gacha oshadi. Demak farqning asosiy qismi vaqt bo‘yicha birinchi tartibli xatodan kelib chiqadi.

**MODFLOW 6 bilan solishtirish**

Shu masala MODFLOW 6 da [20] tuzildi: har bir ajratuvchi 20 ta model qatlami (K33 $=K'$, SS $=S'_s$), suvli qatlamlarda K33 $=10^6$ m/sut, jami 43 qatlam, vaqt qadamlari bir xil. To‘qqizta kuzatuv nuqtasida naporlar farqi $4\cdot10^{-9}$ m dan oshmaydi. Ikkala dasturning Laplas etalonidan farqi ham bir xil. Ikkala dastur bir xil diskret tenglamalarni yechadi. Farq shundaki, bizning dasturda siyrak tizim 43 emas, 3 qatlam uchun tuziladi, ajratuvchilar esa alohida uch diagonalli tizimlar bilan hisoblanadi.

**To‘r va vaqt qadami bo‘yicha yaqinlashish, suv balansi**

**1-jadval.** Ajratuvchi ustuni ($K'=10^{-2}$ m/sut, $b'=2$ m, $S'_s=10^{-2}$ 1/m) yuqori chegarasida napor birlik qiymatga sakrab o‘zgargandan keyin $t=0{,}5$ sut dagi chegara oqimi $q^+$ ning qator ko‘rinishidagi aniq yechimdan nisbiy farqi, $\tau=10^{-4}$ sut.

| $M$ | $q^+$ ning nisbiy xatosi | kuzatilgan tartib |
|---|---|---|
| 4 | $3{,}9\cdot10^{-2}$ | |
| 8 | $8{,}5\cdot10^{-3}$ | 2,20 |
| 16 | $2{,}1\cdot10^{-3}$ | 2,00 |
| 32 | $5{,}8\cdot10^{-4}$ | 1,86 |

$M=32$ da tartibning biroz pasayishi vaqt bo‘yicha xatodan kelib chiqadi: $\tau=10^{-4}$ sut da u shu kattalikda.

2-jadvalda uch qatlamli bog‘langan sxema butunligicha tekshiriladi (`tajribalar/t8_yaqinlashish.py`). Soha 1000 × 1000 m, chegaralarda oqim nolga teng. $K_1$, $K_2$ va 1-ajratuvchidagi $K'$ $x$, $y$ koordinatalarga bog‘liq ravishda silliq o‘zgaradi. Ikkala ajratuvchida elastik suv berishi bor ($b'=4$ m, $S'_s=2\cdot10^{-3}$ 1/m). Boshlang‘ich holatda 1-qatlamda balandligi 1 m bo‘lgan Gauss shaklidagi do‘nglik olingan, yechimlar $t=5$ sut da solishtiriladi. Fazo bo‘yicha yacheyka o‘lchami $\Delta x$ va qatlamcha qalinligi $\delta$ birga ikki marta kichraytiriladi. Xato uchta suvli qatlam naporlarining 160 × 160, $M=32$ yechimining yacheykalar bo‘yicha o‘rtacha qiymatlaridan o‘rtacha kvadratik chetlanishi sifatida hisoblanadi. Vaqt bo‘yicha 40 × 40, $M=8$ to‘rda $\tau$ ikki marta kichraytiriladi, etalon $\tau=1/256$ sut.

**2-jadval.** Bog‘langan sxemaning to‘r va vaqt qadami bo‘yicha yaqinlashishi: $t=5$ sut dagi naporning o‘rtacha kvadratik xatosi.

| $n\times n$, $M$ | xato, m | tartib | $\tau$, sut | xato, m | tartib |
|---|---|---|---|---|---|
| 20 × 20, 4 | $1{,}49\cdot10^{-4}$ | | 0,5 | $8{,}0\cdot10^{-4}$ | |
| 40 × 40, 8 | $3{,}55\cdot10^{-5}$ | 2,07 | 0,25 | $3{,}95\cdot10^{-4}$ | 1,02 |
| 80 × 80, 16 | $7{,}10\cdot10^{-6}$ | 2,32 | 0,125 | $1{,}94\cdot10^{-4}$ | 1,03 |
| | | | 0,0625 | $9{,}39\cdot10^{-5}$ | 1,05 |

Tartiblar $O(\Delta x^2+\delta^2+\tau)$ bahoni tasdiqlaydi. Eng mayda to‘rdagi 2,32 qiymat biroz katta chiqqan, chunki bu to‘r etalondan faqat bir marta yirikroq.

Bitta ajratuvchi ustunida vaqt qadami maydalanganda ham tartib 1 ga teng. Barcha jarayonlar qatnashgan geterogen, murakkab shakldagi masalada suv balansi qoldig‘i har bir qadamda $10^{-10}$ dan kichik. $S'_s\to0$ da yechim elastik suv berishi hisobga olinmagan modelga yaqinlashadi (farq $<10^{-8}$ m).

**Dalem tajriba ma’lumotlari**

Dalem tajribasi Kruseman va de Ridder [21] kitobining 4.2-jadvalida keltirilgan. Quduq sarfi $Q=761$ m³/sut, to‘rtta pyezometr quduqdan 30–120 m masofada. Ma’lumotlar yuqori qatlam napori o‘zgarmas deb olingan Laplas etaloni bilan moslashtirildi.

**3-jadval.** Dalem tajribasi: uchta talqindagi parametrlar va o‘rtacha kvadratik farq (`tajribalar/t4_dalem.py`).

| Talqin | $T$, m²/sut | $S$ | $c$, sut | $S'$ | RMSE, mm |
|---|---|---|---|---|---|
| Walton usuli [21] | 1731 | $1{,}9\cdot10^{-3}$ | 468 | | 6,9 |
| ajratuvchining elastik suv berishisiz, eng kichik kvadratlar | 1674 | $1{,}77\cdot10^{-3}$ | 325 | | 5,87 |
| ajratuvchining elastik suv berishi bilan, eng kichik kvadratlar | 1670 | $1{,}52\cdot10^{-3}$ | 370 | $1{,}1\cdot10^{-3}$ | 5,80 |

Ajratuvchining elastik suv berishini qo‘shish xatoni deyarli kamaytirmaydi, $S'$ esa ishonchli aniqlanmaydi: $\lg S'$ ning standart chetlanishi 0,41. Kuzatuvlar 0,015–0,33 sut oralig‘ida, bu topilgan $t_c\approx0{,}4$ sut bilan bir tartibda. Demak bu ma’lumotlar modelni tasdiqlaydi, lekin faqat suvli qatlamdagi pasayish bo‘yicha ajratuvchining elastik suv berishini tasdiqlab bo‘lmaydi. Shunga qaramay topilgan $S'=1{,}1\cdot10^{-3}$ qiymat Kruseman va de Ridder ([21], 97–98-betlar) Neuman–Witherspoon nisbatlar usuli bilan olgan $S'=1{,}1\cdot10^{-3}$ bilan mos keladi. Ular ajratuvchi ichidagi qo‘shimcha pyezometrdan foydalangan ($b'=8$ m, $K'b'/S'=126$ m²/sut). Ularning o‘rtacha parametrlari: $T=1800$ m²/sut, $S=1{,}7\cdot10^{-3}$, $c=450$ sut. O‘lchangan pasayishlar chop etilishdan oldin quduqning to‘liq ochmaganligi va dengiz suvi ko‘tarilishi ta’siri bo‘yicha tuzatilgan, biz ularni shu ko‘rinishda ishlatdik.

**Chop etilgan ko‘p qatlamli misollar**

Olsthoorn [22] uchta ajratuvchi ($c=100$, $S'=0{,}0016$) orasidagi ikki suvli qatlam ($T=100$, $S=10^{-4}$) uchun pasayishlarni keltiradi. Tizim ustida va ostida pasayish nolga teng, $r=10$, $t=10^{-5}$–5. Maqolada bu qiymatlar Hemker va Maas [10] natijalari bilan bir xil ekani aytilgan. Ikki tashqi ajratuvchi bilan kengaytirilgan Laplas etalonimiz jadvaldagi 36 qiymatning hammasini bosilgan to‘rt xonagacha takrorlaydi (`testlar/test_masala1.py`). Sonli modelda tashqi naporlar napori berilgan ikki qatlam bilan, har bir ajratuvchi $M=20$ qatlamcha bilan tasvirlandi. To‘rning eng yaqin nuqtasida ($r=10{,}69$) etalondan farq quduqli qatlamda $t\ge10^{-3}$ da 0,31% dan, ikkinchi qatlamda $t\ge0{,}1$ da 1,1% dan oshmaydi (`tajribalar/t7_maas_mlu.py`). Nisbiy farq faqat birinchi vaqt qadamlarida, ikkinchi qatlamdagi pasayish hali 0,01 dan kichik bo‘lganda kattaroq.

MLU qo‘llanmasidagi "Two-aquifers" tekshiruv misoli [23] bosimsiz qatlam, 10 m qalinlikdagi ajratuvchi va quduqli qatlamdan ($Q=180$ m³/sut) iborat. Unda ajratuvchining elastik suv berishi va gorizontal oqimi uchta yupqa qatlam bilan tasvirlangan, jami oltita qatlam. Laplas etalonimiz 1 minutdan keyin $r=5{,}01$ m da 0,29826 m beradi, bu MLU qiymatining barcha bosilgan raqamlari bilan bir xil. 15,85 m da 0,0496 m olinadi, MLU da 0,050 m. Xuddi shu olti qatlamli tizim uchun sonli model etalondan to‘rning ikki eng yaqin nuqtasida 0,04% va 0,3% farq qiladi.

### 3.2. Ajratuvchining elastik suv berishini qachon hisobga olmaslik mumkin?

3.1-bo‘limdagi tizim $K'=10^{-3}$ m/sut va $b'=5$ m bilan olinadi, bunda $t_c=2{,}5$ sut. Suvli qatlamlarning elastik suv berish koeffitsiyentlari ko‘paytuvchi bilan o‘zgartirilib, $\varepsilon=0{,}083$–83 oraliq hosil qilindi. Ikki model $r=30$ m da solishtirildi (2-rasm).

**4-jadval.** Quduqli qatlamda $r=30$ m da ajratuvchining elastik suv berishi hisobga olingan va olinmagan modellar orasidagi nisbiy farq (`tajribalar/t2_tc_mezoni.py`).

| $\varepsilon$ | Farq 5% dan katta bo‘lgan oxirgi $t/t_c$ | $t=10^3\,t_c$ dagi farq |
|---|---|---|
| 0,083 | 0,25 | 0,4% |
| 0,83 | 0,79 | 2,3% |
| 8,3 | $10^3$ dan katta | 6,6% |
| 83 | $10^3$ dan katta | 12% |

![](t2_tc_mezoni.png){width=16cm}

**2-rasm.** Ajratuvchining elastik suv berishi hisobga olingan ($s$) va olinmagan ($s_0$) modellardagi napor pasayishlarining nisbiy farqi $|s-s_0|/s$ (%), o‘lchamsiz vaqt $t/t_c$ ga bog‘liq ravishda, $\varepsilon$ ning to‘rt qiymati uchun; (a) quduqli 2-qatlam, (b) qo‘shni 1-qatlam.

$\varepsilon$ o‘zgarmas bo‘lganda $t/t_c$ bo‘yicha chizilgan egri chiziqlar ustma-ust tushadi. Kichik $\varepsilon$ da $t_c$ dan biroz keyin ajratuvchining elastik suv berishini hisobga olmaslik mumkin. $\varepsilon\gtrsim1$ da esa bunday emas: yopiq tizimda ajratuvchidan ajralgan suv umumiy elastik suv zaxirasini oshirib turaveradi. Quduq bo‘lmagan qo‘shni qatlamda farq yana ham katta: $\varepsilon=0{,}83$ da $t=10^3\,t_c$ da 10%. Faqat $t_c$ ga asoslangan mezon bu holatlarda noto‘g‘ri xulosaga olib keladi.

### 3.3. Bosimsiz yuqori qatlamli geterogen maydon

Soha 2000 × 1000 m, to‘r 80 × 40 yacheyka. 1-qatlam bosimsiz, unda filtratsiya koeffitsiyenti kichik linza va egri-bugri yo‘nalgan yuqori o‘tkazuvchan o‘zan bor. $K_2(x,y)$ silliq o‘zgaradi va linzaga ega, $K_3$ ikki zonadan iborat. 1-ajratuvchida $K'$ 20 marta katta bo‘lgan gidrogeologik oyna bor. Infiltratsion ta’minot $6\cdot10^{-4}$ m/sut; bug‘lanish parametrlari $E_0=1{,}5\cdot10^{-3}$ m/sut, $\Delta=3$ m, $n=1{,}5$. Chap va o‘ng chegarada napor berilgan. To‘rtta quduq jami 3200 m³/sut suv oladi: uchtasining filtri 2-qatlamda, bittasiniki 3-qatlamda. Hisob statsionar holatdan boshlanadi.

Yupqa ajratuvchilarda ($t_c=11$ va 26 sut) geterogenlik 2-qatlamdagi eng katta pasayishni bir jinsli maydonga nisbatan ikki baravar oshiradi (10,5 m va 5,6 m). Oyna orqali pasayish grunt suvlari sathiga ham o‘tadi (0,67 m va 0,05 m). Bir yil davomida quduqlar suvining 0,6% i ajratuvchilar zaxirasidan olinadi va elastik suv berishi pasayishni 0,5% dan kam o‘zgartiradi (`tajribalar/t5_geterogen.py`).

Qalin gilli ajratuvchilarda ($b'=15$ va 20 m, $K'=10^{-4}$ va $5\cdot10^{-5}$ m/sut, $S'_s=4\cdot10^{-4}$ 1/m) $t_c=900$ va 3200 sut, ya’ni hisoblangan bir yildan uzoq. Barcha o‘zgarishlar faqat quduqlardan kelishi uchun infiltratsion ta’minot o‘zgarmas olindi (3-rasm).

![](t6_qalin_ajratuvchi.png){width=16cm}

**3-rasm.** Qalin gilli ajratuvchilar: (a) to‘rtta nuqtadagi napor pasayishi, ajratuvchining elastik suv berishi hisobga olingan (tutash chiziq) va olinmagan (uzuq chiziq) model; (b) elastik suv berishi hisobga olingan modelda quduqlar suvining manbalari, umumiy sarfga nisbatan foizda.

Elastik suv berishi 2-qatlamda dastlabki napor pasayishini 18–30% ga sekinlashtiradi. Taxminan $t=1$ sut da quduqlar suvining 26% i ajratuvchilardan keladi. Keyinchalik asosiy manba napor berilgan chegaralar bo‘ladi, bir yildan keyin quduqli qatlamdagi farq 0,5% dan kam. Bosimsiz qatlamda esa holat boshqacha: bir yildan keyin grunt suvlari sathi elastik suv berishi hisobga olingan modelda 0,051 m ga, hisobga olinmagan modelda 0,060 m ga pasayadi. Demak elastik suv berishi sath pasayishini 14% ga kamaytiradi va bu farq hisob oxirigacha saqlanadi. Balans qoldig‘i $4\cdot10^{-12}$ dan kichik, Pikar iteratsiyalari har bir qadamda 4 tadan oshmaydi.

## 4. Muhokama

Natijalardan amaliy xulosa kelib chiqadi. Agar $\varepsilon$ kichik bo‘lsa, $t$ bir necha $t_c$ dan oshgandan keyin quduqli qatlamda ajratuvchining elastik suv berishini hisobga olmaslik mumkin. Qalin gil qatlam ustidagi grunt suvlari qatlamida esa $t_c$ dan kichik vaqtlarda bunday model sath pasayishini oshirib baholaydi, bug‘lanish va tuz to‘planishini esa aynan shu pasayish belgilaydi. Sug‘oriladigan tekisliklarga xos ajratuvchilarda (10–20 m qalinlikdagi gil va qumoq) $t_c$ yillar bilan o‘lchanadi, shuning uchun elastik suv berishi modelda saqlanishi kerak.

Ajratuvchi ustunlarini yo‘qotish MODFLOW dagi qatlamli tasvirga teng kuchli. Natijalar mashina aniqligigacha mos keladi, lekin bizning tizim matritsasining o‘lchami faqat suvli qatlamlar masalasiga teng. 2-lemma bu yo‘qotish M-matritsa tuzilishini saqlashini ko‘rsatadi. Demak musbatlik va turg‘unlik testlarda kuzatilibgina qolmay, kondensatsiyalangan tizimga isbot orqali o‘tadi.

Modelning cheklovlari quyidagilar. 2- va 3-qatlamlar doimo bosimli deb olinadi, har bir quduqning filtri bitta qatlamda. Ajratuvchilarda faqat vertikal oqim hisobga olinadi. 3.1-bo‘limdagi MLU misolida uchta qatlamni uzluksiz (6) tenglama bilan almashtirish ($b'=10$ m, $K'=0{,}1$ m/sut, $S'=0{,}004$) quduqli qatlamda $r=5{,}01$ m dagi pasayishni 1 minutda −7% ga, 7 sutkada +1,2% ga o‘zgartiradi; 15,85 m da bu farqlar −16% va +1,3%. Farqning bir qismi MLU tasviridagi vertikal yo‘nalishdagi yirik bo‘linishdan, bir qismi bizning modelda hisobga olinmagan ajratuvchidagi gorizontal oqimdan kelib chiqadi; bu ikki ta’sir alohida ajratilmadi. Vaqt bo‘yicha sxema birinchi tartibli. BDF2 kabi ikkinchi tartibli sxema qadam cheklanmasa M-matritsa xossasini yo‘qotadi, shuning uchun oshkormas Eyler sxemasi saqlandi va xato qadam o‘sishi bilan boshqariladi. Pikar iteratsiyasining yaqinlashishi isbotlanmagan, har qadamda nazorat qilinadi. Dala ma’lumotlari bilan tekshiruv bitta klassik tajribaga asoslangan va bu tajriba ajratuvchining elastik suv berishini aniqlay olmaydi. Buning uchun Dalemdagi kabi ajratuvchi ichida pyezometri bo‘lgan tajriba kerak.

## 5. Xulosalar

1. Har bir ajratuvchida elastik rejim tenglamasi, $K(x,y)$, bosimsiz yuqori qatlam, infiltratsion ta’minot, bug‘lanish va quduqlar bo‘lgan uch qatlamli model massa saqlanish qonuni va Darsi qonunidan keltirib chiqarildi. U har bir ajratuvchi ustunini aniq yo‘qotadigan chekli hajmlar sxemasi bilan yechildi.
2. Sxema massani aniq saqlaydi, elastik suv zaxirasi bilan vaznlangan normada absolyut turg‘un va diskret maksimum prinsipini qanoatlantiradi. Kondensatsiyalangan almashinuv matritsasi simmetrik va musbat yarim aniq.
3. Dastur Theis, Hantush–Jacob va Laplas sohasidagi ko‘p qatlamli yechimlarni 0,74% aniqlikda takrorlaydi. MODFLOW 6 bilan farq $4\cdot10^{-9}$ m. Yaqinlashish tartibi fazo bo‘yicha (suvli qatlamlar to‘ri va ajratuvchi qatlamchalari) ikki, vaqt bo‘yicha bir.
4. Ajratuvchining elastik suv berishini hisobga olmaslik mumkinligi $t/t_c$ va $\varepsilon=S'/\sum S$ ga bog‘liq. $\varepsilon\gtrsim1$ da uning ta’siri $t_c$ dan ancha keyin ham saqlanadi.
5. Qalin gilli ajratuvchilar va geterogen maydonda ajratuvchining elastik suv berishi hisobga olinganda bir yildan keyin bosimsiz qatlamdagi sath pasayishi taxminan 14% ga kam bo‘ladi (0,051 m va 0,060 m); hisobga olinmagan model bu pasayishni oshirib baholaydi.

Keyingi ish: ajratuvchi orqali tuzlar ko‘chishi bilan bog‘lash va ajratuvchida pyezometrlari bo‘lgan obyekt ma’lumotlari bo‘yicha kalibrlash.

**Mualliflar hissasi:** g‘oya, N.R.; metodologiya, N.R. va J.E.; dastur, J.E.; tekshiruv, J.E.; tahlil, J.E.; tadqiqot, J.E.; dastlabki matn, J.E.; ko‘rib chiqish va tahrirlash, N.R. va J.E.; ilmiy rahbarlik, N.R. Barcha mualliflar maqolaning chop etiladigan nusxasini o‘qigan va unga rozi.

**Moliyalashtirish:** Tadqiqot tashqi moliyalashtirishsiz bajarilgan.

**Ma’lumotlar mavjudligi:** Maqoladagi har bir raqam va rasmni hosil qiluvchi dastur kodi, kiruvchi ma’lumotlar va skriptlar https://github.com/javokhir-erkinov/1-masala manzilida ochiq.

**Minnatdorchilik:** Maqolani tayyorlashda mualliflar dastur kodi, rasmlar va til tahririda Claude (Anthropic) yordamidan foydalangan. Mualliflar natijani ko‘rib chiqqan va tahrirlagan, maqola mazmuni uchun to‘liq javobgar.

**Manfaatlar to‘qnashuvi:** Mualliflar manfaatlar to‘qnashuvi yo‘qligini bildiradi.

## Belgilar

| Belgi | Ma’nosi | Birligi |
|---|---|---|
| $h_k$ | $k$-suvli qatlamdagi napor | m |
| $u_j$ | $j$-ajratuvchi qatlamdagi napor | m |
| $K_k$, $T_k$ | $k$-suvli qatlamning filtratsiya koeffitsiyenti va suv o‘tkazuvchanligi | m/sut, m²/sut |
| $b_k$ | $k$-bosimli suvli qatlam qalinligi | m |
| $S_k$, $\mu$ | $k$-qatlamning elastik suv berish koeffitsiyenti, 1-qatlamning suv berish koeffitsiyenti | – |
| $S_{s,k}$ | $k$-qatlamning solishtirma elastik suv berish koeffitsiyenti | 1/m |
| $K'_j$, $b'_j$ | $j$-ajratuvchining vertikal filtratsiya koeffitsiyenti va qalinligi | m/sut, m |
| $S'_{s,j}$, $S'_j$ | $j$-ajratuvchining solishtirma va to‘liq ($S'_sb'$) elastik suv berish koeffitsiyenti | 1/m, – |
| $c$ | ajratuvchining gidravlik qarshiligi $b'/K'$ | sut |
| $\mathbf q$, $q_z$ | filtratsiya tezligining gorizontal va vertikal tashkil etuvchilari | m/sut |
| $q^+_j$, $q^-_j$ | $j$-ajratuvchining yuqori va pastki chegarasi orqali solishtirma sarf, pastga musbat | m/sut |
| $W$, $E$ | infiltratsion ta’minot va bug‘lanish jadalligi | m/sut |
| $E_0$, $\Delta$, $n$ | yer sathidagi bug‘lanish, bug‘lanish to‘xtaydigan chuqurlik, daraja ko‘rsatkichi | m/sut, m, – |
| $z_0$, $z_s$ | 1-qatlam tubi va yer sathi belgisi | m |
| $Q$ | quduq sarfi, suv olinganda musbat | m³/sut |
| $\zeta$ | ajratuvchining yuqori chegarasidan pastga o‘lchanadigan chuqurlik | m |
| $t_c$ | ajratuvchining xarakterli vaqti $b'^2S'_s/K'$ | sut |
| $\varepsilon$ | elastik suv berish koeffitsiyentlari nisbati $S'/\sum_kS_k$ | – |
| $\tau$, $\delta$, $M$ | vaqt qadami, ajratuvchi qatlamchasi qalinligi, qatlamchalar soni | sut, m, – |
| $C_{PN}$, $A_P$ | $P$ va $N$ yacheykalar orasidagi o‘tkazuvchanlik, yacheyka yuzasi | m²/sut, m² |
| $\Delta x$ | yacheyka o‘lchami | m |
| $\sigma$ | ajratuvchi ustuni tizimidagi $S'_s\delta/\tau$ | m/sut |
| $\Lambda$ | ajratuvchi ustunining $2\times2$ o‘lchamli almashinuv matritsasi | m/sut |

$k=1,2,3$ indeksi suvli qatlamlarni yuqoridan pastga, $j=1,2$ indeksi ajratuvchilarni raqamlaydi; shtrix ajratuvchi parametrini bildiradi.

## Adabiyotlar

1. Ravshanov, N.; Shadmanov, I.; Adizova, F.; Shadmanova, K.; Sayidova, N.; Jurayeva, N.; Kamalova, M. Quasi-3D Numerical Modeling of Groundwater Flow, Particle Transport, and Clogging-Induced Interlayer Leakage in Heterogeneous Multilayer Aquifers. *Hydrology* **2026**, *13*, 276. https://doi.org/10.3390/hydrology13100276
2. Ravshanov, N.; Shadmanova, K.; Shadmanov, I. Numerical Modeling of Nonlinear Groundwater Flow in a Heterogeneous Four-Layer Porous Medium. *Hydrology* **2026**, *13*, 181. https://doi.org/10.3390/hydrology13070181
3. Karimov, M.; Yakhshiboev, M.; Rakhimova, F.; Yadgarova, L. Modeling of Groundwater Flow in a Multilayer Porous Medium Based on a Nonlinear Mathematical Model. In *Proceedings of the Fourth International Conference on Digital Technologies, Optics, and Materials Science (DTIEE 2025)*; SPIE: Bellingham, WA, USA, 2025; Volume 13662, p. 25. https://doi.org/10.1117/12.3072569
4. Mukhamadiyev, A.; Karimov, M.; Khujakulov, T.; Sattarov, O.; Cho, J. A Nonlinear Model of Three-Layer Groundwater Flow with Evaporation Dependent on the Critical Groundwater Level. *Mathematics* **2026**, *14*, 256. https://doi.org/10.3390/math14020256
5. Kodirov, K.R. Mathematical Models and Approximate Analytical Methods of Mass Transfer in Multilayer Media. Ph.D. Thesis, Digital Technologies and Artificial Intelligence Development Research Institute, Tashkent, Uzbekistan, 2023. (In Russian)
6. Ravshanov, N.; Kodirov, K.; Islamov, Yu.N.; Kukanova, M.A. Mathematical Model of Flow Filtration in a Three-Layer Stratum and Its Analytical Solution. *Probl. Comput. Appl. Math.* **2017**, *1*, 47–53. (In Russian)
7. Hantush, M.S. Modification of the Theory of Leaky Aquifers. *J. Geophys. Res.* **1960**, *65*, 3713–3725. https://doi.org/10.1029/JZ065i011p03713
8. Neuman, S.P.; Witherspoon, P.A. Theory of Flow in a Confined Two Aquifer System. *Water Resour. Res.* **1969**, *5*, 803–816. https://doi.org/10.1029/WR005i004p00803
9. Hemker, C.J. Transient Well Flow in Leaky Multiple-Aquifer Systems. *J. Hydrol.* **1985**, *81*, 111–126. https://doi.org/10.1016/0022-1694(85)90170-2
10. Hemker, C.J.; Maas, C. Unsteady Flow to Wells in Layered and Fissured Aquifer Systems. *J. Hydrol.* **1987**, *90*, 231–249. https://doi.org/10.1016/0022-1694(87)90069-2
11. Cihan, A.; Zhou, Q.; Birkholzer, J.T. Analytical Solutions for Pressure Perturbation and Fluid Leakage through Aquitards and Wells in Multilayered-Aquifer Systems. *Water Resour. Res.* **2011**, *47*, W10504. https://doi.org/10.1029/2011WR010721
12. Herrera, I.; Yates, R. Integrodifferential Equations for Systems of Leaky Aquifers and Applications: 3. A Numerical Method of Unlimited Applicability. *Water Resour. Res.* **1977**, *13*, 725–732. https://doi.org/10.1029/WR013i004p00725
13. Leake, S.A.; Leahy, P.P.; Navoy, A.S. *Documentation of a Computer Program to Simulate Transient Leakage from Confining Units Using the Modular Finite-Difference, Ground-Water Flow Model*; Open-File Report 94-59; U.S. Geological Survey: Reston, VA, USA, 1994. https://doi.org/10.3133/ofr9459
14. Hughes, J.D.; Leake, S.A.; Galloway, D.L.; White, J.T. *Documentation for the Skeletal Storage, Compaction, and Subsidence (CSUB) Package of MODFLOW 6*; Techniques and Methods 6-A62; U.S. Geological Survey: Reston, VA, USA, 2022. https://doi.org/10.3133/tm6A62
15. Herrera, I.; Figueroa V., G.E. A Correspondence Principle for the Theory of Leaky Aquifers. *Water Resour. Res.* **1969**, *5*, 900–904. https://doi.org/10.1029/WR005i004p00900
16. Forsyth, P.A.; Sammon, P.H. Quadratic Convergence for Cell-Centered Grids. *Appl. Numer. Math.* **1988**, *4*, 377–394. https://doi.org/10.1016/0168-9274(88)90016-5
17. Stehfest, H. Algorithm 368: Numerical Inversion of Laplace Transforms. *Commun. ACM* **1970**, *13*, 47–49. https://doi.org/10.1145/361953.361969
18. Theis, C.V. The Relation between the Lowering of the Piezometric Surface and the Rate and Duration of Discharge of a Well Using Ground-Water Storage. *Trans. Am. Geophys. Union* **1935**, *16*, 519–524. https://doi.org/10.1029/TR016i002p00519
19. Hantush, M.S.; Jacob, C.E. Non-Steady Radial Flow in an Infinite Leaky Aquifer. *Trans. Am. Geophys. Union* **1955**, *36*, 95–100. https://doi.org/10.1029/TR036i001p00095
20. Langevin, C.D.; Hughes, J.D.; Banta, E.R.; Niswonger, R.G.; Panday, S.; Provost, A.M. *Documentation for the MODFLOW 6 Groundwater Flow Model*; Techniques and Methods 6-A55; U.S. Geological Survey: Reston, VA, USA, 2017. https://doi.org/10.3133/tm6A55
21. Kruseman, G.P.; de Ridder, N.A. *Analysis and Evaluation of Pumping Test Data*, 2nd ed.; ILRI Publication 47; International Institute for Land Reclamation and Improvement: Wageningen, The Netherlands, 1990.
22. Olsthoorn, T.N. Matlab Function hantushn (Column of C. Maas). *Stromingen* **2003**, *9*, 48–50. (In Dutch)
23. Hemker, C.J.; Randall, J. *Modeling with MLU: Applying the Multilayer Approach to Aquifer Test Analysis*; Tutorial; Microfem: Amsterdam, The Netherlands, 2010.
