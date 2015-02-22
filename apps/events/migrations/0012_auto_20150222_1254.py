# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0011_auto_20150222_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('name',), 'verbose_name': 'Event',
                     'verbose_name_plural': 'Events',
                     'permissions': (('view_event', 'Can view event'),)},
        ),
        migrations.AlterModelOptions(
            name='participation',
            options={'verbose_name': 'Participant',
                     'verbose_name_plural': 'Participants',
                     'permissions': (('view_participation', 'Can view Participation'),)},
        ),
        migrations.AlterModelOptions(
            name='transportation',
            options={
            'permissions': (('view_transportation', 'Can view Transportation'),)},
        ),
    ]
