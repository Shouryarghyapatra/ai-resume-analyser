import os
from pdf2image import convert_from_path
import pytesseract

from preprocess import clean_text

resume_folder = "data/resumes"

# Create output folder
output_folder = "data/resumes_text"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(resume_folder):

    if filename.endswith(".pdf"):

        pdf_path = os.path.join(
            resume_folder,
            filename
        )

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

            # -----------------------------
            # SAVE CLEANED TEXT
            # -----------------------------

            output_path = os.path.join(
                output_folder,
                filename.replace(".pdf", ".txt")
            )

            with open(
                output_path,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(cleaned_text)

        except Exception as e:

            print(
                f"Error processing "
                f"{filename}: {e}"
            )
