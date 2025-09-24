#!/bin/bash

# Docker run script for Python Website

set -e

echo "🚀 Starting Python Website Container..."

# Stop any existing container
docker stop python-website 2>/dev/null || true
docker rm python-website 2>/dev/null || true

# Run the container
docker run -d \
    --name python-website \
    -p 8000:8000 \
    -e FLASK_ENV=production \
    -e SECRET_KEY="your-production-secret-key-$(date +%s)" \
    python-website:latest

echo "✅ Container started successfully!"
echo "📍 Website available at: http://localhost:8000"
echo "🏥 Health check: http://localhost:8000/api/health"

# Show container status
echo ""
echo "📊 Container status:"
docker ps --filter name=python-website --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo ""
echo "📋 Useful commands:"
echo "   View logs:     docker logs -f python-website"
echo "   Stop container: docker stop python-website"
echo "   Remove container: docker rm python-website"
