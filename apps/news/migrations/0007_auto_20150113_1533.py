# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0006_auto_20141221_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='headline',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='entry_image',
            new_name='thumbnail',
        ),
    ]
