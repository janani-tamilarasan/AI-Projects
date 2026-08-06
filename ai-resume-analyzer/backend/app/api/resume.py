from fastapi import APIRouter, UploadFile, File, Form
from app.services.pdf_service import PdfService
from app.utils.validator import validate_resume
from app.services.ai_service import AIService
from sqlalchemy.orm import Session
from app.database.db import engine
from app.services.resume_service import ResumeService
from app.services.analysis_service import AnalysisService
from app.services.job_service import JobService

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
    validate_resume(file)

    text = PdfService.extract_file(file.file)

    resume = ResumeService.save_resume(db, file.filename, text)

    job = JobService.save_job_description(db, job_description)

    response = AIService.analyze_resume(text, job)

    AnalysisService.save_analysis(db, resume.id, response)

    return {
        "response": response
    }