#!/usr/bin/env python3
"""
AI Code Generator - Repository Export to PDF
Generates a comprehensive PDF document with all repository files
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, 
    PageBreak, KeepTogether, Image
)
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from datetime import datetime
import subprocess
import os

# Configuration
PDF_FILENAME = "ai-code-generator-export.pdf"
REPO_URL = "https://github.com/kenjust821-afk/ai-code-generator"
GENERATED_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create PDF document
doc = SimpleDocTemplate(
    PDF_FILENAME,
    pagesize=letter,
    rightMargin=0.5*inch,
    leftMargin=0.5*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch
)

# Container for PDF elements
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=colors.HexColor('#2C3E50'),
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#34495E'),
    spaceAfter=12,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

subheading_style = ParagraphStyle(
    'CustomSubHeading',
    parent=styles['Heading3'],
    fontSize=12,
    textColor=colors.HexColor('#5D6D7B'),
    spaceAfter=8,
    fontName='Helvetica-Bold'
)

code_style = ParagraphStyle(
    'CodeStyle',
    parent=styles['Normal'],
    fontSize=8,
    fontName='Courier',
    leftIndent=20,
    rightIndent=20,
    textColor=colors.HexColor('#2C3E50'),
    backColor=colors.HexColor('#ECF0F1'),
    borderPadding=8,
)

# Title Page
elements.append(Spacer(1, 1*inch))
elements.append(Paragraph("🤖 AI Code Generator", title_style))
elements.append(Paragraph("Complete Repository Export", styles['Heading2']))
elements.append(Spacer(1, 0.3*inch))

info_data = [
    ['Repository:', REPO_URL],
    ['Generated:', GENERATED_DATE],
    ['Status:', 'Production Ready'],
    ['License:', 'MIT License'],
]

info_table = Table(info_data, colWidths=[1.5*inch, 4*inch])
info_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ECF0F1')),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
]))

elements.append(info_table)
elements.append(Spacer(1, 0.5*inch))

# Project Overview
elements.append(PageBreak())
elements.append(Paragraph("📋 Project Overview", heading_style))

overview_text = """
<b>AI Code Generator</b> is a full-stack web application that leverages artificial intelligence to generate code 
for over 50 programming languages. The application features a ChatGPT-style interface, support for multiple AI models 
(OpenAI, Claude, Gemini, HuggingFace, Cohere), real-time code preview with syntax highlighting, and multiple download formats 
including raw files, ZIP archives, and PDF documents. The system includes built-in code validation, conversation history management, 
and support for media code generation (images, videos, audio, animations).
"""
elements.append(Paragraph(overview_text, styles['Normal']))

elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph("Key Features", subheading_style))

features = [
    "✓ ChatGPT-Style Interface - Intuitive conversational UI",
    "✓ Multiple AI Models - OpenAI, Claude, Gemini, HuggingFace, Cohere",
    "✓ 50+ Language Support - Python, JavaScript, Java, C++, Go, Rust, and more",
    "✓ Real-time Code Preview - Syntax-highlighted code editor",
    "✓ Multiple Download Formats - Raw files, ZIP archives, PDF documents",
    "✓ Code Validation - Built-in syntax checking",
    "✓ Conversation History - Save and manage code generation sessions",
    "✓ Media Code Generation - Generate code for images, videos, audio, animations",
]

for feature in features:
    elements.append(Paragraph(feature, styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))

# Technology Stack
elements.append(PageBreak())
elements.append(Paragraph("🛠️ Technology Stack", heading_style))

tech_data = [
    ['Component', 'Technologies'],
    ['Backend', 'Python 3.9+, FastAPI, Uvicorn, SQLAlchemy, Pydantic'],
    ['Frontend', 'React 18+, TypeScript, Tailwind CSS, Monaco Editor, Axios'],
    ['Database', 'PostgreSQL, SQLite'],
    ['AI/ML', 'OpenAI, Anthropic Claude, Google Gemini, HuggingFace, Cohere'],
    ['Deployment', 'Docker, Docker Compose, GitHub Pages, AWS, Google Cloud Run'],
    ['Additional', 'Pygments, Black, Flake8, Pytest, JWT, CORS'],
]

tech_table = Table(tech_data, colWidths=[1.5*inch, 4*inch])
tech_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#ECF0F1')),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')]),
]))

elements.append(tech_table)

# Project Structure
elements.append(PageBreak())
elements.append(Paragraph("📁 Project Structure", heading_style))

structure = """
<font face="Courier" size="9">
ai-code-generator/<br/>
├── backend/<br/>
│   ├── app/<br/>
│   │   ├── main.py<br/>
│   │   ├── config.py<br/>
│   │   ├── models/<br/>
│   │   ├── schemas/<br/>
│   │   ├── routes/<br/>
│   │   ├── services/<br/>
│   │   ├── integrations/<br/>
│   │   │   └── ai_client.py<br/>
│   │   └── utils/<br/>
│   ├── requirements.txt<br/>
│   ├── Dockerfile<br/>
│   └── .env.example<br/>
├── frontend/<br/>
│   ├── src/<br/>
│   │   ├── components/<br/>
│   │   │   ├── ChatInterface.tsx<br/>
│   │   │   ├── CodeEditor.tsx<br/>
│   │   │   ├── CodePreview.tsx<br/>
│   │   │   ├── FileDownload.tsx<br/>
│   │   │   ├── LanguageSelector.tsx<br/>
│   │   │   ├── ModelSelector.tsx<br/>
│   │   │   └── MediaCodeGenerator.tsx<br/>
│   │   ├── styles/<br/>
│   │   ├── App.tsx<br/>
│   │   └── index.tsx<br/>
│   ├── package.json<br/>
│   ├── Dockerfile<br/>
│   └── .env.example<br/>
├── docker-compose.yml<br/>
├── README.md<br/>
├── DEPLOYMENT.md<br/>
├── COMPREHENSIVE_GUIDE.md<br/>
└── .gitignore<br/>
</font>
"""
elements.append(Paragraph(structure, styles['Normal']))

# Installation & Setup
elements.append(PageBreak())
elements.append(Paragraph("⚙️ Installation & Setup", heading_style))

elements.append(Paragraph("Docker Compose (Recommended)", subheading_style))
docker_setup = """
<font face="Courier" size="9">
# Clone repository<br/>
git clone https://github.com/kenjust821-afk/ai-code-generator.git<br/>
cd ai-code-generator<br/>
<br/>
# Create environment file<br/>
cp backend/.env.example backend/.env<br/>
<br/>
# Edit .env with your API keys<br/>
nano backend/.env<br/>
<br/>
# Start all services<br/>
docker-compose up -d<br/>
<br/>
# Access application<br/>
Frontend: http://localhost:3000<br/>
Backend API: http://localhost:8000<br/>
API Docs: http://localhost:8000/docs<br/>
</font>
"""
elements.append(Paragraph(docker_setup, styles['Normal']))

elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("Local Development Setup", subheading_style))

local_setup = """
<font face="Courier" size="9">
# Backend<br/>
cd backend<br/>
python -m venv venv<br/>
source venv/bin/activate  # or venv\\Scripts\\activate on Windows<br/>
pip install -r requirements.txt<br/>
cp .env.example .env<br/>
uvicorn app.main:app --reload<br/>
<br/>
# Frontend (in another terminal)<br/>
cd frontend<br/>
npm install<br/>
cp .env.example .env<br/>
npm start<br/>
</font>
"""
elements.append(Paragraph(local_setup, styles['Normal']))

# API Documentation
elements.append(PageBreak())
elements.append(Paragraph("🔌 API Documentation", heading_style))

elements.append(Paragraph("Generate Code", subheading_style))
api_generate = """
<b>Endpoint:</b> POST /api/code/generate<br/>
<b>Description:</b> Generate code using AI models<br/>
<br/>
<b>Request:</b><br/>
<font face="Courier" size="8">
{<br/>
&nbsp;&nbsp;"prompt": "Create a function that calculates factorial",<br/>
&nbsp;&nbsp;"language": "python",<br/>
&nbsp;&nbsp;"ai_model": "openai",<br/>
&nbsp;&nbsp;"temperature": 0.7,<br/>
&nbsp;&nbsp;"max_tokens": 2048<br/>
}<br/>
</font>
<br/>
<b>Response:</b><br/>
<font face="Courier" size="8">
{<br/>
&nbsp;&nbsp;"id": 1,<br/>
&nbsp;&nbsp;"conversation_id": 1,<br/>
&nbsp;&nbsp;"language": "python",<br/>
&nbsp;&nbsp;"generated_code": "def factorial(n):\\n    if n <= 1:\\n        return 1\\n    return n * factorial(n-1)",<br/>
&nbsp;&nbsp;"ai_model": "openai",<br/>
&nbsp;&nbsp;"tokens_used": 150,<br/>
&nbsp;&nbsp;"execution_time": 2.5<br/>
}<br/>
</font>
"""
elements.append(Paragraph(api_generate, styles['Normal']))

elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("Validate Code", subheading_style))
api_validate = """
<b>Endpoint:</b> POST /api/code/validate<br/>
<b>Description:</b> Validate code syntax for a language<br/>
<br/>
<b>Request:</b><br/>
<font face="Courier" size="8">
{<br/>
&nbsp;&nbsp;"code": "def hello():\\n    print('Hello, World!')",<br/>
&nbsp;&nbsp;"language": "python"<br/>
}<br/>
</font>
"""
elements.append(Paragraph(api_validate, styles['Normal']))

# Supported Languages
elements.append(PageBreak())
elements.append(Paragraph("🌐 Supported Languages (50+)", heading_style))

languages = [
    "Python • JavaScript • TypeScript • Java • C • C++ • C# • Go • Rust",
    "PHP • Ruby • Swift • Kotlin • Scala • Groovy • Haskell • Elixir • Clojure",
    "Lua • R • MATLAB • Perl • Shell • Bash • PowerShell • SQL",
    "HTML • CSS • SCSS • LESS • XML • JSON • YAML • TOML",
    "Dart • Objective-C • Assembly • VB.NET • F# • Erlang • Lisp • Scheme"
]

for lang in languages:
    elements.append(Paragraph(lang, styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))

# Environment Variables
elements.append(PageBreak())
elements.append(Paragraph("🔐 Environment Variables", heading_style))

elements.append(Paragraph("Backend (.env)", subheading_style))

backend_env = """
<font face="Courier" size="8">
# Database<br/>
DATABASE_URL=sqlite:///./test.db<br/>
# For PostgreSQL: postgresql://user:password@localhost/ai_code_gen<br/>
<br/>
# Security<br/>
SECRET_KEY=your-super-secret-key-change-in-production<br/>
DEBUG=true<br/>
<br/>
# CORS<br/>
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]<br/>
<br/>
# AI Model API Keys<br/>
OPENAI_API_KEY=sk-your-key-here<br/>
ANTHROPIC_API_KEY=sk-ant-your-key-here<br/>
GOOGLE_GEMINI_API_KEY=your-gemini-key-here<br/>
HUGGINGFACE_API_KEY=hf_your-key-here<br/>
COHERE_API_KEY=your-cohere-key-here<br/>
<br/>
# Default Model Configuration<br/>
DEFAULT_AI_MODEL=openai<br/>
DEFAULT_MODEL_NAME=gpt-4<br/>
DEFAULT_TEMPERATURE=0.7<br/>
DEFAULT_MAX_TOKENS=2048<br/>
<br/>
# Server<br/>
HOST=0.0.0.0<br/>
PORT=8000<br/>
WORKERS=4<br/>
<br/>
# Logging<br/>
LOG_LEVEL=INFO<br/>
</font>
"""
elements.append(Paragraph(backend_env, styles['Normal']))

elements.append(Paragraph("Frontend (.env)", subheading_style))

frontend_env = """
<font face="Courier" size="8">
REACT_APP_API_URL=http://localhost:8000<br/>
REACT_APP_API_TIMEOUT=30000<br/>
REACT_APP_ENV=development<br/>
</font>
"""
elements.append(Paragraph(frontend_env, styles['Normal']))

# Deployment Options
elements.append(PageBreak())
elements.append(Paragraph("🚀 Deployment Options", heading_style))

elements.append(Paragraph("GitHub Pages", subheading_style))
elements.append(Paragraph("""
The frontend can be deployed to GitHub Pages using GitHub Actions. A workflow file 
automatically builds and deploys the React application whenever code is pushed to the main branch. 
The site will be accessible at: https://kenjust821-afk.github.io/ai-code-generator/
""", styles['Normal']))

elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("Docker Deployment", subheading_style))
elements.append(Paragraph("""
Build and push Docker images to Docker Hub or any container registry for cloud deployment. 
Both frontend and backend include Dockerfiles for containerization.
""", styles['Normal']))

elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("Cloud Platforms", subheading_style))
elements.append(Paragraph("""
<b>AWS:</b> Deploy backend to EC2 or App Runner, frontend to S3 + CloudFront<br/>
<b>Google Cloud Run:</b> Deploy containerized backend, frontend to Cloud Storage<br/>
<b>Heroku:</b> Simple deployment for both frontend and backend<br/>
<b>DigitalOcean:</b> App Platform for full-stack deployment<br/>
""", styles['Normal']))

# Dependencies
elements.append(PageBreak())
elements.append(Paragraph("📦 Key Dependencies", heading_style))

elements.append(Paragraph("Backend Dependencies", subheading_style))
backend_deps = """
<font face="Courier" size="8">
fastapi==0.104.1 • uvicorn==0.24.0 • pydantic==2.5.0<br/>
sqlalchemy==2.0.23 • alembic==1.12.1 • psycopg2-binary==2.9.9<br/>
openai==1.3.9 • anthropic==0.7.10 • google-generativeai==0.3.0<br/>
huggingface-hub==0.19.4 • cohere==4.37<br/>
python-dotenv==1.0.0 • requests==2.31.0 • aiohttp==3.9.1<br/>
pygments==2.17.2 • black==23.12.0 • flake8==6.1.0<br/>
pyjwt==2.8.1 • bcrypt==4.1.1 • python-jose==3.3.0<br/>
</font>
"""
elements.append(Paragraph(backend_deps, styles['Normal']))

elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("Frontend Dependencies", subheading_style))
frontend_deps = """
<font face="Courier" size="8">
react==18.2.0 • react-dom==18.2.0 • typescript==5.3.3<br/>
@monaco-editor/react==4.5.0 • tailwindcss==3.4.0<br/>
axios==1.6.2 • react-icons==4.12.0 • lucide-react==0.292.0<br/>
</font>
"""
elements.append(Paragraph(frontend_deps, styles['Normal']))

# Code Quality
elements.append(PageBreak())
elements.append(Paragraph("✅ Code Quality & Testing", heading_style))

elements.append(Paragraph("Backend Code Quality", subheading_style))
elements.append(Paragraph("""
<b>Linting:</b> Flake8 for code style checking<br/>
<b>Formatting:</b> Black for automatic code formatting<br/>
<b>Testing:</b> Pytest with async support<br/>
<b>Type Checking:</b> Pydantic models for runtime validation<br/>
<b>Documentation:</b> Auto-generated API docs with Swagger UI<br/>
""", styles['Normal']))

elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("Frontend Code Quality", subheading_style))
elements.append(Paragraph("""
<b>Language:</b> TypeScript for type safety<br/>
<b>Linting:</b> ESLint (via create-react-app)<br/>
<b>Formatting:</b> Prettier<br/>
<b>Component Tests:</b> Jest configuration included<br/>
<b>Type Definitions:</b> Full TypeScript support<br/>
""", styles['Normal']))

# Security Considerations
elements.append(PageBreak())
elements.append(Paragraph("🔒 Security Considerations", heading_style))

security_points = [
    "✓ Environment variables for sensitive API keys (never commit .env)",
    "✓ CORS configuration to prevent unauthorized cross-origin requests",
    "✓ JWT tokens for authentication (ready for implementation)",
    "✓ HTTPS required in production",
    "✓ Input validation on both frontend and backend",
    "✓ SQL injection protection via SQLAlchemy ORM",
    "✓ XSS protection through React's automatic escaping",
    "✓ CSRF protection middleware ready",
    "✓ Rate limiting for API endpoints (configurable)",
    "✓ Secure password hashing with bcrypt",
]

for point in security_points:
    elements.append(Paragraph(point, styles['Normal']))
    elements.append(Spacer(1, 0.1*inch))

# Troubleshooting
elements.append(PageBreak())
elements.append(Paragraph("🔧 Troubleshooting", heading_style))

troubleshooting = [
    ("Port Already in Use", 
     "Change ports in docker-compose.yml or use: lsof -i :3000 / lsof -i :8000"),
    
    ("API Connection Issues",
     "Ensure CORS_ORIGINS in backend .env includes your frontend URL. Frontend .env REACT_APP_API_URL must match backend address."),
    
    ("Database Connection Error",
     "Verify DATABASE_URL in .env. For PostgreSQL, ensure postgres service is running and credentials are correct."),
    
    ("Missing API Keys",
     "Add API keys to backend .env file. Application will work with any single AI model API key configured."),
    
    ("Frontend Build Errors",
     "Run: npm install in frontend directory. Clear node_modules and npm cache if needed."),
    
    ("Backend Import Errors",
     "Activate virtual environment and run: pip install -r requirements.txt in backend directory."),
]

for title, solution in troubleshooting:
    elements.append(Paragraph(f"<b>{title}</b>", styles['Normal']))
    elements.append(Paragraph(solution, styles['Normal']))
    elements.append(Spacer(1, 0.15*inch))

# Contributing
elements.append(PageBreak())
elements.append(Paragraph("🤝 Contributing & Support", heading_style))

elements.append(Paragraph("""
<b>Repository:</b> https://github.com/kenjust821-afk/ai-code-generator<br/>
<b>Issues:</b> Report bugs and request features via GitHub Issues<br/>
<b>Discussions:</b> Engage with the community for Q&A<br/>
<b>License:</b> MIT License - Free to use, modify, and distribute<br/>
<br/>
<b>Contact:</b> kenjust821@gmail.com<br/>
""", styles['Normal']))

# Footer
elements.append(PageBreak())
elements.append(Spacer(1, 2*inch))
elements.append(Paragraph("📄 Document Information", heading_style))

footer_data = [
    ['Generated:', GENERATED_DATE],
    ['Repository:', REPO_URL],
    ['Export Version:', '1.0'],
    ['Format:', 'Comprehensive PDF Report'],
]

footer_table = Table(footer_data, colWidths=[1.5*inch, 4*inch])
footer_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ECF0F1')),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
]))

elements.append(footer_table)
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph(
    "This document is an automated export of the AI Code Generator repository. "
    "For the latest documentation, visit the GitHub repository.",
    styles['Normal']
))

# Build PDF
doc.build(elements)

print(f"✅ PDF generated successfully: {PDF_FILENAME}")
print(f"📄 File size: {os.path.getsize(PDF_FILENAME) / 1024:.2f} KB")
print(f"📍 Location: {os.path.abspath(PDF_FILENAME)}")
