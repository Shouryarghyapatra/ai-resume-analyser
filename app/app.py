import streamlit as st
import os
import sys
import numpy as np

sys.path.append(os.path.abspath("."))

from src.parser2 import extract_resume_text
from src.pipeline import match_resume

st.set_page_config(
    page_title="AI Resume Analyser",
    layout="wide"
)

st.title("AI Resume Analyser")

st.write(
    "Upload your resume and evaluate its semantic alignment with job descriptions."
)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    os.makedirs("temp", exist_ok=True)

    temp_path = os.path.join(
        "temp",
        uploaded_file.name
    )

    with open(temp_path, "wb") as f:

        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully!")

    with st.spinner("Extracting resume text..."):

        resume_text = extract_resume_text(temp_path)

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text[:3000],
        height=300
    )

    with st.spinner("Analyzing resume..."):

        results = match_resume(resume_text)

    st.subheader("Semantic Match Analysis")

    scores = [score for _, score in results]

    mean_score = np.mean(scores)

    st.metric(
        label="Mean Semantic Similarity Score",
        value=f"{mean_score:.4f}"
    )

    if mean_score > -5:

        st.success("Excellent semantic alignment with job descriptions.")

    elif mean_score > -7:

        st.info("Strong semantic alignment with job descriptions.")

    elif mean_score > -8.5:

        st.warning("Moderate semantic alignment with job descriptions.")

    else:

        st.error("Weak semantic alignment with job descriptions.")

    st.write(
        "Higher semantic similarity scores indicate stronger contextual alignment between the resume and job descriptions."
    )

    st.subheader("Top Matching Job Descriptions")

    for rank, (jd_name, score) in enumerate(results, start=1):

        st.write(
            f"{rank}. {jd_name} → {score:.4f}"
        )
