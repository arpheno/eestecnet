# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTeam',
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
            name='Commitment',
            fields=[
                ('baseteam_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='teams.BaseTeam')),
            ],
            options={
                'abstract': False,
            },
            bases=('teams.baseteam',),
        ),
        migrations.CreateModel(
            name='InternationalTeam',
            fields=[
                ('baseteam_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='teams.BaseTeam')),
            ],
            options={
                'abstract': False,
            },
            bases=('teams.baseteam',),
        ),
    ]
