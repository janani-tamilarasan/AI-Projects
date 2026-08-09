from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

from app.services.document_service import DocumentService
from app.rag.rag_graph import build_graph


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


class RetrievalRequest(BaseModel):

    question: str


graph = build_graph()


# -----------------------------
# UPLOAD
# -----------------------------

@router.post("/upload")
def upload(
    file: UploadFile = File(...)
):

    document_service = DocumentService(
        file
    )

    chunks = document_service.process_document()

    return {
        "filename": file.filename,
        "message": "Document processed successfully"
    }


# -----------------------------
# ASK QUESTION
# -----------------------------

@router.post("/retrieve")
def retrieve(
    request: RetrievalRequest
):

    result = graph.invoke({

        "question": request.question,

        "documents": [],

        "answer": ""
    })

    return {
        "question": request.question,
        "answer": result["answer"]
    }