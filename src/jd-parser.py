import os

from striprtf.striprtf import rtf_to_text

from preprocess import clean_text

job_folder = "data/jobs"

# Create output folder
output_folder = "data/jobs_text"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(job_folder):

    if filename.lower().endswith(".rtf"):

        file_path = os.path.join(
            job_folder,
            filename
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            rtf_content = file.read()

        # Convert RTF → plain text
        text = rtf_to_text(rtf_content)

        # Clean text
        cleaned_text = clean_text(text)

        print(f"\n----- {filename} -----\n")

        print(cleaned_text[:1000])

        # -----------------------------
        # SAVE CLEANED TEXT
        # -----------------------------

        output_path = os.path.join(
            output_folder,
            filename.replace(".rtf", ".txt")
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(cleaned_text)
