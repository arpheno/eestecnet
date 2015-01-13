# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0008_auto_20141229_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eestecer',
            old_name='personal',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='eestecer',
            old_name='profile_picture',
            new_name='thumbnail',
        ),
        migrations.AlterField(
            model_name='eestecer',
            name='hangouts',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
