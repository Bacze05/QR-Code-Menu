#!/bin/bash
DJANGO_DIR=$(dirname $(cd "$(dirname "$0")" && pwd))
DJANGO_SETTINGS_MODULE=QRMenu.settings
cd $DJANGO_DIR
source env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
exec python manage.py runserver 0:8000
