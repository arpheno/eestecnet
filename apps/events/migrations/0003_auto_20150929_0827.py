# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150925_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseevent',
            name='end_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exchange',
            name='participation_fee',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
