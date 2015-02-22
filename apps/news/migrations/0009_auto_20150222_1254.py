# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0008_entry_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries',
                     'permissions': (('view_entry', 'Can view entry'),)},
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'permissions': (('view_membership', 'Can view membership'),)},
        ),
    ]
