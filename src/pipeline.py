import os

from embedder import encode
from retriever import get_top_k
from reranker import rerank


# =============================
# CONFIG
# =============================

JOB_FOLDER = "data/jobs_text"
RESUME_FOLDER = "data/resumes_text"
TOP_K = 5


# =============================
# LOAD FILES
# =============================

def load_files(folder):

    texts = []
    names = []

    for file in os.listdir(folder):

        if file.endswith(".txt"):

            path = os.path.join(folder, file)

            with open(path, "r", encoding="utf-8") as f:

                text = f.read().strip()

            texts.append(text)
            names.append(file)

    return names, texts


jd_names, jd_texts = load_files(JOB_FOLDER)
resume_names, resume_texts = load_files(RESUME_FOLDER)


# =============================
# ENCODE ALL JDs (BI-ENCODER)
# =============================

jd_vectors = encode(jd_texts)


# =============================
# MAIN PIPELINE
# =============================

for i, resume_text in enumerate(resume_texts):

    resume_name = resume_names[i]

    print(f"\n========== {resume_name} ==========")


    # -----------------------------
    # Encode resume
    # -----------------------------

    resume_vec = encode([resume_text])[0]


    # -----------------------------
    # Retrieve Top-K JDs
    # -----------------------------

    top_k_idx, _ = get_top_k(
        resume_vec,
        jd_vectors,
        k=TOP_K
    )

    top_jd_texts = [jd_texts[j] for j in top_k_idx]
    top_jd_names = [jd_names[j] for j in top_k_idx]


    # -----------------------------
    # Cross-Encoder Reranking
    # -----------------------------

    rerank_results = rerank(
        resume_text,
        top_jd_texts
    )


    # -----------------------------
    # Map JD text → JD name
    # -----------------------------

    jd_map = dict(zip(top_jd_texts, top_jd_names))

    scored_results = []

    for jd_text, score in rerank_results:

        jd_name = jd_map.get(jd_text, "UNKNOWN")

        scored_results.append((jd_name, float(score)))


    # -----------------------------
    # Sort by raw score
    # -----------------------------

    scored_results.sort(key=lambda x: x[1], reverse=True)


    # -----------------------------
    # OUTPUT (RAW SCORES ONLY)
    # -----------------------------

    print("\nMatch strength is based on semantic similarity score (higher is better)\n")
    best = scored_results[0]

    for rank, (jd_name, score) in enumerate(scored_results, start=1):

        print(f"{jd_name} -> {score:.4f}")

    print(f"\nBest Match: {best[0]} ({best[1]:.4f})")
