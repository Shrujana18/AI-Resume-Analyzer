import streamlit as st
import pandas as pd
import plotly.express as px
from resume_parser import extract_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import match_roles
from roadmap_generator import generate_roadmap

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer & Job Recommendation System")
st.caption("Educational guidance tool — match scores are estimates, not hiring decisions.")

uploaded = st.file_uploader("Upload your resume", type=["pdf", "docx"])

roles = pd.read_csv("data/job_roles.csv")
selected_role = st.selectbox("Select target role", roles["role"].tolist())

if uploaded:
    try:
        raw_text = extract_text(uploaded)
        cleaned = clean_text(raw_text)
        skills = extract_skills(cleaned)

        st.success(f"Resume loaded: {uploaded.name}")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Extracted Skills")
            if skills:
                st.write(", ".join(skills))
            else:
                st.warning("No skills from the current dictionary were detected.")

        results = match_roles(cleaned, roles)
        selected = results[results["role"] == selected_role].iloc[0]

        with col2:
            st.subheader("Target Role Match")
            st.metric("Match Score", f"{selected['score']:.0f}%")

        st.subheader("Recommended Roles")
        top3 = results.head(3)[["role", "score"]].copy()
        top3["score"] = top3["score"].round(1)
        st.dataframe(top3, use_container_width=True, hide_index=True)

        fig = px.bar(
            results.head(5),
            x="role",
            y="score",
            title="Top Job-Role Match Scores",
            range_y=[0, 100]
        )
        st.plotly_chart(fig, use_container_width=True)

        required = [x.strip().lower() for x in selected["required_skills"].split(",")]
        found = {x.lower() for x in skills}
        missing = [x for x in required if x not in found]
        found_target = [x for x in required if x in found]

        st.subheader(f"Skill Gap Analysis — {selected_role}")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Skills Found**")
            st.write(", ".join(found_target) if found_target else "None detected")
        with c2:
            st.markdown("**Missing / Weak Skills**")
            st.write(", ".join(missing) if missing else "No missing skills detected")

        st.subheader("Learning Roadmap")
        roadmap = generate_roadmap(missing)
        if roadmap:
            for i, item in enumerate(roadmap, 1):
                st.write(f"**Week {i}:** {item}")
        else:
            st.write("No roadmap needed based on the selected role.")

        st.subheader("Extracted Resume Text")
        with st.expander("Show text"):
            st.text_area("Resume text", cleaned, height=250)

        report = f"""AI RESUME ANALYZER REPORT

Resume: {uploaded.name}
Target role: {selected_role}
Match score: {selected['score']:.0f}%

Skills found:
{", ".join(skills)}

Missing skills:
{", ".join(missing) if missing else "None"}

Recommended roles:
{top3.to_string(index=False)}
"""
        st.download_button(
            "⬇️ Download Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Could not process the resume: {e}")
else:
    st.info("Upload a PDF or DOCX resume to begin.")
    st.markdown("### Project modules")
    st.write("1. Resume Upload  2. Text Extraction  3. Skill Extraction  4. Job Dataset  5. Matching  6. Skill Gap  7. Dashboard")
