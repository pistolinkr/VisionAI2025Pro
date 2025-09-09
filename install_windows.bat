@echo off
echo ========================================
echo VisionAI Pro Windows Installation
echo ========================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python found. Checking version...
python --version

REM Create virtual environment
echo.
echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo.
echo Installing requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install requirements
    echo Try installing Visual Studio Build Tools from:
    echo https://visualstudio.microsoft.com/visual-cpp-build-tools/
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation completed successfully!
echo ========================================
echo.
echo To run the server:
echo 1. Activate virtual environment: venv\Scripts\activate.bat
echo 2. Run server: python main.py zero-shot
echo.
echo Web interface will be available at:
echo http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
echo.
pause
