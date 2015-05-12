from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import CharField, \
    TextField
from guardian.shortcuts import assign_perm
from polymorphic import PolymorphicModel

from apps.accounts.models import Account, Group
from apps.teams.models import BaseTeam
from common.models import Applicable, Confirmable, Confirmation
from common.util import Reversable


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Announcement(Confirmable, Reversable):
    """
    Class that encapsulates logic for things that can be
    published on the website intended for the general public.
    Possibly having pictures pointed at.
    """

    name = CharField(max_length=300)
    description = TextField(max_length=300)

    def save(self, *args, **kwargs):
        if not self.pk:
            result = super(Announcement, self).save()
            i = Confirmation.objects.create(confirmable=self)
            assign_perm('change_confirmation',
                        Applicable.objects.get(name="international board").organizers, i)
        else:
            result = super(Announcement, self).save()
        return result

    def __unicode__(self):
        return unicode(self.name)


class News(Announcement):
    pass


class CareerOffer(Announcement):
    pass


