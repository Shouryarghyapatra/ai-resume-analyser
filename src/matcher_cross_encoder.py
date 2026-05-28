import os

from sentence_transformers import CrossEncoder

# -----------------------------
# LOAD CROSS ENCODER MODEL
# -----------------------------

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

resume_folder = "data/resumes_text"

job_folder = "data/jobs_text"

# -----------------------------
# LOAD JOB DESCRIPTIONS
# -----------------------------

job_data = []

for job_file in os.listdir(job_folder):

    if job_file.endswith(".txt"):

        job_path = os.path.join(
            job_folder,
            job_file
        )

        with open(
            job_path,
            "r",
            encoding="utf-8"
        ) as file:

            jd_text = file.read()

        job_data.append(
            (
                job_file,
                jd_text
            )
        )

# -----------------------------
# MATCH RESUMES
# -----------------------------

for resume_file in os.listdir(
    resume_folder
):

    if resume_file.endswith(".txt"):

        resume_path = os.path.join(
            resume_folder,
            resume_file
        )

        with open(
            resume_path,
            "r",
            encoding="utf-8"
        ) as file:

            resume_text = file.read()

        print(
            f"\n========== "
            f"{resume_file} "
            f"=========="
        )

        best_score = -999

        best_job = ""

        # -----------------------------
        # COMPARE WITH ALL JDs
        # -----------------------------

        for job_file, jd_text in job_data:

            # Resume + JD pair
            pair = [
                (
                    resume_text,
                    jd_text
                )
            ]

            # Predict similarity
            score = model.predict(pair)[0]

            print(
                f"{job_file} "
                f"-> "
                f"{score:.2f}"
            )

            # Best Match
            if score > best_score:

                best_score = score

                best_job = job_file

        print(
            f"\nBest Match: "
            f"{best_job} "
            f"({best_score:.2f})"
        )
