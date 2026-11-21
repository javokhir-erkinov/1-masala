"""Uzbek parallel text in the MDPI layout of maqola1_hydrology.md (same numbering of sections,
equations, figures and references). Output: maqola/mdpi/maqola1_hydrology_uz.md"""
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mdpi_refs import R

ROOT = pathlib.Path(__file__).resolve().parents[2]
src = (ROOT / "maqola/maqola1_qoralama_uz.md").read_text()
body = src[src.index("## 1. Kirish"):src.index("## Sun’iy intellektdan foydalanish")]
nomen = src[src.index("## Belgilar"):src.index("## 1. Kirish")]
abst = src[src.index("## Annotatsiya"):src.index("## Belgilar")]

body = re.sub(r"\{\\rm ([A-Za-z]+)\}", r"\\mathrm{\1}", body)
body = body.replace(" Veling va Maas (2009) misolida faqat zarrachalar trayektoriyalari keltirilgani uchun u ishlatilmadi.", "")
body = body.replace(" (dissertatsiyaning 2-masalasi)", "")
body = body.replace("4.2-jadvalida De Ridder (1961) bo‘yicha keltirilgan", "4.2-jadvalida keltirilgan")
assert "1961" not in body, re.search(r".{80}1961.{40}", body).group(0)

C = [
    (r"Qodirov \(2023; shuningdek Ravshanov va boshq\. 2017\)", "Qodirov [@kod23; @rav17]"),
    (r"Ravshanov va boshq\. \(2026a\)", "Ravshanov va boshq. [@rav26a]"),
    (r"Ravshanov va boshq\. \(2026b\)", "Ravshanov va boshq. [@rav26b]"),
    (r"Karimov va boshq\. \(2025\)", "Karimov va boshq. [@kar25]"),
    (r"Mukhamadiyev va boshq\. \(2026\)", "Mukhamadiyev va boshq. [@muk26]"),
    (r"\(Hantush 1960 dagi joylashuv\)", "(Hantush [@han60] dagi joylashuv)"),
    (r"Hantush \(1960\)", "Hantush [@han60]"),
    (r"\(Hantush 1960\)", "[@han60]"),
    (r"Neuman va Witherspoon \(1969\)", "Neuman va Witherspoon [@nw69]"),
    (r"Hemker va Maas \(1987\)", "Hemker va Maas [@hm87]"),
    (r"Hemker–Maas \(1987\)", "Hemker–Maas [@hm87]"),
    (r"Hemker \(1985\)", "Hemker [@hem85]"),
    (r"Cihan va boshq\. \(2011\)", "Cihan va boshq. [@cih11]"),
    (r"Herrera va Yates \(1977\)", "Herrera va Yates [@hy77]"),
    (r"\(Leake va boshq\. 1994\)", "[@lea94]"),
    (r"\(Hughes va boshq\. 2022\)", "[@hug22]"),
    (r"Herrera va Figueroa \(1969\)", "Herrera va Figueroa [@hf69]"),
    (r"\(Forsyth va Sammon 1988\)", "[@fs88]"),
    (r"Stehfest \(1970\)", "Stehfest [@ste70]"),
    (r"Theis \(1935\)", "Theis [@the35]"),
    (r"Hantush–Jacob \(1955\)", "Hantush–Jacob [@hj55]"),
    (r"\(Langevin va boshq\. 2017\)", "[@lan17]"),
    (r"Kruseman va de Ridder \(1990, 97–98-betlar\)", "Kruseman va de Ridder ([@kr90], 97–98-betlar)"),
    (r"\(Kruseman, de Ridder 1990\)", "[@kr90]"),
    (r"Kruseman va de Ridder \(1990\)", "Kruseman va de Ridder [@kr90]"),
    (r"Olsthoorn \(2003\)", "Olsthoorn [@ols03]"),
    (r"\(Hemker va Randall 2010\)", "[@hr10]"),
]
for a, b in C:
    body, n = re.subn(a, b, body)
    assert n, a
left = re.findall(r".{40}\b(?:19|20)\d\d[ab]?\).{10}", body)
assert not left, left

