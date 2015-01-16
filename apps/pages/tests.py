# Create your tests here.
from django.test import TestCase, Client

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
            ["/events/inktronics/applications", "admin", 200],
            ["/events/inktronics/applications", "local", 200],
            ["/events/inktronics/applications", "pseudo", 403],
            ["/events/inktronics/applications/export", "admin", 200],
            ["/events/inktronics/applications/export", "local", 200],
            ["/events/inktronics/applications/export", "pseudo", 403],
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

    def query_url(self, data):
        c = Client()
        if data[1] == "admin":
            c.login(username="admin@eestec.net", password="test")
        elif data[1] == "local":
            c.login(username="privileged@eestec.net", password="test")
        elif data[1] == "pseudo":
            c.login(username="pseudo@eestec.net", password="test")
        elif data[1] == "auth":
            c.login(username="user@eestec.net", password="test")
        if len(data) == 3:
            print data[0]
            response = c.get(data[0])
            self.assertEqual(response.status_code, data[2])

    def test_urls_work(self):
        for url in self.urls:
            self.query_url(url)
