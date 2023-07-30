#!/bin/bash

# check if python 3 is installed - w3althy
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# check if "main.py" exists - w3althy
if [ ! -f "main.py" ]; then
    echo "Error: 'main.py' not found. Please make sure the file exists in the current directory."
    exit 1
fi

# run the python script - w3althy
python3 main.py

# check the exit status of the python script - w3althy
if [ $? -ne 0 ]; then
    echo "Error: The Python script 'main.py' did not execute successfully."
    read -rp "Press Enter to continue..."
    exit 1
fi

# wait for user input before exiting - w3althy
read -rp "Press Enter to continue..."
