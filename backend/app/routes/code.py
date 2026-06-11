from fastapi import APIRouter, HTTPException, UploadFile, File
from app.schemas.code import CodeRequest, CodeResponse, CodePreviewRequest
from app.services.code_generator import CodeGeneratorService
from app.utils.code_utils import validate_syntax, highlight_code
from typing import Optional
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
code_service = CodeGeneratorService()


@router.post("/generate", response_model=CodeResponse)
async def generate_code(request: CodeRequest):
    """Generate code based on prompt and language"""
    try:
        result = await code_service.generate_code(
            prompt=request.prompt,
            language=request.language,
            ai_model=request.ai_model,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            conversation_id=request.conversation_id
        )
        return result
    except Exception as e:
        logger.error(f"Code generation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/preview")
async def preview_code(request: CodePreviewRequest):
    """Preview code with syntax highlighting"""
    try:
        highlighted = highlight_code(request.code, request.language)
        is_valid = validate_syntax(request.code, request.language)
        
        return {
            "language": request.language,
            "code": request.code,
            "highlighted_html": highlighted,
            "syntax_valid": is_valid
        }
    except Exception as e:
        logger.error(f"Preview error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/validate")
async def validate_code(request: CodePreviewRequest):
    """Validate code syntax"""
    try:
        is_valid = validate_syntax(request.code, request.language)
        return {"language": request.language, "valid": is_valid}
    except Exception as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/download")
async def download_code(code: str, language: str, format: str = "raw", filename: str = "generated_code"):
    """Download code in various formats (raw, zip, pdf)"""
    try:
        from app.services.file_service import FileService
        file_service = FileService()
        
        result = file_service.prepare_download(
            code=code,
            language=language,
            format=format,
            filename=filename
        )
        return result
    except Exception as e:
        logger.error(f"Download error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/explain")
async def explain_code(request: CodePreviewRequest):
    """Get AI explanation of code"""
    try:
        explanation = await code_service.explain_code(
            code=request.code,
            language=request.language
        )
        return {"explanation": explanation, "language": request.language}
    except Exception as e:
        logger.error(f"Explanation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
