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
When it's done installing please type
choco install python2 git pip pycharm-community

Alternatively you can install the pycharm professional edition from their website if you're a student.
Debian/Ubuntu
=============

In a command shell do ::
sudo apt-get install pip virtualenv

If you want the pycharm IDE, google it and install it. It's awesome, seriously.


**Configuration**

*Git:*

In PyCharm go to File->Settings -> Version Control -> Git and set your git path accordingly
For example C:\Program Files (x86)\Git\cmd\git.exe

*Github:*

In PyCharm go to File->Settings -> Version Control -> Github and set your github information accordingly.

*Python:*

In PyCharm go to File->Settings -> Project Interpreter-> Configure interpreters
If your python installation is not there yet, add it.
In the window Packages below, select install and install

* pip
* virtualenv
* setuptools

 Now use Tools => open terminal to open a terminal. ::

     pip install -r requirements.txt

 This command will install all dependencies.
 Some python modules have to be compiled for your platform. Please install a C compiler like
 Visual Studio or MinGW it's very difficult otherwise.

For the windows version you will have to install cygwin and add it to your path. Make sure the gnu file utility is installed
and also the library cygmagic. In site-packages/magic.py on windows change "win32": XXXXX to "win32":"cygmagic-1.dll" .

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

Import EESTECNET
################
In pycharm select “VCS-> checkout from version control -> github”
Git repository url: https://github.com/arpheno/eestecnet
Hit clone
Everything should download now.
