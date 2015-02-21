# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from datetime import timedelta

from django.contrib.auth.models import Group, Permission
from django.core.files import File
from django.utils import timezone
from django.utils.datetime_safe import datetime

from apps.account.models import Eestecer, Position
from apps.events.models import Event, Application, EventImage
from apps.pages.models import Stub, Page
from apps.teams.models import Team, MemberImage
from apps.news.models import Entry, Membership


def create_stubs():
    for part in ['conference', 'teams', 'competition', 'events']:
        stub = Stub.objects.create(
            description=open("eestecnet/stub/" + part + ".txt").read(),
            name=open("eestecnet/stub/" + part + "_head.txt").read(),
            link="/",
            group="activities"
        )
        with open('eestecnet/stub/' + part + '.jpg', 'rb') as doc_file:
            stub.image.save(part + ".jpg", File(doc_file), save=True)
    for part in ['news', 'history', 'cities', 'documents', 'governance']:
        stub = Stub.objects.create(
            description=open("eestecnet/stub/" + part + ".txt").read(),
            name=open("eestecnet/stub/" + part + "_head.txt").read(),
            link="/",
            group="about"
        )
        with open('eestecnet/stub/' + part + '.jpg', 'rb') as doc_file:
            stub.image.save(part + ".jpg", File(doc_file), save=True)


def create_eestec_news():
    cng = Entry.objects.create(name="Congress in athens",
                               description=open("eestecnet/news/congress.txt").read())
    mw = Entry.objects.create(name="Mw in Munich",
                              description=open("eestecnet/news/mw.txt").read())

    with open('eestecnet/news/congress.jpg', 'rb') as doc_file:
        cng.thumbnail.save("cng.jpg", File(doc_file), save=True)
    with open('eestecnet/news/mw.jpg', 'rb') as doc_file:
        mw.thumbnail.save("mw.jpg", File(doc_file), save=True)
    cng.save()
    mw.save()
    mw.author.add(Team.objects.get(slug='munich'))
    cng.author.add(Team.objects.get(slug='athens'))


def create_eestec_teams():
    Team.objects.create(name='Training Team',
                        category='team',
                        teamstub='In our trainer division we lay the foundation for the \
                        coming generations of EESTECers by educating and passing on the \
                        experience and skills we acquired.',


    )
    Team.objects.create(name='Magazine Team',
                        category='team',
                        teamstub='Our Magazine Team is responsible for \
                         publishing issues of  EESTEC Magazine twice a year, on the \
                         occasion of EESTEC Chairpersons’ Meeting and the EESTEC '
                                 'Annual Congress.',
    )
    Team.objects.create(name='Design Team',
                        category='team',
                        teamstub='Our Design Team is responsible for designing EESTEC '
                                 'promotional\
                         materials and also this very website, based  on the rules in '
                                 'our Branding Guide.'
    )
    Team.objects.create(name='IT Team',
                        category='team',
                        teamstub='Our IT Team is responsible for providing IT '
                                 'solutions for EESTEC needs.'
                                 'It is responsible for providing the maintaining '
                                 'resources such as the  \
                                 EESTEC website and the mailing lists.'
    )
    Team.objects.create(name='International Bureau',
                        category='team',
                        teamstub='The International Bureau is the body responsible for '
                                 'keeping'
                                 ' the history and records of the  Association. It '
                                 'gathers reports and other data concerning all events '
                                 'and activities, sent by the   Local Committees or '
                                 'other'
                                 ' bodies of the Association.'
    )
    Team.objects.create(name='Yearbook Committee',
                        category='team',
                        teamstub='Yearbook Committee is responsible for publishing '
                                 'EESTEC'
                                 ' Yearbook, a yearly publication   which gathers '
                                 'information about all the events and activities '
                                 'carried'
                                 ' out in EESTEC during the year.'
    )
    for team in Team.objects.filter(category='team'):
        team.description = open("eestecnet/team/" + team.slug + ".txt").read()
        with open('eestecnet/team/' + team.slug + '.jpg', 'rb') as doc_file:
            team.thumbnail.save(team.slug + ".jpg", File(doc_file), save=True)
        team.save()


def create_pages():
    Page.objects.create(url='documents', content="a")


