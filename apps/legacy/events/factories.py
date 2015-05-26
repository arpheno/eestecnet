# -*- coding: utf-8 -*-
import datetime

import factory

from apps.legacy.account.factories import LegacyAccountFactory
from apps.legacy.events.models import Event, Transportation, Participation, Application
from apps.legacy.feedback.factories import LegacyAnswerSetFactory
from apps.legacy.teams.factories import LegacyTeamFactory


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class LegacyTransportationFactory(factory.Factory):
    class Meta:
        model = Transportation

    arrival = datetime.datetime.now().date()
    arrive_by = "plane"
    arrival_number = "123"
    departure = datetime.datetime.now().date()
    depart_by = "plane"
    comment = "comment"


class LegacyParticipationFactory(factory.Factory):
    class Meta:
        model = Participation

    participant = factory.SubFactory(LegacyAccountFactory)
    target = factory.SubFactory('apps.events.factories.LegacyEventFactory')
    confirmed = True
    confirmation = "LOL"
    transportation = factory.SubFactory(LegacyTransportationFactory)
    feedback = factory.SubFactory(LegacyAnswerSetFactory)


class LegacyApplicationFactory(factory.Factory):
    class Meta:
        model = Application

    applicant = factory.SubFactory(LegacyAccountFactory)
    target = factory.SubFactory('apps.events.factories.LegacyEventFactory')
    letter = "letter"
    priority = 1
    accepted = True
    questionnaire = factory.SubFactory(LegacyAnswerSetFactory)


class LegacyEventFactory(factory.Factory):
    class Meta:
        model = Event

    name = factory.sequence(lambda x: "name" + str(x))
    thumbnail = factory.django.ImageField(color="red")
    description = "description"
    category = "workshop"
    slug = "slug"
    # People
    # Participants and Organizers
    max_participants = 10
    participation_fee = 10

    @factory.post_generation
    def many2many(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        # A list of groups were passed in, use them
        self.organizers.add(LegacyAccountFactory())
        self.organizers.add(LegacyAccountFactory())
        self.organizing_committee.add(LegacyTeamFactory())
        LegacyParticipationFactory(participant=LegacyAccountFactory(), target=self)
        LegacyApplicationFactory(user=LegacyAccountFactory(), event=self)

    #Time and place
    scope = "international"
    location = "munich"
    """Start of the event."""
    start_date = datetime.datetime.now().date()
    """End of the event."""
    end_date = datetime.datetime.now().date()
    """Deadline until no more applications will be accepted."""
    deadline = datetime.datetime.now()
    #Content
    """ A detailed description of the event. Pictures and videos can be included here"""
    pax_report = "pax_report"
    """ Optional: This is a field where the participants report can be stored and
    accessed."""
    organizer_report = "organizer_report"
    """ Optional: This is a field where the organizers report can be stored and
    accessed."""
