"""5-tajriba: K(x,y), bosimsiz yuqori qatlam, infiltratsiya, bug'lanish va quduqlar.
To'rt holat: sig'imli/sig'imsiz ajratuvchi x geterogen/bir jinsli K.
Boshlang'ich holat: quduqlarsiz statsionar holat. Hisob 365 sutka."""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import masala1 as m1

Lx, Ly, nx, ny = 2000.0, 1000.0, 80, 40
g = m1.Tor(np.full(nx, Lx / nx), np.full(ny, Ly / ny))
X, Y = np.meshgrid(g.xc, g.yc)


def ellips(cx, cy, a, b):
    return ((X - cx) / a) ** 2 + ((Y - cy) / b) ** 2 < 1


def maydonlar(geterogen):
    if not geterogen:
        return [8.0, 12.0, 20.0], [1e-3, 5e-4]
    K1 = 8.0 * np.where(ellips(800, 600, 300, 150), 0.25, 1.0)
    K1 = np.where(abs(Y - (0.35 * Ly + 0.1 * Ly * np.sin(2 * np.pi * X / Lx))) < 60, 8.0 * 2.5, K1)
    K2 = 12.0 * (1 + 0.4 * np.sin(2 * np.pi * X / Lx) * np.cos(np.pi * Y / Ly))
    K2 = np.where(ellips(1300, 400, 250, 180), 12.0 * 0.3, K2)
    K3 = 20.0 * np.where(X > 1100, 1.5, 0.8)
    Kv1 = 1e-3 * np.where(ellips(1500, 650, 200, 120), 20.0, 1.0)  # gidrogeologik oyna
    Kv2 = 5e-4 * (1 + 0.5 * np.cos(2 * np.pi * X / Lx))
    return [K1, K2, K3], [Kv1, Kv2]


hd = [np.where(X < Lx / nx, 18.0, np.where(X > Lx - Lx / nx, 16.0, np.nan)),
      np.where(X < Lx / nx, 17.0, np.where(X > Lx - Lx / nx, 15.5, np.nan)),
      np.where(X < Lx / nx, 16.5, np.where(X > Lx - Lx / nx, 15.0, np.nan))]
quduq_joy = [(1, 20, 30, 800.0), (1, 20, 50, 800.0), (1, 12, 40, 600.0), (2, 28, 40, 1000.0)]


def hisob(sigimli, geterogen):
    K, Kv = maydonlar(geterogen)
    base = dict(N=3, K=K, b=[0.0, 15.0, 25.0], S=[0.10, 3e-4, 4e-4], bosimsiz=True, z_tub=0.0,
                z_yer=20.0, E0=1.5e-3, Delta=3.0, nE=1.5, W=lambda t: 6e-4 * (1 + np.cos(2 * np.pi * (t - 60) / 365)),
                Kv=Kv, bq=[6.0, 8.0], Ss=[3e-4, 2e-4] if sigimli else [0.0, 0.0],
                M=[12, 12] if sigimli else [0, 0], hD=hd)
    mo0 = m1.Model(g, **base)
    H = m1.Yechuvchi(mo0).statsionar([np.full(g.nc, 17.0), np.full(g.nc, 16.5), np.full(g.nc, 16.0)])
    mo = m1.Model(g, quduqlar=[m1.Quduq(*q) for q in quduq_joy], **base)
    y = m1.Yechuvchi(mo)
    y._ajratuvchi_boshlang(H)
    kuz = [(1, 20, 30), (0, 20, 30), (2, 20, 30), (0, 30, 60)]
    Hn, tl, o, bals = y.hisob(H, 365.0, 0.05, 1.15, tau_max=5.0, kuzat=kuz)
    jam = {k: float(sum(b[k] for b in bals)) for k in ("dV_qatlam", "dV_ajratuvchi", "W", "E", "Q", "chegara")}
    return dict(H0=[h.reshape(ny, nx) for h in H], H=[h.reshape(ny, nx) for h in Hn], t=tl, o=o, jam=jam,
                balans=max(abs(y.balans_xatosi(b)[1]) for b in bals), iter_max=max(b["iter"] for b in bals))


nat, R = {}, {}
for sig in (True, False):
    for get in (True, False):
        key = f"{'sigimli' if sig else 'sigimsiz'}_{'geterogen' if get else 'birjinsli'}"
        r = hisob(sig, get)
        R[key] = r
        s2 = r["H0"][1] - r["H"][1]
        nat[key] = {"jamlanma_m3": r["jam"], "balans_nisbiy_max": r["balans"], "pikar_max": r["iter_max"],
                    "pasayish_2qatlam_max_m": float(s2.max()),
                    "pasayish_1qatlam_max_m": float((r["H0"][0] - r["H"][0]).max()),
                    "quduq_suvi_ajratuvchidan_ulush": -r["jam"]["dV_ajratuvchi"] / r["jam"]["Q"]}
        print(key, json.dumps(nat[key]))
json.dump(nat, open("tajribalar/t5_geterogen.json", "w"), indent=1)

fig, ax = plt.subplots(2, 2, figsize=(10, 5.6), sharex=True, sharey=True)
for a, key in zip(ax.ravel(), ["sigimli_geterogen", "sigimsiz_geterogen", "sigimli_birjinsli", "sigimsiz_birjinsli"]):
    r = R[key]
    s = r["H0"][1] - r["H"][1]
    cs = a.contourf(g.xc, g.yc, s, levels=np.linspace(0, max(R[k]["H0"][1].max() - 0 for k in R) * 0 + 4.0, 17), cmap="viridis_r", extend="max")
    a.contour(g.xc, g.yc, r["H0"][0] - r["H"][0], levels=[0.1, 0.25, 0.5, 1.0], colors="w", linewidths=.7)
    a.set_title(key.replace("_", ", ").replace("sigim", "sig'im"), fontsize=9)
    a.set_aspect("equal")
for a in ax[1]: a.set_xlabel("x, m")
for a in ax[:, 0]: a.set_ylabel("y, m")
fig.colorbar(cs, ax=ax, label="2-qatlamda napor pasayishi, m (oq: 1-qatlam)")
fig.savefig("tajribalar/t5_geterogen.png", dpi=200, metadata={"Software": None})
