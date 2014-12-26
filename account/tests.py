from django.test import TestCase, Client

# Create your tests here.
from account.models import Eestecer
from teams.tests import EESTECMixin


class CanLoginTestcase(EESTECMixin, TestCase):
    def setUp(self):
        super(CanLoginTestcase, self).setUp()
        self.register = {
            "first_name": "test",
            "last_name": "user",
            "email": "testuser@eestec.net",
            "gender": "m",
            "password1": "test",
            "password2": "test",
        }
    def test_can_login(self):
        c = Client()
        response = c.post("/login/", {"username": "user@eestec.net", "password": "test"})
        response = c.get("/")
        assert (response.context['user'] == self.user)

    def test_can_register(self):
        c = Client()
        response = c.post("/register/", self.register)
        user = Eestecer.objects.get(email=self.register['email'])
        self.assertEqual(response.status_code, 302)
        assert (user.is_active == False)

    def test_cant_register_twice(self):
        # TODO THIS IS NOT WORKING RIGHT
        c = Client()
        response = c.post("/register/", self.register)
        self.assertEqual(response.status_code, 302)
        Eestecer.objects.get(email=self.register['email'])
