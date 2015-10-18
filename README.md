[![Build Status](https://travis-ci.org/arpheno/eestecnet.svg?branch=green)](https://travis-ci.org/arpheno/eestecnet)
[![Coverage Status](https://coveralls.io/repos/arpheno/eestecnet/badge.svg?branch=green&service=github)](https://coveralls.io/github/arpheno/eestecnet?branch=green)
# EESTECNET

## Motivation

The motivation for creating this open source project is to provide an online platform for the
Electrical Engineering Students' European Association (EESTEC). Its purpose is to serve
as a central communication and administration hub for the association and preserve knowledge for
future generations.

===============
Getting Started
===============

Windows
=======
The easiest way to get all dependencies is to install chocolatey from http://chocolatey.org/
Chocolatey is a package manager for Windows and works similar to apt on Debian or yum on rpm based linux distributions.

To do this, open an administrative command shell (cmd.exe) and copy&paste the following ::

    @powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

When it's done installing please type ::

    choco install git virtualbox vagrant ssh

Alternativley install the dependencies manually and add them to your path.

Debian/Ubuntu
=============

In a command shell do ::

    sudo apt-get install git virtualbox vagrant

Development tools
=================

I personally recommend the JetBrains PyCharm IDE. It is available for free as in beer for students.

Set up
======

Everything will run inside a virtual machine on your machine, with all dependencies and tools encapsulated in that machine.
We use Vagrant to manage the virtualmachine.
Depending on your machine the following steps to pull the project and set up for local development may take several minutes.

    vagrant plugin install vagrant-reload
    git clone http://github.com/arpheno/eestecnet/
    vagrant up

When it finishes you should check localhost:8000 for a running instance of eestecnet,
if you encouncter problems :


    vagrant ssh
    cd /vagrant/
    sudo service supervisor stop
    sudo killall python
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver 0.0.0.0:8000

This will launch a local webserver on port 8000.
The website will now display, albeit with no preloaded content
