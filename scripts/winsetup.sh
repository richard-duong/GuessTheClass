#!/bin/bash

echo ""
echo "Creating virtual environment"
winpty python -m venv env						# generates virtual environment

echo "Installing requirements.txt"
env/Scripts/pip install -r requirements.txt		# installs prerequistes

