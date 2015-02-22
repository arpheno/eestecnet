# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0009_auto_20150113_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'permissions': (('view_achievement', 'Can view achievement'),)},
        ),
        migrations.AlterModelOptions(
            name='eestecer',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'user',
                     'verbose_name_plural': 'users',
                     'permissions': (('view_eestecer', 'Can view Eestecer'),)},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'permissions': (('view_position', 'Can view position'),)},
        ),
    ]
