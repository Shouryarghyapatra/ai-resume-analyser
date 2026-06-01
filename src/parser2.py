import pdfplumber
from pdf2image import convert_from_path
import pytesseract

from src.preprocess import clean_text


def extract_resume_text(pdf_path):

    text = ""

    try:

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + " "

        if len(text.strip()) > 100:
            return clean_text(text)

        pages = convert_from_path(pdf_path)

        for page in pages:
            text += pytesseract.image_to_string(page)

        return clean_text(text)

    except Exception as e:

        return f"Error processing resume: {e}"
