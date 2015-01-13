# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0007_auto_20141221_1837'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eestecer',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'user',
                     'verbose_name_plural': 'users'},
        ),
    ]
