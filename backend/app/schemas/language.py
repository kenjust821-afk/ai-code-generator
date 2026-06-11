from pydantic import BaseModel
from typing import Optional


class LanguageResponse(BaseModel):
    id: int
    name: str
    display_name: str
    file_extension: str
    syntax_highlight: str
    hello_world: str
    keywords: str
    comment_syntax: str
    is_compiled: bool
    framework_examples: Optional[str] = None

    class Config:
        from_attributes = True
