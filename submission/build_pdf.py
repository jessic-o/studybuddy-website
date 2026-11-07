#!/usr/bin/env python3
"""Build StudyBuddy finalized website submission PDF with screenshots."""

from pathlib import Path

from fpdf import FPDF
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SHOTS = ROOT / "screenshots"
OUT = ROOT / "submission" / "StudyBuddy_Finalized_Website.pdf"
URL = "https://jessic-o.github.io/studybuddy-website/"

PAGES = [
    ("Homepage", "index.png"),
    ("About Us", "about.png"),
    ("Product & Services", "product.png"),
    ("Pricing", "pricing.png"),
    ("Payment Portal (Checkout)", "checkout.png"),
    ("Testimonials / Reviews", "testimonials.png"),
    ("FAQ", "faq.png"),
    ("Contact Us", "contact.png"),
    ("Privacy Policy", "privacy.png"),
    ("Business Policies", "policies.png"),
]

CHECKLIST = [
    "Homepage",
    "Navigation Links",
    "Contact Us Page",
    "FAQ Page",
    "About Us Page",
    "Product and/or Services Pages",
    "Payment Portal",
    "Social Media Links",
    "Privacy Policy",
    "Business Policies",
    "Testimonials / Product Reviews Page",
    "Multimedia Content (pictures, video, ad space)",
]


class PDF(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", size=9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, f"Page {self.page_no()}", align="C")


def add_wrapped(pdf: PDF, text: str, size=11, style="", color=(20, 30, 40)):
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", style=style, size=size)
    pdf.set_text_color(*color)
    pdf.multi_cell(pdf.epw, 6, text)


def fit_image(pdf: PDF, path: Path, max_w=180, max_h=200):
    with Image.open(path) as im:
        w, h = im.size
    aspect = h / w
    display_w = max_w
    display_h = display_w * aspect
    if display_h > max_h:
        display_h = max_h
        display_w = display_h / aspect
    x = (pdf.w - display_w) / 2
    pdf.image(str(path), x=x, w=display_w)


def main():
    pdf = PDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=18)

    # Cover
    pdf.add_page()
    pdf.set_fill_color(7, 19, 31)
    pdf.rect(0, 0, 216, 70, "F")
    pdf.set_xy(15, 22)
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 12, "StudyBuddy")
    pdf.set_xy(15, 36)
    pdf.set_font("Helvetica", size=14)
    pdf.set_text_color(20, 196, 168)
    pdf.cell(0, 8, "Finalized Website Submission")

    pdf.set_xy(15, 85)
    add_wrapped(pdf, "Course assignment: Finalized Website", 12, "B")
    pdf.ln(2)
    add_wrapped(
        pdf,
        "Team: Heather Hoang, Leah Loza, Jessica O'Bonna, Erica Skelly",
        11,
    )
    pdf.ln(2)
    add_wrapped(pdf, "Business: StudyBuddy", 11)
    pdf.ln(4)
    add_wrapped(pdf, "Live website link:", 11, "B")
    pdf.ln(1)
    pdf.set_text_color(10, 122, 106)
    pdf.set_font("Helvetica", "U", 11)
    pdf.cell(0, 6, URL, link=URL)
    pdf.ln(10)
    add_wrapped(
        pdf,
        "This document includes screenshots of the finalized StudyBuddy website. "
        "The site covers the suggested checklist items listed below.",
        11,
    )
    pdf.ln(6)
    add_wrapped(pdf, "Final Website Checklist", 13, "B")
    pdf.ln(2)
    for item in CHECKLIST:
        add_wrapped(pdf, f"[x]  {item}", 11)

    pdf.ln(8)
    add_wrapped(pdf, "Repository (source):", 11, "B")
    pdf.ln(1)
    repo = "https://github.com/jessic-o/studybuddy-website"
    pdf.set_text_color(10, 122, 106)
    pdf.set_font("Helvetica", "U", 11)
    pdf.cell(0, 6, repo, link=repo)

    # Screenshot pages
    for title, filename in PAGES:
        path = SHOTS / filename
        if not path.exists():
            continue
        pdf.add_page()
        add_wrapped(pdf, title, 16, "B", (7, 19, 31))
        pdf.ln(2)
        add_wrapped(pdf, f"Screenshot from {URL}", 9, "", (90, 100, 110))
        pdf.ln(4)
        fit_image(pdf, path)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
