#!/bin/sh -e
sudo apt-get -y update
sudo apt-get -y install postgresql-server-dev-9.1 postgresql-9.1 postgresql-contrib-9.1
sudo apt-get -y install  nginx memcached python-pip libjpeg-dev
sudo apt-get -y install  python-dev g++ vim supervisor
sudo pip install gunicorn psycopg2
sudo pip install -r /vagrant/requirements.txt

