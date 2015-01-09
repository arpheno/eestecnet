# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='name',
            field=models.CharField(default=b'Feedback Sheet', max_length=100),
            preserve_default=True,
        ),
    ]
