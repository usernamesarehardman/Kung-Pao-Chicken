@echo off
echo Starting Pseudo-Wireshark...

:: Check for admin privileges (optional, Windows 10/11 only)
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo This script needs to be run as Administrator.
    pause
    exit /b
)

:: Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

python app.py
pause