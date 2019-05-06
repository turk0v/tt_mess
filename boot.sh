#!/bin/sh
source "venv/bin/activate"
flask db upgrade
gunicorn --bind 0.0.0.0:5000 wsgi:app
