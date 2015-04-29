from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import ForeignKey, TextField
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
        result, created = self.packages.get_or_create(name=self.name + '_organizers')
        if created:
            label = self._meta.object_name
            assign_perm('change_' + label.lower(), result, self)
        return result

    @property
    def officials(self):
        result, created = self.packages.get_or_create(name=self.name + '_officials')
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


class Questionnaire(models.Model):
    """ Questionnaires store information about Questions that Event organizers would like
    to ask their (potential) participants. """
    group = ForeignKey('accounts.Group')


class Question(models.Model):
    """ Questions appear as atoms in Questionnaires """
    questionnaire = ForeignKey('events.Questionnaire')
    question = TextField()