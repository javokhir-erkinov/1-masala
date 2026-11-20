# 1-masala

Uch qatlamli muhitda suv filtratsiyasi: har bir ajratuvchida elastik suv zaxirasi, qatlamlarda K(x,y), bosimsiz yuqori qatlam, quduqlar, infiltratsiya va bug'lanish. 1-maqola uchun hisoblash dasturi.

## Model

- Uch suvli qatlam (yuqoridan pastga 1, 2, 3), ular orasida ikki ajratuvchi.
- 1-qatlam bosimsiz: T₁ = K₁(x,y)(h₁ − z_tub), sig'im μ, infiltratsiya W(x,y,t), bug'lanish S.F. Averyanov qonuni bo'yicha.
- 2- va 3-qatlam bosimli: T_k = K_k(x,y) b_k(x,y), elastik sig'im S_k.
- Har bir ajratuvchida vertikal bir o'lchamli elastik rejim tenglamasi S′_s ∂u/∂t = K′ ∂²u/∂ζ², tutashuv chegaralarida napor va oqim uzluksizligi; K′, b′, S′_s x, y ga bog'liq. M = 0 bo'lsa sig'imsiz (kvazistatsionar) ajratuvchi.
- Ixtiyoriy shakldagi soha (aktiv yacheykalar), 1-tur shart berilgan yacheykalar, quduqlar.

## Sonli usul

- Konservativ chekli hajmlar, yuz o'tkazuvchanligi ketma-ket qarshiliklar bo'yicha (garmonik o'rtacha).
- Vaqt bo'yicha oshkormas Eyler sxemasi, bosimsiz qatlam va bug'lanish uchun Pikar iteratsiyasi.
- Har bir ajratuvchi ustunida uch diagonalli tizim vektorlashgan progonka bilan yechilib, ajratuvchi noma'lumlari yo'qotiladi; natijada har ustun uchun 2×2 simmetrik musbat yarim aniq almashinuv matritsasi olinadi. Suvli qatlamlar naporlari bitta simmetrik siyrak tizimdan topiladi.
- Har bir qadamda suv balansi: suvli qatlamlar va ajratuvchilardagi zaxira o'zgarishi, infiltratsiya, bug'lanish, quduqlar, chegara orqali oqim.

## Tekshiruv

| Test | Natija |
|---|---|
| Laplas sohasidagi ko'p qatlamli yechim ↔ Teys | nisbiy farq < 10⁻⁵ |
| Laplas sohasidagi ko'p qatlamli yechim ↔ Xantush–Jakob | nisbiy farq < 10⁻⁴ |
| Ajratuvchi ustuni ↔ aniq qator yechim | fazoviy tartib ≈ 2, vaqt bo'yicha ≈ 1 |
| Ss → 0 da sig'imli ajratuvchi ↔ sig'imsiz model | farq < 10⁻⁸ m |
| Murakkab masala (K(x,y), ixtiyoriy soha, bosimsiz qatlam, bug'lanish, 3 quduq) | balans nisbiy qoldig'i < 10⁻¹⁰ |
| Uch qatlam, sig'imli ajratuvchilar, quduq ↔ Laplas etaloni (`tajribalar/t1_etalon.py`) | 10 sutkada eng katta nisbiy farq 0,7% |

## Ishlatish

```
pip install -e .[test]
pytest testlar
python tajribalar/t1_etalon.py 2.0 20 1.05
```

Muallif: Javokhir Erkinov, Samarqand davlat universiteti.
