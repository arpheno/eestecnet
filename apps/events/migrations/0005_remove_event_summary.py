# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0004_auto_20141226_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='summary',
        ),
    ]