def create_eestec_lcs():
    Team.objects.create(name='Aachen',
                        founded=1986,
                        website="http://www.eestec.rwth-aachen.de",
                        address="Karmansr. 9\n52056 Aachen\nGermany", )
    Team.objects.create(name='Ankara',
                        founded=2006,
                        website="http://eestectr.org/ankara",
                        address="Middle East Technical University\nDepartment of "
                                "Electrical and Electronics Engineering\A-203 06531 "
                                "Ankara\nTurkey")
    Team.objects.create(name='Antwerp',
                        founded=2010,
                        website="http://www.eestec.be",
                        address="Middelheimlaan 1\n2020 Antwerpen\nBelgium")
    Team.objects.create(name='Athens',
                        founded=2004,
                        website="http://www.eestec.ntua.gr",
                        address="Iroon Polytexneiou 9\n Zografou 15780\nGreece")
    Team.objects.create(name='Banja Luka',
                        founded=2004,
                        website="http://www.eestec.etfbl.net",
                        address='Patre 5th\nFaculty of Electrical Engineering\n78 '
                                '000\bBanja Luka\nBosnia')
    Team.objects.create(name='Belgrade',
                        founded=2000,
                        website="http://www.eestec.etf.rs",
                        address='Bulevar kralja Aleksandra 73\n11000 Belgrade\nSerbia')
    Team.objects.create(name='Bucharest',
                        founded=2003,
                        website="http://www.eestec.ro",
                        address="Splaiul Independentei nr.313\ncorp Rectorat\nAN "
                                "204bis\n060042 Bucharest\nRomania")
    Team.objects.create(name='Budapest',
                        founded=1986,
                        website="http://www.eestec.hu/pages/home.php",
                        address=u"Eszék utca 9-11\nH-1114 Budapest\nHungary")
    Team.objects.create(name='Cosenza',
                        founded=1998,
                        website="http://www.asiunical.org",
                        address="ASI-UNICAL\nvia Pietro Bucci, Cubo 42D, "
                                "piano terra\nUniversita della Calabria\n87036 "
                                "Arcavacata di Rende Cosenza)\nItaly")
    Team.objects.create(name='Craiova',
                        founded=2006,
                        website="http://www.eestec.go.ro",
                        address="B-dul Decebal Nr. 107, Sala N8\nCraiova 200440,"
                                "Dolj\nRomania")
    Team.objects.create(name='Delft',
                        founded=1906,
                        website="http://www.etv.tudelft.nl",
                        address="Mekelweg 4\n 2628 CD Delft\nThe Netherlands")
    Team.objects.create(name='East Sarajevo',
                        founded=2005,
                        website="http://www.eestec-es.rs.ba",
                        address="Vuka Karadzica 30, Istacno Sarajevo, Republika "
                                "Srpska,\nBosna i Hercegovina")
    Team.objects.create(name='Eskisehir',
                        founded=2006,
                        website="http://www.eesteceskisehir.net",
                        address="Anadolu University, Iki Eylul Campus, Electrical and "
                                "Electronics Department\nTurkey")
    Team.objects.create(name='Famagusta',
                        founded=2006,
                        address="Electrical and Electronic Engineering "
                                "Department\nEastern Mediterranean "
                                "University\nFamagusta, via Mersin 10 \nTurkey")
    Team.objects.create(name='Gliwice',
                        founded=2010,
                        address="Gliwice 44-100\nAkademicka 16\nPoland")
    Team.objects.create(name='Hamburg',
                        founded=2004,
                        website="http://www.eestec-hamburg.de",
                        address=u"EESTEC für Hamburg e.V.\nc/o FSR E/I, Berliner Tor "
                                u"7, 20099 Hamburg")
    Team.objects.create(name='Helsinki',
                        founded=1986,
                        website="http://eestec.ayy.fi",
                        address="SIK / EESTEC LC Helsinki PL 13000, 00076 "
                                "AALTO\nFinland")
    Team.objects.create(name='Istanbul',
                        founded=2005,
                        website="http://www.eestec.itu.edu.tr",
                        address=u"EESTEC LC Istanbul\nITÜ Elektrik-Elektronik "
                                u"Fakültesi\nMaslak\Istanbul\n34469\nTurkey")
    Team.objects.create(name='Izmir',
                        founded=2009,
                        address=u"Dokuz Eylül Üniversitesi, Tinaztepe Kampüsü, "
                                u"Elektrik-Elektronik Müh., Toplu-luklar "
                                u"odasi\nBuca/Izmir\nTurkey")
    Team.objects.create(name='Krakow',
                        founded=1998,
                        website="http://www.eestec.agh.edu.pl",
                        address="Akademia Gorniczo-Hutnicza im. Stanislawa Staszica w "
                                "Krakowie\nAl. Mickiewicza 30\n30-059 Krakow")
    Team.objects.create(name='Lille',
                        founded=2010,
                        website="http://www.eesteclille.wordpress.com",
                        address="Club EESTEC\n Polytech Lille,E402\nAvenue Paul "
                                "Langevin\n59655 Villeneuve d'Ascq cedex\nFrance")
    Team.objects.create(name='Lisbon',
                        founded=2010,
                        address="Nucleo de Engenharia Electrotecnica e Computadores\n "
                                "Dep. Engenharia Electrecnica\n Faculdade de Ciencias "
                                "e Tecnologias\n 2829-516 Caparica\nPortugal")
    Team.objects.create(name='Ljubljana',
                        founded=1986,
                        website="http://www.eestec-lj.org",
                        address="EESTEC, drustvo studentov elektrotehnike in "
                                "racunalnistva\n SOU - mednarodna pisarna\n Vojkova "
                                "ulica 63\n1000 Ljubljana\nSlovenia")
    Team.objects.create(name='Madrid',
                        founded=1986,
                        website="http://www.eestec.es",
                        address=u"Eurielec - EESTEC LC Madrid\nETSI Telecomunicación "
                                u"UPM\nAvda.Complutense 30\n28040 - Madrid\n Spain")
    Team.objects.create(name='Munich',
                        founded=1999,
                        website="http://eestec.tum.de",
                        address="uEESTEC Munich e.V.\nTechnische Universität "
                                "München\nArcisstr.21\n80333 München\nGermany")
    Team.objects.create(name='Nis',
                        founded=2000,
                        website="http://eestec.rs",
                        address="Aleksandra Medvedeva 14\n18000 Nis\nSerbia")
    Team.objects.create(name='Novi Sad',
                        founded=2000,
                        website="http://www.eestecns.org",
                        address="Trg Dositeja Obradovica 6\n21000 Novi Sad\nSerbia")
    Team.objects.create(name='Podgorica',
                        founded=2000,
                        website="http://www.eestec.me",
                        address="University of Montenegro, Faculty of Electrical "
                                "Engineering\nDzordza Vasingtona bb.\n 20 000 "
                                "Podgorica\nMontenegro")
    Team.objects.create(name='Riga',
                        founded=2008,
                        website="http://www.eestec.lv",
                        address="EESTEC; Kronvalda bulvaris 1\nRiga\Latvia\LV-1010")
    Team.objects.create(name='Rijeka',
                        founded=1999,
                        website="http://www.eestec.hr",
                        address="Vukovarska 58\n51000 Rijeka\nCroatia")
    Team.objects.create(name='Sarajevo',
                        founded=2006,
                        website="http://www.eestec-sa.ba",
                        address="Zmaja od Bosne bb\n71 000 Sarajevo\nBosnia and "
                                "Herzegovina")
    Team.objects.create(name='Skopje',
                        founded=2003,
                        website="http://www.eestec-sk.org.mk",
                        address="Fakultet za Elektrotehnika i informaciski "
                                "tehnologii\nul. Rugjer Boshkovikj b.b\n1000 "
                                "Skopje\nMacedonia")
    Team.objects.create(name='Tallinn',
                        founded=2005,
                        website="http://www.eestec.ee",
                        address="EESTEC LC Tallinn\nEhitajate tee 5\n19086 "
                                "Tallinn\nEstonia")
    Team.objects.create(name='Tampere',
                        founded=1986,
                        website="http://tampere.eestec.net",
                        address="TTY/EESTEC\nKorkeakoulunkatu 3\n33720 Tampere\nFinland")
    Team.objects.create(name='Trieste',
                        founded=2006,
                        website="http://ts.eestec.it",
                        address="EESTEC LC Trieste - via Fabio Severo, 154 - C.d.S. E3 "
                                "- 34127 -Trieste\nItaly")
    Team.objects.create(name='Tuzla',
                        founded=2007,
                        website="http://www.eestec-tz.ba",
                        address="Franjevacka 2,75000 Tuzla, Bosnia and Herzegovina")
    Team.objects.create(name='Xanthi',
                        founded=2010,
                        website="http://eestec.ee.duth.gr",
                        address="Tsimiski street, xanthi\nGreece")
    Team.objects.create(name='Zagreb',
                        founded=2007,
                        website="http://eestec-zg.hr",
                        address="FER\nUnska 3\n10 000 Zagreb\nCroatia")
    Team.objects.create(name='Zurich',
                        founded=1986,
                        website="http://eestec.ch",
                        address=u"AMIV an der ETH Zuerich\nEESTEC LC Zurich\nCAB "
                                u"E37\nUniversitätsstrasse 6\n8092 Zürich\nSwitzerland")
    for lc in Team.objects.filter(category="lc"):
        lc.description = open("eestecnet/lc/" + lc.slug + ".txt").read()
        try:
            with open('eestecnet/lc/' + lc.slug + '.jpg', 'rb') as doc_file:
                lc.thumbnail.save(lc.slug + ".jpg", File(doc_file), save=True)
        except:
            with open('eestecnet/lc/test.png', 'rb') as doc_file:
                lc.thumbnail.save(lc.slug + ".png", File(doc_file), save=True)
        try:
            lc.thumbsource = open("eestecnet/lc/" + lc.slug + "-credit.txt").read()
        except:
            pass
        lc.save()


