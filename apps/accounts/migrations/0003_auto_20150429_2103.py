# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_account_group_participation'),
        ('common', '0002_applicable_managable'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='applicable',
            field=models.ForeignKey(related_name='packages', to='common.Applicable'),
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(related_query_name=b'user',
                                         related_name='user_set', to='auth.Group',
                                         through='accounts.Participation', blank=True,
                                         help_text='The groups this user belongs to. A '
                                                   'user will get all permissions '
                                                   'granted to each of their groups.',
                                         verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name=b'user',
                                         related_name='user_set', to='auth.Permission',
                                         blank=True,
                                         help_text='Specific permissions for this user.',
                                         verbose_name='user permissions'),
        ),
    ]
