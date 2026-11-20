import numpy as np
import pytest
import masala1 as m1
from masala1 import etalon
from masala1.yechuvchi import progonka


def test_progonka():
    rng = np.random.default_rng(0)
    M, n = 7, 4
    off = -rng.uniform(0.5, 1.0, (M - 1, n))
    dia = 2.5 + rng.uniform(0, 1, (M, n))
    rhs = rng.normal(size=(M, n, 3))
    X = progonka(dia, off, rhs)
    for c in range(n):
        A = np.diag(dia[:, c]) + np.diag(off[:, c], 1) + np.diag(off[:, c], -1)
        assert np.allclose(A @ X[:, c, :], rhs[:, c, :])


def test_laplas_teys():
    t = np.array([0.01, 0.1, 1.0, 10.0])
    s = etalon.kop_qatlam(50.0, t, [100.0], [1e-4], [], [], [], [1000.0])[:, 0]
    assert np.allclose(s, etalon.teys(50.0, t, 100.0, 1e-4, 1000.0), rtol=1e-5)


def test_laplas_xantush_jakob():
    t = np.array([0.01, 0.1, 1.0, 10.0])
    s = etalon.kop_qatlam(50.0, t, [1e8, 100.0], [1e8, 1e-4], [1e-3], [2.0], [0.0], [0, 1000.0])[:, 1]
    assert np.allclose(s, etalon.xantush_jakob(50.0, t, 100.0, 1e-4, 1000.0, 2e3), rtol=1e-4)


def _ajratuvchi_ustun(M, tau, t_oxir=2.0):
    """Ikki qatlam napori berilgan: 0-qatlamda 1 m, 1-qatlamda 0 m; ajratuvchi boshida 0 m."""
    g = m1.Tor([1.0], [1.0])
    Kv, b, Ss = 1e-2, 2.0, 1e-2
    mo = m1.Model(g, N=2, bosimsiz=False, Kv=[Kv], bq=[b], Ss=[Ss], M=[M], hD=[1.0, 0.0])
    y = m1.Yechuvchi(mo)
    y.u[0] = np.zeros((M, 1))
    H = [np.array([1.0]), np.array([0.0])]
    t = 0.0
    qs = []
    while t < t_oxir - 1e-12:
        H, bal = y.qadam(H, t, tau)
        t += tau
    # yuqori chegaradagi oqim: c_end (h_top - u_1)
    q = 2 * Kv / (b / M) * (1.0 - y.u[0][0, 0])
    D = Kv / Ss
    n = np.arange(1, 400)
    q_ex = Kv / b * (1 + 2 * np.sum(np.exp(-n ** 2 * np.pi ** 2 * D * t / b ** 2)))
    return q, q_ex, bal, y


def test_ajratuvchi_fazoviy_tartib():
    e = []
    for M in (4, 8, 16):
        q, q_ex, _, _ = _ajratuvchi_ustun(M, 1e-4, 0.5)
        e.append(abs(q - q_ex))
    p = np.log2(np.array(e[:-1]) / np.array(e[1:]))
    assert np.all(p > 1.8)


def test_ajratuvchi_vaqt_tartib():
    e = []
    for tau in (0.04, 0.02, 0.01):
        q, q_ex, _, _ = _ajratuvchi_ustun(80, tau)
        e.append(q)
    q_ex = _ajratuvchi_ustun(80, 1e-4)[0]
    err = np.abs(np.array(e) - q_ex)
    p = np.log2(err[:-1] / err[1:])
    assert np.all(p > 0.85)


def _murakkab_model():
    nx, ny = 24, 18
    g = m1.Tor(np.full(nx, 25.0), np.linspace(15, 35, ny))
    X, Y = np.meshgrid(g.xc, g.yc)
    K1 = 5 * (1 + 0.5 * np.sin(2 * np.pi * X / 600)) * np.where((X - 300) ** 2 / 90 ** 2 + (Y - 250) ** 2 / 60 ** 2 < 1, 0.3, 1.0)
    K2 = 3 * np.exp(0.3 * np.cos(2 * np.pi * Y / 450))
    K3 = np.where(X < 300, 8.0, 15.0)
    akt = ((X - 300) ** 2 / 300 ** 2 + (Y - 225) ** 2 / 230 ** 2) < 1
    hd1 = np.where(X > 520, 18.0, np.nan)
    hd3 = np.where(X < 60, 14.0, np.nan)
    mo = m1.Model(g, N=3, K=[K1, K2, K3], b=[20.0, 10.0, 15.0], S=[0.12, 2e-4, 3e-4],
                  z_tub=0.0, z_yer=20.0 + 0.002 * X, E0=2e-3, Delta=3.0, nE=1.5,
                  W=lambda t: 1e-3 * (1 + np.sin(2 * np.pi * t / 365)),
                  Kv=[1e-3 * (1 + 0.5 * X / 600), 5e-4], bq=[3.0, 5.0 + 0.002 * Y], Ss=[2e-4, 1e-4],
                  M=[8, 6], aktiv=[akt] * 3, hD=[hd1, np.nan, hd3],
                  quduqlar=[m1.Quduq(1, 9, 12, 300.0), m1.Quduq(2, 8, 8, 200.0), m1.Quduq(0, 10, 14, 30.0)])
    return mo, g


