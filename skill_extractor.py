import pandas as pd
import re

SKILLS = pd.read_csv("data/skill_dictionary.csv")["skill"].dropna().tolist()

def extract_skills(text):
    found = []
    lower = text.lower()
    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"
        if re.search(pattern, lower):
            found.append(skill)
    return sorted(found)
