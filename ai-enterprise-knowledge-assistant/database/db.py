from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config.settings import settings

print("SETTINGS TYPE:", type(settings))
print("DATABASE:", settings.database_url)

engine = create_engine(
    settings.database_url
)


Base = declarative_base()


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()