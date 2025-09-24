# Docker Setup for Python Website

This document provides comprehensive instructions for containerizing and deploying your Python Flask website using Docker.

## 🐳 Container Overview

Your Python website is now fully containerized with the following components:

- **Base Image**: Python 3.11 slim
- **Web Server**: Gunicorn (production WSGI server)
- **Application**: Flask with Bootstrap frontend
- **Port**: 8000 (internal/external)
- **Security**: Non-root user execution

## 📁 Docker Files

### Core Files
- `Dockerfile` - Container build instructions
- `.dockerignore` - Files to exclude from build context
- `docker-compose.yml` - Multi-container orchestration
- `nginx.conf` - Reverse proxy configuration (optional)

### Helper Scripts
- `docker-build.sh` - Build Docker image
- `docker-run.sh` - Run container with proper configuration

## 🚀 Quick Start

### Build and Run (Simple)
```bash
# Build the image
./docker-build.sh

# Run the container
./docker-run.sh
```

### Using Docker Compose
```bash
# Start the web application
docker-compose up

# Start with database (optional)
docker-compose --profile database up

# Start with nginx reverse proxy (optional)
docker-compose --profile production up
```

## 🔧 Manual Docker Commands

### Build Image
```bash
docker build -t python-website:latest .
```

### Run Container
```bash
docker run -d \
    --name python-website \
    -p 8000:8000 \
    -e FLASK_ENV=production \
    python-website:latest
```

### Container Management
```bash
# View logs
docker logs -f python-website

# Stop container
docker stop python-website

# Remove container
docker rm python-website

# Remove image
docker rmi python-website:latest
```

## 🌐 Access Points

- **Main Website**: http://localhost:8000
- **Health Check**: http://localhost:8000/api/health
- **Contact Form**: http://localhost:8000/contact
- **About Page**: http://localhost:8000/about

## 📊 Container Features

### Production Ready
- ✅ Multi-stage build optimization
- ✅ Non-root user for security
- ✅ Health checks
- ✅ Proper signal handling
- ✅ Optimized layer caching

### Performance
- ✅ Gunicorn WSGI server
- ✅ 4 worker processes
- ✅ 120-second timeout
- ✅ Optimized Docker layers

### Security
- ✅ Non-root user execution
- ✅ Minimal base image
- ✅ No unnecessary packages
- ✅ Proper file permissions

## 🔍 Container Inspection

### View Container Details
```bash
# Container information
docker inspect python-website

# Resource usage
docker stats python-website

# Container processes
docker exec python-website ps aux
```

### Access Container Shell
```bash
# Interactive shell
docker exec -it python-website /bin/bash

# Run commands
docker exec python-website python --version
```

## 🚀 Deployment Options

### 1. Local Development
```bash
docker-compose up
```

### 2. Production with Nginx
```bash
docker-compose --profile production up -d
```

### 3. With Database
```bash
docker-compose --profile database up -d
```

### 4. Cloud Deployment

#### Docker Hub
```bash
# Tag for Docker Hub
docker tag python-website:latest yourusername/python-website:latest

# Push to Docker Hub
docker push yourusername/python-website:latest
```

#### AWS ECS/Fargate
```bash
# Build for AWS
docker build -t python-website:aws .

# Tag for ECR
docker tag python-website:aws your-account.dkr.ecr.region.amazonaws.com/python-website:latest
```

## 🔧 Configuration

### Environment Variables
```bash
# Production settings
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secure-secret-key

# Database (if using)
DATABASE_URL=postgresql://user:pass@db:5432/dbname
```

### Port Configuration
- **Internal Port**: 8000 (Gunicorn)
- **External Port**: 8000 (default)
- **Custom Port**: `docker run -p 3000:8000 python-website:latest`

## 📈 Monitoring

### Health Checks
```bash
# Container health
docker ps

# Application health
curl http://localhost:8000/api/health
```

### Logs
```bash
# Follow logs
docker logs -f python-website

# Recent logs
docker logs --tail 100 python-website
```

## 🛠️ Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000

# Use different port
docker run -p 8001:8000 python-website:latest
```

#### Container Won't Start
```bash
# Check logs
docker logs python-website

# Run interactively
docker run -it python-website:latest /bin/bash
```

#### Permission Issues
```bash
# Check file permissions
docker exec python-website ls -la /app

# Fix permissions (if needed)
docker exec python-website chown -R appuser:appuser /app
```

### Debug Mode
```bash
# Run with debug environment
docker run -p 8000:8000 \
    -e FLASK_ENV=development \
    -e FLASK_DEBUG=True \
    python-website:latest
```

## 🔄 Updates and Maintenance

### Update Application
```bash
# Rebuild image
docker build -t python-website:latest .

# Restart container
docker-compose down && docker-compose up
```

### Clean Up
```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove everything
docker system prune -a
```

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/)
- [Gunicorn Configuration](https://docs.gunicorn.org/en/stable/configure.html)
- [Flask Deployment](https://flask.palletsprojects.com/en/2.3.x/deploying/)

---

**Your Python website is now fully containerized and ready for deployment! 🐳**
