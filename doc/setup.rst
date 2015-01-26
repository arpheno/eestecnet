===================================
How to set up for local development
===================================
This tutorial will help you install python on your windows machine.

You will also install the PyCharm IDE and git. After the installation you will be able to run eestec.net on
your own machine, write and modify code, and upload your changes using git.

Setup
=====

Feel free to leave out any steps you have already completed.

Windows
=======
Please install chocolatey from http://chocolatey.org/
To do this, open an administrative command shell (cmd.exe) and copy&paste the following ::

    @powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
When it's done installing please type ::

    choco install python2 git pip vim npm cygwin
    cd C:\users\*your username*\
    mkdir development
    cd development
    pip install virtualenv
    virtualenv .
    git clone http://github.com/arpheno/eestecnet/
    scripts\activate
    cd eestecnet
    pip install -r requirements.txt
    npm install -g coffee
Additionally you will have to install cygwin and copy some files: ::

    cd C:\tools\cygwin\bin
    cp cygwin1.dll cygz.dll cygmagic-1.dll cyggcc_s-1.dll C:\windows\system32


Alternatively instead of vim you can install the pycharm professional edition from their website if you're a student.


Debian/Ubuntu
=============

In a command shell do ::

    sudo apt-get install pip virtualenv coffeescript
    cd
    mkdir development
    cd development
    pip install virtualenv
    virtualenv .
    git clone http://github.com/arpheno/eestecnet/
    source bin/activate
    cd eestecnet
    pip install -r requirements.txt


If you want the pycharm IDE, google it and install it. It's awesome, seriously.

Some python modules have to be compiled for your platform. Please install a C compiler like
Visual Studio or MinGW or the GNU compiler collection, it's very difficult otherwise.


Local
#####
Activate your virtualenv.
Navigate to the project root and do ::
    python manage.py syncdb
    python manage.py migrate
    python manage.py runserver

This will launch a local webserver on port 8000.
The website will now display, albeit with no preloaded content.
If you want to preload content, hit CTRL + C and do ::
    python manage.py shell
    >>> from eestecnet.views import init
    >>> init(5)

This will preload some content, including an admin account with login credentials:

username arpheno@gmail.com
password test

Server
######
To run in a production environment several programs are required to run as well.
Memcached is a very efficient cache.
Memcached should run on port 11212 as a daemon ::

    memcached -d -P memcached.pid -p 11212

Celery is a module that makes asynchronous processing of messages possible. It's important
for sending e-mails without blocking the actual process. Otherwise sending e-mails can take
a very long time. ::
    python eestecnet/manage.py celery worker -l debug --workdir=. --pool=threads -f celery.log --pidfile=celery.pid &

gunicorn is a webserver implemented in python that will be responsible to serve all dynamic requests (i.e. not static files or user data)
it has to be configured with nginx, so nginx serves all static files. ::
    gunicorn --env DJANGO_SETTINGS_MODULE=eestecnet.settings.deployment --settings eestecnet.settings.deployment eestecnet.wsgi -b 0.0.0.0:8003 -p ../unstable.pid -D

There are some useful scripts in the scripts folder, however you will have to adjust them to your paths.(I'm assuming the old server burnt down or something)

