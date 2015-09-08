# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('accounts', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('confirmable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='common.Confirmable')),
                ('group', models.ForeignKey(to='auth.Group')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('common.confirmable',),
        ),
        migrations.AddField(
            model_name='group',
            name='applicable',
            field=models.ForeignKey(to='common.Applicable'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(related_query_name=b'user', related_name='user_set', to='auth.Group', through='accounts.Participation', blank=True, help_text=b'The groups this user belongs to. A user will  get all permissions granted to each of  their groups.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name=b'user', related_name='user_set', null=True, to='auth.Permission', blank=True),
            preserve_default=True,
        ),
    ]
