from fabric.operations import local

__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def remove_migrations():
    apps = local('ls -1 apps', capture=True).split()
    for app in apps:
        try:
            local('rm apps/' + app + '/migrations/0*')
        except:
            pass
    try:
        local('rm common/migrations/0*')
    except:
        pass

def cleanup():
    local(r"find . -name '*.pyc' -delete")
def test():
    apps = local('ls  -d -1 apps/*/', capture=True).split()
    files = [app + "tests.py" for app in apps]
    local(r'py.test common/tests.py ' + " ".join(files))
def coverage():
    apps = local('ls  -d -1 apps/*/', capture=True).split()
    files = [app + "tests.py" for app in apps]
    local(r'coverage run --source . -m py.test common/tests.py ' + " ".join(files))
