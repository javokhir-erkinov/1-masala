import numpy as np


class Tor:
    """To'g'ri burchakli (tenzor) to'r: x bo'yicha dx[i], y bo'yicha dy[j] qadamlar.
    Massivlar (ny, nx) shaklida saqlanadi."""

    def __init__(s, dx, dy, x0=0.0, y0=0.0):
        s.dx = np.asarray(dx, float)
        s.dy = np.asarray(dy, float)
        s.nx, s.ny = len(s.dx), len(s.dy)
        s.xc = x0 + np.cumsum(s.dx) - s.dx / 2
        s.yc = y0 + np.cumsum(s.dy) - s.dy / 2
        s.A = np.outer(s.dy, s.dx)          # yacheyka yuzasi
        s.nc = s.nx * s.ny

    @staticmethod
    def teleskop(L, d0, q):
        """Markaziy yacheyka d0, undan har ikki tomonga q marta o'suvchi qadamlar;
        markazdan chetgacha masofa kamida L."""
        h, x, d = [], d0 / 2, d0
        while x < L:
            d *= q
            h.append(d)
            x += d
        h = np.array(h)
        return np.concatenate([h[::-1], [d0], h])

    def eng_yaqin(s, x, y):
        return int(np.argmin(abs(s.yc - y))), int(np.argmin(abs(s.xc - x)))
