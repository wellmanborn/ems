#!/bin/sh
pkill -f celery
pkill -f runserver
cd /var/ems
source venv/bin/activate
screen -m -d python manage.py runserver
celery -A ems purge -f
screen -m -d celery -A ems beat
screen -m -d celery -A ems worker