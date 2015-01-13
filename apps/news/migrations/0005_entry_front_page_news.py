# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0004_entry_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='front_page_news',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
