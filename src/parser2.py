import os
from pdf2image import convert_from_path
import pytesseract

from preprocess import clean_text

resume_folder = "data/resumes"

for filename in os.listdir(resume_folder):

    if filename.endswith(".pdf"):

        pdf_path = os.path.join(resume_folder, filename)

        text = ""

        try:

            # Convert PDF pages to images
            pages = convert_from_path(pdf_path)

            # OCR each page
            for page in pages:

                extracted_text = pytesseract.image_to_string(page)

                text += extracted_text + " "

            # Clean text
            cleaned_text = clean_text(text)

            print(f"\n----- {filename} -----\n")

            print(cleaned_text[:1000])

        except Exception as e:

            print(f"Error processing {filename}: {e}")
