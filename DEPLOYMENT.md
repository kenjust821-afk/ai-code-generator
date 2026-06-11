# Deployment Guide

## Local Development

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL (optional, can use SQLite)
- Docker & Docker Compose (for containerized setup)

### Quick Start with Docker

```bash
# Clone the repository
git clone https://github.com/kenjust821-afk/ai-code-generator.git
cd ai-code-generator

# Create .env file
cp backend/.env.example backend/.env

# Update API keys in .env
# OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=sk-ant-...
# etc.

# Start all services
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## Production Deployment

### Using Heroku

```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set OPENAI_API_KEY=sk-...
heroku config:set ANTHROPIC_API_KEY=sk-ant-...
# etc.

# Deploy
git push heroku main
```

### Using AWS

1. **Backend:**
   - Deploy FastAPI app to EC2 or use AWS App Runner
   - Use RDS for PostgreSQL database
   - Configure API Gateway for CORS

2. **Frontend:**
   - Build: `npm run build`
   - Deploy to S3 + CloudFront
   - Configure CloudFront to proxy API requests

### Using Google Cloud Run

```bash
# Backend
cd backend
gcloud run deploy ai-code-generator-backend \
  --source . \
  --platform managed \
  --region us-central1 \
  --set-env-vars OPENAI_API_KEY=sk-...,DATABASE_URL=...

# Frontend
cd ../frontend
npm run build
gsutil -m cp -r build/* gs://ai-code-generator/
```

## Environment Variables

All required environment variables are listed in:
- Backend: `backend/.env.example`
- Frontend: `frontend/.env.example`

## Database Migrations

```bash
cd backend
alembic upgrade head
```

## Monitoring & Logging

- Backend logs available at `/var/log/ai-code-generator/`
- Frontend errors logged to browser console
- Use Sentry for error tracking

## Scaling

1. **Horizontal Scaling:**
   - Use load balancer (nginx, HAProxy)
   - Multiple backend instances
   - Static frontend CDN

2. **Database:**
   - Read replicas for PostgreSQL
   - Redis cache for frequent queries

3. **API Rate Limiting:**
   - Implement rate limiting per user
   - Cache API responses
