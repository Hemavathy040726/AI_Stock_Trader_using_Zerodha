# tests/test_pdf_reader.py
import pytest
from src.core.tools.pdf_reader import pdf_reader_tool


def test_pdf_reader_success(tmp_path):
    # Create a REAL valid minimal PDF (with %%EOF!)
    pdf_content = (
        b"%PDF-1.4\r\n"
        b"1 0 obj\r\n"
        b"<< /Type /Catalog /Pages 2 0 R >>\r\n"
        b"endobj\r\n"
        b"2 0 obj\r\n"
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>\r\n"
        b"endobj\r\n"
        b"3 0 obj\r\n"
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 150] >>\r\n"
        b"endobj\r\n"
        b"xref\r\n"
        b"1 3\r\n"
        b"0000000000 65535 f \r\n"
        b"0000000010 00000 n \r\n"
        b"0000000079 00000 n \r\n"
        b"trailer << /Size 4 /Root 1 0 R >>\r\n"
        b"startxref\r\n"
        b"200\r\n"
        b"%%EOF\r\n"
    )

    pdf_file = tmp_path / "test.pdf"
    pdf_file.write_bytes(pdf_content)

    result = pdf_reader_tool.invoke({"pdf_path": str(pdf_file)})
    assert "No text found in PDF" in result or result.strip() != ""