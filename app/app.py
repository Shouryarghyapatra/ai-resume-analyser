import streamlit as st
import os
import sys
import numpy as np

sys.path.append(os.path.abspath("."))

from src.parser2 import extract_resume_text
from src.pipeline import (
    match_resume,
    match_resume_to_jd
)

st.set_page_config(
    page_title="AI Resume Analyser",
    layout="wide"
)

st.title("AI Resume Analyser")

st.write(
    "Upload your resume and evaluate its semantic alignment with job descriptions."
)

mode = st.radio(
    "Analysis Mode",
    [
        "Match Against JD Database",
        "Match Against Custom JD"
    ]
)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

jd_text = ""

if mode == "Match Against Custom JD":

    jd_file = st.file_uploader(
        "Upload Job Description (.txt)",
        type=["txt"]
    )

    jd_text = st.text_area(
        "Or Paste Job Description Here",
        height=250
    )

    if jd_file is not None:

        jd_text = jd_file.read().decode(
            "utf-8"
        )

        st.subheader(
            "Uploaded Job Description"
        )

        st.text_area(
            "JD Content",
            jd_text[:3000],
            height=250
        )

if uploaded_file is not None:

    os.makedirs(
        "temp",
        exist_ok=True
    )

    temp_path = os.path.join(
        "temp",
        uploaded_file.name
    )

    with open(
        temp_path,
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    st.success(
        "Resume uploaded successfully!"
    )

    with st.spinner(
        "Extracting resume text..."
    ):

        resume_text = extract_resume_text(
            temp_path
        )

    st.subheader(
        "Extracted Resume Text"
    )

    st.text_area(
        "Resume Content",
        resume_text[:3000],
        height=300
    )

    if mode == "Match Against JD Database":

        with st.spinner(
            "Analyzing resume..."
        ):

            results = match_resume(
                resume_text
            )

        st.subheader(
            "Semantic Match Analysis"
        )

        scores = [
            score
            for _, score in results
        ]

        mean_score = np.mean(
            scores
        )

        st.metric(
            label="Mean Semantic Similarity Score",
            value=f"{mean_score:.4f}"
        )

        if mean_score > -5:

            st.success(
                "Excellent semantic alignment with job descriptions."
            )

        elif mean_score > -7:

            st.info(
                "Strong semantic alignment with job descriptions."
            )

        elif mean_score > -8.5:

            st.warning(
                "Moderate semantic alignment with job descriptions."
            )

        else:

            st.error(
                "Weak semantic alignment with job descriptions."
            )

        st.subheader(
            "Top Matching Job Descriptions"
        )

        for rank, (
            jd_name,
            score
        ) in enumerate(
            results,
            start=1
        ):

            st.write(
                f"{rank}. {jd_name} → {score:.4f}"
            )

    else:

        if not jd_text.strip():

            st.warning(
                "Please upload or paste a Job Description."
            )

        else:

            with st.spinner(
                "Analyzing Resume vs Job Description..."
            ):

                score = match_resume_to_jd(
                    resume_text,
                    jd_text
                )

            st.subheader(
                "Resume vs Job Description Analysis"
            )

            st.metric(
                "Semantic Match Score",
                f"{score:.4f}"
            )

            if score > -5:

                st.success(
                    "Strong Match"
                )

            elif score > -7:

                st.info(
                    "Good Match"
                )

            elif score > -8.5:

                st.warning(
                    "Moderate Match"
                )

            else:

                st.error(
                    "Weak Match"
                )

            st.write(
                "The score represents the semantic similarity between the uploaded resume and the provided job description."
            )

