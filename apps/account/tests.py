from io import BytesIO
from django.test import TestCase, Client

# Create your tests here.
import pytest
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from apps.account.factories import LegacyAccountFactory
from apps.account.models import Eestecer
from apps.account.serializers import LegacyAccountSerializer
from apps.teams.tests import EESTECMixin


@pytest.mark.django_db
def test_account_tautonomic():
    #Build a regular user
    old_account=LegacyAccountFactory(email="asdf@asdf.de")
    #Serialize it
    data=LegacyAccountSerializer(old_account).data
    # Send it over the wire
    json = JSONRenderer().render(data)
    stream = BytesIO(json)
    new_input = JSONParser().parse(stream)
    #Deserialize it
    serializer = LegacyAccountSerializer(data=new_input)
    old_account.delete()
    serializer.is_valid(raise_exception=True)
    new_account = serializer.save()
    #Compare the two objects
    del new_input['user_permissions']
    del new_input['groups']
    assert "cvs" in old_account.curriculum_vitae.path
    assert "cvs" in new_account.curriculum_vitae.path
    del new_input["curriculum_vitae"]
    assert "jpg" in old_account.thumbnail.path
    assert "jpg" in new_account.thumbnail.path
    del new_input["thumbnail"]
    del new_input["id"]
    for key in new_input:
        assert getattr(new_account,key) == getattr(old_account,key)


