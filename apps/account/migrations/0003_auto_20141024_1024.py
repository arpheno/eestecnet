# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0001_initial'),
        ('teams', '0001_initial'),
        ('account', '0002_achievement_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='member',
            field=models.ForeignKey(to='teams.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievement',
            name='person',
            field=models.ForeignKey(related_name=b'achievements',
                                    to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievement',
            name='position',
            field=models.ForeignKey(to='account.Position'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eestecer',
            name='groups',
            field=models.ManyToManyField(related_query_name='user',
                                         related_name='user_set', to='auth.Group',
                                         blank=True,
                                         help_text='The groups this user belongs to. A '
                                                   'user will get all permissions '
                                                   'granted to each of his/her group.',
                                         verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eestecer',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user',
                                         related_name='user_set', to='auth.Permission',
                                         blank=True,
                                         help_text='Specific permissions for this user.',
                                         verbose_name='user permissions'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='eestecer',
            unique_together=set([('first_name', 'middle_name', 'last_name')]),
        ),
    ]
