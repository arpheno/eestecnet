from django.contrib.contenttypes.models import ContentType
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from apps.accounts.factories import AccountFactory
from apps.accounts.models import Participation
from apps.events.models import BaseEvent, Workshop, Training, Exchange, Congress, IMW, \
    Project, SSA, Operational
from apps.legacy.account.serializers import ConversionMixin
from apps.legacy.events.models import Event
from apps.legacy.feedback.serializers import LegacyQuestionSetSerializer
from apps.legacy.news.serializers import ConversionOrganizerSerializer, \
    ConversionParticipationSerializer
from apps.teams.models import BaseTeam
from common.serializers import LocationSerializer, ImageSerializer, ReportSerializer, \
    Base64ImageField


class ConversionEventSerializer(ConversionMixin, ModelSerializer):
    class Meta:
        model = BaseEvent

    conversion_map = {
        "organizing_committee": None,
        "members": None,
        "participation_fee": None,
        "max_participants": None,
        "thumbnail": None,
        "images": None,
        "location": None,
        "organizer_report": None,
        "pax_report": None,
        "category": None,
        "organizers": None,
        # Throw away
        "scope": None,
        "feedbacksheet": None,
        "questionaire": None,
        "slug": None,
        "applicants": None,
    }

    def create(self, validated_data):
        if self.keep["category"] == "workshop":
            result = Workshop(**validated_data)
        elif self.keep["category"] == "training":
            result = Training(**validated_data)
        elif self.keep["category"] == "exchange":
            result = Exchange(**validated_data)
        elif self.keep["category"] == "congress":
            result = Congress(**validated_data)
        elif self.keep["category"] == "project":
            result = Project(**validated_data)
        elif self.keep["category"] == "ssa":
            result = SSA(**validated_data)
        elif self.keep["category"] == "operational":
            result = Operational(**validated_data)
        elif self.keep["category"] == "imw":
            result = IMW(**validated_data)
        result.owner = AccountFactory()
        result.save()
        result.officials.max_participants = self.keep["max_participants"]
        result.officials.fee = self.keep["participation_fee"]
        for oc in self.keep["organizing_committee"]:
            e = BaseTeam.objects.get(name=oc)
            result.organizing_committee.add(e)
        if self.keep["members"]:
            for user in self.keep["members"]:
                data = {
                    "user": user,
                    "team": result.name,
                }
                c = ConversionParticipationSerializer(data=data)
                c.is_valid(raise_exception=True)
                c.save()
        try:
            for image in self.keep["images"]:
                ct = ContentType.objects.get(app_label="events", model="baseevent")
                data = {
                    "full_size": image["image"],
                    "content_object": result,
                    "content_type": ct.pk,
                    "object_id": result.pk}
                thumbnail = ImageSerializer(data=data)
                thumbnail.is_valid(raise_exception=True)
                thumbnail.save()
        except KeyError:
            print "Something went wrong with an image"
            pass
        if self.keep["organizers"]:
            for user in self.keep["organizers"]:
                data = {
                    "user": user,
                    "team": result.name,
                }
                c = ConversionOrganizerSerializer(data=data)
                c.is_valid(raise_exception=True)
                c.save()
        if self.keep["thumbnail"]:
            ct = ContentType.objects.get(app_label="events", model="baseevent")
            data = {
                "full_size": self.keep["thumbnail"],
                "content_object": result,
                "content_type": ct.pk,
                "object_id": result.pk}
            thumbnail = ImageSerializer(data=data)
            thumbnail.is_valid(raise_exception=True)
            thumbnail.save()
        if self.keep["pax_report"]:
            ct = ContentType.objects.get(app_label="events", model="baseevent")
            data = {
                "name": "Participants' Report",
                "description": self.keep["pax_report"],
                "content_object": result,
                "content_type": ct.pk,
                "object_id": result.pk}
            rel = ReportSerializer(data=data)
            rel.is_valid(raise_exception=True)
            rel.save()
        if self.keep["organizer_report"]:
            ct = ContentType.objects.get(app_label="events", model="baseevent")
            data = {
                "name": "Organizers' Report",
                "description": self.keep["organizer_report"],
                "content_object": result,
                "content_type": ct.pk,
                "object_id": result.pk}
            rel = ReportSerializer(data=data)
            rel.is_valid(raise_exception=True)
            rel.save()
        if self.keep["location"]:
            data = {
                "string": self.keep["location"],
                "content_object": result,
                "content_type": ct.pk,
                "object_id": result.pk}
            location = LocationSerializer(data=data)
            location.is_valid(raise_exception=True)
            location.save()

        return result


class LegacyEventSerializer(ModelSerializer):
    class Meta:
        model = Event

    questionaire = LegacyQuestionSetSerializer(read_only=True)
    feedbacksheet = LegacyQuestionSetSerializer(read_only=True)
    organizers = SlugRelatedField("slug", many=True, read_only=True)
    members = SlugRelatedField("slug", many=True, read_only=True)
    organizing_committee = SlugRelatedField("slug", many=True, read_only=True)
    thumbnail = Base64ImageField(max_length=0, use_url=True)


class LegacyParticipationSerializer(ModelSerializer):
    class Meta:
        model = Participation

    participant = SlugRelatedField("slug", read_only=True)
    target = SlugRelatedField("slug", read_only=True)
