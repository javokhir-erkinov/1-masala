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

R = {
 "rav26a": "Ravshanov, N.; Shadmanov, I.; Adizova, F.; Shadmanova, K.; Sayidova, N.; Jurayeva, N.; Kamalova, M. Quasi-3D Numerical Modeling of Groundwater Flow, Particle Transport, and Clogging-Induced Interlayer Leakage in Heterogeneous Multilayer Aquifers. *Hydrology* **2026**, *13*, 276. https://doi.org/10.3390/hydrology13100276",
 "rav26b": "Ravshanov, N.; Shadmanova, K.; Shadmanov, I. Numerical Modeling of Nonlinear Groundwater Flow in a Heterogeneous Four-Layer Porous Medium. *Hydrology* **2026**, *13*, 181. https://doi.org/10.3390/hydrology13070181",
 "kar25": "Karimov, M.; Yakhshiboev, M.; Rakhimova, F.; Yadgarova, L. Modeling of Groundwater Flow in a Multilayer Porous Medium Based on a Nonlinear Mathematical Model. *Proc. SPIE* **2025**, *13662*, 136620J. https://doi.org/10.1117/12.3072569",
 "muk26": "Mukhamadiyev, A.; Karimov, M.; Khujakulov, T.; Sattarov, O.; Cho, J. A Nonlinear Model of Three-Layer Groundwater Flow with Evaporation Dependent on the Critical Groundwater Level. *Mathematics* **2026**, *14*, 256. https://doi.org/10.3390/math14020256",
 "kod23": "Kodirov, K.R. Mathematical Models and Approximate Analytical Methods of Mass Transfer in Multilayer Media. Ph.D. Thesis, Digital Technologies and Artificial Intelligence Development Research Institute, Tashkent, Uzbekistan, 2023. (In Russian)",
 "rav17": "Ravshanov, N.; Kodirov, K.; Islamov, Yu.N.; Kukanova, M.A. Mathematical Model of Flow Filtration in a Three-Layer Stratum and Its Analytical Solution. *Probl. Comput. Appl. Math.* **2017**, *1*, 47–53. (In Russian)",
 "han60": "Hantush, M.S. Modification of the Theory of Leaky Aquifers. *J. Geophys. Res.* **1960**, *65*, 3713–3725. https://doi.org/10.1029/JZ065i011p03713",
 "nw69": "Neuman, S.P.; Witherspoon, P.A. Theory of Flow in a Confined Two Aquifer System. *Water Resour. Res.* **1969**, *5*, 803–816. https://doi.org/10.1029/WR005i004p00803",
 "hem85": "Hemker, C.J. Transient Well Flow in Leaky Multiple-Aquifer Systems. *J. Hydrol.* **1985**, *81*, 111–126. https://doi.org/10.1016/0022-1694(85)90170-2",
 "hm87": "Hemker, C.J.; Maas, C. Unsteady Flow to Wells in Layered and Fissured Aquifer Systems. *J. Hydrol.* **1987**, *90*, 231–249. https://doi.org/10.1016/0022-1694(87)90069-2",
 "cih11": "Cihan, A.; Zhou, Q.; Birkholzer, J.T. Analytical Solutions for Pressure Perturbation and Fluid Leakage through Aquitards and Wells in Multilayered-Aquifer Systems. *Water Resour. Res.* **2011**, *47*, W10504. https://doi.org/10.1029/2011WR010721",
 "hy77": "Herrera, I.; Yates, R. Integrodifferential Equations for Systems of Leaky Aquifers and Applications: 3. A Numerical Method of Unlimited Applicability. *Water Resour. Res.* **1977**, *13*, 725–732. https://doi.org/10.1029/WR013i004p00725",
 "lea94": "Leake, S.A.; Leahy, P.P.; Navoy, A.S. *Documentation of a Computer Program to Simulate Transient Leakage from Confining Units Using the Modular Finite-Difference Ground-Water Flow Model*; Open-File Report 94-59; U.S. Geological Survey: Reston, VA, USA, 1994. https://doi.org/10.3133/ofr9459",
 "hug22": "Hughes, J.D.; Leake, S.A.; Galloway, D.L.; White, J.T. *Documentation for the Skeletal Storage, Compaction, and Subsidence (CSUB) Package of MODFLOW 6*; Techniques and Methods 6-A62; U.S. Geological Survey: Reston, VA, USA, 2022. https://doi.org/10.3133/tm6A62",
 "hf69": "Herrera, I.; Figueroa V., G.E. A Correspondence Principle for the Theory of Leaky Aquifers. *Water Resour. Res.* **1969**, *5*, 900–904. https://doi.org/10.1029/WR005i004p00900",
 "fs88": "Forsyth, P.A.; Sammon, P.H. Quadratic Convergence for Cell-Centered Grids. *Appl. Numer. Math.* **1988**, *4*, 377–394. https://doi.org/10.1016/0168-9274(88)90016-5",
 "ste70": "Stehfest, H. Algorithm 368: Numerical Inversion of Laplace Transforms. *Commun. ACM* **1970**, *13*, 47–49. https://doi.org/10.1145/361953.361969",
 "the35": "Theis, C.V. The Relation between the Lowering of the Piezometric Surface and the Rate and Duration of Discharge of a Well Using Ground-Water Storage. *Trans. Am. Geophys. Union* **1935**, *16*, 519–524. https://doi.org/10.1029/TR016i002p00519",
 "hj55": "Hantush, M.S.; Jacob, C.E. Non-Steady Radial Flow in an Infinite Leaky Aquifer. *Trans. Am. Geophys. Union* **1955**, *36*, 95–100. https://doi.org/10.1029/TR036i001p00095",
 "lan17": "Langevin, C.D.; Hughes, J.D.; Banta, E.R.; Niswonger, R.G.; Panday, S.; Provost, A.M. *Documentation for the MODFLOW 6 Groundwater Flow Model*; Techniques and Methods 6-A55; U.S. Geological Survey: Reston, VA, USA, 2017. https://doi.org/10.3133/tm6A55",
 "kr90": "Kruseman, G.P.; de Ridder, N.A. *Analysis and Evaluation of Pumping Test Data*, 2nd ed.; ILRI Publication 47; International Institute for Land Reclamation and Improvement: Wageningen, The Netherlands, 1990.",
 "ols03": "Olsthoorn, T.N. Matlab Function hantushn (Column of C. Maas). *Stromingen* **2003**, *9*, 48–50. (In Dutch)",
 "hr10": "Hemker, C.J.; Randall, J. *Modeling with MLU: Applying the Multilayer Approach to Aquifer Test Analysis*; Tutorial; Microfem: Amsterdam, The Netherlands, 2010.",
}
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

**Abstract:** In layered aquifer systems, water released from elastic storage in the aquitards delays the response of the adjacent aquifers, yet numerical models used for irrigated plains often treat aquitards as storage-free leakance interfaces. We formulate a model of three aquifers coupled through two aquitards, each governed by a one-dimensional vertical diffusion equation with continuity of head and flux at both faces. Conductivity varies in plan in all units, and the upper aquifer is unconfined, with recharge, depth-dependent evaporation and wells. The model is discretised with cell-centred finite volumes and backward Euler time stepping. The aquitard unknowns are eliminated column by column, leaving one sparse symmetric system for the aquifer heads. We prove exact discrete mass conservation, unconditional stability in an energy norm and a discrete maximum principle. The code reproduces the Theis, Hantush–Jacob and a Laplace-domain multilayer solution with aquitard storage within 0.7% and agrees with MODFLOW 6 to $4\\times10^{-9}$ m. Experiments show that the aquitard time scale $t_c$ alone does not decide when storage can be neglected; the storage ratio $\\varepsilon$ matters as well. With thick clay aquitards, a storage-free model overestimates the water-table decline by 14% after one year.

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
