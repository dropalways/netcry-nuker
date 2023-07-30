#!/bin/bash

# inform the user about the script's purpose - w3althy
echo "Installing requirements..."

# check if 'pip' and 'python 3' are installed - w3althy
if ! command -v pip3 &>/dev/null; then
    echo "Error: pip is not installed. Please install Python 3 and pip before running this script."
    exit 1
fi

if ! command -v python3 &>/dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 and pip before running this script."
    exit 1
fi

# install Python packages from requirements.txt - w3althy
pip3 install -r requirements.txt

# inform the user that the installation is complete - w3althy
echo "Requirements installed successfully."

# run the main.py script - w3althy
python3 main.py

# prompt the user to press Enter before exiting - w3althy
read -rp "Press 'Enter' to exit..."
