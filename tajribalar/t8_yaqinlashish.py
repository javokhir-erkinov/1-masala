"""8-tajriba: uch qatlamli masalada to'r (h, delta) va vaqt qadami (tau) bo'yicha yaqinlashish tartibi.
Bosimli qatlamlar, silliq K(x,y), ajratuvchilarda elastik suv berishi, chegarada oqim nol,
boshlang'ich holat: 1-qatlamda Gauss do'mbog'i. Xato eng mayda yechimga nisbatan (yacheyka o'rtachasi)."""
import json
import numpy as np
import masala1 as m1

L = 1000.0
t_end = 5.0


def yechim(n, tau, M):
    g = m1.Tor(np.full(n, L / n), np.full(n, L / n))
    X, Y = np.meshgrid(g.xc, g.yc)
    K = [5 * np.exp(0.5 * np.sin(2 * np.pi * X / L) * np.cos(np.pi * Y / L)),
         3 * np.exp(0.4 * np.cos(2 * np.pi * Y / L)), 8.0 + 0 * X]
    mo = m1.Model(g, N=3, K=K, b=[10.0] * 3, S=[1e-3, 5e-4, 5e-4], bosimsiz=False,
                  Kv=[5e-3 * (1 + 0.5 * np.sin(np.pi * X / L)), 2e-3], bq=[4.0, 4.0], Ss=[2e-3, 2e-3], M=[M, M])
    h1 = np.exp(-((X - 0.45 * L) ** 2 + (Y - 0.55 * L) ** 2) / (0.12 * L) ** 2)
    y = m1.Yechuvchi(mo)
    H0 = [h1.ravel(), np.zeros(g.nc), np.zeros(g.nc)]
    y._ajratuvchi_boshlang(H0)
    t = 0.0
    H = H0
    while t < t_end - 1e-12:
        H, _ = y.qadam(H, t, tau)
        t += tau
    return np.array([h.reshape(n, n) for h in H]), y


def oqir(A, n):
    f = A.shape[1] // n
    return A.reshape(3, n, f, n, f).mean(axis=(2, 4))


nat = {}
# fazo: h va delta birga maydalanadi, tau kichik
tau = 1 / 64
ref, _ = yechim(160, tau, 32)
e = []
for n, M in ((20, 4), (40, 8), (80, 16)):
    A, _ = yechim(n, tau, M)
    e.append(float(np.sqrt(np.mean((A - oqir(ref, n)) ** 2))))
p = np.log2(np.array(e[:-1]) / np.array(e[1:]))
nat["fazo"] = {"n": [20, 40, 80], "M": [4, 8, 16], "rmse_m": e, "tartib": p.tolist(), "ref": "160x160, M=32, tau=1/64"}
print("fazo", e, p)
# vaqt
ref, _ = yechim(40, 1 / 256, 8)
e = []
taus = [0.5, 0.25, 0.125, 0.0625]
for tau in taus:
    A, _ = yechim(40, tau, 8)
    e.append(float(np.sqrt(np.mean((A - ref) ** 2))))
p = np.log2(np.array(e[:-1]) / np.array(e[1:]))
nat["vaqt"] = {"tau": taus, "rmse_m": e, "tartib": p.tolist(), "ref": "40x40, M=8, tau=1/256"}
print("vaqt", e, p)
json.dump(nat, open("tajribalar/t8_yaqinlashish.json", "w"), indent=1)
