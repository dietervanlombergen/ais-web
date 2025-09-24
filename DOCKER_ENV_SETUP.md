# Docker Environment Setup with Cohere AI

This guide shows how to set up your Docker environment with Cohere AI integration.

## 🔧 Environment Variables Setup

### Option 1: Using .env File (Recommended)

Create a `.env` file in your project root:

```bash
# Create .env file
touch .env
```

Add the following content to `.env`:

```env
# Flask Configuration
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secure-secret-key-here

# Cohere AI Configuration
# Get your API key from: https://dashboard.cohere.ai/api-keys
COHERE_API_KEY=co-your-api-key-here

# Database Configuration (optional)
DATABASE_URL=postgresql://webapp:secure_password_here@db:5432/python_website
```

### Option 2: Export Environment Variables

```bash
# Set environment variables
export COHERE_API_KEY="co-your-api-key-here"
export SECRET_KEY="your-secure-secret-key-here"
export FLASK_ENV="production"
export FLASK_DEBUG="False"
```

### Option 3: Docker Compose Override

Create a `docker-compose.override.yml` file:

```yaml
version: '3.8'

services:
  web:
    environment:
      - COHERE_API_KEY=${COHERE_API_KEY}
      - SECRET_KEY=${SECRET_KEY}
```

## 🚀 Running with Docker

### 1. Basic Setup (No AI)
```bash
# Start without Cohere API key
docker-compose up
```

### 2. With Cohere AI
```bash
# Set your API key
export COHERE_API_KEY="co-your-api-key-here"

# Start the application
docker-compose up
```

### 3. Using .env File
```bash
# Create .env file with your API key
echo "COHERE_API_KEY=co-your-api-key-here" > .env

# Start the application
docker-compose up
```

## 🔍 Verifying Setup

### Check Container Logs
```bash
# View logs to see if AI service is initialized
docker-compose logs web
```

You should see:
```
Cohere AI service initialized successfully
```

Instead of:
```
Cohere API key not found. AI features will be disabled.
```

### Test API Health
```bash
# Check if AI is available
curl http://localhost:8000/api/health
```

Expected response:
```json
{
  "ai_available": true,
  "message": "Server is running",
  "status": "healthy"
}
```

### Test AI Features
1. Visit http://localhost:8000/articles
2. Fetch some RSS articles
3. Click "AI Summary" or "Sentiment" buttons
4. Verify AI analysis appears

## 🔒 Security Best Practices

### 1. Never Commit API Keys
```bash
# Add to .gitignore
echo ".env" >> .gitignore
echo "docker-compose.override.yml" >> .gitignore
```

### 2. Use Strong Secrets
```bash
# Generate secure secret key
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 3. Production Deployment
```bash
# Use environment variables in production
docker run -e COHERE_API_KEY="your-key" python-website:latest
```

## 🛠️ Troubleshooting

### Common Issues

#### "Cohere API key not found" in logs
```bash
# Check if environment variable is set
docker-compose config | grep COHERE_API_KEY

# If empty, set it:
export COHERE_API_KEY="co-your-key-here"
docker-compose up
```

#### Container won't start
```bash
# Check logs
docker-compose logs web

# Rebuild container
docker-compose down
docker-compose build --no-cache
docker-compose up
```

#### AI features not working
```bash
# Verify API key format
echo $COHERE_API_KEY
# Should start with "co-"

# Check Cohere account credits
# Visit: https://dashboard.cohere.ai/
```

## 📊 Docker Compose Profiles

### Development Mode
```bash
# Start with development settings
docker-compose --profile development up
```

### Production Mode
```bash
# Start with nginx reverse proxy
docker-compose --profile production up
```

### With Database
```bash
# Start with PostgreSQL database
docker-compose --profile database up
```

## 🔄 Environment Updates

### Update API Key
```bash
# Stop containers
docker-compose down

# Update environment variable
export COHERE_API_KEY="co-new-api-key-here"

# Restart containers
docker-compose up
```

### Update .env File
```bash
# Edit .env file
nano .env

# Restart containers
docker-compose down
docker-compose up
```

## 🎯 Production Deployment

### Environment Variables for Production
```env
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-production-secret-key
COHERE_API_KEY=co-your-production-api-key
```

### Docker Compose Production
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - FLASK_ENV=production
      - FLASK_DEBUG=False
      - SECRET_KEY=${SECRET_KEY}
      - COHERE_API_KEY=${COHERE_API_KEY}
    restart: unless-stopped
```

## 🎉 Success!

Your Docker setup with Cohere AI is now configured! 

**Next Steps:**
1. Get your Cohere API key
2. Set the environment variable
3. Start the containers
4. Enjoy AI-powered article analysis!

Visit http://localhost:8000/articles to see it in action! 🚀
