#!/bin/bash

# Startup script for Autonomous Business Agent Web UI

echo "🚀 Starting Autonomous Business Agent Web UI..."
echo ""

# Check if virtual environment exists
if [ ! -d "../.venv" ]; then
    echo "❌ Virtual environment not found at ../.venv"
    echo "Please make sure you have created the virtual environment in the autonomous-business-agent directory."
    exit 1
fi

# Start the FastAPI backend in the background
echo "📡 Starting FastAPI backend on port 8000..."
cd api

# Activate virtual environment if not already activated
if [ -z "$VIRTUAL_ENV" ]; then
    source ../.venv/bin/activate
fi

python main.py &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Start the Next.js frontend
echo "🌐 Starting Next.js frontend on port 3002..."
npm run dev

# Cleanup on exit
trap "echo ''; echo '🛑 Shutting down...'; kill $BACKEND_PID 2>/dev/null" EXIT
