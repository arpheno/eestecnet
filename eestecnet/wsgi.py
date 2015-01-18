"""
WSGI config for eestecnet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eestecnet.settings.deployment")
import djcelery
os.environ['HTTPS'] = "on"
djcelery.setup_loader()
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
