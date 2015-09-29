from rest_framework_nested import routers
from apps.legacy.views import Accounts, Events, Teams, Entries

from apps.teams.views import BaseTeamViewSet, InternationalTeamViewSet
from apps.teams.views import CommitmentViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

legacyrouter = routers.SimpleRouter()
legacyrouter.register(r'teams', Teams,'legacyteams')
legacyrouter.register(r'events', Events,'legacyevents')
legacyrouter.register(r'accounts', Accounts,'legacyaccounts')
legacyrouter.register(r'entries', Entries,'legacyentries')


