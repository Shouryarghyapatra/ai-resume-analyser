def create_weighted_text(sections):

    weighted_text = ""

    # Skills = highest importance
    weighted_text += (sections["skills"] + " ") * 3

    # Projects
    weighted_text += (sections["projects"] + " ") * 2

    # Experience
    weighted_text += (sections["experience"] + " ") * 2

    # Education
    weighted_text += (sections["education"] + " ")

    return weighted_text
