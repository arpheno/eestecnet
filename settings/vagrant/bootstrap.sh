#!/bin/sh -e
sudo apt-get -y update
sudo apt-get -y install postgresql-server-dev-9.3 postgresql-9.3 postgresql-contrib-9.3
sudo apt-get -y install  nginx memcached python-pip libjpeg-dev libclosure-compiler-java
sudo apt-get -y install  python-dev g++ vim supervisor npm curl git
sudo rm -f /usr/bin/node
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo npm install -g bower babel protractor grunt
sudo pip install gunicorn psycopg2 python-memcached pytest-django pytest-xdist ijson
sudo pip install -r /vagrant/requirements.txt
cd /vagrant
bower install --allow-root
