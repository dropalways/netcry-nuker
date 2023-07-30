@echo off
title Installing requirements...

REM check if 'pip' is available in the system - w3althy
where /q pip
if %errorlevel% neq 0 (
    echo Error: 'pip' command not found. Make sure Python is installed and is added to the system PATH.
    pause
    exit /b 1
)

REM install python packages from requirements.txt - w3althy
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install Python packages. Check if the requirements.txt file is valid.
    pause
    exit /b 1
)

REM run the main.py script - w3althy
py main.py
if %errorlevel% neq 0 (
    echo Error: Failed to run Netcry. Check if the file 'main.py' exists.
    pause
    exit /b 1
)

echo Installation and execution completed successfully.
pause
exit /b 0
