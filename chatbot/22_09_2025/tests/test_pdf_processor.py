from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from unittest import TestCase

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from core.pdf_processor import PDFProcessor


class PDFProcessorTests(TestCase):
    def test_rejects_non_pdf_files(self):
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "notes.txt"
            path.write_text("hello", encoding="utf-8")

            with self.assertRaises(ValueError):
                PDFProcessor().extract_text(str(path))
