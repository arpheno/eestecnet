from rest_framework_nested import routers
from apps.legacy.views import Accounts, Events, Teams

from apps.teams.views import BaseTeamViewSet, InternationalTeamViewSet
from apps.teams.views import CommitmentViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

legacyrouter = routers.SimpleRouter()
legacyrouter.register(r'teams', Teams)
legacyrouter.register(r'events', Events)
legacyrouter.register(r'accounts', Accounts)


