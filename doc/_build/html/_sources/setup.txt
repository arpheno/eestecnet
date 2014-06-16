===================================
How to set up for local development
===================================
This tutorial will help you install python on your windows machine.

You will also install the PyCharm IDE and git. After the installation you will be able to run eestec.net on
your own machine, write and modify code, and upload your changes using git.

Setup
=====

Feel free to leave out any steps you have already completed.

Python
######
The first thing you need to do is get a working python interpreter. EESTECNET will run python 2.7 because it is more compatible with django.

**Download**

https://www.python.org/ftp/python/2.7.7/python-2.7.7.msi and install it with default options. it will be installed under C:\\python27\\

**Configuration**

* Control panel
* Open System Properties
* Switch to the Advanced tab
* Click Environment Variables
* Select PATH in the System variables section
* Click Edit
* Add python's path to the end of the list (the paths are separated by semicolons). For example::
        C:\\Windows;C:\\Windows\\System32;C:\\Python27
* Save


Git and Github
##############

**Download git**

http://git-scm.com/download/win

**Create a github account**

https://github.com/

JetBrains PyCharm IDE
#####################

I’m a vim guy and I hate to use anything but vim. This IDE kicks so much ass though, that I never want to develop with anything else ever. ( There is a VIM plugin ;) )

**Download**

http://www.jetbrains.com/pycharm/download/  Make sure you get the *professional edition* you have 30 days free trial. Then contact arpheno@gmail.com

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
* django
* gunicorn
* setuptools
* sorl-thumbnail

Additionally install Pillow, but you have to check the “options” checkbox and provide --wheel as options.

Import EESTECNET
################
In pycharm select “VCS-> checkout from version control -> github”
Git repository url: https://github.com/arpheno/eestecnet
Hit clone
Everything should download now.
