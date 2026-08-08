from fastapi import FastAPI
from app.api.documents import router

app = FastAPI(
    title="AI Enterprise Knowledge Assistant",
    description="Enterprise RAG Application using LangChain, Llama and Qdrant",
    version="1.0.0"
)

app.include_router(router=router)

@app.get('/')
def health_check():
    return {
        "status": "running",
        "application": "AI Enterprise Knowledge Assistant"
    }