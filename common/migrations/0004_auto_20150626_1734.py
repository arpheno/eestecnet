# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0003_auto_20150626_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
