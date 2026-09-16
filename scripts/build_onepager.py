# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase.pdfmetrics import stringWidth

OUT = "/home/user/Apex_Fleet_Consulting/Apex_Fleet_Consulting_One-Pager.pdf"

# ---- palette ----
NAVY      = HexColor("#0E2340")
NAVY_MID  = HexColor("#16335C")
STEEL     = HexColor("#4A6280")
ACCENT    = HexColor("#D97C1F")   # amber/orange, highway-safety adjacent
PALE      = HexColor("#F2F5F8")
PALE_BOX  = HexColor("#E9EEF3")
TEXT_DARK = HexColor("#1B2733")
TEXT_MUT  = HexColor("#5B6B7A")
WHITE     = HexColor("#FFFFFF")
RULE      = HexColor("#C9D3DC")

PAGE_W, PAGE_H = letter
MARGIN = 0.55 * inch
CONTENT_W = PAGE_W - 2 * MARGIN

c = canvas.Canvas(OUT, pagesize=letter)

def para(text, style_kwargs, width, x, y_top):
    style = ParagraphStyle('p', **style_kwargs)
    p = Paragraph(text, style)
    w, h = p.wrap(width, 1000)
    p.drawOn(c, x, y_top - h)
    return h

def center_text(text, x_center, y, font, size, color):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawCentredString(x_center, y, text)

# =========================================================
# HEADER BAND
# =========================================================
HEADER_H = 1.15 * inch
c.setFillColor(NAVY)
c.rect(0, PAGE_H - HEADER_H, PAGE_W, HEADER_H, stroke=0, fill=1)

# thin accent line at very top
c.setFillColor(ACCENT)
c.rect(0, PAGE_H - 5, PAGE_W, 5, stroke=0, fill=1)

c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 25)
c.drawString(MARGIN, PAGE_H - 0.52*inch, "APEX FLEET CONSULTING")

c.setFont("Helvetica", 11.5)
c.setFillColor(HexColor("#CBD8E6"))
c.drawString(MARGIN, PAGE_H - 0.78*inch, "Independent Fleet Maintenance Consulting for Mid-Sized Commercial Fleets")

c.setFont("Helvetica", 9)
c.setFillColor(HexColor("#9FB3C8"))
contact = "info@apexfleetconsulting.com      701-997-2739      www.apexfleetconsulting.com"
c.drawString(MARGIN, PAGE_H - 1.00*inch, contact)

# =========================================================
# POSITIONING SENTENCE
# =========================================================
y = PAGE_H - HEADER_H - 0.24*inch
intro = ('<font color="#0E2340"><b>Operators, not advisors.</b></font> '
         '<font color="#3C4C5C">We work exclusively with fleets running 50&#8211;500 vehicles, delivering '
         'operational playbooks &#8212; not strategy decks &#8212; with any conflicts disclosed in writing.</font>')
h = para(intro, dict(fontName="Helvetica", fontSize=10.5, leading=14.5, alignment=TA_LEFT), CONTENT_W, MARGIN, y)
y -= h + 0.30*inch

# =========================================================
# STAT CALLOUT ROW
# =========================================================
stats = [
    ("$50K–$150K", "Recoverable maintenance spend\ntypically identified per audit"),
    ("20–35%", "Lower per-vehicle maintenance\ncost within year one"),
    ("90 Days", "Typical payback on engagement\nfee via vendor savings"),
    ("$150K–$400K", "Typical annual savings on a\n$25K engagement"),
]
n = len(stats)
gap = 0.12*inch
box_w = (CONTENT_W - gap*(n-1)) / n
box_h = 1.08*inch
box_top = y

