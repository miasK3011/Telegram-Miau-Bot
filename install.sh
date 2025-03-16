#!/usr/bin/env sh

check_status() {
    if [ $? -ne 0 ]; then
        echo "$1"
        exit 1
    fi
}

python3 --version > /dev/null 2>&1
if [ $? -eq 1 ]; then
    echo "Python3 is not installed. Installing Python3"
    sudo apt install -y python3
    check_status "Failed to install Python3"
    echo "Python3 installed successfully."
fi

if [ -d ".venv" ]; then
    echo "Virtual environment already exists. Skipping creation and activation."
    
    echo "Activating virtual environment..."
    . .venv/bin/activate
    check_status "Failed to activate virtual environment."
    echo "Virtual environment activated."
else
    echo "Creating virtual environment..."
    python3 -m venv .venv
    check_status "Failed to create virtual environment."
    echo "Virtual environment created."

    echo "Activating virtual environment..."
    . .venv/bin/activate
    check_status "Failed to activate virtual environment."
    echo "Virtual environment activated."

    echo "Installing dependencies..."
    pip install -r requirements.txt
    check_status "Failed to install dependencies."
    echo "Dependencies installed successfully."
fi

echo "Starting bot..."
python3 botmain.py