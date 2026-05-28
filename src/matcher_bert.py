import os

from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity

# Load Model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

resume_folder = "data/resumes_text"

job_folder = "data/jobs_text"

# -----------------------------
# LOAD JOB DESCRIPTIONS
# -----------------------------

job_data = []

for job_file in os.listdir(job_folder):

    if job_file.endswith(".txt"):

        path = os.path.join(
            job_folder,
            job_file
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read()

        job_data.append(
            (job_file, text)
        )

# -----------------------------
# MATCH RESUMES
# -----------------------------

for resume_file in os.listdir(
    resume_folder
):

    if resume_file.endswith(".txt"):

        path = os.path.join(
            resume_folder,
            resume_file
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            resume_text = file.read()

        # Resume Embedding
        resume_embedding = model.encode(
            resume_text
        )

        print(
            f"\n========== "
            f"{resume_file} "
            f"=========="
        )

        best_score = 0

        best_job = ""

        for job_file, jd_text in job_data:

            # JD Embedding
            jd_embedding = model.encode(
                jd_text
            )

            # Similarity
            similarity = cosine_similarity(
                [resume_embedding],
                [jd_embedding]
            )

            score = similarity[0][0]

            print(
                f"{job_file} "
                f"-> "
                f"{score:.2f}"
            )

            if score > best_score:

                best_score = score

                best_job = job_file

        print(
            f"\nBest Match: "
            f"{best_job} "
            f"({best_score:.2f})"
        )
