#!/bin/sh -e
cd /vagrant
sudo service supervisor restart
sudo service nginx restart
