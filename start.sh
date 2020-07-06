#!/bin/sh
python3 django_docker/manage.py migrate --no-input
python3 django_docker/manage.py collectstatic --no-input
python3 django_docker/manage.py runserver