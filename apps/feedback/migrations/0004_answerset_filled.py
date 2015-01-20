# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20150120_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerset',
            name='filled',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
    ]
