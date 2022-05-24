#EMS


server {
    listen 80;
    server_name 212.16.66.13;

    location / {
        proxy_set_header   X-Forwarded-For $remote_addr;
        proxy_set_header   Host $http_host;
        proxy_pass         "http://127.0.0.1:8000";
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location /static/ {
        root /var/ems;
    }
}

#!/bin/sh
pkill -f celery
pkill -f runserver
cd /var/ems
setenforce 0
source venv/bin/activate
screen -m -d hypercorn ems.asgi:application
#screen -m -d python manage.py runserver
celery -A ems purge -f
screen -m -d celery -A ems beat
screen -m -d celery -A ems worker
