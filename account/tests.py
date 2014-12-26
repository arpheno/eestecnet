from django.test import TestCase, Client

# Create your tests here.
from teams.tests import EESTECMixin


class CanLoginTestcase(EESTECMixin, TestCase):
    def test_can_login(self):
        c = Client()
        response = c.post("/login/", {"username": "user@eestec.net", "password": "test"})
        response = c.get("/")
        assert (response.context['user'] == self.user)
