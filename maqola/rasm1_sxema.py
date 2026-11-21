"""1-rasm: uch qatlamli tizim sxemasi (inglizcha va o'zbekcha)."""
import sys
UZ = len(sys.argv) > 1 and sys.argv[1] == "uz"
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(8, 4.6))
L = 10.0
qat = [(("1-suvli qatlam (bosimsiz)\n" if UZ else "Aquifer 1 (unconfined)\n") + "$K_1(x,y)$, $\\mu$", 6.6, 1.1, "#f3e3b3"),
       (("1-ajratuvchi: " if UZ else "Aquitard 1: ") + "$S'_{s,1}\\,\\partial_t u_1=K'_1\\,\\partial_\\zeta^2u_1$", 5.6, 1.0, "#c9b79c"),
       (("2-suvli qatlam (bosimli)\n" if UZ else "Aquifer 2 (confined)\n") + "$T_2(x,y)$, $S_2$", 4.0, 1.6, "#f3e3b3"),
       (("2-ajratuvchi: " if UZ else "Aquitard 2: ") + "$S'_{s,2}\\,\\partial_t u_2=K'_2\\,\\partial_\\zeta^2u_2$", 3.0, 1.0, "#c9b79c"),
       (("3-suvli qatlam (bosimli)\n" if UZ else "Aquifer 3 (confined)\n") + "$T_3(x,y)$, $S_3$", 1.4, 1.6, "#f3e3b3")]
for nom, y0, h, c in qat:
    hatch = "...." if ("Aquitard" in nom or "ajratuvchi" in nom) else None
    ax.add_patch(Rectangle((0, y0), L, h, fc=c, ec="k", lw=.8, hatch=hatch))
    ax.text(0.2, y0 + h / 2, nom, va="center", fontsize=8.5,
            bbox=dict(fc="white", ec="none", alpha=.85, pad=1.5))
ax.add_patch(Rectangle((0, 1.0), L, 0.4, fc="#888", ec="k", lw=.8))
ax.text(L / 2, 1.2, ("suv o‘tkazmaydigan asos" if UZ else "impermeable base"), ha="center", va="center", fontsize=8, color="w")
ax.plot([0, L], [7.7, 7.7], "k-", lw=1)
ax.plot([0, 3, 5, 7, L], [7.35, 7.3, 7.05, 7.3, 7.35], "b-", lw=1.2)
ax.text(6.2, 7.8, ("yer sathi $z_s$" if UZ else "ground surface $z_s$"), fontsize=8)
ax.text(8.3, 7.1, "$h_1$", color="b", fontsize=9)
for x in (1.5, 2.3):
    ax.annotate("", xy=(x, 7.75), xytext=(x, 8.3), arrowprops=dict(arrowstyle="->", color="tab:blue"))
ax.text(1.9, 8.4, "$W$", color="tab:blue", ha="center")
ax.annotate("", xy=(8.9, 8.3), xytext=(8.9, 7.75), arrowprops=dict(arrowstyle="->", color="tab:red"))
ax.text(8.9, 8.4, "$E(h_1)$", color="tab:red", ha="center")
ax.plot([5, 5], [4.2, 7.7], "k-", lw=2)
ax.add_patch(Rectangle((4.93, 4.1), 0.14, 1.4, fc="w", ec="k", lw=.8, hatch="||"))
ax.text(5.15, 4.6, ("quduq $Q_{2}$" if UZ else "well $Q_{2}$"), fontsize=8)
bb = dict(fc="white", ec="none", alpha=.9, pad=1)
for y, t in ((6.6, "$q_1^{+}$"), (5.6, "$q_1^{-}$"), (4.0, "$q_2^{+}$"), (3.0, "$q_2^{-}$")):
    ax.annotate("", xy=(7.4, y - 0.22), xytext=(7.4, y + 0.22), arrowprops=dict(arrowstyle="-|>", color="k"))
    ax.text(7.55, y, t, fontsize=9, va="center", bbox=bb)
for y, t in ((6.6, "$u_1=h_1$"), (5.6, "$u_1=h_2$"), (4.0, "$u_2=h_2$"), (3.0, "$u_2=h_3$")):
    ax.text(8.6, y, t, fontsize=8, va="center", bbox=bb)
ax.set_xlim(-0.1, L + 0.1); ax.set_ylim(0.9, 8.6); ax.axis("off")
fig.tight_layout(); fig.savefig("maqola/rasm1_sxema_uz.png" if UZ else "maqola/rasm1_sxema.png", dpi=250, metadata={"Software": None})
