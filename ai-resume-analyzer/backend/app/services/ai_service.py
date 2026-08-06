import google.generativeai as genai
from app.config.settings import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

class AIService:

    @staticmethod
    def analyze_resume(text):
        model = genai.GenerativeModel(
            "gemini-3.5-flash"
        )

        prompt = f"""
            You are an expert technical recruiter.

            Analyze this resume.

            Resume:

            {text}


            Return:

            1. Overall score out of 100
            2. Technical skills
            3. Experience summary
            4. Strengths
            5. Missing skills
            6. Improvement suggestions
            7. Interview questions

            Return response in JSON format.
        """
        response = model.generate_content(prompt)
        return response.text