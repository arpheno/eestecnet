# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0004_eestecer_personal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='member',
            field=models.ForeignKey(blank=True, to='teams.Team', null=True),
        ),
    ]
