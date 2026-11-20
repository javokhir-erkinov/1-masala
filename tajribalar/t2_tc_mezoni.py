"""2-tajriba: sig'imli va sig'imsiz ajratuvchili modellar farqi.
Bir jinsli uch qatlam, o'rta qatlamda quduq, Laplas sohasidagi etalon.
Farq ikki o'lchamsiz parametrga bog'liq: t/t_c va eps = S'/sum(S_k)."""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
from masala1 import etalon

T = [200.0, 100.0, 300.0]; S0 = np.array([2e-4, 1e-4, 3e-4])
Kv = [1e-3, 1e-3]; bq = [5.0, 5.0]; Q = 500.0; r = 30.0; Ss = 1e-4
tc = bq[0] ** 2 * Ss / Kv[0]
t = tc * np.logspace(-3, 3, 61)
nat = {"tc": tc, "t_tc": (t / tc).tolist(), "holatlar": []}
fig, ax = plt.subplots(1, 2, figsize=(9, 3.6), sharex=True)
for m in (10.0, 1.0, 0.1, 0.01):
    S = S0 * m
    eps = Ss * bq[0] / S.sum()
    s1 = etalon.kop_qatlam(r, t, T, S, Kv, bq, [Ss, Ss], [0, Q, 0])
    s0 = etalon.kop_qatlam(r, t, T, S, Kv, bq, [0.0, 0.0], [0, Q, 0])
    e = np.abs(s1 - s0) / np.maximum(np.abs(s1), 1e-30)
    e[s1 < 0.01 * s1[:, [1]]] = np.nan
    nat["holatlar"].append({"eps": eps, "farq": e.tolist()})
    for a, k in zip(ax, (1, 0)):
        a.loglog(t / tc, 100 * e[:, k], label=f"ε = {eps:.2g}")
for a, sar in zip(ax, ("a) quduqli 2-qatlam", "b) 1-qatlam")):
    a.set_xlabel("t / t_c"); a.set_title(sar, fontsize=10); a.grid(alpha=.3, which="both")
    a.axhline(5, color="k", lw=.8, ls="--")
    a.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
ax[0].set_ylabel("|s − s₀| / s, %"); ax[0].legend(fontsize=8)
fig.tight_layout()
fig.savefig("tajribalar/t2_tc_mezoni.png", dpi=200, metadata={"Software": None})
json.dump(nat, open("tajribalar/t2_tc_mezoni.json", "w"))
for h in nat["holatlar"]:
    e = np.array(h["farq"])
    i = np.flatnonzero(np.nan_to_num(e[:, 1]) > 0.05)
    print(f"eps={h['eps']:.3g}: 2-qatlam farqi 5% dan katta oxirgi t/tc =",
          f"{nat['t_tc'][i[-1]]:.3g}" if i.size else "yo'q")
