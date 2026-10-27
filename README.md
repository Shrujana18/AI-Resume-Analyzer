# AI Resume Analyzer and Job Recommendation System

An educational NLP application that extracts resume text, identifies job-related skills, compares the resume with predefined job roles using TF-IDF and cosine similarity, recommends suitable roles, identifies skill gaps, and creates a basic learning roadmap.

## Features
- PDF and DOCX resume upload
- Text extraction and cleaning
- Controlled skill dictionary
- 7 job roles
- TF-IDF + cosine similarity matching
- Top 3 role recommendations
- Target-role skill-gap analysis
- Basic learning roadmap
- Streamlit dashboard
- Downloadable text analysis report

## Setup

### Windows PowerShell
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, run:
```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app.py
```

## Project Structure
- app.py
- resume_parser.py
- text_cleaner.py
- skill_extractor.py
- job_matcher.py
- roadmap_generator.py
- data/job_roles.csv
- data/skill_dictionary.csv
- tests/test_cases.csv

## Responsible AI
This system is for educational guidance, not automatic hiring or rejection. It should evaluate job-related information only and should not score protected personal attributes.

## Limitations
Keyword-based skill extraction can miss skills expressed using different wording. TF-IDF measures text similarity and does not understand every semantic relationship. Match scores are estimates.
