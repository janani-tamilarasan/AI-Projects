from fastapi import FastAPI
from app.api.resume import router
from app.database.db import Base, engine
from app.models.resumes import Resume
from app.models.analysis_reports import AnalysisReport
from app.models.job_description import JobDescription

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def startup():
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)

@app.get('/')
def home():
    return { "message": 'AI Resume Analyser'}