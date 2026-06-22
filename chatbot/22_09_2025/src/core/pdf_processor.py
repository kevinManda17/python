from pathlib import Path

from pypdf import PdfReader


class PDFProcessor:
    def __init__(self):
        self.supported_formats = [".pdf"]

    def extract_text(self, file_path: str, method: str = "pypdf") -> str:
        path = Path(file_path)
        if path.suffix.lower() not in self.supported_formats:
            raise ValueError("Format non supporte. Utilise un fichier PDF.")

        try:
            if method == "pdfplumber":
                text = self._extract_with_pdfplumber(path)
            else:
                text = self._extract_with_pypdf(path)
        except Exception as exc:
            raise RuntimeError(f"Erreur d'extraction PDF: {exc}") from exc

        if not text.strip():
            raise ValueError("Aucun texte lisible n'a ete trouve dans ce PDF.")

        return text

    def _extract_with_pypdf(self, file_path: Path) -> str:
        reader = PdfReader(str(file_path))
        pages = [(page.extract_text() or "") for page in reader.pages]
        return "\n".join(pages)

    def _extract_with_pdfplumber(self, file_path: Path) -> str:
        import pdfplumber

        with pdfplumber.open(str(file_path)) as pdf:
            pages = [(page.extract_text() or "") for page in pdf.pages]
        return "\n".join(pages)
