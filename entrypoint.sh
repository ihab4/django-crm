#!/bin/bash

python3 manage.py migrate --no-input

gunicorn crm.application --bind 0.0.0.0:8000
