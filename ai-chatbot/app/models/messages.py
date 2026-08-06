from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db import Base

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id'))
    role = Column(String)
    content = Column(String)