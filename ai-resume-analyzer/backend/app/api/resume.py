from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import PdfService
from app.utils.validator import validate_resume
from app.services.ai_service import AIService

router = APIRouter(
    prefix= '/resume',
    tags = ['Resume']
)

@router.post('/upload')
async def upload_resume(file: UploadFile = File(...)):
    # Validation
    validate_resume(file)

    # Extract PDF text

    text = PdfService.extract_file(file.file)

    response = AIService.analyze_resume(text)

    return {
        "response": response,
    }