#Empty required models file
import os

from eestecnet.settings import MEDIA_ROOT, MEDIA_URL
from elfinder.volumes.filesystem import ElfinderVolumeLocalFileSystem
from events.models import Event
from teams.models import Team


class Attribute(dict):
    def __init__(self, pattern, rights):
        super(dict, self).__init__()
        self['pattern'] = pattern
        self['read'] = "r" in rights
        self['write'] = "w" in rights
        self['hidden'] = "h" in rights
        self['locked'] = "l" in rights


class Root(dict):
    def __init__(self, name, priv=0):
        super(dict, self).__init__()
        self['driver'] = ElfinderVolumeLocalFileSystem
        self['path'] = os.path.join(MEDIA_ROOT, unicode(name))
        self['id'] = name
        self['alias'] = name
        self['URL'] = '%s%s/' % (MEDIA_URL, name)
        if not priv:
            self['attributes'] = []
            self['attributes'].append(Attribute("/internal","h"))
            self['attributes'].append(Attribute("/archive","r"))


def roots_for_user(user):
    """ Adds permissions to access filemanager """
    roots=[]
    if user.is_superuser:
        for member in Team.objects.all():
            roots.append(Root(member.slug,True))
        for event in Event.objects.all().exclude(category="recruitment"):
            roots.append(Root(event.slug,True))
        roots.append(Root("Public",True))
        return roots
    elif user.is_authenticated():
        for team in user.privileged.all():
            roots.append(Root(team.slug,True))
        for team in user.teams.all():
            if not team in user.teams_administered.all():
                roots.append(Root(team.slug))
        for event in user.events_organized.all():
            roots.append(Root(event.slug),True)
        for event in user.events.all():
            roots.append(Root(event.slug))
    roots.append(Root("Public"))

    return roots

