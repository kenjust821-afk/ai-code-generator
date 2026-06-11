# AI Code Generator - Comprehensive Installation & Usage Guide

## Complete Project Documentation

### Table of Contents
1. [Project Overview](#project-overview)
2. [System Requirements](#system-requirements)
3. [Installation Guide](#installation-guide)
4. [Configuration](#configuration)
5. [Running the Application](#running-the-application)
6. [API Documentation](#api-documentation)
7. [Frontend Components](#frontend-components)
8. [Supported Languages](#supported-languages)
9. [Deployment](#deployment)
10. [Troubleshooting](#troubleshooting)

---

## Project Overview

AI Code Generator is a full-stack web application that leverages artificial intelligence to generate code for over 50 programming languages. The application features:

- **ChatGPT-Style Interface**: Intuitive conversational UI
- **Multiple AI Models**: OpenAI, Claude, Gemini, HuggingFace, Cohere
- **50+ Language Support**: Python, JavaScript, Java, C++, Go, Rust, and more
- **Real-time Code Preview**: Syntax-highlighted code editor
- **Multiple Download Formats**: Raw files, ZIP archives, PDF documents
- **Code Validation**: Built-in syntax checking
- **Conversation History**: Save and manage code generation sessions

---

## System Requirements

### Minimum Requirements
- **Python**: 3.9 or higher
- **Node.js**: 16 or higher
- **RAM**: 4GB minimum
- **Disk Space**: 2GB

### Optional
- **Docker**: 20.10+
- **PostgreSQL**: 12+ (or use SQLite)
- **Git**: 2.30+

---

## Installation Guide

### Option 1: Docker Compose (Recommended)

#### Prerequisites
```bash
# Install Docker
https://docs.docker.com/get-docker/

# Install Docker Compose
https://docs.docker.com/compose/install/
```

#### Steps
```bash
# 1. Clone repository
git clone https://github.com/kenjust821-afk/ai-code-generator.git
cd ai-code-generator

# 2. Create environment file
cp backend/.env.example backend/.env

# 3. Edit .env with your API keys
nano backend/.env

# 4. Start all services
docker-compose up -d

# 5. View logs
docker-compose logs -f
```

Access points:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Database: localhost:5432 (PostgreSQL)

---

### Option 2: Local Development Setup

#### Backend Setup

```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create environment file
cp .env.example .env

# 6. Edit .env with your settings
# nano .env (or use your preferred editor)

# 7. Run migrations (optional)
alembic upgrade head

# 8. Start server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: http://localhost:8000

#### Frontend Setup

```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Create environment file
cp .env.example .env

# 4. Start development server
npm start
```

Frontend will be available at: http://localhost:3000

---

## Configuration

### Backend Configuration (.env)

```ini
# Database Configuration
DATABASE_URL=sqlite:///./test.db
# For PostgreSQL: postgresql://user:password@localhost/ai_code_gen

# Security
SECRET_KEY=your-super-secret-key-change-in-production
DEBUG=true

# CORS Configuration
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]

# AI Model API Keys
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here
GOOGLE_GEMINI_API_KEY=your-gemini-key-here
HUGGINGFACE_API_KEY=hf_your-key-here
COHERE_API_KEY=your-cohere-key-here

# Default Model Configuration
DEFAULT_AI_MODEL=openai
DEFAULT_MODEL_NAME=gpt-4
DEFAULT_TEMPERATURE=0.7
DEFAULT_MAX_TOKENS=2048

# Server Configuration
HOST=0.0.0.0
PORT=8000
WORKERS=4

# Logging
LOG_LEVEL=INFO
```

### Frontend Configuration (.env)

```ini
# API Configuration
REACT_APP_API_URL=http://localhost:8000
REACT_APP_API_TIMEOUT=30000
REACT_APP_ENV=development
```

### Getting API Keys

#### OpenAI
1. Go to https://platform.openai.com/signup
2. Create account
3. Go to API keys page
4. Create new secret key
5. Copy and paste into .env

#### Anthropic Claude
1. Visit https://console.anthropic.com/
2. Sign up or login
3. Go to API keys
4. Create new key
5. Copy to .env

#### Google Gemini
1. Visit https://makersuite.google.com/app/apikey
2. Create new API key
3. Copy to .env

#### HuggingFace
1. Go to https://huggingface.co/settings/tokens
2. Create new token
3. Copy to .env

#### Cohere
1. Visit https://dashboard.cohere.ai/
2. Sign up
3. Go to API keys
4. Create new key
5. Copy to .env

---

## Running the Application

### Using Docker Compose

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### Manual Start (Two Terminals)

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

### Testing the Setup

```bash
# Test backend health
curl http://localhost:8000/health

# Expected response:
# {"status": "healthy"}

# Access API documentation
# Open: http://localhost:8000/docs
```

---

## API Documentation

### Base URL
```
http://localhost:8000/api
```

### Code Generation

#### Generate Code
```http
POST /code/generate
Content-Type: application/json

{
  "prompt": "Create a function that calculates factorial",
  "language": "python",
  "ai_model": "openai",
  "temperature": 0.7,
  "max_tokens": 2048
}
```

**Response:**
```json
{
  "id": 1,
  "conversation_id": 1,
  "language": "python",
  "prompt": "Create a function that calculates factorial",
  "generated_code": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)",
  "ai_model": "openai",
  "tokens_used": 150,
  "execution_time": 2.5,
  "created_at": "2024-01-01T00:00:00Z"
}
```

#### Validate Code
```http
POST /code/validate
Content-Type: application/json

{
  "code": "def hello():\n    print('Hello, World!')",
  "language": "python"
}
```

**Response:**
```json
{
  "language": "python",
  "valid": true
}
```

#### Preview Code
```http
POST /code/preview
Content-Type: application/json

{
  "code": "def hello():\n    print('Hello')",
  "language": "python"
}
```

**Response:**
```json
{
  "language": "python",
  "code": "def hello():\n    print('Hello')",
  "highlighted_html": "<pre>...</pre>",
  "syntax_valid": true
}
```

#### Explain Code
```http
POST /code/explain
Content-Type: application/json

{
  "code": "def factorial(n):\n    return 1 if n <= 1 else n * factorial(n-1)",
  "language": "python"
}
```

**Response:**
```json
{
  "explanation": "This is a recursive function that calculates the factorial...",
  "language": "python"
}
```

### Conversations

#### Create Conversation
```http
POST /conversations
Content-Type: application/json

{
  "title": "Python Web App",
  "description": "Building a Flask application",
  "language": "python",
  "ai_model": "openai"
}
```

#### Get All Conversations
```http
GET /conversations
```

#### Get Conversation Details
```http
GET /conversations/{id}
```

#### Add Message to Conversation
```http
POST /conversations/{id}/messages
Content-Type: application/json

{
  "content": "Generate a Flask route for user login",
  "role": "user",
  "message_type": "text"
}
```

### Languages

#### Get All Languages
```http
GET /languages
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "python",
    "display_name": "Python",
    "file_extension": ".py",
    "syntax_highlight": "python"
  },
  ...
]
```

#### Get Specific Language
```http
GET /languages/{id}
```

#### Get Language by Name
```http
GET /languages/by-name/{name}
```

### AI Models

#### Get Available Models
```http
GET /models/available
```

**Response:**
```json
{
  "models": [
    {
      "name": "openai",
      "display_name": "OpenAI GPT-4",
      "variants": ["gpt-4", "gpt-3.5-turbo"]
    },
    ...
  ]
}
```

#### Check Model Status
```http
GET /models/status/{model_name}
```

---

## Frontend Components

### Main Components

#### App.tsx
- Main application component
- Manages conversation state
- Handles message sending

#### ChatInterface.tsx
- Displays conversation messages
- Input area for user prompts
- Real-time message display

#### CodeEditor.tsx
- Monaco Editor integration
- Code display and highlighting
- Copy to clipboard functionality

#### CodePreview.tsx
- Code validation display
- Syntax checking feedback
- Status indicators

#### LanguageSelector.tsx
- Dropdown for 50+ languages
- Easy language switching
- Default language selection

#### ModelSelector.tsx
- AI model selection
- All 5 models available
- Easy model switching

#### FileDownload.tsx
- Download as raw file
- Download as ZIP archive
- Download as PDF

---

## Supported Languages (50+)

### Web Development
- JavaScript
- TypeScript
- HTML
- CSS
- SCSS
- Less
- PHP
- Dart

### Backend
- Python
- Java
- Go
- Rust
- Ruby
- C#
- Kotlin
- Scala

### Systems Programming
- C
- C++
- Rust
- Go
- Assembly

### Data Science
- Python
- R
- Julia
- MATLAB

### DevOps
- Docker
- Terraform
- Kubernetes
- Bash
- PowerShell

### Data Formats
- JSON
- XML
- YAML
- TOML
- Protocol Buffers
- Avro
- Thrift

### Functional Languages
- Haskell
- Lisp
- Clojure
- Elixir
- Erlang
- OCaml
- Racket
- Scheme

### Others
- SQL
- GraphQL
- Markdown
- Lua
- Perl
- Groovy
- Scala
- Swift
- Fortran
- COBOL

---

## Deployment

### Heroku Deployment

```bash
# 1. Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# 2. Login
heroku login

# 3. Create app
heroku create your-app-name

# 4. Set environment variables
heroku config:set OPENAI_API_KEY=sk-...
heroku config:set ANTHROPIC_API_KEY=sk-ant-...
# ... (set all required keys)

# 5. Deploy
git push heroku main
```

### AWS Deployment

#### Backend (EC2/App Runner)
```bash
# Using AWS App Runner
aws apprunner create-service \
  --service-name ai-code-generator \
  --source-configuration RepositoryType=GITHUB,ImageRepository={ImageIdentifier=your-image}
```

#### Frontend (S3 + CloudFront)
```bash
# Build frontend
cd frontend
npm run build

# Upload to S3
aws s3 sync build/ s3://your-bucket-name/

# Create CloudFront distribution
aws cloudfront create-distribution \
  --origin-domain-name your-bucket-name.s3.amazonaws.com
```

### Google Cloud Run

```bash
# Backend
cd backend
gcloud run deploy ai-code-generator \
  --source . \
  --platform managed \
  --region us-central1 \
  --set-env-vars OPENAI_API_KEY=sk-...

# Frontend
cd ../frontend
npm run build
gcloud app deploy
```

---

## Troubleshooting

### Common Issues

#### 1. Backend won't start

**Error:** `ModuleNotFoundError: No module named 'app'`

**Solution:**
```bash
cd backend
export PYTHONPATH="${PYTHONPATH}:."
uvicorn app.main:app --reload
```

#### 2. API Key not working

**Error:** `Unauthorized` or `Invalid API key`

**Solution:**
- Check API key is correct
- Verify API key has necessary permissions
- Check API key hasn't expired
- Regenerate key if needed

#### 3. Frontend can't connect to backend

**Error:** `CORS error` or `Failed to fetch`

**Solution:**
Ensure backend `.env` includes frontend URL:
```ini
CORS_ORIGINS=["http://localhost:3000"]
```

#### 4. Database connection error

**Error:** `Can't connect to database`

**Solution:**
```bash
# For SQLite
# Ensure directory exists
mkdir -p backend/data

# For PostgreSQL
# Check PostgreSQL is running
psql -U postgres -c "SELECT 1"
```

#### 5. Code generation timeout

**Error:** `Request timeout`

**Solution:**
- Reduce `max_tokens` in request
- Check API rate limits
- Increase timeout in frontend `.env`:
```ini
REACT_APP_API_TIMEOUT=60000
```

### Debugging

#### Check Backend Logs
```bash
# In backend terminal, look for errors
# Or check container logs
docker-compose logs backend
```

#### Check Frontend Logs
```bash
# Open browser console (F12)
# Check Network tab for API errors
```

#### Test API Endpoints
```bash
# Using curl
curl -X POST http://localhost:8000/api/code/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello world", "language": "python"}'

# Using Postman
# Import from http://localhost:8000/docs
```

---

## Performance Optimization

### Backend
- Use connection pooling for database
- Implement caching for language definitions
- Enable gzip compression
- Use async/await for I/O operations

### Frontend
- Code splitting with React.lazy()
- Image optimization
- Minimize bundle size
- Enable production builds

---

## Security Considerations

1. **Never commit API keys** - Use .env files
2. **Validate all inputs** - Use Pydantic schemas
3. **Rate limiting** - Implement per user
4. **HTTPS only** - In production
5. **CORS properly configured** - Only allow trusted origins
6. **Keep dependencies updated** - Regular security patches

---

## Support & Contributing

For issues or contributions, visit:
https://github.com/kenjust821-afk/ai-code-generator

## License

MIT License - See LICENSE file
