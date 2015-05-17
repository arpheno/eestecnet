# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import guardian.mixins

import apps.accounts.models


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
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=40)),
                ('second_last_name', models.CharField(max_length=40, blank=True)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('birthday', models.DateField()),
                ('birthday_show', models.BooleanField(default=True)),
                ('tshirt_size', models.CharField(max_length=15, choices=[(b'mxs', b'Male XS'), (b'ms', b'Male S'), (b'mm', b'Male M'), (b'ml', b'Male L'), (b'mxl', b'Male XL'), (b'mxxl', b'Male XXL'), (b'mxxxl', b'Male XXXL'), (b'fxs', b'Female XS'), (b'fs', b'Female S'), (b'fm', b'Female M'), (b'fl', b'Female L'), (b'fxl', b'Female XL'), (b'fxxl', b'Female XXL'), (b'fxxxl', b'Female XXXL')])),
                ('allergies', models.CharField(max_length=300, blank=True)),
                ('food_preferences', models.CharField(blank=True, max_length=30, choices=[(b'none', b'None'), (b'kosher', b'Kosher'), (b'halal', b'Halal'), (b'nopork', b'No Pork'), (b'nofish', b'Pescarian'), (b'veggie', b'Vegetarian'), (b'vegan', b'Vegan')])),
                ('passport_number', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=50, blank=True)),
                ('skype', models.CharField(max_length=50, blank=True)),
                ('hangouts', models.CharField(max_length=50, blank=True)),
                ('gender', models.CharField(max_length=15, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'x', b'Other')])),
                ('field_of_study', models.CharField(max_length=50, choices=[(b'ee', b'Electrical Engineering'), (b'it', b'Information Technology'), (b'cs', b'Computer Science'), (b'bm', b'Biomedical Engineering'), (b'tc', b'Telecommunications'), (b'pe', b'Power Engineering'), (b'se', b'Software Engineering'), (b'au', b'Automatics'), (b'ns', b'Natural Sciences'), (b'ss', b'Social Sciences'), (b'ec', b'Economy'), (b'oe', b'Other engineering subjects'), (b'oo', b'Other')])),
                ('curriculum_vitae', models.FileField(null=True, upload_to=b'currcula_vitae', blank=True)),
                ('receive_eestec_active', models.BooleanField(default=True)),
                ('activation_link', models.CharField(max_length=100, blank=True)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('is_superuser', models.BooleanField(default=False, help_text=b'Designates that this user has all permissions without  explicitly assigning them.')),
            ],
            options={
                'abstract': False,
            },
            bases=(guardian.mixins.GuardianUserMixin, apps.accounts.models.AbstractAccount, models.Model, object),
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
