from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import ForeignKey
from guardian.shortcuts import assign_perm
from polymorphic import PolymorphicModel

from apps.accounts.models import Account, Group
from apps.teams.models import BaseTeam
from common.models import Applicable, Confirmable, Confirmation, NameMixin, \
    DescriptionMixin
from common.util import Reversable


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Announcement(Confirmable, Reversable, NameMixin, DescriptionMixin):
    """
    Class that encapsulates logic for things that can be
    published on the website intended for the general public.
    Possibly having pictures pointed at.
    """

    owner = ForeignKey('accounts.Account', editable=False)
    images = GenericRelation('common.Image', related_query_name='images')

    def save(self, *args, **kwargs):
        if not self.pk:
            result = super(Announcement, self).save()

            assign_perm('change_'+self._meta.object_name.lower(),self.owner,self)
            assign_perm('view_'+self._meta.object_name.lower(),self.owner,self)
            assign_perm('delete_'+self._meta.object_name.lower(),self.owner,self)
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


