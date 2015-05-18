from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import ForeignKey, ManyToManyField, IntegerField
from guardian.shortcuts import assign_perm
from polymorphic import PolymorphicModel

from apps.accounts.models import Account
from apps.events.models import BaseEvent
from apps.teams.models import Commitment
from common.models import Applicable
from common.util import Reversable


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Priority(PolymorphicModel, Reversable):
    """
    Through model to attach the actual priority to an individual.
    """

    class Meta:
        unique_together = ('priority', 'priority_list')

    priority_list = ForeignKey('prioritylists.PriorityList')
    user = ForeignKey(Account)
    priority = IntegerField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.priority)


class PriorityList(PolymorphicModel, Reversable):
    """
    Prioritylists are sent out by commitments to rank the applications for an event
    against
    each other.
    """

    class Meta:
        unique_together = ('event', 'commitment')

    event = ForeignKey(BaseEvent)
    commitment = ForeignKey(Commitment)
    users = ManyToManyField(Account, through='prioritylists.Priority')

    def save(self, *args, **kwargs):
        """
        When a prioritylist is created, the sending commitment's board should be able
        to set the priorities,
        and the receiving event's oganizers should have view rights.
        The corresponding Priority objects need to be created as well.
        """
        if self.pk:
            result = super(PriorityList, self).save(*args, **kwargs)
        else:
            result = super(PriorityList, self).save(*args, **kwargs)
            assign_perm('view_prioritylist', self.event.organizers, self)
            assign_perm('change_prioritylist', self.commitment.board, self)
            for user in self.event.officials.user_set.all():
                Priority.objects.create(user=user, priority_list=self)
        return result


