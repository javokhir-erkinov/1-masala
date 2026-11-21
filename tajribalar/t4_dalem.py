"""4-tajriba: Dalem tajriba-filtratsion ishlari (Kruseman, de Ridder 1990, 4.2-jadval).
Ikki talqin: (a) sig'imsiz ajratuvchi (Xantush–Jakob): KD, S, c;
(b) sig'imli ajratuvchi: KD, S, c, S' (ustki qatlam napori o'zgarmas).
Ikkalasi ham Laplas sohasidagi etalon orqali, eng kichik kvadratlar usuli bilan."""
import json
import numpy as np
from scipy.optimize import least_squares
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from masala1 import etalon

d = np.genfromtxt("malumotlar/dalem.csv", delimiter=",", names=True, skip_header=2)
Q = 761.0
BIG = 1e9


def model(p, sig):
    KD, S, c = 10 ** p[0], 10 ** p[1], 10 ** p[2]
    Sp = 10 ** p[3] if sig else 0.0
    bq = 1.0  # b' = 1 deb olinadi: K' = 1/c, S'_s = S'; natija faqat c va S' ga bog'liq
    out = np.empty(len(d))
    for r in np.unique(d["r_m"]):
        i = d["r_m"] == r
        out[i] = etalon.kop_qatlam(r, d["t_sut"][i], [BIG, KD], [BIG, S],
                                   [bq / c], [bq], [Sp], [0, Q])[:, 1]
    return out


nat = {}
for nom, sig, p0 in (("sigimsiz", False, [3.2, -3, 2.7]), ("sigimli", True, [3.2, -3, 2.7, -3])):
    f = least_squares(lambda p: model(p, sig) - d["s_m"], p0, method="lm")
    J = f.jac; res = f.fun
    dof = len(res) - len(f.x)
    cov = np.linalg.inv(J.T @ J) * (res @ res) / dof
    sd = np.sqrt(np.diag(cov))
    par = {"KD": 10 ** f.x[0], "S": 10 ** f.x[1], "c": 10 ** f.x[2]}
    if sig:
        par["Sp"] = 10 ** f.x[3]
        par["t_c"] = par["c"] * par["Sp"]
    nat[nom] = {"parametrlar": par, "log10_sd": sd.tolist(),
                "RMSE_m": float(np.sqrt(np.mean(res ** 2))),
                "max_abs_m": float(np.max(abs(res))), "x": f.x.tolist()}
# Kruseman–de Ridder (Walton usuli) parametrlari bilan
pK = [np.log10(1731), np.log10(1.9e-3), np.log10(468)]
rK = model(pK, False) - d["s_m"]
nat["kruseman_walton"] = {"parametrlar": {"KD": 1731, "S": 1.9e-3, "c": 468},
                          "RMSE_m": float(np.sqrt(np.mean(rK ** 2)))}
print(json.dumps(nat, indent=1))
json.dump(nat, open("tajribalar/t4_dalem.json", "w"), indent=1)

fig, ax = plt.subplots(figsize=(5.5, 4))
tt = np.logspace(-2.1, -0.4, 60)
for r, mk in zip((30, 60, 90, 120), "osd^"):
    i = d["r_m"] == r
    ax.semilogx(d["t_sut"][i], d["s_m"][i], mk, mfc="none", color="k", ms=5)
    for nom, ls in (("sigimsiz", "--"), ("sigimli", "-")):
        p = nat[nom]["x"]
        KD, S, c = 10 ** p[0], 10 ** p[1], 10 ** p[2]
        Sp = 10 ** p[3] if len(p) > 3 else 0.0
        s = etalon.kop_qatlam(r, tt, [BIG, KD], [BIG, S], [1 / c], [1.0], [Sp], [0, Q])[:, 1]
        ax.semilogx(tt, s, ls, color="C0" if nom == "sigimli" else "C3", lw=1)
ax.plot([], [], "-", color="C0", label="ajratuvchining elastik suv berishi bilan")
ax.plot([], [], "--", color="C3", label="ajratuvchining elastik suv berishisiz")
ax.set_xlabel(r"$t$, sut"); ax.set_ylabel(r"$s$, m"); ax.legend(fontsize=8); ax.grid(alpha=.3, which="both")
fig.tight_layout(); fig.savefig("tajribalar/t4_dalem.png", dpi=200, metadata={"Software": None})
