[![Build Status](https://travis-ci.org/arpheno/eestecnet.svg?branch=green)](https://travis-ci.org/arpheno/eestecnet)
# EESTECNET

## Motivation

The motivation for creating this open source project is to provide an online platform for the
Electrical Engineering Students' European Association (EESTEC). Its purpose is to serve
as a central communication and administration hub for the association and preserve knowledge for
future generations.

===================================
How to set up for local development
===================================

Windows
=======
Please install chocolatey from http://chocolatey.org/
To do this, open an administrative command shell (cmd.exe) and copy&paste the following ::

    @powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

When it's done installing please type ::

    choco install git virtualbox vagrant
    git clone http://github.com/Sebastian Woznyo/eestecnet/
    vagrant up
    vagrant ssh


Debian/Ubuntu
=============

In a command shell do ::

    sudo apt-get install git virtualbox vagrant
    git clone http://github.com/Sebastian Woznyo/eestecnet/
    pip install -r requirements.txt
    vagrant up
    vagrant ssh


If you want the pycharm IDE, google it and install it. It's awesome, seriously.

Some python modules have to be compiled for your platform. Please install a C compiler like
Visual Studio or MinGW or the GNU compiler collection, it's very difficult otherwise.


Local
#####
Navigate to the project root and do ::

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver 0.0.0.0:8000

This will launch a local webserver on port 8000.
The website will now display, albeit with no preloaded content.
