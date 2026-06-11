from app.integrations.ai_client import AIClient
from app.utils.code_utils import get_language_prompt_template
from typing import Optional
import logging
import time

logger = logging.getLogger(__name__)


class CodeGeneratorService:
    def __init__(self):
        self.ai_client = AIClient()
    
    async def generate_code(
        self,
        prompt: str,
        language: str,
        ai_model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        conversation_id: Optional[int] = None
    ) -> dict:
        """Generate code using specified AI model"""
        try:
            start_time = time.time()
            
            # Get language-specific prompt template
            template = get_language_prompt_template(language)
            enhanced_prompt = f"{template}\n\nUser Request: {prompt}"
            
            # Generate code
            result = await self.ai_client.generate(
                prompt=enhanced_prompt,
                model=ai_model,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            execution_time = time.time() - start_time
            
            return {
                "id": 1,
                "conversation_id": conversation_id or 1,
                "language": language,
                "prompt": prompt,
                "generated_code": result["text"],
                "ai_model": result["model"],
                "tokens_used": result.get("tokens", 0),
                "execution_time": execution_time,
                "created_at": "2024-01-01T00:00:00Z"
            }
        except Exception as e:
            logger.error(f"Code generation failed: {str(e)}")
            raise
    
    async def explain_code(self, code: str, language: str) -> str:
        """Get AI explanation of code"""
        try:
            prompt = f"Explain this {language} code:\n\n{code}"
            result = await self.ai_client.generate(
                prompt=prompt,
                temperature=0.5
            )
            return result["text"]
        except Exception as e:
            logger.error(f"Code explanation failed: {str(e)}")
            raise
    
    async def refine_code(self, code: str, language: str, refinement: str) -> str:
        """Refine generated code based on feedback"""
        try:
            prompt = f"Refine this {language} code: {refinement}\n\n{code}"
            result = await self.ai_client.generate(
                prompt=prompt,
                temperature=0.7
            )
            return result["text"]
        except Exception as e:
            logger.error(f"Code refinement failed: {str(e)}")
            raise
