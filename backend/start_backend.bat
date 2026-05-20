@echo off
echo ================================================
echo    DevNest Backend Server Startup
echo ================================================
echo.

cd backend
call venv\Scripts\activate
echo Virtual environment activated.
echo.

echo Checking Ollama...
ollama list >nul 2>&1
if errorlevel 1 (
    echo WARNING: Ollama not running. Start it with: ollama serve
) else (
    echo Ollama running
    
    REM Check for 1.5B model
    ollama list | findstr "qwen2.5-coder:1.5B" >nul
    if errorlevel 1 (
    echo Model qwen2.5-coder:1.5B not found!
    echo Download it: ollama pull qwen2.5-coder:1.5B-instruct
        pause
        exit /b 1
    ) else (
        echo Qwen 1.5B found
    )
)

echo.
echo Starting Server...
echo Backend will be available at: http://localhost:8000
echo Press Ctrl+C to stop the server.
echo.
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause