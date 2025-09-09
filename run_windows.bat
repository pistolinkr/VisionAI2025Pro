@echo off
echo ========================================
echo VisionAI Pro Server Launcher
echo ========================================

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found
    echo Please run install_windows.bat first
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Set PYTHONPATH
set PYTHONPATH=%PYTHONPATH%;%CD%

REM Check command line arguments
if "%1"=="" (
    echo.
    echo Available servers:
    echo   zero-shot  - Zero-shot classification server (port 8002)
    echo   advanced   - Advanced classification server (port 8001)
    echo   firebase   - Firebase server (port 8003)
    echo.
    echo Usage: run_windows.bat [server_type]
    echo Example: run_windows.bat zero-shot
    pause
    exit /b 1
)

REM Run the specified server
if "%1"=="zero-shot" (
    echo Starting Zero-shot Classification Server...
    echo Web interface: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
    python main.py zero-shot
) else if "%1"=="advanced" (
    echo Starting Advanced Classification Server...
    echo Web interface: http://localhost:8001/web_apps/advanced/advanced_web_app.html
    python main.py advanced
) else if "%1"=="firebase" (
    echo Starting Firebase Server...
    echo Web interface: http://localhost:8003/web_apps/firebase/firebase_web_app.html
    python main.py firebase
) else (
    echo ERROR: Unknown server type: %1
    echo Available types: zero-shot, advanced, firebase
    pause
    exit /b 1
)

pause
