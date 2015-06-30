# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0004_auto_20150626_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType',
                                    null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
