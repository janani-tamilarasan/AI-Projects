from fastapi import APIRouter, UploadFile, File
from app.services.document_service import DocumentService


router = APIRouter(
    prefix= "/documents",
    tags= ['Documents']
)

@router.post('/upload')
def upload(file: UploadFile = File(...)):
   
    document_service = DocumentService(file)

    vector_store = document_service.process_document()


    


    ## Embeddings -> FaceEmbed
    ## Store to vector db
    ## Retrival
    ## PRompt
    ## LLm
    #  Store response
    return {
        "filename": file.filename,
        "message": "Document processed successfully"
    }