import streamlit as st
import os
import sys
import numpy as np

sys.path.append(os.path.abspath("."))

from src.parser2 import extract_resume_text
from src.pipeline import match_resume, match_resume_to_jd


st.set_page_config(
    page_title="AI Resume Analyser",
    layout="wide"
)

st.title("AI Resume Analyser")

st.write(
    "Upload your resume and evaluate its semantic alignment with job descriptions."
)

# ---------------- MODE SELECTION ---------------- #

mode = st.radio(
    "Analysis Mode",
    [
        "Match Against JD Database",
        "Match Against Custom JD"
    ]
)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# ---------------- CUSTOM JD INPUT ---------------- #

custom_jd = None

if mode == "Match Against Custom JD":
    custom_jd = st.text_area(
        "Paste your Job Description here",
        height=200
    )

# ---------------- MAIN LOGIC ---------------- #

if uploaded_file is not None:

    os.makedirs("temp", exist_ok=True)

    temp_path = os.path.join("temp", uploaded_file.name)

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully!")

    # ---------------- RESUME EXTRACTION ---------------- #

    try:
        with st.spinner("Extracting resume text..."):

            st.write("Starting PDF extraction...")

            resume_text = extract_resume_text(temp_path)

            st.write("PDF extraction completed")

            if resume_text.startswith("Error processing resume"):
                st.error(resume_text)
                st.stop()

    except Exception as e:
        st.error(f"Resume extraction failed: {e}")
        st.stop()

    st.subheader("Extracted Resume Preview")

    st.text_area(
        "Resume Content",
        resume_text[:3000],
        height=300
    )

    # ---------------- CUSTOM JD MODE ---------------- #

    if mode == "Match Against Custom JD":

        if custom_jd and custom_jd.strip():

            with st.spinner("Analyzing custom JD..."):

                score = match_resume_to_jd(resume_text, custom_jd)

            st.subheader("Match Score")

            st.metric(
                label="Semantic Similarity",
                value=f"{score:.4f}"
            )

            if score > -5:
                st.success("Excellent Match")

            elif score > -7:
                st.info("Strong Match")

            elif score > -8.5:
                st.warning("Moderate Match")

            else:
                st.error("Weak Match")

        else:
            st.warning("Please paste a Job Description.")

    # ---------------- JD DATABASE MODE ---------------- #

    else:

        with st.spinner("Analyzing against JD database..."):

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

        st.subheader("Top Matching Job Descriptions")

        for rank, (jd_name, score) in enumerate(results, start=1):

            st.write(f"{rank}. {jd_name} → {score:.4f}")
