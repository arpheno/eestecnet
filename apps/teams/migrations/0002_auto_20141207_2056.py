# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='cp',
            field=models.OneToOneField(related_name=b'cp_in_board', null=True,
                                       blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='treasurer',
            field=models.OneToOneField(related_name=b'treasurer_in_board', null=True,
                                       blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='vcea',
            field=models.OneToOneField(related_name=b'ea_in_board', null=True,
                                       blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='vcia',
            field=models.OneToOneField(related_name=b'ia_in_board', null=True,
                                       blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='vcpa',
            field=models.OneToOneField(related_name=b'pa_in_board', null=True,
                                       blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='type',
            field=models.CharField(default=b'lc', max_length=30,
                                   choices=[(b'body', b'Body'),
                                            (b'team', b'International Team'),
                                            (b'department', b'Board Department'),
                                            (b'lc', b'Local Committee'),
                                            (b'jlc', b'Junior Local Committee'),
                                            (b'observer', b'Observer')]),
        ),
    ]
