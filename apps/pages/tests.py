# Create your tests here.
import logging

from django.test import TestCase, Client

logger = logging.getLogger(__name__)
from apps.teams.tests import EESTECMixin


class UrlTests(EESTECMixin, TestCase):
    def setUp(self):
        super(UrlTests, self).setUp()
        self.urls = [
            ["", "anon", 200],
            ["/cities", "anon", 200],
            ["/news", "anon", 200],
            ["/sitemap", "anon", 200],

            ["/governance", "anon", 200],
            # ["/documents","anon",200], #this is a dynamic view
            ["/people", "anon", 200],
            ["/people/me", "anon", 403],
            ["/people/me", "auth", 200],
            ["/register/", "anon", 200],
            ["/admin", "anon", 302],
            ["/activities", "anon", 200],
            ["/about", "anon", 200],
            ["/materials", "anon", 403],
            ["/materials", "auth", 200],
            ["/wiki/", "auth", 200],
            ["/active", "local", 403],
            ["/active", "admin", 200],
            ["/teams", "anon", 200],
            ["/teams/munich/", "anon", 200],

            ["/teams/munich/members", "pseudo", 403],
            ["/teams/munich/members", "local", 200],
            ["/teams/munich/members", "admin", 200],

            ["/teams/munich/images", "pseudo", 403],
            ["/teams/munich/images", "local", 200],
            ["/teams/munich/images", "admin", 200],

            ["/teams/munich/outgoing", "pseudo", 403],
            ["/teams/munich/outgoing", "local", 200],
            ["/teams/munich/outgoing", "admin", 200],

            ["/teams/munich/description", "pseudo", 403],
            ["/teams/munich/description", "local", 200],
            ["/teams/munich/description", "admin", 200],

            ["/teams/munich/board", "pseudo", 403],
            ["/teams/munich/board", "local", 200],
            ["/teams/munich/board", "admin", 200],

            ["/teams/munich/applications", "pseudo", 403],
            ["/teams/munich/applications", "local", 200],
            ["/teams/munich/applications", "admin", 200],
            ["/events", "anon", 200],
            ["/events/create", "auth", 403],
            ["/events/create", "local", 200],
            ["/events/questionaire/create", "auth", 403],
            ["/events/questionaire/create", "local", 200],
            ["/events/inktronics/", "anon", 200],
            ["/events/inktronics/feedback", "auth", 403],
            ["/events/inktronics/feedback", "anon", 403],
            ["/events/inktronics/feedback", "participant", 200],
            ["/events/inktronics/feedback", "admin", 403],
            ["/events/inktronics/feedback", "local", 403],
            ["/events/inktronics/feedback", "pseudo", 403],
            ["/events/inktronics/feedback/export", "admin", 200],
            ["/events/inktronics/feedback/export", "local", 200],
            ["/events/inktronics/feedback/export", "pseudo", 403],
            ["/events/inktronics/applications", "admin", 200],
            ["/events/inktronics/applications", "local", 200],
            ["/events/inktronics/applications", "pseudo", 403],
            ["/events/inktronics/applications/export", "admin", 200],
            ["/events/inktronics/applications/export", "local", 200],
            ["/events/inktronics/applications/export", "pseudo", 403],
            ["/events/inktronics/participants", "admin", 200],
            ["/events/inktronics/participants", "local", 200],
            ["/events/inktronics/participants", "pseudo", 403],
            ["/events/inktronics/participants/export", "admin", 200],
            ["/events/inktronics/participants/export", "local", 200],
            ["/events/inktronics/participants/export", "pseudo", 403],
            ["/events/inktronics/description", "local", 200],
            ["/events/inktronics/description", "admin", 200],
            ["/events/inktronics/description", "pseudo", 403],
            ["/events/inktronics/details", "local", 200],
            ["/events/inktronics/details", "admin", 200],
            ["/events/inktronics/details", "pseudo", 403],
            ["/events/inktronics/images", "local", 200],
            ["/events/inktronics/images", "admin", 200],
            ["/events/inktronics/images", "pseudo", 403],
            ["/events/inktronics/apply", "anon", 403],
            ["/events/inktronics/apply", "auth", 200],
        ]

    def make_request(self, client, data):
        if len(data) == 3:
            print data[0]
            response = client.get(data[0])
            self.assertEqual(response.status_code, data[2])

    def query_url_admin(self, urls):
        c = Client()
        c.login(username="admin@eestec.net", password="test")
        for data in urls:
            self.make_request(c, data)

    def query_url_local(self, urls):
        c = Client()
        c.login(username="privileged@eestec.net", password="test")
        for data in urls:
            self.make_request(c, data)

    def query_url_pseudo(self, urls):
        c = Client()
        c.login(username="pseudo@eestec.net", password="test")
        for data in urls:
            self.make_request(c, data)

    def query_url_auth(self, urls):
        c = Client()
        c.login(username="user@eestec.net", password="test")
        for data in urls:
            self.make_request(c, data)

    def query_url_participant(self, urls):
        c = Client()
        c.login(username="participant@eestec.net", password="test")
        for data in urls:
            self.make_request(c, data)

    def test_urls_work(self):
        local = (data for data in self.urls if data[1] == "local")
        admin = (data for data in self.urls if data[1] == "admin")
        pseudo = (data for data in self.urls if data[1] == "pseudo")
        auth = (data for data in self.urls if data[1] == "auth")
        participant = (data for data in self.urls if data[1] == "participant")
        self.query_url_admin(admin)
        self.query_url_local(local)
        self.query_url_pseudo(pseudo)
        self.query_url_auth(auth)
        self.query_url_participant(participant)
