#!/bin/sh -e
sudo chmod 777 -R /var/log /var/run
sudo rm -rf /var/www
sudo mkdir -p /var/www
sudo mkdir -p /var/run
sudo ln -sfn /vagrant /var/www/eestecnet -f
sudo ln -sfn /vagrant/settings/etc/supervisor/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf -f
sudo rm -f /etc/nginx/sites-enabled/default
sudo rm -f /etc/nginx/sites-enabled/eestec.conf
sudo ln -sfn /vagrant/settings/etc/nginx/sites-enabled/eestec.conf /etc/nginx/sites-enabled -f
sudo service nginx start
sudo nginx -s reload
cd /vagrant
fab remove_migrations