def test_massa_balansi_murakkab():
    mo, g = _murakkab_model()
    y = m1.Yechuvchi(mo)
    H0 = [np.full(g.nc, 17.0), np.full(g.nc, 16.0), np.full(g.nc, 15.0)]
    H, tl, o, bals = y.hisob(H0, 60.0, 0.5, 1.3, tau_max=5.0)
    err = max(abs(y.balans_xatosi(b)[1]) for b in bals)
    assert err < 1e-10
    assert all(b["iter"] < 50 for b in bals)


def test_kvazistatsionar_chegara():
    """Ss -> 0 da sig'imli ajratuvchi yechimi sig'imsiz (M=0) yechimga intiladi."""
    g = m1.Tor(np.full(9, 20.0), np.full(9, 20.0))
    base = dict(N=3, K=[10.0, 5.0, 8.0], b=[10.0] * 3, S=[1e-3] * 3, bosimsiz=False,
                Kv=[1e-2, 5e-3], bq=[2.0, 3.0], hD=[np.nan, np.nan, np.nan],
                quduqlar=[m1.Quduq(1, 4, 4, 100.0)])
    H0 = [np.zeros(g.nc)] * 3
    res = []
    for M, Ss in ((0, 0.0), (10, 1e-12)):
        y = m1.Yechuvchi(m1.Model(g, Ss=[Ss, Ss], M=[M, M], **base))
        H, *_ = y.hisob(H0, 1.0, 0.05)
        res.append(np.concatenate(H))
    assert np.max(abs(res[0] - res[1])) < 1e-8


def test_simmetriya_va_musbatlik():
    mo, g = _murakkab_model()
    y = m1.Yechuvchi(mo)
    H0 = [np.full(g.nc, 17.0), np.full(g.nc, 16.0), np.full(g.nc, 15.0)]
    y._ajratuvchi_boshlang(H0)
    aj = [y._ajratuvchi(k, 1.0) for k in range(2)]
    L, r = y._operator(H0, aj)
    assert abs(L - L.T).max() < 1e-12 * abs(L).max()
    for d in aj:
        det = d["tt"] * d["bb"] - d["tb"] * d["bt"]
        assert np.all(d["tt"] >= 0) and np.all(det >= -1e-14)


# Olsthoorn (Maas rukni), Stromingen 9(3) 2003, 50-bet, N = 10 ustuni; manbada Hemker–Maas 1987 bilan aynan mos deyilgan
MAAS_T = [1e-5, 1e-4, 1e-3, 1e-2, 0.1, 1.0, 5.0]
MAAS_S1 = [0.0, 0.0, 0.0, 0.0030, 0.3404, 0.5362, 0.5363]
MAAS_S2 = [0.0165, 0.6585, 1.8541, 3.0419, 4.0997, 4.3178, 4.3178]


def test_laplas_maas_olsthoorn_2003():
    a = (0.01, 1.0, 0.0016)
    s = etalon.kop_qatlam(10.0, MAAS_T, [100.0, 100.0], [1e-4, 1e-4], [0.01], [1.0], [0.0016],
                          [0, 4 * np.pi * 100], Ns=10, ust=a, ost=a)
    assert np.allclose(s[:, 0], MAAS_S1, atol=6e-5)
    assert np.allclose(s[:, 1], MAAS_S2, atol=6e-5)


def test_laplas_mlu_two_aquifers():
    """MLU tutorial (Hemker, Randall 2010), Two-aquifers: 1 min da 5,01 m da 0,29826 m, 15,85 m da 0,050 m."""
    T = [10, 90, 1.67, 1.66, 1.67, 100]
    S = [0.2, 0.004, 0.00133, 0.00134, 0.00133, 0.0008]
    c = [0.55, 17, 33, 33, 17]
    Q = [0, 0, 0, 0, 0, 180.0]
    s1 = etalon.kop_qatlam(5.01, [1 / 1440], T, S, [1 / x for x in c], [1] * 5, [0] * 5, Q, Ns=10)[0, 5]
    s2 = etalon.kop_qatlam(15.85, [1 / 1440], T, S, [1 / x for x in c], [1] * 5, [0] * 5, Q, Ns=10)[0, 5]
    assert abs(s1 - 0.29826) < 1e-5
    assert abs(s2 - 0.050) < 6e-4
