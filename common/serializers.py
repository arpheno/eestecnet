from collections import OrderedDict
import logging

from django.contrib.auth.models import Permission
from rest_framework import viewsets
from rest_framework.fields import Field

from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

from common.fields import ThumbnailField
from common.models import Image, Report, URL, Location, Content

logger = logging.getLogger(__name__)


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission


class Permissions(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class Base64PdfField(serializers.FileField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    # def to_representation(self, value):
    #     try:
    #         with open(value.path, "rb") as image_file:
    #             value = base64.b64encode(image_file.read())
    #         return value
    #     except ValueError:
    #         return None

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_pdf')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension,)

            data = ContentFile(decoded_file, name=complete_file_name)

        self.allow_empty_file = True
        return super(Base64PdfField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        return "pdf"


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    # def to_representation(self, value):
    #     with open(value.path.encode("utf-8"), "rb") as image_file:
    #         value = base64.b64encode(image_file.read())
    #     return value
    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension,)

            data = ContentFile(decoded_file, name=complete_file_name)
        self.allow_empty_file = True
        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image

    full_size = Base64ImageField(
        max_length=None, use_url=True,
        allow_empty_file=True, allow_null=True,
    )
    square = ThumbnailField(
        dimensions="250x250",
        options={'crop': 'center'},
        source="full_size",
        read_only=True
    )
    large_square = ThumbnailField(
        dimensions="500x500",
        options={'crop': 'center'},
        source="full_size",
        read_only=True
    )


class ImageURLSerializer(ModelSerializer):
    class Meta:
        model = Image


class ContentInSerializer(ModelSerializer):
    class Meta:
        model = Content

    images = ImageSerializer(many=True)

    def update(self, instance, validated_data):
        images = validated_data.pop('images')
        instance.images = [Image.objects.create(**img) for img in images]
        return super(ContentInSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        images = validated_data.pop('images')
        instance = Content.objects.create(**validated_data)
        instance.save()
        instance.images = [Image.objects.create(**img) for img in images]
        return instance


def serializer_factory(mdl, fields=None, **kwargss):
    """ Generalized serializer factory to increase DRYness of code.

    :param mdl: The model class that should be instanciated
    :param fields: the fields that should be exclusively present on the serializer
    :param kwargss: optional additional field specifications
    :return: An awesome serializer
    """

    def _get_declared_fields(attrs):
        fields = [(field_name, attrs.pop(field_name))
                  for field_name, obj in list(attrs.items())
                  if isinstance(obj, Field)]
        fields.sort(key=lambda x: x[1]._creation_counter)
        return OrderedDict(fields)

    # Create an object that will look like a base serializer
    class Base(object):
        pass

    Base._declared_fields = _get_declared_fields(kwargss)

    class MySerializer(Base, ModelSerializer):
        class Meta:
            model = mdl

        if fields:
            setattr(Meta, "fields", fields)

    return MySerializer


# TODO: The below could be cleaned up using factories.
class ContentOutSerializer(ModelSerializer):
    class Meta:
        model = Content

    images = ImageURLSerializer(many=True)


class URLSerializer(ModelSerializer):
    class Meta:
        model = URL


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
