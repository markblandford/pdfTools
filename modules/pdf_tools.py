from PyPDF2 import PdfReader

class PdfTools:
    def convert_pdf_to_text(self, file_name):
        reader = PdfReader(file_name)

        pdf_text = ""

        for p in reader.pages:
            pdf_text+=p.extract_text() or ""

        return pdf_text