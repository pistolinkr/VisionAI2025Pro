#!/bin/bash
# VisionAI Pro Advanced Server Startup Script

echo "🧠 Starting VisionAI Pro Advanced Server..."

# Change to project root directory
cd "$(dirname "$0")/../.."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "📦 Activating virtual environment..."
    source venv/bin/activate
fi

# Set environment variables
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
export ENVIRONMENT="production"

# Start the server
echo "🚀 Starting Advanced Classification Server on port 8001..."
python3 main.py advanced
