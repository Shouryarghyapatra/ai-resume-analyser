import os
import pdfplumber

from preprocess import clean_text

resume_folder = "data/resumes"

success_count = 0
failed_count = 0

for filename in os.listdir(resume_folder):

    if filename.endswith(".pdf"):

        pdf_path = os.path.join(resume_folder, filename)

        extracted_text = ""

        try:

            with pdfplumber.open(pdf_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        extracted_text += page_text + " "

            # Clean text
            cleaned_text = clean_text(extracted_text)

            print(f"\n----- {filename} -----\n")

            print(cleaned_text[:1000])

            # Success / failure tracking
            if cleaned_text.strip():

                success_count += 1

            else:

                failed_count += 1

                print(f"{filename} -> Empty or unreadable PDF")

        except Exception as e:

            failed_count += 1

            print(f"Error processing {filename}: {e}")

print(f"\nSuccessful: {success_count}")

print(f"Failed: {failed_count}")
