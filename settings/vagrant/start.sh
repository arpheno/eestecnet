#!/bin/sh -e
cd /vagrant
sudo pip install -r /vagrant/requirements.txt
python manage.py makemigrations --settings=settings.deployment
python manage.py migrate --settings=settings.deployment
python manage.py collectstatic --noinput  --settings=settings.deployment
sudo service supervisor stop
sudo service supervisor start
sudo nginx -s reload
