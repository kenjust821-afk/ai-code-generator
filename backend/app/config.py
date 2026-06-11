from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Database
    database_url: str = "sqlite:///./test.db"
    
    # Security
    secret_key: str = "your-super-secret-key-change-in-production"
    debug: bool = True
    
    # CORS
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    
    # AI Model API Keys
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    google_gemini_api_key: str = ""
    huggingface_api_key: str = ""
    cohere_api_key: str = ""
    
    # Default Model Configuration
    default_ai_model: str = "openai"
    default_model_name: str = "gpt-4"
    default_temperature: float = 0.7
    default_max_tokens: int = 2048
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
