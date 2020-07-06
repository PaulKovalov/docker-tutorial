#!/bin/sh
python3 django_docker/manage.py migrate --no-input
python3 django_docker/manage.py collectstatic --no-input
uwsgi --http-socket 127.0.0.1:3031 --chdir ./django_docker/ --wsgi-file django_docker/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191