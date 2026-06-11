from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class CodeGeneration(Base):
    __tablename__ = "code_generations"
    
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)
    language = Column(String(50), nullable=False)
    prompt = Column(Text, nullable=False)
    generated_code = Column(Text, nullable=False)
    ai_model = Column(String(50), nullable=False)
    temperature = Column(Float, default=0.7)
    tokens_used = Column(Integer, default=0)
    execution_time = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
