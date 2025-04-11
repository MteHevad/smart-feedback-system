from fpdf import FPDF

def generate_pdf_report(content: str, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(190, 10, txt=content)
    pdf.output(filename)
