from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str
    database_url: str
    groq_api_key: str
    qdrant_url: str
    qdrant_api_key: str | None = None
    redis_url: str


    class Config:
        env_file = ".env"


settings = Settings()