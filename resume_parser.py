from pypdf import PdfReader
from docx import Document

def extract_text(uploaded_file):
    name = uploaded_file.name.lower()

    if name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if name.endswith(".docx"):
        document = Document(uploaded_file)
        return "\n".join(p.text for p in document.paragraphs)

    raise ValueError("Only PDF and DOCX resumes are supported.")
