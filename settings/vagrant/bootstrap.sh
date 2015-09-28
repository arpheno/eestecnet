#!/bin/sh -e
sudo apt-get -y update
sudo apt-get -y install libjpeg-dev libclosure-compiler-java
sudo apt-get -y install python-pip python-dev g++ vim  npm curl git supervisor
sudo rm -f /usr/bin/node
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo ln -sfn /vagrant/settings/etc/supervisor/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf -f
sudo npm install -g bower babel protractor grunt-cli
sudo pip install pytest-django pytest-xdist ijson coverage
sudo pip install -r /vagrant/requirements.txt
sudo apt-get -y install postgresql-server-dev-9.3 supervisor nginx memcached
cd /vagrant
bower install --allow-root
npm install grunt
sudo service supervisor restart
