#! /bin/bash

if ["$#" != "1"]; then
    echo "The name of the app must be provided"
else
    ./venv/bin/pip install -r requirements.txt
    cd app && ../venv/bin/python manage.py startapp $1
fi