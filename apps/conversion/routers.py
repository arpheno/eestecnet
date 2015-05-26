from rest_framework.routers import DefaultRouter
from apps.conversion.viewsets import Teams, Events, Accounts, Entries

__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
lrouter =DefaultRouter(trailing_slash=False)
lrouter.register('teams',Teams)
lrouter.register('events',Events)
lrouter.register('accounts',Accounts)
lrouter.register('entries',Entries)
