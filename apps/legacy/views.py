from rest_framework.viewsets import ModelViewSet

from apps.accounts.models import Account
from apps.announcements.models import Announcement
from apps.events.models import BaseEvent
from apps.legacy.account.serializers import ConversionAccountSerializer
from apps.legacy.events.serializers import ConversionEventSerializer
from apps.legacy.news.serializers import ConversionEntrySerializer
from apps.legacy.teams.serializers import ConversionTeamSerializer
from apps.teams.models import BaseTeam


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Accounts(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = ConversionAccountSerializer


class Teams(ModelViewSet):
    queryset = BaseTeam.objects.all()
    serializer_class = ConversionTeamSerializer


class Events(ModelViewSet):
    queryset = BaseEvent.objects.all()
    serializer_class = ConversionEventSerializer
    def create(self, request, *args, **kwargs):
        try:
            return super(Events, self).create(request,*args,**kwargs)
        except Exception as e:
            import pdb;pdb.set_trace()

class Entries(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = ConversionEntrySerializer
    def create(self, request, *args, **kwargs):
        try:
            return super(Entries, self).create(request,*args,**kwargs)
        except Exception as e:
            import pdb;pdb.set_trace()








