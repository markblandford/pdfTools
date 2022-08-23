import sys
from modules.pdf_tools import PdfTools

def convert_to_text(file_name):
    pdf_tools = PdfTools()
    text = pdf_tools.convert_pdf_to_text(file_name)

    print(text)
    sys.exit(0)

def get_pdf_text_between_two_strings(file_name, str0, str1):
    pdf_tools = PdfTools()
    findings = pdf_tools.get_pdf_text_between_two_strings(file_name, str0, str1)

    if (findings):
        for t in findings:
            print(t)

        sys.exit(0)
    else:
        print("Nothing found between " + str0 + " : " + str1)
        sys.exit(-1)

if __name__ == "__main__":
    get_pdf_text_between_two_strings(sys.argv[1], sys.argv[2], sys.argv[3])
