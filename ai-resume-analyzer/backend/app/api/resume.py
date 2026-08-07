from fastapi import APIRouter, UploadFile, File, Form
from app.services.pdf_service import PdfService
from app.utils.validator import validate_resume
from sqlalchemy.orm import Session
from app.database.db import engine
from app.services.resume_service import ResumeService
from app.services.analysis_service import AnalysisService
from app.services.job_service import JobService
from app.rag.chunking.chunk_service import ChunkService
from app.rag.vector_db.chroma_service import ChromaService
from app.rag.retriever.retriever_service import RetrieverService
from app.rag.rag_service import RAGService


router = APIRouter(
    prefix= '/resume',
    tags = ['Resume']
)

db = Session(engine)

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    ## 1. Load Document
    validate_resume(file)

    text = PdfService.extract_file(file.file)

    resume = ResumeService.save_resume(db, file.filename, text)

    ### Chunking
    chunks = ChunkService.create_chunks(text)

    ### Store to vector database
    chroma_service = ChromaService()
    chroma_service.store_chunks(
        chunks,
        resume.id
    )

    ### Save Job Description
    job_service = JobService.save_job_description(db, job_description)

    ## Analyze
    rag_service = RAGService()


    response = rag_service.analyze_resume(
        job_description
    )
    
    ##  save Analysis
    AnalysisService.save_analysis(db, resume.id, response)

    return {
        "response": response
    }