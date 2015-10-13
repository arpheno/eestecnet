# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0004_auto_20150929_0827'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='group',
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name=b'user', related_name='user_set', to='auth.Permission',
                                         blank=True),
        ),
    ]
