# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0006_auto_20141221_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='eestecer',
            name='receive_eestec_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eestecer',
            name='show_date_of_birth',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
