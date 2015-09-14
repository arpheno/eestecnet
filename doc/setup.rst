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

