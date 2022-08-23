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
        expected = "page 0page 1"

        cut = PdfTools()
        actual = cut.convert_pdf_to_text("a-file.pdf")

        self.assertEqual(expected, actual)

    @patch("modules.pdf_tools.PdfTools.convert_pdf_to_text", return_value="some text from a pdf file")
    def test_get_pdf_text_between_two_strings_returns_the_expected_result(self, method):
        expected = [" from a pdf "]

        cut = PdfTools()
        actual = cut.get_pdf_text_between_two_strings("", "some text", "file")

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