for i, (num, label) in enumerate(stats):
    bx = MARGIN + i*(box_w+gap)
    c.setFillColor(PALE_BOX)
    c.roundRect(bx, box_top-box_h, box_w, box_h, 4, stroke=0, fill=1)
    c.setFillColor(ACCENT)
    c.rect(bx, box_top-box_h, 3, box_h, stroke=0, fill=1)
    center_text(num, bx+box_w/2, box_top-0.42*inch, "Helvetica-Bold", 15.5, NAVY)
    # two-line label, centered
    lines = label.split("\n")
    ly = box_top-0.68*inch
    for ln in lines:
        center_text(ln, bx+box_w/2, ly, "Helvetica", 7.6, TEXT_MUT)
        ly -= 11.5

y = box_top - box_h - 0.34*inch

# =========================================================
# WHAT WE DO  (section heading)
# =========================================================
def section_heading(title, y):
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 12.5)
    c.drawString(MARGIN, y, title)
    tw = stringWidth(title, "Helvetica-Bold", 12.5)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(2)
    c.line(MARGIN, y-4, MARGIN+tw, y-4)
    return y - 0.24*inch

y = section_heading("WHAT WE DO", y)

services = [
    ("Fleet Maintenance Audit",
     "Quantifies spend drivers &#8212; PM compliance, downtime patterns, vendor pricing &#8212; and surfaces recoverable dollars in 2&#8211;3 weeks."),
    ("Mobile Maintenance Program Design",
     "Builds the mobile technician operation: coverage plans, dispatch workflows, truck setup, and an executable playbook."),
    ("Vendor Network Optimization",
     "Consolidates vendors, negotiates pricing, and builds a preferred network with consistent quality and cost control."),
    ("Fleet Technology Implementation",
     "Guides the full technology lifecycle &#8212; system assessment, vendor selection, implementation, and team adoption."),
    ("Fleet Operations Assessment",
     "Evaluates dispatch efficiency, coverage modeling, and workforce utilization, with a prioritized improvement roadmap."),
]

col_gap = 0.28*inch
col_w = (CONTENT_W - col_gap) / 2
row_h = 0.98*inch

positions = [
    (MARGIN, y),
    (MARGIN + col_w + col_gap, y),
    (MARGIN, y - row_h),
    (MARGIN + col_w + col_gap, y - row_h),
    (MARGIN, y - 2*row_h),
]

for (title, desc), (bx, by) in zip(services, positions):
    c.setFillColor(ACCENT)
    c.circle(bx+3, by-4, 2.2, stroke=0, fill=1)
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 10.3)
    c.drawString(bx+13, by, title)
    body = f'<font color="#5B6B7A">{desc}</font>'
    para(body, dict(fontName="Helvetica", fontSize=8.6, leading=11.6, alignment=TA_LEFT),
         col_w-13, bx+13, by-13)

y = y - 3*row_h + 0.30*inch

# =========================================================
# HOW IT WORKS
# =========================================================
y = section_heading("HOW IT WORKS", y)

phases = [
    ("1", "ASSESS", "Fleet Maintenance Audit quantifies where spend and downtime are actually coming from."),
    ("2", "OPTIMIZE", "Vendor, mobile-program, and technology work close the gaps the audit surfaces."),
    ("3", "SCALE", "Playbooks and benchmarks hand off to your team to run and sustain."),
]
pgap = 0.22*inch
pw = (CONTENT_W - 2*pgap) / 3
phase_top = y

for i, (num, label, desc) in enumerate(phases):
    px = MARGIN + i*(pw+pgap)
    c.setFillColor(NAVY)
    c.circle(px+9, phase_top-9, 9, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawCentredString(px+9, phase_top-12.3, num)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 9.7)
    c.drawString(px+24, phase_top-11.5, label)
    body = f'<font color="#5B6B7A">{desc}</font>'
    para(body, dict(fontName="Helvetica", fontSize=8.3, leading=11.2, alignment=TA_LEFT),
         pw, px, phase_top-22)
    if i < 2:
        c.setStrokeColor(RULE)
        c.setLineWidth(1)
        ax = px+pw+pgap/2
        c.line(ax-5, phase_top-9, ax+5, phase_top-9)

