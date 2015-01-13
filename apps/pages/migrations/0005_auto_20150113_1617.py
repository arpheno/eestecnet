# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('pages', '0004_auto_20141231_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stub',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='stub',
            old_name='title',
            new_name='name',
        ),
    ]