def setup_event_tests():
    Eestecer.objects.create_superuser(
        "admin@eestec.net",
        "test",
        first_name="specific")
    user = Eestecer.objects.create_user(
        "user@eestec.net",
        "test",
        first_name="random")
    user.save()
    outg = Eestecer.objects.create_user(
        "outgoing@eestec.net",
        "outgoing",
        first_name="outgoing")
    outg.save()
    inc = Eestecer.objects.create_user(
        "incoming@eestec.net",
        "incoming",
        first_name="incoming")
    inc.save()
    tm = Team.objects.create(name='test',
                             founded=1986,
                             website="http://eestec.ch",
                             address=u"AMIV an der ETH Zuerich\nEESTEC LC Zurich\nCAB "
                                     u"E37\nUniversitätsstrasse 6\n8092 "
                                     u"Zürich\nSwitzerland")
    tm.save()
    tm.users.add(inc)
    tm.privileged.add(inc)
    tm.save()
    to = Team.objects.create(name='outtest',
                             founded=1986,
                             website="http://eestec.ch",
                             address=u"AMIV an der ETH Zuerich\nEESTEC LC Zurich\nCAB "
                                     u"E37\nUniversitätsstrasse 6\n8092 "
                                     u"Zürich\nSwitzerland")
    to.save()
    to.users.add(user, outg)
    to.privileged.add(outg)
    to.save()
    ev = Event.objects.create(name="T4T",
                              description="Cool thing",
                              start_date=datetime.now(),
                              category="workshop",
                              scope="international",
                              deadline=datetime.now() + timedelta(days=1),
    )
    ev.save()
    ev.organizing_committee.add(tm)
    ap = Application.objects.create(target=ev, applicant=user)
    ap.save()


