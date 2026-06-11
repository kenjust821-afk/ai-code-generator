# AI Code Generator

An intelligent code generation tool with ChatGPT-style interface supporting 50+ programming languages and multiple AI models.

## Features

✨ **Multi-Language Support**: 50+ programming languages including Python, JavaScript, Java, C++, Go, Rust, Kotlin, Swift, PHP, Ruby, C#, TypeScript, and more.

🤖 **Multiple AI Integrations**:
- OpenAI (GPT-4, GPT-3.5-turbo)
- Anthropic Claude (Claude 3 Opus, Sonnet, Haiku)
- Google Gemini
- HuggingFace Models
- Cohere
- Local LLM support

💬 **ChatGPT-Style Interface**: Conversational UI for intuitive code generation

📝 **Code Preview**: Real-time syntax-highlighted preview of generated code

📥 **Download Options**:
- Download as individual files
- Download as ZIP archive
- Export as PDF
- Copy to clipboard

🎨 **Advanced Features**:
- Language detection and validation
- Conversation history
- Code explanations
- Snippet refinement
- Multi-file project generation

## Tech Stack

**Backend:**
- Python 3.9+
- FastAPI (async web framework)
- Pydantic (data validation)
- SQLAlchemy (database ORM)
- Uvicorn (ASGI server)

**Frontend:**
- React 18+
- TypeScript
- Tailwind CSS
- Monaco Editor (VS Code-like code editor)
- Axios for API calls

**Database:**
- PostgreSQL or SQLite

## Project Structure

```
ai-code-generator/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   └── integrations/
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   └── App.tsx
│   ├── package.json
│   └── .env.example
└── docker-compose.yml
```

## Quick Start

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
cp .env.example .env
npm start
```

## Supported Languages (50+)

Python, JavaScript, TypeScript, Java, C, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala, Groovy, Haskell, Elixir, Clojure, Lua, R, MATLAB, Perl, Shell, Bash, PowerShell, SQL, HTML, CSS, SCSS, Less, XML, JSON, YAML, Markdown, Docker, Terraform, and more...

## License

MIT License - see LICENSE file for details
