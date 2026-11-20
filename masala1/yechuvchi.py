"""Konservativ chekli hajmlar sxemasi (oshkormas Eyler), bog'langan qadam.

Har bir vaqt qadamida:
1. har bir ajratuvchi ustunida uch diagonalli tizim progonka bilan yechilib, ajratuvchi
   noma'lumlari qo'shni suvli qatlamlar naporlari orqali ifodalanadi (statik kondensatsiya);
   natijada har bir ustun uchun 2x2 simmetrik musbat yarim aniq almashinuv matritsasi olinadi;
2. barcha suvli qatlamlar naporlari uchun bitta simmetrik siyrak tizim yechiladi;
3. bosimsiz qatlam o'tkazuvchanligi va bug'lanish Pikar iteratsiyasi bilan aniqlanadi;
4. ajratuvchi naporlari tiklanadi va suv balansi hisoblanadi.
"""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

from .model import qiymat


def progonka(dia, off, rhs):
    """Ustunlar bo'yicha vektorlashgan progonka.
    dia: (M, n); off: (M-1, n) simmetrik yon diagonal; rhs: (M, n, r)."""
    M = dia.shape[0]
    c = np.zeros_like(off)
    d = np.empty_like(rhs)
    beta = dia[0].copy()
    d[0] = rhs[0] / beta[:, None]
    for m in range(1, M):
        c[m - 1] = off[m - 1] / beta
        beta = dia[m] - off[m - 1] * c[m - 1]
        d[m] = (rhs[m] - off[m - 1][:, None] * d[m - 1]) / beta[:, None]
    for m in range(M - 2, -1, -1):
        d[m] -= c[m][:, None] * d[m + 1]
    return d


def _yuz_otkazuvchanlik(T, d, axis):
    """Yacheykalar orasidagi yuz o'tkazuvchanligi: ketma-ket qarshiliklar (garmonik o'rtacha)."""
    if axis == 1:
        a, b = T[:, :-1], T[:, 1:]
        da, db = d[:-1][None, :], d[1:][None, :]
    else:
        a, b = T[:-1, :], T[1:, :]
        da, db = d[:-1][:, None], d[1:][:, None]
    with np.errstate(divide="ignore", invalid="ignore"):
        r = da / (2 * a) + db / (2 * b)
        C = np.where((a > 0) & (b > 0), 1.0 / r, 0.0)
    return C


