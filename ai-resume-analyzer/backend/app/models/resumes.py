from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.db import Base

class Resume(Base):
    __tablename__ = 'resumes'

    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    file_content = Column(String)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )