# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import guardian.mixins
from apps.accounts.models import Account


def seed_admin(aapps,schema):
    try:
        Account.objects.create_superuser("admin@eestec.net","1234")
        print "Created account admin@eestec.net with password 1234"
    except:
        print "Could not create account admin@eestec.net with password 1234"
class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150908_1210')
    ]

    operations = [
        migrations.RunPython(seed_admin ),
    ]
