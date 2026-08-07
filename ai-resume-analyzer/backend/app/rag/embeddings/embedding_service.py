from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config.settings import GEMINI_API_KEY
from typing import List

class EmbeddingService:
    """
    Generates vector embeddings
    using Google Gemini embedding model.
    """

    def __init__(self):
        self.model = embeddings = GoogleGenerativeAIEmbeddings(
                model="gemini-embedding-2-preview",
                api_key = GEMINI_API_KEY
            )
    
    def create_embeddings(self, texts: List[str]) ->  List[List[float]]:
        embeddings = self.model.embed_documents(texts)

        return embeddings