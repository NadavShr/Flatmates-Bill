from Bill import Bill
from Flatmate import Flatmate
from PdfReport import PdfReport

amount = float(input("Please enter the bill amount: "))
period = input("What is the bill period? (E.g December 2021): ")

name1 = input("Please enter your name: ")
days_in_house1 = int(input(f"How many days did {name1} was in the house"
                           f" during {period}? "))
name2 = input("Please enter the second flatmate's name: ")
days_in_house2 = int(input(f"How many days did {name2} was in the house"
                           f" during {period}? "))

the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

pdf_report = PdfReport(filename=f"{period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)