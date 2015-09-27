# -*- coding: utf-8 -*-
import ijson
import pytest

from apps.accounts.factories import AccountFactory
from apps.events.factories import BaseEventFactory
from apps.legacy.account.factories import LegacyAccountFactory
from apps.legacy.account.serializers import LegacyAccountSerializer, \
    ConversionAccountSerializer
from apps.teams.factories import CommitmentFactory, InternationalTeamFactory
from common.models import Image


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def convert(data, conversion_map):
    data[None] = None
    dellist = [key for key in conversion_map]
    update = {conversion_map[key]: data[key] for key in conversion_map}
    data.update(update)
    for key in dellist:
        del data[key]
    del data[None]
    return data


@pytest.mark.django_db
def test_convert_legacy_models():
    from apps.legacy.teams.serializers import ConversionTeamSerializer
    from apps.legacy.events.serializers import ConversionEventSerializer
    from apps.legacy.news.serializers import ConversionEntrySerializer

    InternationalTeamFactory(name="international board")
    with open('apps/legacy/account/laccounts.json', 'rU') as dump:
        accounts = ijson.items(dump, "item")
        for account in accounts:
            serializer = ConversionAccountSerializer(data=account)
            serializer.is_valid(raise_exception=True)
            serializer.save()
    with open('apps/legacy/teams/lteams.json', 'rU') as dump:
        teams = ijson.items(dump, "item")
        for team in teams:
            serializer = ConversionTeamSerializer(data=team)
            serializer.is_valid(raise_exception=True)
            serializer.save()
    with open('apps/legacy/events/levents.json', 'rU') as dump:
        events = ijson.items(dump, "item")
        for event in events:
            serializer = ConversionEventSerializer(data=event)
            serializer.is_valid(raise_exception=True)
            serializer.save()
    with open('apps/legacy/news/lentries.json', 'rU') as dump:
        events = ijson.items(dump, "item")
        for event in events:
            serializer = ConversionEntrySerializer(data=event)
            serializer.is_valid(raise_exception=True)
            serializer.save()


@pytest.mark.django_db
def test_convert_account():
    # Legacy side
    with open('media/example.dat', 'wb') as cv:
        cv.write("LOL")
    with open('media/example.jpg', 'wb') as cv:
        with open('media/images/example.jpg', 'rb') as img:
            cv.write(img.read())
    object = LegacyAccountFactory.build(email="asdf@asdf.de")
    data = LegacyAccountSerializer(object).data
    serializer = ConversionAccountSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    account = serializer.save()
    assert account.middle_name == u"Matteusz"
    assert len(Image.objects.all()) == 1


@pytest.mark.django_db
def test_convert_team():
    from apps.legacy.teams.factories import LegacyTeamFactory
    from apps.legacy.teams.serializers import LegacyTeamSerializer, \
        ConversionTeamSerializer
    # Legacy side
    with open('media/example.dat', 'wb') as cv:
        cv.write("LOL")
    with open('media/example.jpg', 'wb') as cv:
        with open('media/images/example.jpg', 'rb') as img:
            cv.write(img.read())
    objects = [LegacyTeamFactory.build(category=c) for c in
               "observer", "lc", "jlc", "team", "department", "body"]
    for object in objects:
        data = LegacyTeamSerializer(object).data
        serializer = ConversionTeamSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        team = serializer.save()


@pytest.mark.django_db
def test_convert_membership():
    from apps.legacy.news.factories import LegacyMembershipFactory
    from apps.legacy.news.serializers import ConversionMembershipSerializer
    # Legacy side
    a = AccountFactory(first_name="a", middle_name="b", last_name="c")
    d = AccountFactory(first_name="d", last_name="c")
    c = CommitmentFactory(name="munich")
    object = LegacyMembershipFactory.build()
    data = {"user": "a-b-c", "team": "munich"}
    serializer = ConversionMembershipSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    membership = serializer.save()
    data = {"user": "d-c", "team": "munich"}
    serializer = ConversionMembershipSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    membership = serializer.save()
    assert d in c.members
    assert a in c.members


@pytest.mark.django_db
def test_convert_event():
    from apps.legacy.events.factories import LegacyEventFactory
    from apps.legacy.events.serializers import LegacyEventSerializer, \
        ConversionEventSerializer
    # Legacy side
    c = CommitmentFactory(name="munich")
    object = LegacyEventFactory.build()
    data = LegacyEventSerializer(object).data
    serializer = ConversionEventSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    membership = serializer.save()
@pytest.mark.django_db
def test_convert_participation():
    from apps.legacy.events.serializers import ConversionParticipationSerializer
    # Legacy side
    a = AccountFactory(first_name="a", middle_name="b", last_name="c")
    e = BaseEventFactory(name="inktronics")
    data = {"user": "a-b-c", "team": "inktronics"}
    serializer = ConversionParticipationSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    membership = serializer.save()
    assert a in e.members

