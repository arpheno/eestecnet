# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('pages', '0003_auto_20141223_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stub',
            name='link',
            field=models.CharField(max_length=50),
        ),
    ]
