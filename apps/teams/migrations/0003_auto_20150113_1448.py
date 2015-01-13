# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('teams', '0002_auto_20141207_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='type',
            new_name='category',
        ),
    ]
