import sys
from modules.pdf_tools import PdfTools

def convert_to_text(file_name):
    pdf_tools = PdfTools()
    text = pdf_tools.convert_pdf_to_text(file_name)

    print(text)
    sys.exit(0)

if __name__ == "__main__":
    convert_to_text(sys.argv[1])
