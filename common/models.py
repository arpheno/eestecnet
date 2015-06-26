from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import CharField, DateField, BooleanField, ForeignKey, TextField, \
    AutoField, SET_NULL, ImageField, PositiveIntegerField, FloatField, URLField
from polymorphic import PolymorphicModel

from common.util import Reversable

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class DescriptionMixin(models.Model):
    class Meta:
        abstract = True

    description = TextField(blank=True, null=True)

class NameMixin(models.Model):
    class Meta:
        abstract = True

    name = CharField(max_length=300)

class Confirmable(PolymorphicModel):
    """
    Confirmables have two states: Confirmed(Approved) or pending.
    """
    confirmable_identifier = AutoField(primary_key=True)
    confirmed = BooleanField(default=False, editable=False)

    def on_confirm(self):
        pass

    def check_confirm(self):
        """
        Called by a confirmable's confirmations when they are confirmed. If all
        pending confirmations for the object are resolved, set the confirmed attribute
        to True and save. Classes derived from this class may implement on_confirm to
        run custom actions upon confirmation.
        """

        if self.pk and all(
                confirmation.status for confirmation in self.confirmation_set.all()):
            self.on_confirm()
            self.confirmed = True
            self.save()


class Notification(PolymorphicModel, DescriptionMixin):
    """
    Notifications prompt users for action
    """
    pass

class Confirmation(Notification):
    """
    A model that represents the approval of another object by a party,
    which might be a group of users or a user.
    """
    requested = DateField(auto_now=True)
    status = BooleanField(default=False)
    # Because of a bug in django this needs to be deactivated on the first
    # makemigrations call and put in a separate call

    # author = ForeignKey('accounts.Account', null=True, blank=True)
    confirmable = ForeignKey('common.Confirmable', on_delete=SET_NULL, null=True,
                             blank=True)

    def confirm(self):
        self.status = True
        self.save()
        self.confirmable.check_confirm()
    def save(self, *args, **kwargs):
        """
        When a confirmation is saved it should notify its parent about potential changes.
        """
        result = super(Confirmation, self).save(*args, **kwargs)
        self.confirmable.check_confirm()
        return result


class Applicable(Confirmable):
    """
    Basic model that can have groups of users and accepts applications to those groups.
    """

    @property
    def applications(self):
        result = [p for g in self.group_set.all() for p in
                  g.participation_set.filter(confirmed=False)]
        return result

    @property
    def participations(self):
        result = [p for g in self.group_set.all() for p in
                  g.participation_set.filter(confirmed=True)]
        return result

    @property
    def applicants(self):
        result = [p.user for g in self.group_set.all() for p in
                  g.participation_set.filter(confirmed=False)]
        return result

    @property
    def members(self):
        return self.participants
    @property
    def participants(self):
        result = [p.user for g in self.group_set.all() for p in
                  g.participation_set.filter(confirmed=True)]
        return result


class Report(PolymorphicModel, NameMixin, DescriptionMixin):
    """ Reports to stuff """
    content_type = ForeignKey(ContentType)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey()


class URL(PolymorphicModel, NameMixin):
    content_type = ForeignKey(ContentType)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey()
    url = URLField(max_length=255)


class Content(PolymorphicModel):
    name = CharField(max_length=255, unique=True)
    content = TextField(blank=True, null=True)
    images = GenericRelation('common.Image', related_query_name='images')
class Location(PolymorphicModel):
    content_type = ForeignKey(ContentType)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey()
    string = CharField(max_length=200)
    latitude = FloatField(blank=True, null=True)
    longitude = FloatField(blank=True, null=True)
class Image(PolymorphicModel, Reversable):
    content_type = ForeignKey(ContentType)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey()
    full_size = ImageField(upload_to='images')
    thumbnail = BooleanField(default=False)


