@echo off

REM Run the main.py script
py main.py

if %errorlevel% neq 0 (
    echo Error: Failed to run the main.py script. Check if the file 'main.py' exists.
    pause
    exit /b 1
)

