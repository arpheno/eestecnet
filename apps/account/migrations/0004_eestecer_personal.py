# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0003_auto_20141024_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='eestecer',
            name='personal',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