def create_eestec_people():
    ag = Eestecer.objects.create(email="random1@gmail.com",
                                 password="test",
                                 first_name="alexis",
                                 last_name="gonzales",
                                 second_last_name="arguello")
    aa = Eestecer.objects.create(email="random2@gmail.com",
                                 password="test",
                                 first_name="andreas",
                                 last_name="albrecht")
    ab = Eestecer.objects.create_superuser(email="aslihanbener@gmail.com",
                                           password="test",
                                           first_name="aslihan",
                                           last_name="bener")
    bk = Eestecer.objects.create(email="random4@gmail.com",
                                 password="test",
                                 first_name="bartosz",
                                 last_name="kawlatow")
    cm = Eestecer.objects.create(email="random5@gmail.com",
                                 password="test",
                                 first_name="clemens",
                                 last_name="mattersdorfer")
    mp = Eestecer.objects.create(email="random7@gmail.com",
                                 password="test",
                                 first_name="marcus",
                                 last_name="pforte")
    map = Eestecer.objects.create(email="martapolec@gmail.com",
                                  password="test",
                                  first_name="marta",
                                  last_name="polec")
    ez = Eestecer.objects.create(email="random6@gmail.com",
                                 password="test",
                                 first_name="elzbieta",
                                 last_name="zimolag")
    ma = Eestecer.objects.create(email="random8@gmail.com",
                                 password="test",
                                 first_name="melis",
                                 last_name="aca")
    ra = Eestecer.objects.create(email="randomrupter@gmail.com",
                                 password="test",
                                 first_name="rupert",
                                 last_name="amann")
    sw = Eestecer.objects.create_superuser(email="arpheno@gmail.com",
                                           password="test",
                                           first_name="sebastian",
                                           middle_name='stanislaw',
                                           last_name="wozny")
    for user in Eestecer.objects.exclude(first_name=""):
        with open('eestecnet/people/' + user.slug + '.jpg', 'rb') as doc_file:
            user.thumbnail.save(user.slug + ".jpg", File(doc_file), save=True)
        user.save()
    munich = Team.objects.get(slug='munich')
    mm = [ag, aa, cm, ez, mp, ma, ra, sw]
    for user in mm:
        Membership.objects.create(team=munich, user=user).save()
    mb = [cm, mp, ma, ra]
    for membership in Membership.objects.filter(team=munich, user__in=mb):
        membership.organizers = True
        membership.save()
    Team.objects.get(slug='munich').save()
    munich = Team.objects.get(slug='munich')
    for i in range(1, 3):
        a = MemberImage.objects.create(property=munich)
        with open('eestecnet/lc/munich/' + str(i) + '.jpg', 'rb') as doc_file:
            a.image.save(str(i) + ".jpg", File(doc_file), save=True)
        a.save()


