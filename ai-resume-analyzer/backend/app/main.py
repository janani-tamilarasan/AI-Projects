from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.resume import router
from app.database.db import Base, engine
from app.models.resumes import Resume
from app.models.analysis_reports import AnalysisReport
from app.models.job_description import JobDescription

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://urban-fishstick-q6wvg7xw59gc4pg7-5173.app.github.dev"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup():
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer"}

@app.get("/test")
def home():
    return {"message": "AI Resume Analyzer test"}