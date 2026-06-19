@echo off
REM Startup script for Autonomous Business Agent Web UI (Windows)

echo 🚀 Starting Autonomous Business Agent Web UI...
echo.

REM Check if virtual environment exists
if not exist "..\..\..venv" (
    echo ❌ Virtual environment not found. Please run setup first.
    exit /b 1
)

REM Start the FastAPI backend in a new window
echo 📡 Starting FastAPI backend on port 8000...
start "Backend API" cmd /k "cd api && ..\..\..venv\Scripts\activate && python main.py"

REM Wait for backend to start
timeout /t 3 /nobreak > nul

REM Start the Next.js frontend
echo 🌐 Starting Next.js frontend on port 3002...
npm run dev
