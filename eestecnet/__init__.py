# -*- coding: UTF-8 -*-
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_syncdb
from django.utils.datetime_safe import datetime
from eestecnet import settings

from django.db.models.signals import post_syncdb
from members.models import Member


def create_eestec_lcs(sender,**kwargs):
    if kwargs['app'].__name__ == settings.INSTALLED_APPS[-1] + ".models" and not len(Member.objects.all()):
        Member.objects.create(name='Aachen',
                              founded=1986,
                              website="http://www.eestec.rwth-aachen.de",
                              address="Karmansr. 9\n52056 Aachen\nGermany", )
        Member.objects.create(name='Ankara',
                              founded=2006,
                              website="http://eestectr.org/ankara",
                              address="Middle East Technical University\nDepartment of Electrical and Electronics Engineering\A-203 06531 Ankara\nTurkey")
        Member.objects.create(name='Antwerp',
                              founded=2010,
                              website="http://www.eestec.be",
                              address="Middelheimlaan 1\n2020 Antwerpen\nBelgium")
        Member.objects.create(name='Athens',
                              founded=2004,
                              website="http://www.eestec.ntua.gr",
                              address="Iroon Polytexneiou 9\n Zografou 15780\nGreece")
        Member.objects.create(name='Banja Luka',
                              founded=2004,
                              website="http://www.eestec.etfbl.net",
                              address='Patre 5th\nFaculty of Electrical Engineering\n78 000\bBanja Luka\nBosnia')
        Member.objects.create(name='Belgrade',
                              founded=2000,
                              website="http://www.eestec.etf.rs",
                              address='Bulevar kralja Aleksandra 73\n11000 Belgrade\nSerbia')
        Member.objects.create(name='Bucharest',
                              founded=2003,
                              website="http://www.eestec.ro",
                              address="Splaiul Independentei nr.313\ncorp Rectorat\nAN 204bis\n060042 Bucharest\nRomania")
        Member.objects.create(name='Budapest',
                              founded=1986,
                              website="http://www.eestec.hu/pages/home.php",
                              address=u"Eszék utca 9-11\nH-1114 Budapest\nHungary")
        Member.objects.create(name='Consenza',
                              founded=1998,
                              website="http://www.asiunical.org",
                              address="ASI-UNICAL\nvia Pietro Bucci, Cubo 42D, piano terra\nUniversita della Calabria\n87036 Arcavacata di Rende Cosenza)\nItaly")
        Member.objects.create(name='Craiova',
                              founded=2006,
                              website="http://www.eestec.go.ro",
                              address="B-dul Decebal Nr. 107, Sala N8\nCraiova 200440,Dolj\nRomania")
        Member.objects.create(name='Delft',
                              founded=1906,
                              website="http://www.etv.tudelft.nl",
                              address="Mekelweg 4\n 2628 CD Delft\nThe Netherlands")
        Member.objects.create(name='East Sarajevo',
                              founded=2005,
                              website="http://www.eestec-es.rs.ba",
                              address="Vuka Karadzica 30, Istacno Sarajevo, Republika Srpska,\nBosna i Hercegovina")
        Member.objects.create(name='Eskisehir',
                              founded=2006,
                              website="http://www.eesteceskisehir.net",
                              address="Anadolu University, Iki Eylul Campus, Electrical and Electronics Department\nTurkey")
        Member.objects.create(name='Famagusta',
                              founded=2006,
                              address="Electrical and Electronic Engineering Department\nEastern Mediterranean University\nFamagusta, via Mersin 10 \nTurkey")
        Member.objects.create(name='Gliwice',
                              founded=2010,
                              address="Gliwice 44-100\nAkademicka 16\nPoland")
        Member.objects.create(name='Hamburg',
                              founded=2004,
                              website="http://www.eestec-hamburg.de",
                              address=u"EESTEC für Hamburg e.V.\nc/o FSR E/I, Berliner Tor 7, 20099 Hamburg")
        Member.objects.create(name='Helsinki',
                              founded=1986,
                              website="http://eestec.ayy.fi",
                              address="SIK / EESTEC LC Helsinki PL 13000, 00076 AALTO\nFinland")
        Member.objects.create(name='Istanbul',
                              founded=2005,
                              website="http://www.eestec.itu.edu.tr",
                              address=u"EESTEC LC Istanbul\nITÜ Elektrik-Elektronik Fakültesi\nMaslak\Istanbul\n34469\nTurkey")
        Member.objects.create(name='Izmir',
                              founded=2009,
                              address=u"Dokuz Eylül Üniversitesi, Tinaztepe Kampüsü, Elektrik-Elektronik Müh., Toplu-luklar odasi\nBuca/Izmir\nTurkey")
        Member.objects.create(name='Krakow',
                              founded=1998,
                              website="http://www.eestec.agh.edu.pl",
                              address="Akademia Gorniczo-Hutnicza im. Stanislawa Staszica w Krakowie\nAl. Mickiewicza 30\n30-059 Krakow")
        Member.objects.create(name='Lille',
                              founded=2010,
                              website="http://www.eesteclille.wordpress.com",
                              address="Club EESTEC\n Polytech Lille,E402\nAvenue Paul Langevin\n59655 Villeneuve d'Ascq cedex\nFrance")
        Member.objects.create(name='Lisbon',
                              founded=2010,
                              address="Nucleo de Engenharia Electrotecnica e Computadores\n Dep. Engenharia Electrecnica\n Faculdade de Ciencias e Tecnologias\n 2829-516 Caparica\nPortugal")
        Member.objects.create(name='Ljubljana',
                              founded=1986,
                              website="http://www.eestec-lj.org",
                              address="EESTEC, drustvo studentov elektrotehnike in racunalnistva\n SOU - mednarodna pisarna\n Vojkova ulica 63\n1000 Ljubljana\nSlovenia")
        Member.objects.create(name='Madrid',
                              founded=1986,
                              website="http://www.eestec.es",
                              address=u"Eurielec - EESTEC LC Madrid\nETSI Telecomunicación UPM\nAvda.Complutense 30\n28040 - Madrid\n Spain")
        Member.objects.create(name='Munich',
                              founded=1999,
                              website="http://eestec.tum.de",
                              address="uEESTEC Munich e.V.\nTechnische Universität München\nArcisstr.21\n80333 München\nGermany")
        Member.objects.create(name='Nis',
                              founded=2000,
                              website="http://eestec.rs",
                              address="Aleksandra Medvedeva 14\n18000 Nis\nSerbia")
        Member.objects.create(name='Novi Sad',
                              founded=2000,
                              website="http://www.eestecns.org",
                              address="Trg Dositeja Obradovica 6\n21000 Novi Sad\nSerbia")
        Member.objects.create(name='Podgorica',
                              founded=2000,
                              website="http://www.eestec.me",
                              address="University of Montenegro, Faculty of Electrical Engineering\nDzordza Vasingtona bb.\n 20 000 Podgorica\nMontenegro")
        Member.objects.create(name='Riga',
                              founded=2008,
                              website="http://www.eestec.lv",
                              address="EESTEC; Kronvalda bulvaris 1\nRiga\Latvia\LV-1010")
        Member.objects.create(name='Rijeka',
                              founded=1999,
                              website="http://www.eestec.hr",
                              address="Vukovarska 58\n51000 Rijeka\nCroatia")
        Member.objects.create(name='Sarajevo',
                              founded=2006,
                              website="http://www.eestec-sa.ba",
                              address="Zmaja od Bosne bb\n71 000 Sarajevo\nBosnia and Herzegovina")
        Member.objects.create(name='Skopje',
                              founded=2003,
                              website="http://www.eestec-sk.org.mk",
                              address="Fakultet za Elektrotehnika i informaciski tehnologii\nul. Rugjer Boshkovikj b.b\n1000 Skopje\nMacedonia")
        Member.objects.create(name='Tallinn',
                              founded=2005,
                              website="http://www.eestec.ee",
                              address="EESTEC LC Tallinn\nEhitajate tee 5\n19086 Tallinn\nEstonia")
        Member.objects.create(name='Tampere',
                              founded=1986,
                              website="http://tampere.eestec.net",
                              address="TTY/EESTEC\nKorkeakoulunkatu 3\n33720 Tampere\nFinland")
        Member.objects.create(name='Trieste',
                              founded=2006,
                              website="http://ts.eestec.it",
                              address="EESTEC LC Trieste - via Fabio Severo, 154 - C.d.S. E3 - 34127 -Trieste\nItaly")
        Member.objects.create(name='Tuzla',
                              founded=2007,
                              website="http://www.eestec-tz.ba",
                              address="Franjevacka 2,75000 Tuzla, Bosnia and Herzegovina")
        Member.objects.create(name='Xanthi',
                              founded=2010,
                              website="http://eestec.ee.duth.gr",
                              address="Tsimiski street, xanthi\nGreece")
        Member.objects.create(name='Zagreb',
                              founded=2007,
                              website="http://eestec-zg.hr",
                              address="FER\nUnska 3\n10 000 Zagreb\nCroatia")
        Member.objects.create(name='Zurich',
                              founded=1986,
                              website="http://eestec.ch",
                              address=u"AMIV an der ETH Zuerich\nEESTEC LC Zurich\nCAB E37\nUniversitätsstrasse 6\n8092 Zürich\nSwitzerland")
        for lc in Member.objects.all():
            lc.description=open("eestecnet/lc/"+lc.slug+".txt").read()
            lc.save()
def create_local_admins(sender, **kwargs):

    """
    Creates the localadmin gruop
   """
    if kwargs['app'].__name__ == settings.INSTALLED_APPS[-1] + ".models" and not len(Group.objects.all()):
        admins = Group.objects.create(name='Local Admins')
        for perm in [
            'add_entry', 'change_entry', 'delete_entry',
            'add_event', 'change_event', 'delete_event',
            'add_application', 'change_application', 'delete_application',
            'add_eestecer', # This is necessary so local admins can see their members
            'change_member']:
            admins.permissions.add(Permission.objects.get(codename=perm))
            admins.save()
post_syncdb.connect(create_local_admins)
post_syncdb.connect(create_eestec_lcs)
