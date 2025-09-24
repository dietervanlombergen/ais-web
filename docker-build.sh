#!/bin/bash

# Docker build script for Python Website

set -e

echo "🐳 Building Python Website Docker Container..."

# Build the Docker image
docker build -t python-website:latest .

echo "✅ Docker image built successfully!"
echo "📦 Image name: python-website:latest"

# Show image size
echo "📏 Image size:"
docker images python-website:latest --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

echo ""
echo "🚀 To run the container:"
echo "   docker run -p 8000:8000 python-website:latest"
echo ""
echo "🔧 Or use docker-compose:"
echo "   docker-compose up"
