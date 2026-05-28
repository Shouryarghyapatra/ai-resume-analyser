import os

from striprtf.striprtf import rtf_to_text

from preprocess import clean_text

job_folder = "data/jobs"

for filename in os.listdir(job_folder):

    if filename.lower().endswith(".rtf"):

        file_path = os.path.join(job_folder, filename)

        with open(file_path, "r", encoding="utf-8") as file:

            rtf_content = file.read()

        # Convert RTF → plain text
        text = rtf_to_text(rtf_content)

        # Clean text
        cleaned_text = clean_text(text)

        print(f"\n----- {filename} -----\n")

        print(cleaned_text[:1000])
