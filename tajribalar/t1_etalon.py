"""1-tajriba: uch bosimli qatlam, ikki sig'imli ajratuvchi, o'rta qatlamda quduq.
Sonli yechim Laplas sohasidagi etalon bilan solishtiriladi."""
import json, sys, time
import numpy as np
import masala1 as m1
from masala1 import etalon

T = [200.0, 100.0, 300.0]; S = [2e-4, 1e-4, 3e-4]
Kv = [2e-3, 1e-3]; bq = [5.0, 8.0]; Ss = [1e-4, 1e-4]
Q = 500.0
d0 = float(sys.argv[1]) if len(sys.argv) > 1 else 2.0
Mz = int(sys.argv[2]) if len(sys.argv) > 2 else 20
dx = m1.Tor.teleskop(20000.0, d0, 1.15)
g = m1.Tor(dx, dx)
c = g.nx // 2
mo = m1.Model(g, N=3, K=[t / 10 for t in T], b=[10.0] * 3, S=S, bosimsiz=False,
              Kv=Kv, bq=bq, Ss=Ss, M=[Mz, Mz], quduqlar=[m1.Quduq(1, c, c, Q)])
y = m1.Yechuvchi(mo)
H0 = [np.zeros(g.nc)] * 3
rr = [10.0, 30.0, 100.0]
obs = []
for r in rr:
    i = int(np.argmin(abs(g.xc - (g.xc[c] + r))))
    obs.append(i)
kuz = [(k, c, i) for k in range(3) for i in obs]
t0 = time.time()
osish = float(sys.argv[3]) if len(sys.argv) > 3 else 1.2
H, tl, o, bals = y.hisob(H0, 10.0, 1e-4, osish, kuzat=kuz)
cpu = time.time() - t0
res = {"d0": d0, "M": Mz, "nx": g.nx, "cpu_s": cpu, "nqadam": len(bals),
       "balans_max": max(abs(y.balans_xatosi(b)[1]) for b in bals), "nuqtalar": []}
idx = tl > 1e-3
for n, (k, j, i) in enumerate(kuz):
    r = g.xc[i] - g.xc[c]
    se = etalon.kop_qatlam(r, tl[idx], T, S, Kv, bq, Ss, [0, Q, 0])[:, k]
    sn = -o[idx, n]
    res["nuqtalar"].append({"qatlam": k + 1, "r": r,
                            "max_abs": float(np.max(abs(sn - se))),
                            "max_s": float(np.max(se)),
                            "nisbiy": float(np.max(abs(sn - se)) / np.max(se))})
print(json.dumps(res, indent=1))
