# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import guardian.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now,
                                                    verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30, null=True, blank=True)),
                ('last_name', models.CharField(max_length=40)),
                ('second_last_name', models.CharField(max_length=40, null=True,
                                                      blank=True)),
                ('email', models.EmailField(unique=True, max_length=75)),
            ],
            options={
                'abstract': False,
            },
            bases=(guardian.mixins.GuardianUserMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='auth.Group')),
                ('test', models.CharField(default=b'LOL', max_length=100)),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
            bases=('auth.group',),
        ),
    ]
