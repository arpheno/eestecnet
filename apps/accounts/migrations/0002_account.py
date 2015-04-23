# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login',
                 models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('second_last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
