import os
import re
import pdfplumber

resume_folder = "data/resumes"

# Text cleaning function
def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^\w\s]', '', text)

    text = " ".join(text.split())

    return text


for filename in os.listdir(resume_folder):

    if filename.endswith(".pdf"):

        pdf_path = os.path.join(resume_folder, filename)

        extracted_text = ""

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    extracted_text += page_text + " "

        # Clean each resume individually
        cleaned_text = clean_text(extracted_text)

        print(f"\n----- {filename} -----\n")

        print(cleaned_text[:1000])
success_count = 0
failed_count = 0
if cleaned_text.strip():
    success_count += 1
else:
    failed_count += 1
print(f"Successful: {success_count}")
print(f"Failed: {failed_count}")
