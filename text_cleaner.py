import re

def clean_text(text):
    text = text.lower()
    # Preserve important technical forms such as c++, c#, and .net.
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s\+\#\.]", " ", text)
    return re.sub(r"\s+", " ", text).strip()
