from app.database.db import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Conversation(Base):
    __tablename__ = 'conversations'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

