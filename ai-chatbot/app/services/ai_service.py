import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

class AIService:

    @staticmethod
    def generate_response(message):
        model = genai.GenerativeModel(
            "gemini-3.5-flash"
        )

        response = model.generate_content(
            message
        )

        return response.text