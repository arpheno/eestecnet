from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models import BooleanField, ForeignKey, CharField, TextField

from apps.accounts.models import Account


__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your models here.
class BaseEvent(models.Model):
    """ Model that stores basic information common to all events."""
    name = CharField(max_length=50)

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


class Package(Group):
    """ Events can have different packages, which can contain participants. """
    event = ForeignKey('events.BaseEvent', related_name='packages')
    users = models.ManyToManyField('accounts.Account', through='events.Participation')

    def save(self, **kwargs):
        # Make sure the name is unique before saving
        self.name = self.event.name + "_" + self.name
        result = super(Package, self).save(**kwargs)

        # Make sure all users are in the group, put after super in case we create an
        # object.
        self.user_set = self.users.all()
        return result


class Participation(models.Model):
    """ Participations hold information about the application, the transport,
    and feedback when attending an event."""
    user = ForeignKey('accounts.Account')
    package = ForeignKey('events.Package')
    accepted = BooleanField(default=False)
    confirmed = BooleanField(default=False)

    def save(self, **kwargs):
        super(Participation, self).save(**kwargs)


class Questionnaire(models.Model):
    """ Questionnaires store information about Questions that Event organizers would like
    to ask their (potential) participants. """
    package = ForeignKey('events.Package')


class Question(models.Model):
    """ Questions appear as atoms in Questionnaires """
    questionnaire = ForeignKey('events.Questionnaire')
    question = TextField()

