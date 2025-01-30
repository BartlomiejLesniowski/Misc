from fpdf import FPDF
import pandas as pd

FILE = 'Daily Affirmations for Couples.xlsx'

df = pd.read_excel(FILE)

pdf = FPDF(format='A5')
pdf.add_page()
pdf.set_auto_page_break(auto=False)
pdf.add_font('DejaVu', '', 'DejaVuSans.ttf')
pdf.set_font('DejaVu', '', 10)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.cell(100, 10, text=row[0], center = 1, align='C')

pdf.output("output.pdf")
print('Success')