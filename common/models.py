from django.db.models import CharField, DateField, BooleanField, ForeignKey
from polymorphic import PolymorphicModel

__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Confirmable(PolymorphicModel):
    pass


class Confirmation(PolymorphicModel):
    """
    A model that represents the approval of another object by a party,
    which might be a group of users or a user.
    """
    requested = DateField(auto_now=True)
    status = BooleanField(default=False)
    author = ForeignKey('accounts.Account', null=True, blank=True)
    confirmable = ForeignKey('common.Confirmable')


class Applicable(Confirmable):
    """
    Basic model that can have groups of users and accepts applications to those groups.
    """
    name = CharField(max_length=50)
    def get_absolute_url(self):
        raise NotImplementedError("Child classes have to overwrite get_absolute_url")


