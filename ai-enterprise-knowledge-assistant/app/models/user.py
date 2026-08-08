from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from database.db import Base


class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )