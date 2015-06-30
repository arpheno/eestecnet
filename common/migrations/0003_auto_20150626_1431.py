# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0002_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
