"""Builds maqola1_hydrology.docx in an MDPI-like layout from maqola1_hydrology.md."""
import subprocess, pathlib, docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
D = pathlib.Path(__file__).resolve().parent
ref = D / "mdpi_ref.docx"
subprocess.run(f"pandoc --print-default-data-file reference.docx > '{ref}'", shell=True, check=True)
r = docx.Document(ref)
FONT = "Palatino Linotype"
for st in r.styles:
    try:
        f = st.font
    except AttributeError:
        continue
    f.name = FONT
    if f.color is not None and f.color.type is not None:
        f.color.rgb = RGBColor(0, 0, 0)
def set_(name, size, bold=None, align=None, before=0, after=0, italic=None):
    st = next(x for x in r.styles if x.name and x.name.lower() == name.lower()); st.font.size = Pt(size); st.font.name = FONT
    if bold is not None: st.font.bold = bold
    if italic is not None: st.font.italic = italic
    pf = st.paragraph_format; pf.space_before = Pt(before); pf.space_after = Pt(after)
    if align is not None: pf.alignment = align
for n in ("Normal", "Body Text", "First Paragraph", "Compact"):
    set_(n, 10, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=0)
    next(x for x in r.styles if x.name and x.name.lower() == n.lower()).paragraph_format.line_spacing = 1.0
for n in ("Body Text",):
    next(x for x in r.styles if x.name and x.name.lower() == n.lower()).paragraph_format.first_line_indent = Cm(0.75)
set_("Title", 18, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, before=12, after=12)
set_("Heading 2", 10, bold=True, before=12, after=3)
set_("Heading 3", 10, bold=False, italic=True, before=6, after=3)
set_("Image Caption", 9, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=6)
set_("Table Caption", 9, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=3)
for s in r.sections:
    s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    s.left_margin = s.right_margin = Cm(2.0); s.top_margin = s.bottom_margin = Cm(2.5)
from docx.oxml.ns import qn
for st in r.styles:
    el = getattr(st, "element", None)
    if el is None: continue
    rpr = el.find(qn("w:rPr"))
    if rpr is None: continue
    rf = rpr.find(qn("w:rFonts"))
    if rf is None: continue
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(a), FONT)
r.core_properties.author = "Javokhir Erkinov"; r.core_properties.last_modified_by = "Javokhir Erkinov"
r.save(ref)
import sys
NAME = sys.argv[1] if len(sys.argv) > 1 else "maqola1_hydrology"
out = D / (NAME + ".docx")
subprocess.run(["pandoc", str(D / (NAME + ".md")), "-f", "markdown+tex_math_dollars", "-o", str(out),
                "--reference-doc", str(ref), "--resource-path", str(D)], check=True)
d = docx.Document(out)
cp = d.core_properties
cp.author = cp.last_modified_by = "Javokhir Erkinov"; cp.comments = ""; cp.keywords = ""; cp.title = "A Mass-Conservative Numerical Model of Groundwater Flow in a Three-Aquifer System"
for t in d.tables:
    t.style = d.styles["Table"] if "Table" in [s.name for s in d.styles] else t.style
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in p.runs: run.font.size = Pt(9)
d.save(out)
print(out, "equations:", sum(1 for _ in d.element.body.iter("{http://schemas.openxmlformats.org/officeDocument/2006/math}oMath")))
