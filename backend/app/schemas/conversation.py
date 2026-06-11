from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MessageCreate(BaseModel):
    content: str
    role: str  # "user" or "assistant"
    message_type: Optional[str] = "text"


class MessageResponse(BaseModel):
    id: int
    conversation_id: int
    role: str
    content: str
    message_type: str
    created_at: datetime

    class Config:
        from_attributes = True


class ConversationCreate(BaseModel):
    title: str
    description: Optional[str] = None
    language: Optional[str] = "python"
    ai_model: Optional[str] = "openai"


class ConversationResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    language: str
    ai_model: str
    messages: Optional[list] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
