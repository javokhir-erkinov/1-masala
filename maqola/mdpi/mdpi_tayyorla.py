"""Converts maqola/maqola1_qoralama.md into the MDPI Hydrology layout (numbered references,
MDPI section structure and back matter). Output: maqola/mdpi/maqola1_hydrology.md"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
src = (ROOT / "maqola/maqola1_qoralama.md").read_text()

body = src[src.index("## 1. Introduction"):src.index("## Declaration of generative AI use")]
nomen = src[src.index("## Nomenclature"):src.index("## 1. Introduction")]

# --- sentences that cite sources outside the verified list are removed
body = body.replace(", after De Ridder (1961)", "")
body = body.replace(" (problem 2 of the dissertation)", "")
body = body.replace(" The example by Veling and Maas (2009) reports particle paths only and was not used.", "")

body = re.sub(r"\{\\rm ([A-Za-z]+)\}", r"\\mathrm{\1}", body)

# --- citations -> keys
C = [
    (r"Kodirov \(2023; see also Ravshanov et al\. 2017\)", "Kodirov [@kod23; @rav17]"),
    (r"Ravshanov et al\. \(2026a\)", "Ravshanov et al. [@rav26a]"),
    (r"Ravshanov et al\. \(2026b\)", "Ravshanov et al. [@rav26b]"),
    (r"Karimov et al\. \(2025\)", "Karimov et al. [@kar25]"),
    (r"Mukhamadiyev et al\. \(2026\)", "Mukhamadiyev et al. [@muk26]"),
    (r"Hantush \(1960\)", "Hantush [@han60]"),
    (r"\(Hantush 1960\)", "[@han60]"),
    (r"\(the arrangement of Hantush 1960\)", "(the arrangement of Hantush [@han60])"),
    (r"Neuman and Witherspoon \(1969\)", "Neuman and Witherspoon [@nw69]"),
    (r"Hemker and Maas \(1987\)", "Hemker and Maas [@hm87]"),
    (r"Hemker \(1985\)", "Hemker [@hem85]"),
    (r"Cihan et al\. \(2011\)", "Cihan et al. [@cih11]"),
    (r"Herrera and Yates \(1977\)", "Herrera and Yates [@hy77]"),
    (r"\(Leake et al\. 1994\)", "[@lea94]"),
    (r"\(Hughes et al\. 2022\)", "[@hug22]"),
    (r"Herrera and Figueroa \(1969\)", "Herrera and Figueroa [@hf69]"),
    (r"\(Forsyth and Sammon 1988\)", "[@fs88]"),
    (r"Stehfest \(1970\)", "Stehfest [@ste70]"),
    (r"Theis \(1935\)", "Theis [@the35]"),
    (r"Hantush–Jacob \(1955\)", "Hantush–Jacob [@hj55]"),
    (r"\(Langevin et al\. 2017\)", "[@lan17]"),
    (r"Kruseman and de Ridder \(1990, p\. 97–98\)", "Kruseman and de Ridder ([@kr90], pp. 97–98)"),
    (r"Walton type curve \(Kruseman and de Ridder 1990\)", "Walton type curve [@kr90]"),
    (r"Kruseman and de Ridder \(1990\)", "Kruseman and de Ridder [@kr90]"),
    (r"Olsthoorn \(2003\)", "Olsthoorn [@ols03]"),
    (r"\(Hemker and Randall 2010\)", "[@hr10]"),
]
for a, b in C:
    body, n = re.subn(a, b, body)
    assert n, a
left = re.findall(r"\b(?:19|20)\d\d[ab]?\)", body)
assert not left, left

# --- section structure
H = {
    "## 1. Introduction": "## 1. Introduction",
    "## 2. Mathematical model": "## 2. Materials and Methods\n\n### 2.1. Mathematical Model",
    "## 3. Numerical method": "### 2.2. Numerical Method",
    "## 4. Properties of the scheme": "### 2.3. Properties of the Scheme",
    "## 5. Verification": "## 3. Results\n\n### 3.1. Verification",
    "### When can aquitard storage be neglected?": "### 3.2. When Can Aquitard Storage Be Neglected?",
    "### Heterogeneous field with an unconfined top aquifer": "### 3.3. Heterogeneous Field with an Unconfined Top Aquifer",
    "## 6. Results\n\n": "",
    "## 7. Discussion": "## 4. Discussion",
    "## 8. Conclusions": "## 5. Conclusions",
}
for a, b in H.items():
    assert a in body, a
    body = body.replace(a, b)
# remaining level-3 headings become unnumbered run-in subheadings
body = re.sub(r"^### (?!\d)(.+)$", r"**\1**", body, flags=re.M)

S = [("Sections 3 and 4", "Sections 2.2 and 2.3"), ("(Section 2)", "(Section 2.1)"),
     ("(Section 6)", "(Sections 3.2 and 3.3)"), ("Section 3 ", "Section 2.2 "), ("Section 5", "Section 3.1")]
for a, b in S:
    assert a in body, a
    body = body.replace(a, b)

# --- figures and tables
FIG = {1: "rasm1_sxema.png", 2: "t2_tc_mezoni_en.png", 3: "t6_qalin_ajratuvchi_en.png"}
def fig(m):
    n, cap = int(m.group(1)), m.group(2)
    cap = re.sub(r" \(`maqola/rasm1_sxema\.png`\)", "", cap)
    cap = cap.replace("left: pumped aquifer, right: adjacent aquifer", "(a) pumped aquifer 2, (b) adjacent aquifer 1")
    return f"![]({FIG[n]}){{width=16cm}}\n\n**Figure {n}.** {cap}"
body = re.sub(r"^Fig\. (\d)\. (.+)$", fig, body, flags=re.M)
body = re.sub(r"\bFig\. (\d)", r"Figure \1", body)
body = re.sub(r"^Table (\d)\. ", r"**Table \1.** ", body, flags=re.M)

# --- numbering of references by first appearance
order = []
for k in re.findall(r"@(\w+)", body):
    if k not in order:
        order.append(k)
num = {k: i + 1 for i, k in enumerate(order)}
def cite(m):
    ks = re.findall(r"@(\w+)", m.group(0))
    return "[" + ",".join(str(num[k]) for k in ks) + "]"
body = re.sub(r"\[@\w+(?:; @\w+)*\]", cite, body)
body = re.sub(r"\(\[@(\w+)\], pp", lambda m: f"([{num[m.group(1)]}], pp", body)
assert "@" not in body

from mdpi_refs import R
assert set(order) == set(R), set(order) ^ set(R)
refs = "\n".join(f"{num[k]}. {R[k]}" for k in order)

# --- nomenclature (MDPI back matter "Abbreviations" position)
nomen = nomen.replace("## Nomenclature", "## Nomenclature\n\nThe following symbols are used in this manuscript:")

head = """---
title: "A Mass-Conservative Numerical Model of Groundwater Flow in a Three-Aquifer System with Storage in Both Aquitards, Heterogeneous Transmissivity and an Unconfined Top Layer"
---

