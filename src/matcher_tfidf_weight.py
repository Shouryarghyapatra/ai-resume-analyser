import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from section_parser import (
    extract_sections,
    create_weighted_text
)

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

        # -----------------------------
        # SECTION EXTRACTION
        # -----------------------------

        resume_sections = extract_sections(
            resume_text
        )

        weighted_resume = create_weighted_text(
            resume_sections
        )

        resume_data.append(
            (
                resume_file,
                weighted_resume
            )
        )

        documents.append(
            weighted_resume
        )

# -----------------------------
# LOAD JOB DESCRIPTIONS
# -----------------------------

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

        # -----------------------------
        # SECTION EXTRACTION
        # -----------------------------

        jd_sections = extract_sections(
            jd_text
        )

        weighted_jd = create_weighted_text(
            jd_sections
        )

        job_data.append(
            (
                job_file,
                weighted_jd
            )
        )

        documents.append(
            weighted_jd
        )

# -----------------------------
# GLOBAL TF-IDF
# -----------------------------

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,3)
)

vectorizer.fit(documents)

# -----------------------------
# MATCHING
# -----------------------------

for resume_file, resume_text in resume_data:

    print(
        f"\n========== "
        f"{resume_file} "
        f"=========="
    )

    best_score = 0

    best_job = ""

    # Resume Vector
    resume_vector = vectorizer.transform(
        [resume_text]
    )

    # -----------------------------
    # COMPARE WITH ALL JDs
    # -----------------------------

    for job_file, jd_text in job_data:

        # JD Vector
        jd_vector = vectorizer.transform(
            [jd_text]
        )

        # Cosine Similarity
        similarity = cosine_similarity(
            resume_vector,
            jd_vector
        )

        score = similarity[0][0]

        print(
            f"{job_file} "
            f"-> "
            f"{score:.2f}"
        )

        # Track Best Match
        if score > best_score:

            best_score = score

            best_job = job_file

    print(
        f"\nBest Match: "
        f"{best_job} "
        f"({best_score:.2f})"
    )
