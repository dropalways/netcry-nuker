#!/bin/bash

echo "Installing requirements..."
python3 -m pip3 install -r requirements.txt

python3 main.py

read -p "Press Enter to continue..."
