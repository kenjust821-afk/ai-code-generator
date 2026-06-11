from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter
import re


def highlight_code(code: str, language: str) -> str:
    """Highlight code using Pygments"""
    try:
        lexer = get_lexer_by_name(language.lower())
        formatter = HtmlFormatter(style='monokai', full=True)
        highlighted = highlight(code, lexer, formatter)
        return highlighted
    except Exception:
        # Fallback: return code as-is
        return f"<pre><code>{code}</code></pre>"


def validate_syntax(code: str, language: str) -> bool:
    """Basic syntax validation"""
    try:
        if language.lower() == "python":
            compile(code, '<string>', 'exec')
            return True
        elif language.lower() in ["javascript", "typescript"]:
            # Simple validation: check for matching braces
            return validate_braces(code)
        else:
            # For other languages, perform basic checks
            return validate_braces(code) and validate_quotes(code)
    except SyntaxError:
        return False


def validate_braces(code: str) -> bool:
    """Check for matching braces"""
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in code:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0


def validate_quotes(code: str) -> bool:
    """Check for matching quotes"""
    single_quotes = code.count("'")
    double_quotes = code.count('"')
    return single_quotes % 2 == 0 and double_quotes % 2 == 0


def get_language_prompt_template(language: str) -> str:
    """Get language-specific prompt template"""
    templates = {
        "python": "Generate clean, well-documented Python code following PEP 8 style guide. Include type hints where appropriate.",
        "javascript": "Generate modern JavaScript (ES6+) code with proper error handling and documentation.",
        "typescript": "Generate TypeScript code with proper type definitions and interfaces.",
        "java": "Generate Java code following Google Java Style Guide. Include proper class structure and documentation.",
        "cpp": "Generate C++ code with proper memory management and comments.",
        "go": "Generate Go code following Go best practices with proper error handling.",
        "rust": "Generate Rust code with proper error handling and memory safety.",
    }
    return templates.get(language.lower(), f"Generate {language} code with proper formatting and documentation.")
