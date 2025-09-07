#!/bin/bash
# VisionAI Pro Main Server Startup Script

echo "🧠 Starting VisionAI Pro Main Server..."

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
echo "🚀 Starting Main Classification Server on port 8000..."
python3 main.py main
