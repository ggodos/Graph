
@echo off

pip install -r requirements.txt
if not %errorlevel% == 0 (
    echo Error while install requirements
    echo Code: %errorlevel%
    pause
    exit
)

python Main.py
if not %errorlevel% == 0 (
    echo Error while run program
    echo Code: %errorlevel%
    pause
)

