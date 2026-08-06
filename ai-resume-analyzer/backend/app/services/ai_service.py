import google.generativeai as genai
from app.config.settings import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

class AIService:

    @staticmethod
    def analyze_resume(text, job_description):
        model = genai.GenerativeModel(
            "gemini-3.5-flash"
        )

        prompt = f"""
        You are an expert technical recruiter.

        Analyze the resume against the job description.

        Resume:
        {text}

        Job Description:
        {job_description}

        Respond ONLY with valid JSON.
        Do not include markdown.
        Do not wrap the JSON in ```.

        JSON format:

        {{
        "match_score": 0,
        "matched_skills": [],
        "missing_skills": [],
        "strengths": [],
        "suggestions": [],
        "interview_questions": []
        }}
        """
        response = model.generate_content(prompt)
        return response.text