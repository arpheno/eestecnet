from django.contrib import auth
from django.db import models
from django.db.models import ForeignKey, BooleanField, CharField, TextField
from polymorphic import PolymorphicModel

__author__ = 'Arphen'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Applicable(PolymorphicModel):
    """
    Basic model that can have groups of users and accepts applications to those groups.
    """
    name = CharField(max_length=50)


class Group(auth.models.Group):
    """  have different packages, which can contain participants. """
    applicable = ForeignKey('common.Applicable', related_name='packages')
    users = models.ManyToManyField('accounts.Account', through='common.Participation')

    def save(self, **kwargs):
        if not self.pk:
            pass
        result = super(Group, self).save(**kwargs)
        # Make sure all users are in the group, put after super in case we create an
        # object.
        self.user_set = self.users.all()
        return result


class Participation(models.Model):
    """ Participations hold information about the application, the transport,
    and feedback when attending an event."""
    user = ForeignKey('accounts.Account')
    group = ForeignKey('common.Group')
    accepted = BooleanField(default=False)
    confirmed = BooleanField(default=False)

    def save(self, **kwargs):
        super(Participation, self).save(**kwargs)
        self.group.user_set = self.group.users.all()


class Questionnaire(models.Model):
    """ Questionnaires store information about Questions that Event organizers would like
    to ask their (potential) participants. """
    group = ForeignKey('common.Group')


class Question(models.Model):
    """ Questions appear as atoms in Questionnaires """
    questionnaire = ForeignKey('common.Questionnaire')
    question = TextField()

