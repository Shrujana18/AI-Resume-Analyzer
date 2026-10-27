TOPICS = {
    "python": "Python fundamentals and practical projects",
    "sql": "SQL queries, joins, aggregation and database practice",
    "excel": "Excel data analysis, formulas and dashboards",
    "pandas": "Pandas data cleaning and analysis",
    "power bi": "Power BI dashboards and data visualization",
    "machine learning": "Machine learning fundamentals and model evaluation",
    "ml": "Machine learning fundamentals and model evaluation",
    "scikit-learn": "Scikit-learn model building and evaluation",
    "fastapi": "FastAPI basics and REST API development",
    "docker": "Docker fundamentals and containerizing applications",
    "deep learning": "Neural networks and deep learning basics",
    "llm": "Large Language Model fundamentals",
    "rag": "Retrieval-Augmented Generation fundamentals",
    "apis": "REST API concepts and practical API usage",
    "nlp": "Natural Language Processing fundamentals",
    "transformers": "Transformer architecture and NLP applications",
    "hugging face": "Hugging Face models and pipelines",
    "opencv": "OpenCV image processing",
    "cnn": "Convolutional Neural Networks",
    "yolo": "YOLO object detection fundamentals",
    "mlflow": "MLflow experiment tracking and model management",
    "cloud deployment": "Cloud deployment fundamentals"
}

def generate_roadmap(missing):
    roadmap = []
    for skill in missing[:4]:
        roadmap.append(TOPICS.get(skill.lower(), f"Learn {skill} and build a small project"))
    return roadmap
