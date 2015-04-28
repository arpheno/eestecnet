# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0002_auto_20150429_0009'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseEvent',
            fields=[
                ('applicable_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='common.Applicable')),
            ],
            options={
                'abstract': False,
            },
            bases=('common.applicable',),
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('baseevent_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='events.BaseEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=('events.baseevent',),
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('baseevent_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='events.BaseEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=('events.baseevent',),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('baseevent_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='events.BaseEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=('events.baseevent',),
        ),
    ]
