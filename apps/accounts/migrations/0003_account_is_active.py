# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_auto_20150516_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True,
                                      help_text='Designates whether this user should '
                                                'be treated as active. Unselect this '
                                                'instead of deleting accounts.',
                                      verbose_name='active'),
            preserve_default=True,
        ),
    ]
