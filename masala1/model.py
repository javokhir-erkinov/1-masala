"""Masala ma'lumotlari.

Qatlamlar yuqoridan pastga 0, 1, ..., N-1 raqamlanadi; k-ajratuvchi k- va (k+1)-suvli
qatlamlar orasida joylashgan. Barcha maydonlar (ny, nx) shaklidagi massiv yoki son.
Birliklar: m, sutka.
"""
from dataclasses import dataclass, field
from typing import Callable, Union
import numpy as np

Son = Union[float, Callable[[float], float]]


def qiymat(v, t):
    return v(t) if callable(v) else v


@dataclass
class Quduq:
    """Quduq: qatlam raqami, yacheyka (j, i), sarf Q > 0 suv olishni bildiradi [m3/sut]."""
    qatlam: int
    j: int
    i: int
    Q: Son


@dataclass
class Model:
    tor: object
    N: int = 3
    K: list = None            # suvli qatlamlar filtratsiya koeffitsiyenti K_k(x,y) [m/sut]
    b: list = None            # bosimli qatlam qalinligi b_k(x,y) [m]
    S: list = None            # elastik sig'im koeffitsiyenti S_k (yuqori qatlam uchun mu) [-]
    bosimsiz: bool = True     # 0-qatlam bosimsiz (T = K (h - z_tub))
    z_tub: object = 0.0       # bosimsiz qatlam tubi [m]
    z_yer: object = None      # yer sathi (bug'lanish uchun) [m]
    Kv: list = None           # ajratuvchining vertikal filtratsiya koeffitsiyenti K'_k(x,y) [m/sut]
    bq: list = None           # ajratuvchi qalinligi b'_k(x,y) [m]
    Ss: list = None           # ajratuvchining solishtirma elastik sig'imi S'_s [1/m]
    M: list = None            # ajratuvchi qatlamchalari soni (0 = sig'imsiz, kvazistatsionar)
    W: Son = 0.0              # infiltratsiya [m/sut], son, massiv yoki t funksiyasi
    E0: float = 0.0           # bug'lanish intensivligi yer sathida [m/sut]
    Delta: float = 3.0        # bug'lanish to'xtaydigan chuqurlik [m] (Averyanov)
    nE: float = 1.0           # Averyanov ko'rsatkichi
    aktiv: list = None        # soha shakli: True bo'lgan yacheykalar hisoblanadi
    hD: list = None           # berilgan napor (1-tur shart); np.nan bo'lsa erkin
    quduqlar: list = field(default_factory=list)
    b_min: float = 1e-3       # bosimsiz qatlamning eng kichik to'yingan qalinligi [m]

    def __post_init__(s):
        g = s.tor
        shp = (g.ny, g.nx)
        full = lambda v: np.broadcast_to(np.asarray(v, float), shp).copy()
        N, Nq = s.N, s.N - 1
        s.K = [full(v) for v in (s.K or [1.0] * N)]
        s.b = [full(v) for v in (s.b or [1.0] * N)]
        s.S = [full(v) for v in (s.S or [1e-4] * N)]
        s.Kv = [full(v) for v in (s.Kv or [1e-3] * Nq)]
        s.bq = [full(v) for v in (s.bq or [1.0] * Nq)]
        s.Ss = [full(v) for v in (s.Ss or [1e-5] * Nq)]
        s.M = list(s.M if s.M is not None else [10] * Nq)
        s.z_tub = full(s.z_tub)
        s.z_yer = full(s.z_yer if s.z_yer is not None else 1e30)
        s.aktiv = [np.broadcast_to(np.asarray(v, bool), shp).copy()
                   for v in (s.aktiv or [True] * N)]
        s.hD = [full(v) for v in (s.hD or [np.nan] * N)]

    # bug'lanish E(h) va uning hosilasi (S.F. Averyanov qonuni)
    def buglanish(s, h):
        if s.E0 == 0.0:
            z = np.zeros_like(h)
            return z, z
        d = s.z_yer - h
        x = np.clip(1.0 - d / s.Delta, 0.0, 1.0)
        E = s.E0 * x ** s.nE
        dE = np.where((d > 0) & (d < s.Delta), s.E0 * s.nE * x ** (s.nE - 1) / s.Delta, 0.0)
        return E, dE

    def infiltratsiya(s, t):
        return np.broadcast_to(np.asarray(qiymat(s.W, t), float), (s.tor.ny, s.tor.nx))
