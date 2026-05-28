# retriever.py

from sklearn.metrics.pairwise import cosine_similarity

def get_top_k(resume_vec, jd_vectors, k=5):

    scores = cosine_similarity(
        [resume_vec],
        jd_vectors
    )[0]

    top_k_idx = scores.argsort()[-k:][::-1]

    return top_k_idx, scores
