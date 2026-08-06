from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from app.database.db import Base


class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)

    description = Column(Text, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )