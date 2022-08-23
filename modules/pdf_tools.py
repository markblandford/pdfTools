import re
from PyPDF2 import PdfReader

class PdfTools:
    def convert_pdf_to_text(self, file_name):
        reader = PdfReader(file_name)

        pdf_text = ""

        for p in reader.pages:
            pdf_text+=p.extract_text() or ""

        return pdf_text

    def get_pdf_text_between_two_strings(self, file_name, str0, str1):
        pdf_text = self.convert_pdf_to_text(file_name)

        regex_search = "(?<=str0).*?(?=str1)".replace("str0", str0).replace("str1", str1)

        findings = re.findall(regex_search, pdf_text)

        return findings
