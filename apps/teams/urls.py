from rest_framework_nested import routers

from apps.teams.views import BaseTeamViewSet, InternationalTeamViewSet
from apps.teams.views import CommitmentViewSet


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)



