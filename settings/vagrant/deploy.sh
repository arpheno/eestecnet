#!/bin/sh -e
chmod 777 -R /var/log /var/run
sudo rm -rf /var/www
sudo mkdir -p /var/www
sudo mkdir -p /var/run
sudo ln -s /vagrant /var/www/eestecnet -f
sudo ln -s /vagrant/settings/etc/supervisor/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf -f
sudo ln -s /vagrant/settings/etc/nginx.conf /etc/nginx/sites-enabled/default -f
sudo service nginx start
sudo nginx -s reload
cd /vagrant

