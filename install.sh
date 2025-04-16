#!/bin/bash

# Stop the script on errors
set -e

# Create a virtual environment called 'venv' if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created."
else
    echo "📁 Virtual environment already exists."
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements if the file exists
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "📦 Dependencies installed from requirements.txt."
else
    echo "⚠️ No requirements.txt found. Skipping dependency installation."
fi

echo "✅ Environment is ready."