"""7-tajriba: sonli yechim Maas/Olsthoorn 2003 (Hemker–Maas 1987) va MLU "Two-aquifers" misollarida.
Maas: ikki suvli qatlam, uchta sig'imli ajratuvchi (ust va ostida pasayish nol). Sonli modelda
tashqi chegaralar napori berilgan qo'shimcha qatlamlar bilan ifodalanadi.
MLU: Hemker va Randall 2010 ning 6 qatlamli tasviri (ajratuvchi sig'imi yupqa qatlamlarda)."""
import json
import numpy as np
import masala1 as m1
from masala1 import etalon

nat = {}
# ---- Maas / Olsthoorn 2003 ----
MT = np.array([1e-4, 1e-3, 1e-2, 0.1, 1.0, 5.0])
MS = np.array([[0.0, 0.6585], [0.0, 1.8541], [0.0030, 3.0419], [0.3404, 4.0997], [0.5362, 4.3178], [0.5363, 4.3178]])
dx = m1.Tor.teleskop(3000.0, 1.0, 1.12)
g = m1.Tor(dx, dx); c = g.nx // 2
i10 = int(np.argmin(abs(g.xc - (g.xc[c] + 10.0)))); r10 = g.xc[i10] - g.xc[c]
mo = m1.Model(g, N=4, K=[1.0, 100.0, 100.0, 1.0], b=[1.0] * 4, S=[1.0, 1e-4, 1e-4, 1.0], bosimsiz=False,
              Kv=[0.01] * 3, bq=[1.0] * 3, Ss=[0.0016] * 3, M=[20] * 3, hD=[0.0, np.nan, np.nan, 0.0],
              quduqlar=[m1.Quduq(2, c, c, 4 * np.pi * 100)])
y = m1.Yechuvchi(mo)
H, tl, o, bals = y.hisob([np.zeros(g.nc)] * 4, 5.0, 1e-6, 1.06, kuzat=[(1, c, i10), (2, c, i10)])
sn = -np.array([np.interp(MT, tl, o[:, k]) for k in range(2)]).T
a = (0.01, 1.0, 0.0016)
se = etalon.kop_qatlam(r10, MT, [100.0, 100.0], [1e-4, 1e-4], [0.01], [1.0], [0.0016], [0, 4 * np.pi * 100], Ns=12, ust=a, ost=a)
nat["maas"] = {"r": r10, "t": MT.tolist(), "jadval": MS.tolist(), "etalon_r": se.tolist(), "sonli": sn.tolist(),
               "max_farq_etalon": float(np.max(abs(sn - se))), "nqadam": len(bals),
               "balans": max(abs(y.balans_xatosi(b)[1]) for b in bals)}
print("Maas r=%.3f" % r10, np.round(sn, 4).tolist(), "farq", nat["maas"]["max_farq_etalon"])

# ---- MLU Two-aquifers (6 qatlamli tasvir, ajratuvchilar sig'imsiz) ----
T = [10, 90, 1.67, 1.66, 1.67, 100]; S = [0.2, 0.004, 0.00133, 0.00134, 0.00133, 0.0008]; cc = [0.55, 17, 33, 33, 17]
dx = m1.Tor.teleskop(500.0, 0.5, 1.15)
g = m1.Tor(dx, dx); c = g.nx // 2
obs = {r: int(np.argmin(abs(g.xc - (g.xc[c] + r)))) for r in (5.01, 15.85)}
mo = m1.Model(g, N=6, K=T, b=[1.0] * 6, S=S, bosimsiz=False, Kv=[1 / x for x in cc], bq=[1.0] * 5,
              Ss=[0.0] * 5, M=[0] * 5, quduqlar=[m1.Quduq(5, c, c, 180.0)])
y = m1.Yechuvchi(mo)
H, tl, o, bals = y.hisob([np.zeros(g.nc)] * 6, 1 / 1440, 1e-7, 1.05, kuzat=[(5, c, i) for i in obs.values()])
res = {}
for n, (r, i) in enumerate(obs.items()):
    rr = g.xc[i] - g.xc[c]
    se = etalon.kop_qatlam(rr, [1 / 1440], T, S, [1 / x for x in cc], [1] * 5, [0] * 5, [0] * 5 + [180.0], Ns=10)[0, 5]
    res[str(r)] = {"r_tor": rr, "sonli": float(-o[-1, n]), "etalon_r_tor": float(se)}
nat["mlu"] = {"nuqtalar": res, "manba": {"5.01": 0.29826, "15.85": 0.050}, "nqadam": len(bals)}
print("MLU", res)
json.dump(nat, open("tajribalar/t7_maas_mlu.json", "w"), indent=1)
