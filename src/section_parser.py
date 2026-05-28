import re

def extract_sections(text):

    text = text.lower()

    sections = {
        "skills": "",
        "projects": "",
        "experience": "",
        "education": ""
    }

    # -----------------------------
    # SKILLS
    # -----------------------------

    skills_match = re.search(
        r"skills(.*?)(projects|experience|education|certifications|$)",
        text,
        re.DOTALL
    )

    if skills_match:

        sections["skills"] = skills_match.group(1)

    # -----------------------------
    # PROJECTS
    # -----------------------------

    projects_match = re.search(
        r"projects(.*?)(experience|education|skills|certifications|$)",
        text,
        re.DOTALL
    )

    if projects_match:

        sections["projects"] = projects_match.group(1)

    # -----------------------------
    # EXPERIENCE
    # -----------------------------

    experience_match = re.search(
        r"experience(.*?)(projects|education|skills|certifications|$)",
        text,
        re.DOTALL
    )

    if experience_match:

        sections["experience"] = experience_match.group(1)

    # -----------------------------
    # EDUCATION
    # -----------------------------

    education_match = re.search(
        r"education(.*?)(experience|projects|skills|certifications|$)",
        text,
        re.DOTALL
    )

    if education_match:

        sections["education"] = education_match.group(1)

    return sections

def create_weighted_text(sections):

    weighted_text = ""

    # Skills → highest importance
    weighted_text += (
        sections["skills"] + " "
    ) * 3

    # Projects
    weighted_text += (
        sections["projects"] + " "
    ) * 2

    # Experience
    weighted_text += (
        sections["experience"] + " "
    ) * 2

    # Education
    weighted_text += (
        sections["education"] + " "
    )

    return weighted_text
