from fastapi import FastAPI
from app.database.db import Base, engine
from app.models.users import User
from app.models.conversations import Conversation
from app.models.messages import Message
from app.api.chat import router


app = FastAPI(
    title="AI Chatbot API",
    version="1.0.0"
)
app.include_router(router)


@app.on_event("startup")
def startup():
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)


@app.get("/")
def home():

    return {
        "message":"AI Chatbot Running"
    }
