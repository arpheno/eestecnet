#!/bin/sh -e
sudo apt-get -y update
sudo apt-get -y install postgresql-server-dev-9.1 postgresql-9.1 postgresql-contrib-9.1
sudo apt-get -y install  nginx memcached python-pip libjpeg-dev
sudo apt-get -y install  python-dev g++ vim supervisor libffi-dev
sudo pip install gunicorn psycopg2 python-memcached pytest-django pytest-xdist
sudo pip install django-debug-toolbar django-statsd-mozilla https://github.com/graphite-project/ceres/tarball/master whisper carbon graphite-web
sudo pip install -r /vagrant/requirements.txt
sudo apt-get install npm -y
sudo npm config set registry http://registry.npmjs.org/
sudo npm install -g coffee-script