def create_inktronics():
    ink = Event.objects.create(name='Inktronics',
                               deadline=timezone.now() + timedelta(days=10),
                               start_date=timezone.now(),
                               end_date=timezone.now(),
                               category="workshop",
                               max_participants=16,
                               description=open(
                                   'eestecnet/event/inktronics/desc.txt').read(),
                               scope="international")
    with open('eestecnet/event/inktronics.jpg', 'rb') as doc_file:
        ink.thumbnail.save('inktronics.jpg', File(doc_file), save=True)
    ink.save()
    for i in range(1, 4):
        a = EventImage.objects.create(property=ink)
        with open('eestecnet/event/inktronics/' + str(i) + '.jpg', 'rb') as doc_file:
            a.image.save(str(i) + ".jpg", File(doc_file), save=True)
        a.save()
    ink.organizing_committee.add(Team.objects.get(slug='munich'))
    ink.organizers.add(Eestecer.objects.get(first_name='sebastian'))
    ink.organizers.add(Eestecer.objects.get(first_name='andreas'))
    ink.save()


def create_positions_for_achievements():
    Position.objects.create(name='Main Organizer',
                            description="Was majorly responsible for the organization "
                                        "of an Event.").save()
    Position.objects.create(name='Trainer Status',
                            description="Acquired the status of \"Certified EESTEC "
                                        "Trainer\".").save()
    Position.objects.create(name='International Team Coordinator',
                            description="Coordinated the efforts of an International "
                                        "Team during a mandate.").save()
    Position.objects.create(name='Chairperson',
                            description="Held the Chaiperson position in a commitment"
                                        ".").save()
    Position.objects.create(name='Contact person',
                            description="Held the Contact Person position in a "
                                        "commitment.").save()
    Position.objects.create(name='Treasurer',
                            description="Held the Treasurer position in a commitment"
                                        ".").save()
    Position.objects.create(name='Public Relations responsible',
                            description="Was responsible for the public relations in a "
                                        "commitment.").save()
    Position.objects.create(name='IT responsible',
                            description="Was responsible for the IT department in a "
                                        "commitment.").save()
    Position.objects.create(name='Fundraising responsible',
                            description="Was responsible for the Fundraising "
                                        "department in a commitment.").save()
    Position.objects.create(name='Publication and Administration responsible',
                            description="Was responsible for the Publications and "
                                        "Administrations department in a commitment.")\
        .save()


def create_local_admins():
    """
    Creates the localadmin gruop
   """
    admins = Group.objects.create(name='Local Admins')
    for perm in [
        'add_entry', 'change_entry', 'delete_entry',
        'add_event', 'change_event', 'delete_event',
        'change_incomingapplication', 'delete_incomingapplication',
        'change_incomingapplication', 'delete_incomingapplication',
        'change_outgoingapplication',
        'change_participation', 'delete_participation',
        'change_team']:
        print perm
        admins.permissions.add(Permission.objects.get(codename=perm))
        admins.save()


# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app
