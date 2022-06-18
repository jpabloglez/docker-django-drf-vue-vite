#!/bin/sh
python /opt/backend/manage.py collectstatic --noinput --clear
python /opt/backend/manage.py migrate
uwsgi --ini /production.ini

