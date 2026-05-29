import os

from src.embedder import encode
from src.retriever import get_top_k
from src.reranker import rerank


JOB_FOLDER = "data/jobs_text"
TOP_K = 5


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

jd_vectors = encode(jd_texts)


def match_resume(resume_text):

    resume_vec = encode([resume_text])[0]

    top_k_idx, _ = get_top_k(
        resume_vec,
        jd_vectors,
        k=TOP_K
    )

    top_jd_texts = [
        jd_texts[j]
        for j in top_k_idx
    ]

    top_jd_names = [
        jd_names[j]
        for j in top_k_idx
    ]

    rerank_results = rerank(
        resume_text,
        top_jd_texts
    )

    jd_map = dict(
        zip(
            top_jd_texts,
            top_jd_names
        )
    )

    scored_results = []

    for jd_text, score in rerank_results:

        jd_name = jd_map.get(
            jd_text,
            "UNKNOWN"
        )

        scored_results.append(
            (
                jd_name,
                float(score)
            )
        )

    scored_results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return scored_results