H = {
    "## 2. Matematik model": "## 2. Materiallar va usullar\n\n### 2.1. Matematik model",
    "## 3. Sonli usul": "### 2.2. Sonli usul",
    "## 4. Sxemaning xossalari": "### 2.3. Sxemaning xossalari",
    "## 5. Tekshiruv": "## 3. Natijalar\n\n### 3.1. Tekshiruv",
    "### Ajratuvchining elastik suv berishini qachon hisobga olmaslik mumkin?": "### 3.2. Ajratuvchining elastik suv berishini qachon hisobga olmaslik mumkin?",
    "### Bosimsiz yuqori qatlamli geterogen maydon": "### 3.3. Bosimsiz yuqori qatlamli geterogen maydon",
    "## 6. Natijalar\n\n": "",
    "## 7. Muhokama": "## 4. Muhokama",
    "## 8. Xulosalar": "## 5. Xulosalar",
}
for a, b in H.items():
    assert a in body, a
    body = body.replace(a, b)
body = re.sub(r"^### (?!\d)(.+)$", r"**\1**", body, flags=re.M)

S = [("(3- va 4-bo‘limlar)", "(2.2- va 2.3-bo‘limlar)"), ("(5-bo‘lim)", "(3.1-bo‘lim)"), ("3-bo‘limdagi", "2.2-bo‘limdagi"),
     ("5-bo‘limda", "3.1-bo‘limda"), ("(2-bo‘lim)", "(2.1-bo‘lim)"), ("(6-bo‘lim)", "(3.2- va 3.3-bo‘limlar)")]
for a, b in S:
    assert a in body, a
    body = body.replace(a, b)
assert not re.search(r"\b[4-8]-bo‘lim", body), re.findall(r".{30}\b[4-8]-bo‘lim.{10}", body)

FIG = {1: "rasm1_sxema_uz.png", 2: "t2_tc_mezoni.png", 3: "t6_qalin_ajratuvchi.png"}
def fig(m):
    n, cap = int(m.group(1)), m.group(2)
    cap = re.sub(r" \(`maqola/rasm1_sxema\.png`\)", "", cap)
    cap = cap.replace("chapda quduqli qatlam, o‘ngda qo‘shni qatlam", "(a) quduqli 2-qatlam, (b) qo‘shni 1-qatlam")
    return f"![]({FIG[n]}){{width=16cm}}\n\n**{n}-rasm.** {cap}"
body = re.sub(r"^(\d)-rasm\. (.+)$", fig, body, flags=re.M)
body = re.sub(r"^(\d)-jadval\. ", r"**\1-jadval.** ", body, flags=re.M)

order = []
for k in re.findall(r"@(\w+)", body):
    if k not in order:
        order.append(k)
num = {k: i + 1 for i, k in enumerate(order)}
body = re.sub(r"\[@\w+(?:; @\w+)*\]", lambda m: "[" + ",".join(str(num[k]) for k in re.findall(r"@(\w+)", m.group(0))) + "]", body)
assert "@" not in body
assert set(order) == set(R), set(order) ^ set(R)
refs = "\n".join(f"{num[k]}. {R[k]}" for k in order)

