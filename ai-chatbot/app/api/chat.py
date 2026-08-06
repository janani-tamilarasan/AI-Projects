from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database.db import engine
from app.services.chat_service import ChatService
from app.responses.messages import MessageResponse
from app.services.ai_service import AIService

class ChatRequest(BaseModel):

    user_id:int
    message:str

router = APIRouter(
    prefix = '/chat',
    tags= ['Chat']
)

db = Session(engine)

@router.post('/')
def chat(request: ChatRequest):
    # 1. Create Converstation
    conversation = ChatService.create_conversations(db, request.user_id)

    # 2. Save user message
    message = ChatService.save_message(db,conversation.id,'user', request.message)

     # 3. AI response (temporary)

    ai_response = AIService.generate_response(request.message)

    # 4. Save AI message

    ChatService.save_message(

        db,

        conversation.id,

        "assistant",

        ai_response
    )

    return {
        'conversation_id': conversation.id,
         'response': ai_response
    }

@router.get("/{conversation_id}/history", response_model=list[MessageResponse])
def history(conversation_id: int):
    messages = ChatService.get_chat_history(db,conversation_id)

    return messages