from fastapi import APIRouter
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/available")
async def get_available_models():
    """Get list of available AI models"""
    return {
        "models": [
            {
                "name": "openai",
                "display_name": "OpenAI GPT-4",
                "variants": ["gpt-4", "gpt-3.5-turbo", "gpt-4-turbo-preview"]
            },
            {
                "name": "anthropic",
                "display_name": "Anthropic Claude",
                "variants": ["claude-3-opus", "claude-3-sonnet", "claude-3-haiku"]
            },
            {
                "name": "google",
                "display_name": "Google Gemini",
                "variants": ["gemini-pro", "gemini-pro-vision"]
            },
            {
                "name": "huggingface",
                "display_name": "HuggingFace Models",
                "variants": ["meta-llama/Llama-2-7b", "mistralai/Mistral-7B"]
            },
            {
                "name": "cohere",
                "display_name": "Cohere",
                "variants": ["command", "command-light"]
            }
        ]
    }


@router.get("/status/{model_name}")
async def get_model_status(model_name: str):
    """Get status of specific AI model"""
    return {
        "model": model_name,
        "status": "available",
        "response_time_ms": 1200
    }
