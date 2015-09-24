from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import ForeignKey, IntegerField
from guardian.shortcuts import assign_perm

from common.models import Applicable, NameMixin, DescriptionMixin
from common.util import Reversable

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your models here.
class BaseTeam(Applicable, Reversable, NameMixin, DescriptionMixin):
    owner = ForeignKey('accounts.Account', editable=False)
    images = GenericRelation('common.Image', related_query_name='images')
    locations = GenericRelation('common.Location', related_query_name='locations')
    urls = GenericRelation('common.URL', related_query_name='urls')

    @property
    def location(self):
        return self.locations.all()[0]
    def save(self, **kwargs):
        """
        When an Event is first created two groups should always be created:
        Official participants and organizers. Organizers need the right to modify the event.
        """
        if self.pk:
            result = super(BaseTeam, self).save(**kwargs)
        else:
            result = super(BaseTeam, self).save(**kwargs)
            self.group_set.create(name=self.name + '_organizers')
            self.group_set.create(name=self.name + '_members')
            self.group_set.create(name=self.name + '_alumni')
            from apps.accounts.models import Participation

            Participation.objects.create(confirmed=True, group=self.board,
                                         user=self.owner)
            label = self._meta.object_name
            assign_perm('change_' + label.lower(), self.board, self)
            assign_perm('delete_' + label.lower(), self.board, self)
            assign_perm('view_' + label.lower(), self.board, self)

        return result
    @property
    def organizers(self):
        return self.group_set.get(name=self.name + '_organizers')

    @property
    def board(self):
        return self.group_set.get(name=self.name + '_organizers')
    @property
    def users(self):
        return self.group_set.get(name=self.name + '_members')

class Commitment(BaseTeam):
    RANKS = [(0, 'Observer'), (1, 'JLC'), (2, 'LC')]
    founded = IntegerField(blank=True, null=True)
    rank = IntegerField(choices=RANKS, default=0, blank=True, null=True)
class InternationalTeam(BaseTeam):
    pass


class InternationalBody(BaseTeam):
    pass


class InternationalDepartment(BaseTeam):
    pass
