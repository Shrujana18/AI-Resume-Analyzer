import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_roles(resume_text, roles_df):
    job_texts = roles_df["required_skills"].tolist()
    corpus = [resume_text] + job_texts

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten() * 100

    result = roles_df.copy()
    result["score"] = scores
    return result.sort_values("score", ascending=False).reset_index(drop=True)
