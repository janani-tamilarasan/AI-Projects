from langchain_core.prompts import PromptTemplate


resume_analysis_prompt = PromptTemplate(

    input_variables=[
        "context",
        "job_description"
    ],

    template="""

You are an AI Resume Analyzer.

Analyze the candidate resume based ONLY on the provided context.

Resume Context:
{context}


Job Description:
{job_description}


Provide response in JSON format:

{{
    "match_score": number,
    "matched_skills": [],
    "missing_skills": [],
    "experience_summary": "",
    "recommendation": ""
}}

Do not assume information that is not present in the resume.

"""
)