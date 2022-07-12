import webbrowser
from fpdf import FPDF

class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due
    amount, and the period of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        total_days = flatmate1.days_in_house + flatmate2.days_in_house
        goodbye_str = "Thank you for staying with us, hope to see you again!"

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)

        pdf.set_font(family='Times', size=14, style='B')

        #insert Period lable and value
        pdf.cell(w=100, h=40, txt='Period', border=0)
        pdf.cell(w=130, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', size=12)

        #insert Name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=130, h=40, txt=flatmate1_pay, border=0, ln=1)

        #insert Name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=130, h=40, txt=flatmate2_pay, border=0, ln=1)

        #insert the total sum and days
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=100, h=100, txt=f"Total days: {total_days}", border=0)
        pdf.cell(w=130, h=100, txt=f"Sum: {bill.amount}", border=0, ln=1)

        #print good bye
        pdf.cell(w=0, h=80, txt=goodbye_str, border=0, align='R', ln=1)

        pdf.output(self.filename) # Generates the pdf to the folder
        webbrowser.open(self.filename) # Automatic opening pdf