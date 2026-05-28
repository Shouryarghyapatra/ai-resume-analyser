# reranker.py

from sentence_transformers import CrossEncoder

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

def rerank(resume, jds):

    pairs = [
        (resume, jd) for jd in jds
    ]

    scores = model.predict(pairs)

    ranked = sorted(
        zip(jds, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked
