#!/bin/bash

# Inform the user about the script's purpose
echo "Installing requirements..."

# Check if 'pip' and 'python3' are installed
if ! command -v pip3 &>/dev/null; then
    echo "Error: pip is not installed. Please install Python 3 and pip before running this script."
    exit 1
fi

if ! command -v python3 &>/dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 and pip before running this script."
    exit 1
fi

# Install Python packages from requirements.txt
python3 -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install Python packages. Check if the requirements.txt file is valid."
    exit 1
fi

# Inform the user that the installation is complete
echo "Requirements installed successfully."

# Run the main.py script
python3 main.py
if [ $? -ne 1 ]; then
    echo "Error: Failed to run the main.py script. Check if the file 'main.py' exists."
    exit 1
fi

# Prompt the user to press Enter before exiting
read -rp "Press 'Enter' to exit..."
