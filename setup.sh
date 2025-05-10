#!/usr/bin/env bash
set -e  # Exit on error

echo "Setting up Python 3.11 development environment..."

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python -m venv .venv
fi
# Activate virtual environment
source .venv/bin/activate

if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
fi

echo "Setup complete! Environment is ready."
python -c "import sys; print(f'Python version: {sys.version}')"
