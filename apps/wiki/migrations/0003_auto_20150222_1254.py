# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('wiki', '0002_wikipage_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wikipage',
            options={'permissions': (('view_wikipage', 'Can view wikipage'),)},
        ),
    ]
