# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0006_auto_20150113_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='participants',
            new_name='members',
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(
                help_text='Please provide a detailed description for interested '
                          'readers'),
            preserve_default=True,
        ),
    ]
