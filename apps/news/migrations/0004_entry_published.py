# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0003_membership_alumni'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
