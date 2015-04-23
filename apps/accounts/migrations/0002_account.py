# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
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
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30, null=True, blank=True)),
                ('last_name', models.CharField(max_length=40)),
                ('second_last_name',
                 models.CharField(max_length=40, null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('groups', models.ManyToManyField(related_query_name='user',
                                                  related_name='user_set',
                                                  to='auth.Group', blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user',
                                                            related_name='user_set',
                                                            to='auth.Permission',
                                                            blank=True,
                                                            help_text='Specific permissions for this user.',
                                                            verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
