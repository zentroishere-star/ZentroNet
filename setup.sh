#!/bin/bash
# ==========================================
# Zentro Setup Script for Mac/Linux
# ==========================================

echo ""
echo "========================================"
echo "  Zentro - Professional Website Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ using:"
    echo "  macOS: brew install python3"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip python3-venv"
    exit 1
fi

# Create virtual environment
echo "[1/6] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

# Activate virtual environment
echo "[2/6] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate virtual environment"
    exit 1
fi

# Upgrade pip
echo "[3/6] Upgrading pip..."
python -m pip install --upgrade pip
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to upgrade pip"
    exit 1
fi

# Install dependencies
echo "[4/6] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

# Run migrations
echo "[5/6] Running database migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to run migrations"
    exit 1
fi

# Create superuser
echo "[6/6] Creating superuser account..."
python manage.py createsuperuser

# Load sample data
echo ""
read -p "Do you want to load sample data? (y/n): " load_sample
if [[ $load_sample == "y" || $load_sample == "Y" ]]; then
    python manage.py load_sample_data
fi

echo ""
echo "========================================"
echo "   Setup Complete!"
echo "========================================"
echo ""
echo "To start the development server:"
echo "  1. Run: source venv/bin/activate"
echo "  2. Run: python manage.py runserver"
echo ""
echo "Then open your browser to:"
echo "  Website: http://127.0.0.1:8000/"
echo "  Admin Panel: http://127.0.0.1:8000/admin/"
echo ""
