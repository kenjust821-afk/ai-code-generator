from app.config import settings
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class AIClient:
    def __init__(self):
        self.default_model = settings.default_ai_model
        self.default_temperature = settings.default_temperature
    
    async def generate(
        self,
        prompt: str,
        model: Optional[str] = None,
        temperature: float = None,
        max_tokens: int = 2048
    ) -> dict:
        """Generate text using specified AI model"""
        model = model or self.default_model
        temperature = temperature or self.default_temperature
        
        try:
            if model == "openai":
                return await self._generate_openai(prompt, temperature, max_tokens)
            elif model == "anthropic":
                return await self._generate_anthropic(prompt, temperature, max_tokens)
            elif model == "google":
                return await self._generate_google(prompt, temperature, max_tokens)
            elif model == "huggingface":
                return await self._generate_huggingface(prompt, temperature, max_tokens)
            elif model == "cohere":
                return await self._generate_cohere(prompt, temperature, max_tokens)
            else:
                raise ValueError(f"Unsupported model: {model}")
        except Exception as e:
            logger.error(f"AI generation failed: {str(e)}")
            raise
    
    async def _generate_openai(self, prompt: str, temperature: float, max_tokens: int) -> dict:
        """Generate using OpenAI API"""
        try:
            import openai
            openai.api_key = settings.openai_api_key
            
            response = await openai.ChatCompletion.acreate(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return {
                "text": response.choices[0].message.content,
                "model": "openai",
                "tokens": response.usage.total_tokens
            }
        except Exception as e:
            logger.error(f"OpenAI error: {str(e)}")
            raise
    
    async def _generate_anthropic(self, prompt: str, temperature: float, max_tokens: int) -> dict:
        """Generate using Anthropic Claude API"""
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
            
            response = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return {
                "text": response.content[0].text,
                "model": "anthropic",
                "tokens": response.usage.input_tokens + response.usage.output_tokens
            }
        except Exception as e:
            logger.error(f"Anthropic error: {str(e)}")
            raise
    
    async def _generate_google(self, prompt: str, temperature: float, max_tokens: int) -> dict:
        """Generate using Google Gemini API"""
        try:
            import google.generativeai as genai
            genai.configure(api_key=settings.google_gemini_api_key)
            
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=max_tokens
                )
            )
            
            return {
                "text": response.text,
                "model": "google",
                "tokens": 0  # Google API doesn't return token count
            }
        except Exception as e:
            logger.error(f"Google Gemini error: {str(e)}")
            raise
    
    async def _generate_huggingface(self, prompt: str, temperature: float, max_tokens: int) -> dict:
        """Generate using HuggingFace Models"""
        try:
            from huggingface_hub import InferenceClient
            
            client = InferenceClient(
                model="HuggingFaceH4/zephyr-7b-beta",
                token=settings.huggingface_api_key
            )
            
            response = client.text_generation(
                prompt,
                temperature=temperature,
                max_new_tokens=max_tokens
            )
            
            return {
                "text": response,
                "model": "huggingface",
                "tokens": 0
            }
        except Exception as e:
            logger.error(f"HuggingFace error: {str(e)}")
            raise
    
    async def _generate_cohere(self, prompt: str, temperature: float, max_tokens: int) -> dict:
        """Generate using Cohere API"""
        try:
            import cohere
            co = cohere.Client(settings.cohere_api_key)
            
            response = co.generate(
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                model="command"
            )
            
            return {
                "text": response.generations[0].text,
                "model": "cohere",
                "tokens": 0
            }
        except Exception as e:
            logger.error(f"Cohere error: {str(e)}")
            raise
