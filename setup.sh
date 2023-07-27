#!/bin/bash

echo "Installing requirements..."
pip3 install -r requirements.txt

python3 main.py

read -p "Press Enter to continue..."
