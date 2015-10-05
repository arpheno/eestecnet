from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.accounts.factories import AccountFactory
from apps.accounts.models import Participation, Account
from apps.announcements.models import Announcement, News, CareerOffer
from apps.events.models import BaseEvent
from apps.legacy.account.serializers import ConversionMixin
from apps.teams.models import BaseTeam
from apps.legacy.news.models import Membership, Entry
from common.serializers import Base64ImageField, ImageSerializer


def get_account(r):
    return Account.objects.get(email=r)
    names = r.split("-")
    names = [name.strip() for name in names]
    print names
    try:
        return Account.objects.get(last_name=names[-1],is_active=True)
    except:
        pass
    try:
        if len(names) == 4:
            return Account.objects.get(first_name=names[0], middle_name=names[1],
                                       last_name=names[2],is_active=True)
        elif len(names) == 3:
            return Account.objects.get(first_name=names[0], middle_name=names[1],
                                       last_name=names[2],is_active=True)
        else:
            return Account.objects.get(first_name=names[0],middle_name="", last_name=names[1],is_active=True)
    except:
        return Account.objects.get(first_name__startswith=names[0], last_name__startswith=names[-1],is_active=True)


def get_team(r):
    try:
        return BaseTeam.objects.get(name=r)
    except:
        pass
    try:
        return BaseTeam.objects.get(name__startswith=r[:-1])
    except:
        pass
    try:
        return BaseTeam.objects.get(name__startswith=r[:3])
    except:
        pass

def get_event(r):
    try:
        return BaseEvent.objects.get(name=r)
    except:
        return BaseEvent.objects.get(name__startswith=r[:-1])


class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership


class LegacyMembershipSerializer(ModelSerializer):
    class Meta:
        model = Membership

    user = SlugRelatedField("slug", read_only=True)
    team = SlugRelatedField("slug", read_only=True)


class ConversionMembershipSerializer(ConversionMixin, Serializer):
    conversion_map = {
        "user": None,
        "team": None,
    }
    def create(self, validated_data):
        u = get_account(self.keep["user"])
        e = get_team(self.keep["team"])
        p = Participation(user=u, group=e.group_set.get(name__endswith="members"),
                          confirmed=True)
        p.save()
        return p


class ConversionOrganizerSerializer(ConversionMixin, Serializer):
    conversion_map = {
        "user": None,
        "team": None,
    }

    def create(self, validated_data):
        u = get_account(self.keep["user"])
        e = get_event(self.keep["team"])
        p = Participation(user=u, group=e.group_set.get(name__endswith="organizers"),
                          confirmed=True)
        p.save()
        return p


class ConversionParticipationSerializer(ConversionMixin, Serializer):
    conversion_map = {
        "user": None,
        "team": None,
    }

    def create(self, validated_data):
        u = get_account(self.keep["user"])
        e = get_event(self.keep["team"])
        p = Participation(user=u, group=e.group_set.get(name__endswith="officials"),
                          confirmed=True)
        p.save()
        return p

class ConversionApplicationSerializer(ConversionMixin, Serializer):
    conversion_map = {
        "user": None,
        "team": None,
    }

    def create(self, validated_data):
        u = get_account(self.keep["user"])
        e = get_event(self.keep["team"])
        p = Participation(user=u, group=e.group_set.get(name__endswith="officials"),
                          confirmed=False)
        p.save()
        return p

class EntrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Entry


class LegacyEntrySerializer(ModelSerializer):
    class Meta:
        model = Entry

    thumbnail = Base64ImageField(max_length=0, allow_empty_file=True, use_url=True)


class ConversionEntrySerializer(ConversionMixin, ModelSerializer):
    class Meta:
        model = Announcement

    conversion_map = {
        "thumbnail": None,
        "author": None,
        "category": None,
        "slug": None,
        "published": None,
        "front_page_news": "important",
    }

    def create(self, validated_data):
        if self.keep["category"] == "news":
            result = News(**validated_data)
        else:
            result = CareerOffer(**validated_data)
        result.owner = AccountFactory()
        result.save()
        ct = result.polymorphic_ctype
        if self.keep["thumbnail"]:
            data = {
                "full_size": self.keep["thumbnail"],
                "content_object": result,
                "content_type": ct.pk,
                "object_id": result.pk}
            thumbnail = ImageSerializer(data=data)
            thumbnail.is_valid(raise_exception=True)
            thumbnail.save()
        return result
