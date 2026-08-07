from langchain_google_genai import ChatGoogleGenerativeAI

from app.config.settings import GEMINI_API_KEY
from app.rag.retriever.retriever_service import RetrieverService
from app.rag.prompts.resume_prompt import resume_analysis_prompt


class RAGService:


    def __init__(self):

        self.retriever = RetrieverService()


        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash",
            google_api_key=GEMINI_API_KEY,
            temperature=0.2
        )


    def analyze_resume(
        self,
        job_description: str
    ):


        print("RAG: Starting retrieval")


        documents = self.retriever.retrieve(
            job_description
        )


        print(
            "Documents:",
            len(documents)
        )


        context = "\n\n".join(
            [
                doc.page_content
                for doc in documents
            ]
        )


        prompt = resume_analysis_prompt.format(
            context=context,
            job_description=job_description
        )


        print("Calling Gemini")


        response = self.llm.invoke(
            prompt
        )


        print("Gemini completed")


        return str(response.content)