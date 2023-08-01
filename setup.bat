@echo off

title Installing requirements...

py -m pip install -r requirements.txt
py main.py
pause