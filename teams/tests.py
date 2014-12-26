from django.db.models import get_model

from django.test import TestCase, Client
from django.utils import timezone

from news.models import Membership


Eestecer = get_model('account', 'Eestecer')
from events.models import Event, Application
from teams.models import Team


class EESTECMixin(object):
    def tearDown(self):
        self.munich.delete()
        self.skopje.delete()
        self.admin.delete()
        self.privileged.delete()
        self.user.delete()
        self.inktronics.delete()
        self.pseudo_privileged.delete()
        for mship in self.memberships:
            mship.delete()

    def setUp(self):
        # Create Teams
        self.skopje = Team.objects.create(name="skopje")
        self.munich = Team.objects.create(name="munich")
        self.munich.save()
        self.skopje.save()

        # Create Users
        self.admin = Eestecer.objects.create_superuser(
            email="admin@eestec.net",
            password="test",
            first_name="admin")
        self.privileged = Eestecer.objects.create_user(
            email="privileged@eestec.net",
            password="test",
            first_name="privileged")
        self.pseudo_privileged = Eestecer.objects.create_user(
            email="pseudo@eestec.net",
            password="test",
            first_name="pseudo")
        self.user = Eestecer.objects.create_user(
            email="user@eestec.net",
            password="test",
            first_name="user")
        self.admin.save()
        self.privileged.save()
        self.user.save()
        self.pseudo_privileged.save()

        #Create Memberships
        self.memberships = []
        self.memberships.append(
            Membership.objects.create(user=self.user, team=self.munich))
        self.memberships.append(
            Membership.objects.create(user=self.pseudo_privileged, team=self.skopje,
                                      privileged=True))
        self.memberships.append(
            Membership.objects.create(user=self.privileged, team=self.munich,
                                      privileged=True))
        for mship in self.memberships:
            mship.save()
        today = timezone.now().date()
        self.inktronics = Event.objects.create(
            name="Inktronics",
            deadline=timezone.now() + timezone.timedelta(days=3),
            start_date=today + timezone.timedelta(days=5),
            end_date=today + timezone.timedelta(days=15),
        )
        self.inktronics.save()


class ManageTeamTestCase(EESTECMixin, TestCase):
    # Urls:
    def setUp(self):
        super(ManageTeamTestCase, self).setUp()
        management = ["images", "outgoing", "board", "details", "members"]
        self.management_urls = ["/cities/munich/" + tail for tail in management]

    def manage_lc(self, c):
        responses = []
        for url in self.management_urls:
            # print "Accessing ",url
            response = c.get(url)
            #print " as ",response.context['user']
            responses.append(response.status_code)
        return responses

    def test_admin_can_manage_lc(self):
        c = Client()
        c.login(username="admin@eestec.net", password="test")
        expected = 200
        assert (all(x == expected for x in self.manage_lc(c)))

    def test_privileged_can_manage_lc(self):
        c = Client()
        c.login(username="privileged@eestec.net", password="test")
        expected = 200
        assert (all(x == expected for x in self.manage_lc(c)))

    def test_pseudo_privileged_cant_manage_lc(self):
        c = Client()
        c.login(username="pseudo@eestec.net", password="test")
        expected = 403
        assert (all(x == expected for x in self.manage_lc(c)))

    def test_user_cant_manage_lc(self):
        c = Client()
        c.login(username="user@eestec.net", password="test")
        expected = 403
        assert (all(x == expected for x in self.manage_lc(c)))


class JoinTeamTestCase(EESTECMixin, TestCase):
    def test_application_can_be_accepted(self):
        assert (not Membership.objects.filter(user=self.user, team=self.skopje))
        a = Application.objects.create(applicant=self.user, target=Event.objects.get(
            slug="skopje-recruitment"))
        a.save()
        assert (not Membership.objects.filter(user=self.user, team=self.skopje))
        a.accepted = True
        a.save()
        assert (Membership.objects.filter(user=self.user, team=self.skopje))
