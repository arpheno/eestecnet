# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import common.util


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0002_auto_20150511_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('confirmable_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='common.Confirmable')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
            bases=('common.confirmable', common.util.Reversable),
        ),
    ]
