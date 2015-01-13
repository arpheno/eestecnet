# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0002_auto_20141024_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='alumni',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
