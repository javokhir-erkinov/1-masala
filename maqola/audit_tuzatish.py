"""Audit 2026-11-21: corrections applied to both drafts (EN, UZ)."""
import re
def fix(p, reps, common):
    s = open(p).read()
    for a, b in reps + common:
        assert a in s, (p, a[:60]); s = s.replace(a, b)
    open(p, "w").write(s)
common = [
 ("_{PQ}", "_{PN}"), ("\\sum_{Q}", "\\sum_{N}"), ("\\sum_Q", "\\sum_N"), ("T_Q", "T_N"), ("d_Q", "d_N"),
 ("h_Q^{n+1}", "h_N^{n+1}"),
 ("O(\\tau+h^2+\\delta^2)", "O(\\tau+\\Delta x^2+\\delta^2)"), ("O(h^2+\\delta^2+\\tau)", "O(\\Delta x^2+\\delta^2+\\tau)"),
 ("=s\\,u^n", "=\\sigma u^n"), ("s=S'_s\\delta/\\tau", "\\sigma=S'_s\\delta/\\tau"), ("\\mathfrak Ta=su^n", "\\mathfrak Ta=\\sigma u^n"),
 ("=s\\mathbb 1+", "=\\sigma\\mathbb 1+"), ("\\mathfrak T^{-1}s\\mathbb 1", "\\mathfrak T^{-1}\\sigma\\mathbb 1"),
 ("$D'=8$ m, $K'D'/S'=126$", "$b'=8$ m, $K'b'/S'=126$"), ("$kD=100$", "$T=100$"),
]
fix("maqola1_qoralama.md", [
 ("within 0.7%. It agrees", "within 0.74%. It agrees"),
 ("solutions within 0.7%. It reproduces", "solutions within 0.74%. It reproduces"),
 ("neighbour $Q$", "neighbour $N$"),
 ("the cell size $h$ and", "the cell size $\\Delta x$ and"),
 ("| Interpretation | $KD$ (m²/d)", "| Interpretation | $T$ (m²/d)"),
 ("Their averaged parameters are $KD=1800$", "Their averaged parameters are $T=1800$"),
 ("differs from the reference at the nearest grid radius ($r=10.69$) by at most 0.25% for $t\\ge10^{-3}$ (`tajribalar/t7_maas_mlu.py`). Larger differences occur only in the first time steps.",
  "differs from the reference at the nearest grid radius ($r=10.69$) by at most 0.31% in the pumped aquifer for $t\\ge10^{-3}$ and by at most 1.1% in the other aquifer for $t\\ge0.1$ (`tajribalar/t7_maas_mlu.py`). Larger relative differences occur only in the first time steps, where the drawdown in the other aquifer is still below 0.01."),
 ("($t_c=11$ and 32 d)", "($t_c=11$ and 26 d)"),
 ("a difference of 14% that is still present", "so storage reduces the decline by 14%, and the difference is still present"),
 ("the storage-free model overestimates the water-table decline in the unconfined aquifer by about 14% after one year.",
  "aquitard storage reduces the water-table decline in the unconfined aquifer after one year by about 14% (0.051 m against 0.060 m); a storage-free model overestimates this decline."),
 ("| $C_{PQ}$, $A_P$ | face conductance, cell area | m²/d, m² |", "| $C_{PQ}$, $A_P$ | face conductance between cells $P$ and $N$, cell area | m²/d, m² |\n| $\\Delta x$ | cell size | m |\n| $\\sigma$ | $S'_s\\delta/\\tau$ in the aquitard column system | m/d |"),
 ("- Karimov M., Yakhshiboev M., Rakhimova F., Yadgarova L. (2025). Modeling of groundwater flow in a multilayer porous medium based on a nonlinear mathematical model. Proc. SPIE 13662, 136620J.",
  "- Karimov M., Yakhshiboev M., Rakhimova F., Yadgarova L. (2025). Modeling of groundwater flow in a multilayer porous medium based on a nonlinear mathematical model. In: Fourth International Conference on Digital Technologies, Optics, and Materials Science (DTIEE 2025), Proc. SPIE 13662, p. 25."),
], common)
fix("maqola1_qoralama_uz.md", [
 ("yechimni 0,7% aniqlikda", "yechimni 0,74% aniqlikda"),
 ("yechimlarni 0,7% aniqlikda", "yechimlarni 0,74% aniqlikda"),
 ("qo‘shni $Q$", "qo‘shni $N$"),
 ("yacheyka o‘lchami $h$ va", "yacheyka o‘lchami $\\Delta x$ va"),
 ("| Talqin | $KD$, m²/sut", "| Talqin | $T$, m²/sut"),
 ("o‘rtacha parametrlari: $KD=1800$", "o‘rtacha parametrlari: $T=1800$"),
 ("To‘rning eng yaqin nuqtasida ($r=10{,}69$) $t\\ge10^{-3}$ da etalondan farq 0,25% dan oshmaydi (`tajribalar/t7_maas_mlu.py`). Kattaroq farqlar faqat birinchi vaqt qadamlarida uchraydi.",
  "To‘rning eng yaqin nuqtasida ($r=10{,}69$) etalondan farq quduqli qatlamda $t\\ge10^{-3}$ da 0,31% dan, ikkinchi qatlamda $t\\ge0{,}1$ da 1,1% dan oshmaydi (`tajribalar/t7_maas_mlu.py`). Nisbiy farq faqat birinchi vaqt qadamlarida, ikkinchi qatlamdagi pasayish hali 0,01 dan kichik bo‘lganda kattaroq."),
 ("($t_c=11$ va 32 sut)", "($t_c=11$ va 26 sut)"),
 ("14% lik bu farq hisob oxirigacha saqlanadi.", "Demak elastik suv berishi sath pasayishini 14% ga kamaytiradi va bu farq hisob oxirigacha saqlanadi."),
 ("hisobga olinmagan model bir yildan keyin bosimsiz qatlamdagi sath pasayishini taxminan 14% ga oshirib baholaydi.",
  "hisobga olinganda bir yildan keyin bosimsiz qatlamdagi sath pasayishi taxminan 14% ga kam bo‘ladi (0,051 m va 0,060 m); hisobga olinmagan model bu pasayishni oshirib baholaydi."),
 ("| $C_{PQ}$, $A_P$ | yacheykalararo o‘tkazuvchanlik, yacheyka yuzasi | m²/sut, m² |", "| $C_{PQ}$, $A_P$ | $P$ va $N$ yacheykalar orasidagi o‘tkazuvchanlik, yacheyka yuzasi | m²/sut, m² |\n| $\\Delta x$ | yacheyka o‘lchami | m |\n| $\\sigma$ | ajratuvchi ustuni tizimidagi $S'_s\\delta/\\tau$ | m/sut |"),
], common)
