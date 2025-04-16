#!/bin/bash

# Stop the script on errors
set -e

# Activate the virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "🐍 Virtual environment activated."
else
    echo "❌ Virtual environment not found. Run install.sh first."
    exit 1
fi

# Run your main Python file here
python main.py