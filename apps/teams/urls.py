from rest_framework_nested import routers

from apps.teams.views import BaseTeamViewSet, InternationalTeamViewSet
from apps.teams.views import CommitmentViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

teamrouter = routers.SimpleRouter()
teamrouter.register(r'teams', BaseTeamViewSet)
teamrouter.register(r'commitments', CommitmentViewSet)
teamrouter.register(r'internationalteams', InternationalTeamViewSet)


