@echo off

rem check if python is installed - w3althy
where /q python || (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b 1
)

rem run the python script - w3althy
python main.py

rem check the exit code of the python script - w3althy
if %errorlevel% neq 0 (
    echo An error occurred while running Netcry.
) else (
    echo The Python script completed successfully.
)

pause