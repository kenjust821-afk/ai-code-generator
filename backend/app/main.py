from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config import settings
from app.routes import code, conversation, language, ai_model
import logging

logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Application startup")
    logger.info(f"Default AI Model: {settings.default_ai_model}")
    yield
    # Shutdown
    logger.info("Application shutdown")


app = FastAPI(
    title="AI Code Generator",
    description="Generate code for 50+ programming languages using AI",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(code.router, prefix="/api/code", tags=["Code"])
app.include_router(conversation.router, prefix="/api/conversations", tags=["Conversations"])
app.include_router(language.router, prefix="/api/languages", tags=["Languages"])
app.include_router(ai_model.router, prefix="/api/models", tags=["AI Models"])


@app.get("/")
async def root():
    return {
        "message": "Welcome to AI Code Generator API",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        workers=settings.workers if not settings.debug else 1
    )
