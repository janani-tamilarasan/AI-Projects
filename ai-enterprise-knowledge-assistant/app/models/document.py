from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from datetime import datetime

from database.db import Base



class Document(Base):

    __tablename__ = "documents"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    filename = Column(
        String(255),
        nullable=False
    )


    file_path = Column(
        String(500),
        nullable=False
    )


    file_type = Column(
        String(100),
        nullable=False
    )


    uploaded_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )