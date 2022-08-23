import unittest
from unittest.mock import MagicMock, patch

from modules.pdf_tools import PdfTools

class MockPdfReader:
    def __init__(self, file_name):
        mock_page_0 = MagicMock()
        mock_page_0.extract_text.return_value = "page 0"

        mock_page_1 = MagicMock()
        mock_page_1.extract_text.return_value = "page 1"

        self.pages = [ mock_page_0, mock_page_1 ]

class TestPdfTools(unittest.TestCase):
    @patch("modules.pdf_tools.PdfReader", MockPdfReader)
    def test_convert_pdf_to_text_converts_a_pdf_file_to_string(self):
        file_name = "a-file.pdf"
        expected = "page 0page 1"

        cut = PdfTools()
        actual = cut.convert_pdf_to_text(file_name)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
