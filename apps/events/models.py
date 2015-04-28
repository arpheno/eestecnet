from django.contrib.auth.models import User, Permission

from django.contrib.contenttypes.models import ContentType
from guardian.shortcuts import assign_perm
from polymorphic import PolymorphicModel

from apps.accounts.models import Account

from common.models import Applicable


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your models here.
class BaseEvent(Applicable):
    """ Model that stores basic information common to all events."""

    @property
    def organizers(self):
        result, created = self.packages.get_or_create(name=self.name + '_Organizers')
        if created:
            label = self._meta.object_name
            assign_perm('change_' + label.lower(), result, self)
        return result

    @property
    def officials(self):
        result, created = self.packages.get_or_create(name=self.name + '_Officials')
        return result

    def save(self, **kwargs):
        result = super(BaseEvent, self).save(**kwargs)
        return result


class Workshop(BaseEvent):
    """ Workshops as defined in the ROP. """
    pass


class Exchange(BaseEvent):
    """ Exchanges as defined in the ROP ."""
    pass


class Training(BaseEvent):
    """ Training Sessions held by EESTEC Trainers ."""
    pass




