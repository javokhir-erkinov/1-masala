"""6-tajriba: qalin gilli ajratuvchilar (t ≲ t_c), 5-tajribadagi geterogen soha, infiltratsiya o'zgarmas.
Sig'imli va sig'imsiz modellar: napor pasayishi, qatlamlararo oqim va quduq suvining manbalari."""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import masala1 as m1
import importlib.util, sys, os

spec = importlib.util.spec_from_file_location("t5", os.path.join(os.path.dirname(__file__), "t5_geterogen.py"))
src = open(spec.origin).read().split("\nnat, R = {}, {}")[0]
t5 = {}
exec(compile(src, "t5", "exec"), t5)
g, maydonlar, hd, quduq_joy, nx, ny = t5["g"], t5["maydonlar"], t5["hd"], t5["quduq_joy"], t5["nx"], t5["ny"]

Kv0 = [1e-4, 5e-5]; bq = [15.0, 20.0]; Ss = [4e-4, 4e-4]
tc = [bq[k] ** 2 * Ss[k] / Kv0[k] for k in range(2)]
eps = [Ss[k] * bq[k] / (0.10 if k == 0 else 3e-4) for k in range(2)]


def hisob(sigimli):
    K, Kv = maydonlar(True)
    Kv = [Kv[0] / 1e-3 * Kv0[0], Kv[1] / 5e-4 * Kv0[1]]
    base = dict(N=3, K=K, b=[0.0, 15.0, 25.0], S=[0.10, 3e-4, 4e-4], bosimsiz=True, z_tub=0.0,
                z_yer=20.0, E0=1.5e-3, Delta=3.0, nE=1.5, W=6e-4,  # o'zgarmas: o'zgarishlar faqat quduqlardan
                Kv=Kv, bq=bq, Ss=Ss if sigimli else [0.0, 0.0], M=[16, 16] if sigimli else [0, 0], hD=hd)
    H = m1.Yechuvchi(m1.Model(g, **base)).statsionar(
        [np.full(g.nc, 17.0), np.full(g.nc, 16.5), np.full(g.nc, 16.0)])
    y = m1.Yechuvchi(m1.Model(g, quduqlar=[m1.Quduq(*q) for q in quduq_joy], **base))
    y._ajratuvchi_boshlang(H)
    kuz = [(1, 20, 30), (1, 20, 40), (0, 20, 40), (2, 28, 40)]
    Hn, tl, o, bals = y.hisob(H, 365.0, 0.02, 1.12, tau_max=2.0, kuzat=kuz)
    return dict(H0=H, H=Hn, t=tl, o=o, bals=bals,
                balans=max(abs(y.balans_xatosi(b)[1]) for b in bals))


R = {k: hisob(k == "sigimli") for k in ("sigimli", "sigimsiz")}
nat = {"t_c_sut": tc, "eps": eps}
for k, r in R.items():
    jam = {q: float(sum(b[q] for b in r["bals"])) for q in ("dV_qatlam", "dV_ajratuvchi", "W", "E", "Q", "chegara")}
    s = [r["H0"][i] - r["H"][i] for i in range(3)]
    nat[k] = {"balans_nisbiy_max": r["balans"], "jamlanma_m3": jam,
              "pasayish_max_m": [float(x.max()) for x in s],
              "ajratuvchi_ulushi": -jam["dV_ajratuvchi"] / jam["Q"]}
o1, o0 = R["sigimli"]["o"], R["sigimsiz"]["o"]
t = R["sigimli"]["t"]
for n, nom in enumerate(["2-qatlam (20,30)", "2-qatlam (20,40)", "1-qatlam (20,40)", "3-qatlam (28,40)"]):
    s1 = o1[0, n] - o1[:, n]
    s0 = np.interp(t, R["sigimsiz"]["t"], o0[0, n] - o0[:, n])
    i = s1 > 0.05 * s1.max()
    nat[nom] = {"s_365_sigimli": float(s1[-1]), "s_365_sigimsiz": float(s0[-1]),
                "max_nisbiy_farq": float(np.max(abs(s1[i] - s0[i]) / s1[i])) if i.any() else None}
print(json.dumps(nat, indent=1))
json.dump(nat, open("tajribalar/t6_qalin_ajratuvchi.json", "w"), indent=1)

fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
for n, (nom, c) in enumerate(zip(["2-qatlam, quduq yonida", "2-qatlam, markaz", "1-qatlam, markaz", "3-qatlam, quduq yonida"], "C0 C1 C2 C3".split())):
    ax[0].plot(t, o1[0, n] - o1[:, n], c, label=nom)
    ax[0].plot(R["sigimsiz"]["t"], o0[0, n] - o0[:, n], c + "--")
ax[0].set_xlabel(r"$t$, sut"); ax[0].set_ylabel("napor pasayishi, m"); ax[0].legend(fontsize=7); ax[0].grid(alpha=.3)
ax[0].set_title("a) tutash: elastik suv berishi bilan, uzuq: usiz", fontsize=9)
b = R["sigimli"]["bals"]; tt = np.array([x["t"] for x in b]); dt = np.diff(np.r_[0, tt])
Qr = np.array([x["Q"] for x in b]) / dt
ax[1].plot(tt, -np.array([x["dV_ajratuvchi"] for x in b]) / dt / Qr * 100, label="ajratuvchilar zaxirasi")
ax[1].plot(tt, -np.array([x["dV_qatlam"] for x in b]) / dt / Qr * 100, label="suvli qatlamlar zaxirasi")
ax[1].plot(tt, np.array([x["chegara"] + x["W"] - x["E"] for x in b]) / dt / Qr * 100,
           label="chegaralar va bug'lanish kamayishi")
ax[1].set_xscale("log"); ax[1].set_xlabel(r"$t$, sut"); ax[1].set_ylabel("quduqlar sarfiga nisbatan, %")
ax[1].legend(fontsize=7); ax[1].grid(alpha=.3, which="both"); ax[1].set_title("b) quduq suvining manbalari (elastik suv berishi hisobga olingan model)", fontsize=9)
fig.tight_layout(); fig.savefig("tajribalar/t6_qalin_ajratuvchi.png", dpi=200, metadata={"Software": None})
