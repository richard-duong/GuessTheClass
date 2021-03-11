@echo off
echo.
echo. This may take a while

echo. Creating virtual environment
echo. python3 -m venv env
echo.
python3 -m venv env

Rem echo. Loading virtual environment
Rem echo. "env/Scripts/activate.bat"
Rem "env/Scripts/activate.bat"

echo. Installing requirements.txt
echo. "env/Scripts/pip.exe" install -r requirements.txt
"env/Scripts/pip.exe" install -r requirements.txt
