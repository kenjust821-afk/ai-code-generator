from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Language(Base):
    __tablename__ = "languages"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    display_name = Column(String(100), nullable=False)
    file_extension = Column(String(20), nullable=False)
    syntax_highlight = Column(String(50), nullable=False)
    hello_world = Column(Text, nullable=False)
    keywords = Column(Text, nullable=False)  # JSON
    comment_syntax = Column(String(50), nullable=False)
    is_compiled = Column(Integer, default=0)  # Boolean: 0 or 1
    framework_examples = Column(Text, nullable=True)  # JSON
