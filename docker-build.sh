#!/bin/bash

# Docker build script for Python Website 4ntoon/ais-web:1
IMAGE_NAME="4ntoon/ais-web:1"

set -e

echo "🐳 Building Python Website Docker Container..."

# Build the Docker image
docker build -t $IMAGE_NAME .

echo "✅ Docker image built successfully!"
echo "📦 Image name: $IMAGE_NAME"

# Show image size
echo "📏 Image size:"
docker images $IMAGE_NAME --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

echo ""
echo "🚀 To run the container:"
echo "   docker run -p 8000:8000 $IMAGE_NAME"
echo ""
echo "🔧 Or use docker-compose:"
echo "   docker-compose up"
