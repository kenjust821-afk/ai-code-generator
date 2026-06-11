from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CodeRequest(BaseModel):
    prompt: str
    language: str
    conversation_id: Optional[int] = None
    ai_model: Optional[str] = None
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 2048


class CodeResponse(BaseModel):
    id: int
    conversation_id: int
    language: str
    prompt: str
    generated_code: str
    ai_model: str
    tokens_used: int
    execution_time: float
    created_at: datetime

    class Config:
        from_attributes = True


class CodePreviewRequest(BaseModel):
    code: str
    language: str


class CodePreviewResponse(BaseModel):
    language: str
    code: str
    highlighted_html: Optional[str] = None
    syntax_valid: bool


class CodeDownloadRequest(BaseModel):
    code: str
    language: str
    format: str  # "zip", "pdf", "raw"
    filename: str


class CodeExplainRequest(BaseModel):
    code: str
    language: str
