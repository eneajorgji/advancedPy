import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates a PDF file that contains data about
    and the period of the ill.
    the flatmates such as their names, their due amount
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_1, flatmate_2, bill):
        flatmate_1_pay = str(round(flatmate_1.pays(bill, flatmate_2), 2))
        flatmate_2_pay = str(round(flatmate_2.pays(bill, flatmate_1), 2))

        pdf = FPDF(orientation="p", unit="pt", format="A4")
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=35, h=35)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times")
        pdf.cell(w=100, h=25, txt=flatmate_1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate_1_pay, border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate_2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate_2_pay, border=0, ln=1)

        # Change directory to files, generate and open the PDF