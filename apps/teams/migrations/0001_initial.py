# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import common.util


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTeam',
            fields=[
                ('applicable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='common.Applicable')),
                ('description', models.TextField(null=True, blank=True)),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
            bases=('common.applicable', common.util.Reversable, models.Model),
        ),
        migrations.CreateModel(
            name='Commitment',
            fields=[
                ('baseteam_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='teams.BaseTeam')),
                ('founded', models.IntegerField(null=True, blank=True)),
                ('rank', models.IntegerField(default=0, null=True, blank=True, choices=[(0, b'Observer'), (1, b'JLC'), (2, b'LC')])),
            ],
            options={
                'abstract': False,
            },
            bases=('teams.baseteam',),
        ),
        migrations.CreateModel(
            name='InternationalBody',
            fields=[
                ('baseteam_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='teams.BaseTeam')),
            ],
            options={
                'abstract': False,
            },
            bases=('teams.baseteam',),
        ),
        migrations.CreateModel(
            name='InternationalDepartment',
            fields=[
                ('baseteam_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='teams.BaseTeam')),
            ],
            options={
                'abstract': False,
            },
            bases=('teams.baseteam',),
        ),
        migrations.CreateModel(
            name='InternationalTeam',
            fields=[
                ('baseteam_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='teams.BaseTeam')),
            ],
            options={
                'abstract': False,
            },
            bases=('teams.baseteam',),
        ),
        migrations.AddField(
            model_name='baseteam',
            name='owner',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
