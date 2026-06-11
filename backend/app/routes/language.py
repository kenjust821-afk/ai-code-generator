from fastapi import APIRouter, HTTPException
from app.services.language_service import LanguageService
from typing import List
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
lang_service = LanguageService()


@router.get("")
async def get_languages():
    """Get list of all supported languages"""
    try:
        languages = await lang_service.get_all_languages()
        return languages
    except Exception as e:
        logger.error(f"Error fetching languages: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{language_id}")
async def get_language(language_id: int):
    """Get language details"""
    try:
        language = await lang_service.get_language(language_id)
        if not language:
            raise HTTPException(status_code=404, detail="Language not found")
        return language
    except Exception as e:
        logger.error(f"Error fetching language: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/by-name/{language_name}")
async def get_language_by_name(language_name: str):
    """Get language by name"""
    try:
        language = await lang_service.get_language_by_name(language_name)
        if not language:
            raise HTTPException(status_code=404, detail="Language not found")
        return language
    except Exception as e:
        logger.error(f"Error fetching language: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
