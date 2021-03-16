#!/bin/bash
echo ""
echo "This may take a while"

echo "Creating virtual environment"
python -m venv env							# generates virtual environment

echo "Installing requirements.txt"
env/bin/pip install -r requirements.txt		# installs prerequistes


