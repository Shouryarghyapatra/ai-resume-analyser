from pdf2image import convert_from_path
import pytesseract

from src.preprocess import clean_text


def extract_resume_text(pdf_path):

    text = ""

    try:

        pages = convert_from_path(pdf_path)

        for page in pages:

            extracted_text = pytesseract.image_to_string(page)

            text += extracted_text + " "

        cleaned_text = clean_text(text)

        return cleaned_text

    except Exception as e:

        return f"Error processing resume: {e}"
