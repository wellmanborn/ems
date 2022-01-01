#!/bin/sh
pkill -f celery
pkill -f runserver
pkill -f hypercorn
#cd /var/ems
#setenforce 0
#source venv/bin/activate
#screen -m -d hypercorn ems.asgi:application
#screen -m -d python manage.py runserver
#celery -A ems purge -f
#screen -m -d celery -A ems beat
#screen -m -d celery -A ems worker
