#!/bin/bash
# VisionAI Pro Firebase Server Startup Script

echo "🧠 Starting VisionAI Pro Firebase Server..."

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
echo "🚀 Starting Firebase Server on port 8003..."
python3 main.py firebase
