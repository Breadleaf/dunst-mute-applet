#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: ./start.sh [1 | 2]"
    exit 1
fi

# if ./venv/ does not exist, create it
if [ ! -d "./venv/" ]; then
    python3 -m venv venv > /dev/null 2>&1
fi

# activate the virtual environment
source venv/bin/activate

# install the required packages
pip install -r requirements.txt > /dev/null 2>&1

# run the application
python3 main.py $1 > /dev/null 2>&1
