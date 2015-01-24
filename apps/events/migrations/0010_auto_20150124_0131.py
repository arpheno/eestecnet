# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20150120_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(default=b'workshop', max_length=40, choices=[(b'ssa', b'Soft Skills Academy'), (b'exchange', b'Exchange'), (b'workshop', b'Workshop'), (b'operational', b'Operational Event'), (b'training', b'Training'), (b'imw', b'IMW'), (b'recruitment', b'recruitment'), (b'project', b'project')]),
            preserve_default=True,
        ),
    ]
