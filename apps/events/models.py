from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import ForeignKey, OneToOneField, DateTimeField, CharField, \
    TextField, DateField, IntegerField
from guardian.shortcuts import assign_perm
from polymorphic import PolymorphicModel

from apps.accounts.models import Account, Participation
from common.models import Applicable, Confirmable, Confirmation, Notification
from common.util import Reversable
from settings.conf.choices import TRAVEL_CHOICES


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your models here.
class ShortEvent(models.Model):
    """ Some Events last longer than a day """

    class Meta:
        abstract = True

    date = DateField()


class LongEvent(models.Model):
    """ Some Events last longer than a day """

    class Meta:
        abstract = True

    start_date = DateField()
    end_date = DateField()


class PhysicalEvent(models.Model):
    class Meta:
        abstract = True

    location = CharField(max_length=200)
class BaseEvent(Applicable, Reversable):
    """ Model that stores basic information common to all events."""

    owner = ForeignKey('accounts.Account', editable=False)
    images = GenericRelation('common.Image', related_query_name='images')
    reports = GenericRelation('common.Report', related_query_name='reports')
    deadline = DateTimeField(null=True, blank=True)
    unofficial_fee = IntegerField(blank=True, null=True)
    max_participants = IntegerField(blank=True, null=True)
    @property
    def organizers(self):
        return self.group_set.get(name=self.name + '_organizers')

    @property
    def officials(self):
        return self.group_set.get(name=self.name + '_officials')

    def save(self, **kwargs):
        """
        When an Event is first created two groups should always be created:
        Official participants and organizers. Organizers need the right to modify the
        event.
        """
        if self.pk:
            result = super(BaseEvent, self).save(**kwargs)
        else:
            result = super(BaseEvent, self).save(**kwargs)
            self.group_set.create(name=self.name + '_officials')
            self.group_set.create(name=self.name + '_organizers')
            Participation.objects.create(confirmed=True, group=self.organizers,
                                         user=self.owner)
            label = self._meta.object_name
            assign_perm('change_' + label.lower(), self.organizers, self)
            assign_perm('view_' + label.lower(), self.organizers, self)
            assign_perm('delete_' + label.lower(), self.organizers, self)

        return result


class Workshop(BaseEvent, LongEvent, PhysicalEvent):
    """ Workshops as defined in the ROP. """
    pass


class Exchange(BaseEvent, LongEvent, PhysicalEvent):
    """ Exchanges as defined in the ROP ."""
    participation_fee = IntegerField()


class Training(BaseEvent, ShortEvent, PhysicalEvent):
    """ Training Sessions held by EESTEC Trainers ."""
    pass


class Travel(Notification, Reversable):
    participation = OneToOneField('accounts.Participation')
    arrival_datetime = DateTimeField()
    arrival_mode = CharField(max_length=100, choices=TRAVEL_CHOICES)
    departure_datetime = DateTimeField()
    departure_mode = CharField(max_length=100, choices=TRAVEL_CHOICES)
    comment = TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            result = super(Travel, self).save(*args, **kwargs)
            label = self._meta.object_name
            assign_perm('view_' + label.lower(),
                        self.participation.package.applicable.organizers, self)
            assign_perm('view_' + label.lower(), self.participation.user, self)
            assign_perm('change_' + label.lower(), self.participation.user, self)
        else:
            result = super(Travel, self).save(*args, **kwargs)
        return result

class ParticipationConfirmation(Confirmable, Confirmation, object):
    """
    A two stage confirmation that requires the organizers to accept a participant,
    before that participant is able to confirm their participation.
    """

    @property
    def acceptance(self):
        return self.confirmation_set.all()[0]
    def on_confirm(self):
        """
        When a participation is accepted by the organizing committee, the applicant
        should be granted rights to confirm their participation.
        """
        assign_perm('change_participationconfirmation', self.confirmable.user, self)
    def save(self, *args, **kwargs):
        if not self.pk:
            result = super(ParticipationConfirmation, self).save(*args, **kwargs)
            acceptance = Confirmation.objects.create(confirmable=self)
            assign_perm('change_confirmation',
                        self.confirmable.package.applicable.organizers, acceptance)
        else:
            result = super(ParticipationConfirmation, self).save(*args, **kwargs)

        self.confirmable.check_confirm()

        return result
