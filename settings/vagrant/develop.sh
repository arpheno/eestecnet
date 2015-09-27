#!/bin/sh -e
cd /vagrant
sudo ln -sfn /vagrant/settings/etc/supervisor/runserver.conf /etc/supervisor/conf.d/runserver.conf -f
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

