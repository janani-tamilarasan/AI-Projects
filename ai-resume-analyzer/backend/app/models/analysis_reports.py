from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.db import Base

class AnalysisReport(Base):
    __tablename__ = 'analysis_reports'

    id = Column(Integer,primary_key=True)
    resume_id = Column(Integer,ForeignKey('resumes.id'))
    analysis = Column(String)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )