import base64
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.account.models import Eestecer
from eestecnet.fields import HyperlinkedSorlImageField


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    thumbnail = HyperlinkedSorlImageField(dimensions="200x200",
                                          options={'crop': 'center'})
    class Meta:
        model = Eestecer
        fields = (
        'thumbnail', 'first_name', 'middle_name', 'last_name', 'second_last_name',
        'is_superuser', 'slug', 'field_of_study', 'groups', 'user_permissions')
        # exclude=('email','password','passport_number','date_of_birth')
class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_representation(self, value):
        with open(value.path, "rb") as image_file:
            value = base64.b64encode(image_file.read())
        return value
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
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
class Base64PdfField(serializers.FileField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_representation(self, value):
        with open(value.path, "rb") as image_file:
            value = base64.b64encode(image_file.read())
        return value
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
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64PdfField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        return "pdf"

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    thumbnail = HyperlinkedSorlImageField(dimensions="200x200",
                                          options={'crop': 'center'})
    class Meta:
        model = Eestecer
        fields = (
            'thumbnail', 'first_name', 'middle_name', 'last_name', 'second_last_name',
            'is_superuser', 'slug', 'field_of_study', 'groups', 'user_permissions')
        # exclude=('email','password','passport_number','date_of_birth')
class LegacyAccountSerializer(ModelSerializer):
    class Meta:
        model = Eestecer
    thumbnail = Base64ImageField(
        max_length=None, use_url=True,
    )
    curriculum_vitae= Base64PdfField(
        max_length=None, use_url=True,
    )
