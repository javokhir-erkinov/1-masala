"""Tekshiruv uchun etalon yechimlar.

* Teys (1935) va Xantush–Jakob (1955) yechimlari.
* Ko'p qatlamli radial tizim: N ta bir jinsli suvli qatlam, ular orasida elastik sig'imli
  ajratuvchilar, o'zgarmas sarfli quduqlar. Laplas sohasida ajratuvchi tenglamasi aniq
  yechiladi (Hemker 1985, Hemker–Maas 1987 yondashuvi), suvli qatlamlar tizimi xos qiymatlar
  orqali Bessel funksiyalariga keltiriladi, vaqt sohasiga Stehfest usuli bilan qaytiladi.
"""
from math import factorial
import numpy as np
from scipy.special import exp1, k0
from scipy.integrate import quad


def teys(r, t, T, S, Q):
    u = r * r * S / (4 * T * np.asarray(t, float))
    return Q / (4 * np.pi * T) * exp1(u)


def xantush_W(u, beta):
    f = lambda y: np.exp(-y - beta * beta / (4 * y)) / y
    v, _ = quad(f, u, np.inf, limit=200)
    return v


def xantush_jakob(r, t, T, S, Q, c):
    """Ustki qatlam napori o'zgarmas, ajratuvchi sig'imsiz; c = b'/K' [sut]."""
    B = np.sqrt(T * c)
    return np.array([Q / (4 * np.pi * T) * xantush_W(r * r * S / (4 * T * tt), r / B)
                     for tt in np.atleast_1d(t)])


def _stehfest(Ns):
    V = np.zeros(Ns)
    h = Ns // 2
    for i in range(1, Ns + 1):
        s = 0.0
        for k in range((i + 1) // 2, min(i, h) + 1):
            s += (k ** h * factorial(2 * k) /
                  (factorial(h - k) * factorial(k) * factorial(k - 1) * factorial(i - k) * factorial(2 * k - i)))
        V[i - 1] = (-1) ** (i + h) * s
    return V


def _B(p, Kv, bq, Ss, N):
    B = np.zeros((N, N))
    for k in range(N - 1):
        c = Kv[k] / bq[k]
        if Ss[k] == 0.0:
            a = d = c
        else:
            lam = bq[k] * np.sqrt(p * Ss[k] / Kv[k])
            a = c * lam / np.tanh(lam)
            d = c * lam / np.sinh(lam) if lam < 700 else 0.0
        B[k, k] += a
        B[k + 1, k + 1] += a
        B[k, k + 1] -= d
        B[k + 1, k] -= d
    return B


def kop_qatlam_laplas(r, p, T, S, Kv, bq, Ss, Q):
    """Laplas sohasidagi napor pasayishi s(r, p), har bir qatlam uchun."""
    T, S, Q = map(lambda v: np.asarray(v, float), (T, S, Q))
    N = len(T)
    Dm = 1.0 / np.sqrt(T)
    As = Dm[:, None] * (np.diag(S * p) + _B(p, Kv, bq, Ss, N)) * Dm[None, :]
    lam, U = np.linalg.eigh(As)
    Kr = k0(r * np.sqrt(lam))
    return Dm * (U @ (Kr * (U.T @ (Dm * Q)))) / (2 * np.pi * p)


def kop_qatlam(r, t, T, S, Kv, bq, Ss, Q, Ns=12):
    """Vaqt sohasidagi napor pasayishi: (len(t), N) massiv."""
    V = _stehfest(Ns)
    t = np.atleast_1d(np.asarray(t, float))
    out = np.zeros((len(t), len(T)))
    for n, tt in enumerate(t):
        a = np.log(2.0) / tt
        for i in range(Ns):
            out[n] += V[i] * kop_qatlam_laplas(r, (i + 1) * a, T, S, Kv, bq, Ss, Q)
        out[n] *= a
    return out