*Article*

Normakhmad Ravshanov ^1^ and Javokhir Erkinov ^2,\\*^

^1^ Digital Technologies and Artificial Intelligence Development Research Institute, 17A Buz-2, Tashkent 100125, Uzbekistan; ravshanzade-09@mail.ru

^2^ Samarkand State University named after Sharof Rashidov, Samarkand 140104, Uzbekistan; erkinovjavohir@samdu.uz

\\* Correspondence: erkinovj110@gmail.com

**Abstract:** In layered aquifer systems, water released from elastic storage in the aquitards delays the response of the adjacent aquifers, yet numerical models used for irrigated plains often treat aquitards as storage-free leakance interfaces. We formulate a model of three aquifers coupled through two aquitards, each governed by a one-dimensional vertical diffusion equation with continuity of head and flux at both faces. Conductivity varies in plan in all units, and the upper aquifer is unconfined, with recharge, depth-dependent evaporation and wells. The model is discretised with cell-centred finite volumes and backward Euler time stepping. The aquitard unknowns are eliminated column by column, leaving one sparse symmetric system for the aquifer heads. We prove exact discrete mass conservation, unconditional stability in an energy norm and a discrete maximum principle. The code reproduces the Theis, Hantush–Jacob and a Laplace-domain multilayer solution with aquitard storage within 0.74% and agrees with MODFLOW 6 to $4\\times10^{-9}$ m. Experiments show that the aquitard time scale $t_c$ alone does not decide when storage can be neglected; the storage ratio $\\varepsilon$ matters as well. With thick clay aquitards, aquitard storage reduces the water-table decline in the unconfined aquifer by 14% after one year.

**Keywords:** multilayer aquifer; aquitard storage; leaky aquifer; finite volume method; unconditional stability; unconfined aquifer; evaporation

"""

back = """
**Author Contributions:** Conceptualization, N.R.; methodology, N.R. and J.E.; software, J.E.; validation, J.E.; formal analysis, J.E.; investigation, J.E.; writing—original draft preparation, J.E.; writing—review and editing, N.R. and J.E.; supervision, N.R. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research received no external funding.

**Data Availability Statement:** The program code, input data and scripts that produce every number and figure in this article are openly available at https://github.com/javokhir-erkinov/1-masala.

**Acknowledgments:** During the preparation of this manuscript, the authors used Claude (Anthropic) for assistance with program code, figure preparation and language editing. The authors have reviewed and edited the output and take full responsibility for the content of this publication.

**Conflicts of Interest:** The authors declare no conflicts of interest.

"""

out = head + body.rstrip() + "\n" + back + nomen.rstrip() + "\n\n## References\n\n" + refs + "\n"
(ROOT / "maqola/mdpi/maqola1_hydrology.md").write_text(out)
words = len(re.sub(r"\$[^$]*\$", "x", head.split("**Abstract:**")[1].split("**Keywords")[0]).split())
print("abstract words:", words, "| refs:", len(order), "| total words:", len(out.split()))
