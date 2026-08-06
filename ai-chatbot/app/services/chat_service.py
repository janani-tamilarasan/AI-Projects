from app.models.conversations import Conversation
from app.models.messages import Message

class ChatService:

    @staticmethod
    def create_conversations(db,user_id):
        try:
            conversation = Conversation(user_id = user_id)
            db.add(conversation)
            db.commit()
            db.refresh(conversation)
            
            return conversation
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def save_message(db, conversation_id, role, content):
        try:
            message = Message(conversation_id=conversation_id, 
            role = role, content = content)
            db.add(message)
            db.commit()
            db.refresh(message)

            return message
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def get_chat_history(db, conversation_id):

        messages = (
            db.query(Message)
            .filter(
                Message.conversation_id == conversation_id
            )
            .order_by(Message.id)
            .all()
        )

        return messages