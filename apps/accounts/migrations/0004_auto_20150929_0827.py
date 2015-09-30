# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='fee',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
    ]
