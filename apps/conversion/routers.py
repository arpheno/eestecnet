from rest_framework.routers import DefaultRouter
from apps.conversion.viewsets import lTeams, lEvents, lAccounts

__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
lrouter =DefaultRouter(trailing_slash=False)
lrouter.register('lteams',lTeams)
lrouter.register('levents',lEvents)
lrouter.register('laccounts',lAccounts)
