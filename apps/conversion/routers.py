from rest_framework.routers import DefaultRouter
from apps.conversion.viewsets import lTeams, lEvents, lAccounts, lEntries

__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
lrouter =DefaultRouter(trailing_slash=False)
lrouter.register('teams',lTeams)
lrouter.register('events',lEvents)
lrouter.register('accounts',lAccounts)
lrouter.register('entries',lEntries)