y = phase_top - 1.15*inch

# =========================================================
# WHO THIS IS FOR
# =========================================================
y = section_heading("WHO THIS IS FOR", y)
who = ('<font color="#3C4C5C">Fleet managers, directors of maintenance, and VPs of operations running '
       '<b>50&#8211;500 vehicles</b> across logistics &amp; delivery, construction &amp; transport, HVAC/plumbing/electrical, '
       'and utility/energy fleets &#8212; facing high maintenance costs, unpredictable downtime, low PM compliance, '
       'or vendor pricing with no benchmark.</font>')
h = para(who, dict(fontName="Helvetica", fontSize=9.2, leading=13.2, alignment=TA_LEFT), CONTENT_W, MARGIN, y)
y -= h + 0.45*inch

# =========================================================
# CTA FOOTER BAND (pinned near bottom)
# =========================================================
FOOTER_H = 0.95*inch
c.setFillColor(NAVY)
c.rect(0, 0, PAGE_W, FOOTER_H, stroke=0, fill=1)
c.setFillColor(ACCENT)
c.rect(0, FOOTER_H-3, PAGE_W, 3, stroke=0, fill=1)

BOOKING_URL = "https://outlook.office.com/book/ApexFleetConsulting2@apexfleetconsulting.com/"
WEBSITE_URL = "https://www.apexfleetconsulting.com"
EMAIL_ADDR = "info@apexfleetconsulting.com"

c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 13)
c.drawString(MARGIN, FOOTER_H-0.34*inch, "Ready to see what's recoverable in your fleet?")

# --- clickable booking CTA (bold line + subtext act as one link) ---
cta_y_top = FOOTER_H-0.60*inch
cta_y_bot = FOOTER_H-0.80*inch
c.setFont("Helvetica-Bold", 10.5)
c.setFillColor(ACCENT)
cta_text = "Book a 30-Minute Discovery Call  →"
c.drawString(MARGIN, cta_y_top, cta_text)
cta_w = stringWidth(cta_text, "Helvetica-Bold", 10.5)

c.setFont("Helvetica", 8.7)
c.setFillColor(HexColor("#CBD8E6"))
sub_text = "Click to schedule instantly online"
c.drawString(MARGIN, cta_y_bot, sub_text)
sub_w = stringWidth(sub_text, "Helvetica", 8.7)

# single link rect spanning both lines for an easy click target
c.linkURL(BOOKING_URL, (MARGIN-2, cta_y_bot-3, MARGIN+max(cta_w, sub_w)+4, cta_y_top+11),
          relative=0, thickness=0)

# --- clickable email + website, right-aligned ---
c.setFont("Helvetica", 8.3)
c.setFillColor(HexColor("#9FB3C8"))
email_y = FOOTER_H-0.60*inch
web_y = FOOTER_H-0.76*inch
c.drawRightString(PAGE_W-MARGIN, email_y, EMAIL_ADDR)
email_w = stringWidth(EMAIL_ADDR, "Helvetica", 8.3)
c.linkURL(f"mailto:{EMAIL_ADDR}",
          (PAGE_W-MARGIN-email_w-2, email_y-2, PAGE_W-MARGIN+2, email_y+9),
          relative=0, thickness=0)

phone_web = "701-997-2739  ·  www.apexfleetconsulting.com"
c.drawRightString(PAGE_W-MARGIN, web_y, phone_web)
web_label = "www.apexfleetconsulting.com"
web_label_w = stringWidth(web_label, "Helvetica", 8.3)
c.linkURL(WEBSITE_URL,
          (PAGE_W-MARGIN-web_label_w-2, web_y-2, PAGE_W-MARGIN+2, web_y+9),
          relative=0, thickness=0)

c.showPage()
c.save()
print("Saved:", OUT)
print("Space between 'who this is for' and footer band top:", y - FOOTER_H)
