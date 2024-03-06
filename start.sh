#!/bin/bash

# if ./venv/ does not exist, create it
if [ ! -d "./venv/" ]; then
    python3 -m venv venv
fi

# activate the virtual environment
source venv/bin/activate

# install the required packages
pip install -r requirements.txt

# run the application
python3 main.py $1
