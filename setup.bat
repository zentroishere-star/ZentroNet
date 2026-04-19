@echo off
REM ==========================================
REM Zentro Setup Script for Windows
REM ==========================================

echo.
echo ========================================
echo   Zentro - Professional Website Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

REM Create virtual environment
echo [1/6] Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo [2/6] Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Upgrade pip
echo [3/6] Upgrading pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo ERROR: Failed to upgrade pip
    pause
    exit /b 1
)

REM Install dependencies
echo [4/6] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

REM Run migrations
echo [5/6] Running database migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Failed to run migrations
    pause
    exit /b 1
)

REM Create superuser
echo [6/6] Creating superuser account...
python manage.py createsuperuser

REM Load sample data
echo.
set /p load_sample="Do you want to load sample data? (y/n): "
if /i "%load_sample%"=="y" (
    python manage.py load_sample_data
)

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo To start the development server:
echo   1. Run: venv\Scripts\activate.bat
echo   2. Run: python manage.py runserver
echo.
echo Then open your browser to:
echo   Website: http://127.0.0.1:8000/
echo   Admin Panel: http://127.0.0.1:8000/admin/
echo.
pause