class Yechuvchi:
    def __init__(s, model):
        s.m = model
        g = model.tor
        s.g = g
        N, nc = model.N, g.nc
        s.N, s.nc = N, nc
        akt = np.concatenate([a.ravel() for a in model.aktiv])
        fix = np.concatenate([~np.isnan(h.ravel()) for h in model.hD]) & akt
        s.erkin = np.flatnonzero(akt & ~fix)
        s.berk = np.flatnonzero(fix)
        s.hfix = np.concatenate([h.ravel() for h in model.hD])[s.berk]
        s.A = g.A.ravel()
        # ajratuvchi ustunlari: ikki qo'shni qatlam ham aktiv bo'lsa
        s.qmask = [(model.aktiv[k] & model.aktiv[k + 1]).ravel() for k in range(N - 1)]
        s.u = [None] * (N - 1)
        s.tarix = []

    # ---- ajratuvchi: kondensatsiya ----
    def _ajratuvchi(s, k, tau):
        m = s.m
        M = m.M[k]
        Kv, bq, Ss = m.Kv[k].ravel(), m.bq[k].ravel(), m.Ss[k].ravel()
        msk = s.qmask[k]
        if M == 0:
            c = np.where(msk, Kv / bq, 0.0)
            z = np.zeros(s.nc)
            return dict(tt=c, tb=-c, bt=-c, bb=c, rt=z, rb=z, alpha=None)
        dl = bq / M
        ci = Kv / dl
        ce = 2 * Kv / dl
        st = Ss * dl / tau
        dia = np.empty((M, s.nc))
        dia[:] = st + 2 * ci
        if M == 1:
            dia[0] = st + 2 * ce
        else:
            dia[0] = st + ce + ci
            dia[-1] = st + ce + ci
        off = np.broadcast_to(-ci, (M - 1, s.nc)).copy()
        rhs = np.zeros((M, s.nc, 3))
        rhs[:, :, 0] = st * s.u[k]
        rhs[0, :, 1] = ce
        rhs[-1, :, 2] = ce
        X = progonka(dia, off, rhs)
        a, al, be = X[:, :, 0], X[:, :, 1], X[:, :, 2]
        w = msk.astype(float)
        return dict(tt=w * ce * (1 - al[0]), tb=-w * ce * be[0],
                    bt=-w * ce * al[-1], bb=w * ce * (1 - be[-1]),
                    rt=w * ce * a[0], rb=w * ce * a[-1],
                    a=a, alpha=al, beta=be, st=st, dl=dl)

    def _ajratuvchi_boshlang(s, H):
        for k in range(s.N - 1):
            M = s.m.M[k]
            if M == 0:
                continue
            z = (np.arange(M) + 0.5) / M
            ht, hb = H[k], H[k + 1]
            s.u[k] = ht[None, :] + (hb - ht)[None, :] * z[:, None]

    # ---- operator ----
    def _T(s, k, h):
        m = s.m
        if k == 0 and m.bosimsiz:
            T = m.K[0] * np.maximum(h.reshape(s.g.ny, s.g.nx) - m.z_tub, m.b_min)
        else:
            T = m.K[k] * m.b[k]
        return np.where(m.aktiv[k], T, 0.0)

    def _operator(s, H, aj):
        """Oqim operatori L (gorizontal + vertikal) va vertikal ozod had r."""
        g, nc, N = s.g, s.nc, s.N
        I, J, V = [], [], []
        idx = np.arange(nc).reshape(g.ny, g.nx)
        for k in range(N):
            T = s._T(k, H[k])
            off = k * nc
            for C, p, q in ((_yuz_otkazuvchanlik(T, g.dx, 1) * g.dy[:, None], idx[:, :-1], idx[:, 1:]),
                            (_yuz_otkazuvchanlik(T, g.dy, 0) * g.dx[None, :], idx[:-1, :], idx[1:, :])):
                C, p, q = C.ravel(), p.ravel() + off, q.ravel() + off
                I += [p, q, p, q]
                J += [p, q, q, p]
                V += [C, C, -C, -C]
        r = np.zeros(N * nc)
        A = s.A
        for k in range(N - 1):
            d = aj[k]
            t0, b0 = k * nc + np.arange(nc), (k + 1) * nc + np.arange(nc)
            I += [t0, t0, b0, b0]
            J += [t0, b0, t0, b0]
            V += [A * d["tt"], A * d["tb"], A * d["bt"], A * d["bb"]]
            r[t0] += A * d["rt"]
            r[b0] += A * d["rb"]
        L = sp.csr_matrix((np.concatenate(V), (np.concatenate(I), np.concatenate(J))),
                          shape=(N * nc, N * nc))
        return L, r

    # ---- bitta vaqt qadami ----
    def qadam(s, H0, t, tau, maxit=50, tol=1e-8):
        m, nc, N, A = s.m, s.nc, s.N, s.A
        AN = np.tile(A, N)
        if s.u[0] is None and any(Mk > 0 for Mk in m.M):
            s._ajratuvchi_boshlang(H0)
        aj = [s._ajratuvchi(k, tau) for k in range(N - 1)]
        h0 = np.concatenate(H0)
        Sv = np.concatenate([m.S[k].ravel() for k in range(N)])
        W = m.infiltratsiya(t + tau).ravel()
        Qv = np.zeros(N * nc)
        for w in m.quduqlar:
            Qv[w.qatlam * nc + w.j * s.g.nx + w.i] += qiymat(w.Q, t + tau)
        h = h0.copy()
        h[s.berk] = s.hfix
        free, fx = s.erkin, s.berk
        for it in range(maxit):
            Hk_lin = [h[k * nc:(k + 1) * nc].copy() for k in range(N)]
            L, r = s._operator(Hk_lin, aj)
            E, dE = m.buglanish(Hk_lin[0].reshape(s.g.ny, s.g.nx))
            E, dE = E.ravel(), dE.ravel()
            diag = Sv * AN / tau
            diag[:nc] += dE * A
            rhs = Sv * AN / tau * h0 + r - Qv
            rhs[:nc] += (W - E + dE * Hk_lin[0]) * A
            Mtx = (L + sp.diags(diag)).tocsr()
            Aff = Mtx[free][:, free]
            b = rhs[free] - Mtx[free][:, fx] @ s.hfix
            hn = h.copy()
            hn[free] = spla.spsolve(Aff.tocsc(), b)
            dmax = np.max(np.abs(hn - h)) if free.size else 0.0
            h = hn
            if not (m.bosimsiz or m.E0 > 0) or dmax < tol:
                break
        # yakuniy balans: oxirgi chiziqlashtirish bo'yicha diskret tenglamalar aniq bajariladi
        Hk = [h[k * nc:(k + 1) * nc] for k in range(N)]
        L, r = s._operator(Hk_lin, aj)
        Elin = (E + dE * (h[:nc] - Hk_lin[0])) * A
        dV_aqt = 0.0
        for k in range(N - 1):
            d = aj[k]
            if d.get("alpha") is None:
                continue
            ht, hb = Hk[k], Hk[k + 1]
            un = d["a"] + d["alpha"] * ht[None, :] + d["beta"] * hb[None, :]
            msk = s.qmask[k]
            dV_aqt += np.sum((m.Ss[k].ravel() * d["dl"] * A * (un - s.u[k]).sum(0))[msk])
            s.u[k] = np.where(msk[None, :], un, s.u[k])
        out_fix = (L @ h - r)[fx]
        bal = dict(
            t=t + tau,
            dV_qatlam=float(np.sum((Sv * AN * (h - h0))[free])),
            dV_ajratuvchi=float(dV_aqt),
            W=float(tau * np.sum((W * A)[free[free < nc]])),
            E=float(tau * np.sum(Elin[free[free < nc]])),
            Q=float(tau * np.sum(Qv[free])),
            chegara=float(tau * np.sum(out_fix)),
            iter=it + 1,
        )
        return Hk, bal

    def _yigindi(s, bal):
        kir = bal["W"] - bal["E"] - bal["Q"] + bal["chegara"]
        jam = bal["dV_qatlam"] + bal["dV_ajratuvchi"]
        shk = max(abs(bal["W"]) + abs(bal["E"]) + abs(bal["Q"]) + abs(bal["chegara"]), 1e-300)
        return jam - kir, (jam - kir) / shk

    def balans_xatosi(s, bal):
        """Qadamdagi suv balansi qoldig'i [m3] va nisbiy qiymati."""
        return s._yigindi(bal)

    def hisob(s, H0, t_oxir, tau0, osish=1.0, tau_max=None, kuzat=(), maxit=50, tol=1e-8):
        """Vaqt bo'yicha hisob. kuzat: [(qatlam, j, i), ...]. Qaytaradi: H, vaqtlar, kuzatuv, balanslar."""
        H = [np.asarray(h, float).ravel().copy() for h in H0]
        t, tau = 0.0, tau0
        tl, obs, bals = [0.0], [[H[k][j * s.g.nx + i] for (k, j, i) in kuzat]], []
        while t < t_oxir * (1 - 1e-12):
            tau = min(tau, t_oxir - t)
            H, bal = s.qadam(H, t, tau, maxit, tol)
            t += tau
            tl.append(t)
            obs.append([H[k][j * s.g.nx + i] for (k, j, i) in kuzat])
            bals.append(bal)
            tau *= osish
            if tau_max:
                tau = min(tau, tau_max)
        return H, np.array(tl), np.array(obs), bals

    def statsionar(s, H0, maxit=200, tol=1e-9):
        """Statsionar holat (sig'im hadlarisiz): juda katta vaqt qadami bilan bir necha qadam."""
        H = [np.asarray(h, float).ravel().copy() for h in H0]
        s._ajratuvchi_boshlang(H)
        for _ in range(5):
            H, _b = s.qadam(H, 0.0, 1e14, maxit, tol)
        s._ajratuvchi_boshlang(H)
        return H
