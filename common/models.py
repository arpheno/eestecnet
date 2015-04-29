from django.db.models import CharField
from polymorphic import PolymorphicModel

__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Managable(PolymorphicModel):
    pass
class Applicable(PolymorphicModel):
    """
    Basic model that can have groups of users and accepts applications to those groups.
    """
    name = CharField(max_length=50)


