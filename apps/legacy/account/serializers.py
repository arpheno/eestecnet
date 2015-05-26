from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import ModelSerializer

from apps.accounts.models import Account
from apps.legacy.account.models import Eestecer
from common.serializers import ImageSerializer, Base64ImageField, Base64PdfField


class ConversionMixin(object):
    def __init__(self, *args, **kwargs):
        self.conversion_map = type(self).conversion_map
        return super(ConversionMixin, self).__init__(*args, **kwargs)

    def to_internal_value(self, data):
        data = self.convert(data)
        return super(ConversionMixin, self).to_internal_value(data)

    def convert(self, data):
        data[None] = None
        dellist = [key for key in self.conversion_map if key in data]
        update = {self.conversion_map[key]: data[key] for key in dellist}
        data.update(update)
        self.keep = {}
        for key in dellist:
            self.keep[key] = data[key]
            del data[key]
        del data[None]
        return data


class ConversionAccountSerializer(ConversionMixin, ModelSerializer):
    class Meta:
        model = Account

    conversion_map = {
        "date_of_birth": "birthday",
        "show_date_of_birth": "birthday_show",
        "activation_link": None,
        "thumbnail": None,
        "slug": None,
    }
    curriculum_vitae = Base64PdfField(
        max_length=None, use_url=True,
    )

    def create(self, validated_data):
        result = super(ConversionAccountSerializer, self).create(validated_data)
        if self.keep["thumbnail"]:
            ct = ContentType.objects.get(app_label="common", model="image")
            data = {
                "full_size": self.keep["thumbnail"],
                "content_object": result,
                "content_type": ct.pk,
                "object_id": result.pk}
            thumbnail = ImageSerializer(data=data, allow_null=True)
            thumbnail.is_valid(raise_exception=True)
            thumbnail.save()
        return result


class LegacyAccountSerializer(ModelSerializer):
    class Meta:
        model = Eestecer

    thumbnail = Base64ImageField(
        max_length=None, use_url=True,
        required=False, allow_empty_file=True,
    )
    curriculum_vitae = Base64PdfField(
        max_length=None, use_url=True,
        required=False, allow_empty_file=True, allow_null=True
    )
