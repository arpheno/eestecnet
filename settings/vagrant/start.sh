#!/bin/sh -e
cd /vagrant
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
sudo service supervisor stop
sudo service supervisor start
sudo nginx -s reload
