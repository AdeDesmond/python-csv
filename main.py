import pandas as pd
from glob import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    file_name = Path(filepath).stem
    invoice_nr, date_from_file = file_name.split("-")
    pdf = FPDF(orientation="portrait", unit="mm", format="A4") #creating the pdf object
    pdf.add_page() # add a page
    
    pdf.set_font(family="Helvetica", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1) # add pdf contents onto the page using the cell
    
    pdf.set_font(family="Helvetica", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date_from_file}") # add pdf contents onto the page using the cell

    pdf.output(f"PDFS/{file_name}.pdf")
    
     