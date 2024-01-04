from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

num_pages = 2

for p in range(0, num_pages):
    pdf.add_page()

    # groups of lines
    for i in range(21, 291, 30):
        for j in range(0, 18, 3):
            pdf.line(10, i+j, 200, i+j)


pdf.output("output2.pdf")
