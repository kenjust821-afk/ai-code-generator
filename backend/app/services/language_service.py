from typing import Optional, List
import logging

logger = logging.getLogger(__name__)

SUPPORTED_LANGUAGES = [
    {"id": 1, "name": "python", "display_name": "Python", "file_extension": ".py", "syntax_highlight": "python"},
    {"id": 2, "name": "javascript", "display_name": "JavaScript", "file_extension": ".js", "syntax_highlight": "javascript"},
    {"id": 3, "name": "typescript", "display_name": "TypeScript", "file_extension": ".ts", "syntax_highlight": "typescript"},
    {"id": 4, "name": "java", "display_name": "Java", "file_extension": ".java", "syntax_highlight": "java"},
    {"id": 5, "name": "cpp", "display_name": "C++", "file_extension": ".cpp", "syntax_highlight": "cpp"},
    {"id": 6, "name": "csharp", "display_name": "C#", "file_extension": ".cs", "syntax_highlight": "csharp"},
    {"id": 7, "name": "go", "display_name": "Go", "file_extension": ".go", "syntax_highlight": "go"},
    {"id": 8, "name": "rust", "display_name": "Rust", "file_extension": ".rs", "syntax_highlight": "rust"},
    {"id": 9, "name": "php", "display_name": "PHP", "file_extension": ".php", "syntax_highlight": "php"},
    {"id": 10, "name": "ruby", "display_name": "Ruby", "file_extension": ".rb", "syntax_highlight": "ruby"},
]


class LanguageService:
    async def get_all_languages(self) -> List[dict]:
        """Get all supported languages"""
        return SUPPORTED_LANGUAGES
    
    async def get_language(self, language_id: int) -> Optional[dict]:
        """Get language by ID"""
        for lang in SUPPORTED_LANGUAGES:
            if lang["id"] == language_id:
                return lang
        return None
    
    async def get_language_by_name(self, language_name: str) -> Optional[dict]:
        """Get language by name"""
        for lang in SUPPORTED_LANGUAGES:
            if lang["name"] == language_name.lower():
                return lang
        return None
