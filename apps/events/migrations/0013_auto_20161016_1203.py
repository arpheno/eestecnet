# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20150222_1254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('name',), 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='participation',
            options={'verbose_name': 'Participant', 'verbose_name_plural': 'Participants'},
        ),
        migrations.AlterModelOptions(
            name='transportation',
            options={},
        ),
    ]
