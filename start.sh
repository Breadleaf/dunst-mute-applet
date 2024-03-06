#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ $# -ne 1 ]; then
    echo "Usage: ./start.sh [1 | 2]" > $DIR/dunst-mute-applet.log 2>&1
    exit 1
fi

# if ./venv/ does not exist in DIR, create it
if [ ! -d "$DIR/venv/" ]; then
    python3 -m venv $DIR/venv > $DIR/dunst-mute-applet.log 2>&1
fi

# activate the virtual environment
source $DIR/venv/bin/activate

# install the required packages
pip install -r $DIR/requirements.txt > $DIR/dunst-mute-applet.log 2>&1

# run the application
python3 $DIR/main.py $1 > $DIR/dunst-mute-applet.log 2>&1