head = """---
title: "Ajratuvchi qatlamlarning elastik suv berishi, suv o‘tkazuvchanlikning koordinatalarga bog‘liqligi va bosimsiz yuqori qatlam hisobga olingan uch qatlamli tizimda yer osti suvlari filtratsiyasining massani saqlovchi sonli modeli"
---

*Maqola (Hydrology jurnaliga yuboriladigan inglizcha matnning o‘zbekcha nusxasi)*

Ravshanov Normaxmad ^1^, Erkinov Javokhir ^2,\\*^

^1^ Raqamli texnologiyalar va sun’iy intellektni rivojlantirish ilmiy-tadqiqot instituti, Buz-2, 17A, Toshkent, 100125, O‘zbekiston; ravshanzade-09@mail.ru

^2^ Sharof Rashidov nomidagi Samarqand davlat universiteti, Samarqand, 140104, O‘zbekiston; erkinovjavohir@samdu.uz

\\* Muallif bilan aloqa: erkinovj110@gmail.com

**Annotatsiya:** Ko‘p qatlamli tizimlarda ajratuvchi qatlamlarning elastik suv zaxirasidan ajraladigan suv qo‘shni suvli qatlamlardagi napor pasayishini kechiktiradi, biroq sug‘oriladigan tekisliklar uchun tuzilgan sonli modellarda ajratuvchilar ko‘pincha elastik suv berishi hisobga olinmagan oqib o‘tish chegarasi sifatida qaraladi. Maqolada ikki ajratuvchi orqali bog‘langan uchta suvli qatlam modeli taklif etiladi; har bir ajratuvchida vertikal bir o‘lchamli elastik rejim tenglamasi yechiladi, ikkala chegarada napor va oqim uzluksiz. Barcha qatlamlarda filtratsiya koeffitsiyenti $x$, $y$ koordinatalarga bog‘liq, yuqori qatlam bosimsiz bo‘lib, unga infiltratsion ta’minot, sizot suvlari chuqurligiga bog‘liq bug‘lanish va quduqlar ta’sir qiladi. Model markazlashgan chekli hajmlar usuli va oshkormas Eyler sxemasi bilan diskretlanadi. Ajratuvchi noma’lumlari har bir ustunda yo‘qotiladi va suvli qatlamlar naporlari uchun bitta simmetrik siyrak tizim qoladi. Diskret massa saqlanishi, energiya normasida absolyut turg‘unlik va diskret maksimum prinsipi isbotlangan. Dastur Theis, Hantush–Jacob va ajratuvchining elastik suv berishini hisobga olgan Laplas sohasidagi ko‘p qatlamli yechimlarni 0,74% aniqlikda takrorlaydi, MODFLOW 6 bilan farq $4\\cdot10^{-9}$ m. Hisoblashlar ajratuvchining elastik suv berishini hisobga olmaslik mumkinligini faqat $t_c$ xarakterli vaqti emas, elastik suv berish koeffitsiyentlari nisbati $\\varepsilon$ ham belgilashini ko‘rsatdi. Qalin gilli ajratuvchilarda elastik suv berishi bir yildan keyin bosimsiz qatlamdagi sath pasayishini 14% ga kamaytiradi.

**Kalit so‘zlar:** ko‘p qatlamli suvli gorizont; ajratuvchining elastik suv berishi; oqib o‘tuvchi qatlam; chekli hajmlar usuli; absolyut turg‘unlik; bosimsiz qatlam; bug‘lanish

"""
back = """
**Mualliflar hissasi:** g‘oya, N.R.; metodologiya, N.R. va J.E.; dastur, J.E.; tekshiruv, J.E.; tahlil, J.E.; tadqiqot, J.E.; dastlabki matn, J.E.; ko‘rib chiqish va tahrirlash, N.R. va J.E.; ilmiy rahbarlik, N.R. Barcha mualliflar maqolaning chop etiladigan nusxasini o‘qigan va unga rozi.

**Moliyalashtirish:** Tadqiqot tashqi moliyalashtirishsiz bajarilgan.

**Ma’lumotlar mavjudligi:** Maqoladagi har bir raqam va rasmni hosil qiluvchi dastur kodi, kiruvchi ma’lumotlar va skriptlar https://github.com/javokhir-erkinov/1-masala manzilida ochiq.

**Minnatdorchilik:** Maqolani tayyorlashda mualliflar dastur kodi, rasmlar va til tahririda Claude (Anthropic) yordamidan foydalangan. Mualliflar natijani ko‘rib chiqqan va tahrirlagan, maqola mazmuni uchun to‘liq javobgar.

**Manfaatlar to‘qnashuvi:** Mualliflar manfaatlar to‘qnashuvi yo‘qligini bildiradi.

"""
out = head + body.rstrip() + "\n" + back + nomen.rstrip() + "\n\n## Adabiyotlar\n\n" + refs + "\n"
(ROOT / "maqola/mdpi/maqola1_hydrology_uz.md").write_text(out)
print("refs:", len(order), "| words:", len(out.split()), "| order same as EN:", order)
