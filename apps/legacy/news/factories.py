import factory

from apps.legacy.account.factories import LegacyAccountFactory
from apps.legacy.news.models import Membership
from apps.legacy.teams.factories import LegacyTeamFactory


__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class LegacyMembershipFactory(factory.DjangoModelFactory):
    class Meta:
        model = Membership

    user = factory.SubFactory(LegacyAccountFactory, first_name="a", middle_name="b",
                              last_name="c")
    team = factory.SubFactory(LegacyTeamFactory, name="munich")

