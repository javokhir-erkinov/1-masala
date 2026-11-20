"""3-tajriba: MODFLOW 6 bilan solishtirish.
1-tajribadagi masala: uch bosimli qatlam, ikki sig'imli ajratuvchi, o'rta qatlamda quduq.
MODFLOW da har bir ajratuvchi M ta alohida qatlam (K33 = K', SS = S'_s), suvli qatlamlarning
vertikal qarshiligi hisobga olinmasligi uchun ularning K33 juda katta olinadi.
Ishga tushirish: python tajribalar/t3_modflow.py <mf6 yo'li>"""
import json, sys, os, time
import numpy as np
import flopy
import masala1 as m1
from masala1 import etalon

exe = sys.argv[1] if len(sys.argv) > 1 else "mf6"
T = [200.0, 100.0, 300.0]; S = [2e-4, 1e-4, 3e-4]; b = [10.0] * 3
Kv = [2e-3, 1e-3]; bq = [5.0, 8.0]; Ss = [1e-4, 1e-4]; Mz = 20
Q = 500.0; t_end = 10.0; nstp = 175; tsm = 1.05
dx = m1.Tor.teleskop(20000.0, 2.0, 1.15)
g = m1.Tor(dx, dx)
c = g.nx // 2
rr = [10.0, 30.0, 100.0]
obs = [int(np.argmin(abs(g.xc - (g.xc[c] + r)))) for r in rr]

# --- MODFLOW 6 ---
ws = "mf6_t3"
th, kh, k33, ss, tur = [], [], [], [], []
for k in range(3):
    th.append(b[k]); kh.append(T[k] / b[k]); k33.append(1e6); ss.append(S[k] / b[k]); tur.append(("q", k))
    if k < 2:
        for m in range(Mz):
            th.append(bq[k] / Mz); kh.append(1e-12); k33.append(Kv[k]); ss.append(Ss[k]); tur.append(("a", k))
nl = len(th)
botm = -np.cumsum(th)
sim = flopy.mf6.MFSimulation(sim_name="t3", sim_ws=ws, exe_name=exe)
flopy.mf6.ModflowTdis(sim, nper=1, perioddata=[(t_end, nstp, tsm)])
flopy.mf6.ModflowIms(sim, complexity="complex", outer_dvclose=1e-10, inner_dvclose=1e-12,
                     inner_maximum=1000, linear_acceleration="bicgstab")
gwf = flopy.mf6.ModflowGwf(sim, modelname="t3")
flopy.mf6.ModflowGwfdis(gwf, nlay=nl, nrow=g.ny, ncol=g.nx, delr=g.dx, delc=g.dy, top=0.0,
                        botm=[np.full((g.ny, g.nx), z) for z in botm])
flopy.mf6.ModflowGwfnpf(gwf, icelltype=0, k=kh, k33=k33)
flopy.mf6.ModflowGwfsto(gwf, iconvert=0, ss=ss, transient={0: True})
flopy.mf6.ModflowGwfic(gwf, strt=0.0)
lay2 = [i for i, t in enumerate(tur) if t == ("q", 1)][0]
flopy.mf6.ModflowGwfwel(gwf, stress_period_data={0: [((lay2, c, c), -Q)]})
qlay = [i for i, t in enumerate(tur) if t[0] == "q"]
obsrec = [(f"q{k+1}_{n}", "HEAD", (qlay[k], c, i)) for k in range(3) for n, i in enumerate(obs)]
flopy.mf6.ModflowUtlobs(gwf, continuous={"t3.obs.csv": obsrec}, digits=12)
flopy.mf6.ModflowGwfoc(gwf, budget_filerecord="t3.cbc", saverecord=[("BUDGET", "LAST")],
                       printrecord=[("BUDGET", "LAST")])
sim.write_simulation(silent=True)
t0 = time.time()
ok, _ = sim.run_simulation(silent=True)
cpu_mf = time.time() - t0
assert ok, "MODFLOW 6 xato bilan tugadi"
d = np.genfromtxt(os.path.join(ws, "t3.obs.csv"), delimiter=",", names=True)
tm = d["time"]

# --- masala1, xuddi shu vaqt qadamlari bilan ---
mo = m1.Model(g, N=3, K=[T[k] / b[k] for k in range(3)], b=b, S=S, bosimsiz=False,
              Kv=Kv, bq=bq, Ss=Ss, M=[Mz, Mz], quduqlar=[m1.Quduq(1, c, c, Q)])
y = m1.Yechuvchi(mo)
tau0 = t_end * (tsm - 1) / (tsm ** nstp - 1)
t1 = time.time()
H, tl, o, bals = y.hisob([np.zeros(g.nc)] * 3, t_end, tau0, tsm,
                         kuzat=[(k, c, i) for k in range(3) for i in obs])
cpu_m1 = time.time() - t1

res = {"cpu_modflow_s": cpu_mf, "cpu_masala1_s": cpu_m1, "nqadam": nstp, "nuqtalar": []}
for k in range(3):
    for n, i in enumerate(obs):
        smf = -d[f"Q{k+1}_{n}".upper()] if f"Q{k+1}_{n}".upper() in d.dtype.names else -d[f"q{k+1}_{n}"]
        sm1 = -np.interp(tm, tl, o[:, k * 3 + n])
        r = g.xc[i] - g.xc[c]
        sl = etalon.kop_qatlam(r, tm[tm > 1e-3], T, S, Kv, bq, Ss, [0, Q, 0])[:, k]
        res["nuqtalar"].append({
            "qatlam": k + 1, "r": round(float(r), 2), "s_max": float(smf.max()),
            "masala1_vs_modflow_max": float(np.max(abs(sm1 - smf))),
            "modflow_vs_laplas_nisbiy": float(np.max(abs(smf[tm > 1e-3] - sl)) / sl.max()),
            "masala1_vs_laplas_nisbiy": float(np.max(abs(sm1[tm > 1e-3] - sl)) / sl.max())})
os.makedirs("natijalar", exist_ok=True)
json.dump(res, open("natijalar/t3_modflow.json", "w"), indent=1)
print(json.dumps(res, indent=1))
