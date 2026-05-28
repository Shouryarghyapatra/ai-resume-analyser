import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume_folder = "data/resumes_text"
job_folder = "data/jobs_text"

# -----------------------------
# STORE DOCUMENTS
# -----------------------------

documents = []

resume_data = []
job_data = []

# -----------------------------
# LOAD RESUMES
# -----------------------------

for resume_file in os.listdir(resume_folder):

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

            text = file.read()

        resume_data.append(
            (resume_file, text)
        )

        documents.append(text)

# -----------------------------
# LOAD JOB DESCRIPTIONS
# -----------------------------

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

        documents.append(text)

# -----------------------------
# GLOBAL TF-IDF
# -----------------------------

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,2)
)

vectorizer.fit(documents)

# -----------------------------
# MATCHING
# -----------------------------

for resume_file, resume_text in resume_data:

    print(f"\n========== {resume_file} ==========")

    best_score = 0
    best_job = ""

    resume_vector = vectorizer.transform([
        resume_text
    ])

    for job_file, job_text in job_data:

        job_vector = vectorizer.transform([
            job_text
        ])

        similarity = cosine_similarity(
            resume_vector,
            job_vector
        )

        score = similarity[0][0]

        print(
            f"{job_file} -> {score:.2f}"
        )

        if score > best_score:

            best_score = score
            best_job = job_file

    print(
        f"\nBest Match: "
        f"{best_job} "
        f"({best_score:.2f})"
    )
