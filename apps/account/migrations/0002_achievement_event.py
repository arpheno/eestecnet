# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='event',
            field=models.ForeignKey(blank=True, to='events.Event', null=True),
            preserve_default=True,
        ),
    ]
