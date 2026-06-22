import fitz  # PyMuPDF
from pdfminer.high_level import extract_text
from langchain.document_loaders import PyPDFLoader
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_path, use_ocr=False):
    text = ""
    
    # Méthode 1: PDF texte standard (PyPDFLoader de LangChain)
    try:
        loader = PyPDFLoader(pdf_path)
        pages = loader.load_and_split()
        text = " ".join([page.page_content for page in pages])
    except:
        pass
    
    # Méthode 2: PDF scannés/Images (OCR avec PyMuPDF et Tesseract)
    if use_ocr or not text.strip():
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))
            text += pytesseract.image_to_string(img)
    
    return text

# Test
if __name__ == "__main__":
    text = extract_text_from_pdf("data/sample.pdf", use_ocr=True)
    print(text[:500])  # Affiche les 500 premiers caractères