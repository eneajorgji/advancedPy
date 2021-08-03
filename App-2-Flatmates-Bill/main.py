from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person, who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate_2):
        weight = self.days_in_house / (self.days_in_house + flatmate_2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a PDF file that contains data about
    and the period of the ill.
    the flatmates such as their names, their due amount
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_1, flatmate_2, bill):
        pdf = FPDF(orientation="p", unit="pt", format="A4")
        pdf.add_page()

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Insert Period label and value
        pdf.cell(w=100, h=40, txt="Period: ", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate_1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate_1.pays(bill, flatmate_2)), border=1, ln=1)

        pdf.output(self.filename)


the_bill = Bill(820, "March 2021")
john = Flatmate("John", 28)
marry = Flatmate("Marry", 25)

print("John pays: ", john.pays(the_bill, marry))
print("Marry pay: ", marry.pays(the_bill, john))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate_1=john, flatmate_2=marry, bill=the_bill)
