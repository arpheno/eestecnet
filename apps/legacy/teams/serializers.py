from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import ModelSerializer

from apps.accounts.factories import AccountFactory
from apps.legacy.account.serializers import ConversionMixin
from apps.legacy.teams.models import Team
from apps.teams.models import BaseTeam, InternationalBody, InternationalTeam, \
    InternationalDepartment, Commitment
from common.serializers import Base64ImageField, ImageSerializer, URLSerializer, \
    LocationSerializer


class LegacyTeamSerializer(ModelSerializer):
    class Meta:
        model = Team

    thumbnail = Base64ImageField(
        max_length=None, use_url=True,
    )


class ConversionTeamSerializer(ConversionMixin, ModelSerializer):
    class Meta:
        model = BaseTeam

    conversion_map = {
        "thumbnail": None,
        "slug": None,
        "users": None,
        "category": None,
        "thumbsource": None,
        "facebook": None,
        "website": None,
        "address": None,
        "lat": None,
        "lng": None,
        "founded": None,
        "images": None,
    }

    def create(self, validated_data):
        if self.keep["category"] == "body":
            result = InternationalBody(**validated_data)
        elif self.keep["category"] == "team":
            result = InternationalTeam(**validated_data)
        elif self.keep["category"] == "department":
            result = InternationalDepartment(**validated_data)
        elif self.keep["category"] == "observer":
            validated_data["rank"] = 0
            validated_data["founded"] = self.keep["founded"]
            result = Commitment(**validated_data)
        elif self.keep["category"] == "jlc":
            validated_data["rank"] = 1
            validated_data["founded"] = self.keep["founded"]
            result = Commitment(**validated_data)
        else:
            validated_data["rank"] = 2
            validated_data["founded"] = self.keep["founded"]
            result = Commitment(**validated_data)
        result.owner = AccountFactory()
        result.name = result.name.lower()
        result.save()

        ct = ContentType.objects.get(app_label="common", model="image")
        data = {
            "full_size": self.keep["thumbnail"],
            "content_object": result,
            "content_type": ct.pk,
            "object_id": result.pk}
        thumbnail = ImageSerializer(data=data)
        thumbnail.is_valid(raise_exception=True)
        thumbnail.save()
        if self.keep["facebook"]:
            ct = ContentType.objects.get(app_label="common", model="url")
            data = {
                "url": self.keep["facebook"],
                "name": "facebook",
                "content_object": result,
                "content_type": ct.pk,
                "object_id": result.pk}
            facebook = URLSerializer(data=data)
            facebook.is_valid(raise_exception=True)
            facebook.save()
        if self.keep["website"]:
            ct = ContentType.objects.get(app_label="common", model="url")
            data = {
                "url": self.keep["website"],
                "name": "website",
                "content_object": result,
                "content_type": ct.pk,
                "object_id": result.pk}
            website = URLSerializer(data=data)
            website.is_valid(raise_exception=True)
            website.save()
        try:
            for image in self.keep["images"]:
                ct = ContentType.objects.get(app_label="common", model="image")
                data = {
                    "full_size": image["image"],
                    "content_object": result,
                    "content_type": ct.pk,
                    "object_id": result.pk}
                thumbnail = ImageSerializer(data=data)
                thumbnail.is_valid(raise_exception=True)
        except KeyError:
            pass
        if self.keep["address"]:
            data = {
                "string": self.keep["address"],
                "longitude": self.keep["lng"],
                "latitude": self.keep["lat"],
                "content_object": result,
                "content_type": ct.pk,
                "object_id": result.pk}
            location = LocationSerializer(data=data)
            location.is_valid(raise_exception=True)
            location.save()

        return result


