import os
import re
from pdf2image import convert_from_path
import pytesseract

resume_folder = "data/resumes"

# Cleaning function
def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^\w\s]', '', text)

    text = " ".join(text.split())

    return text


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
