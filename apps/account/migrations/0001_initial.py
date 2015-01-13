# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import autoslug.fields


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eestecer',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now,
                                                    verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this '
                                                               'user has all '
                                                               'permissions without '
                                                               'explicitly assigning '
                                                               'them.',
                                                     verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=254,
                                            verbose_name='email address')),
                ('skype',
                 models.CharField(max_length=30, null=True, verbose_name='Skype Account',
                                  blank=True)),
                ('hangouts', models.CharField(max_length=30, null=True,
                                              verbose_name='Google Hangouts account',
                                              blank=True)),
                ('mobile', models.CharField(
                    help_text='Please provide your phone number in +XX XXX XXXXXX '
                              'format',
                    max_length=30, null=True, verbose_name='Mobile Phone Number',
                    blank=True)),
                ('first_name',
                 models.CharField(max_length=30, verbose_name='first name')),
                ('middle_name',
                 models.CharField(max_length=30, verbose_name='middle name',
                                  blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('second_last_name',
                 models.CharField(max_length=30, verbose_name='second last name',
                                  blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('profile_picture',
                 models.ImageField(null=True, upload_to=b'users', blank=True)),
                ('gender', models.CharField(max_length=15,
                                            choices=[(b'm', b'Male'), (b'f', b'Female'),
                                                     (b'x', b'Other')])),
                ('tshirt_size', models.CharField(blank=True, max_length=15, null=True,
                                                 choices=[(b'mxs', b'Male XS'),
                                                          (b'ms', b'Male S'),
                                                          (b'mm', b'Male M'),
                                                          (b'ml', b'Male L'),
                                                          (b'mxl', b'Male XL'),
                                                          (b'mxxl', b'Male XXL'),
                                                          (b'mxxxl', b'Male XXXL'),
                                                          (b'fxs', b'Female XS'),
                                                          (b'fs', b'Female S'),
                                                          (b'fm', b'Female M'),
                                                          (b'fl', b'Female L'),
                                                          (b'fxl', b'Female XL'),
                                                          (b'fxxl', b'Female XXL'),
                                                          (b'fxxxl', b'Female XXXL')])),
                ('allergies', models.CharField(max_length=50, null=True, blank=True)),
                ('passport_number',
                 models.CharField(max_length=20, null=True, blank=True)),
                ('activation_link',
                 models.CharField(max_length=50, null=True, blank=True)),
                ('field_of_study', models.CharField(max_length=50, choices=[
                    (b'ee', b'Electrical Engineering'),
                    (b'it', b'Information Technology'), (b'cs', b'Computer Science'),
                    (b'bm', b'Biomedical Engineering'), (b'tc', b'Telecommunications'),
                    (b'pe', b'Power Engineering'), (b'se', b'Software Engineering'),
                    (b'au', b'Automatics'), (b'ns', b'Natural Sciences'),
                    (b'ss', b'Social Sciences'), (b'ec', b'Economy'),
                    (b'oe', b'Other engineering subjects'), (b'oo', b'Other')])),
                ('food_preferences', models.CharField(default=b'none', max_length=15,
                                                      choices=[(b'none', b'None'),
                                                               (b'kosher', b'Kosher'),
                                                               (b'halal', b'Halal'),
                                                               (b'nopork', b'No Pork'),
                                                               (b'nofish', b'Pescarian'),
                                                               (
                                                               b'veggie', b'Vegetarian'),
                                                               (b'vegan', b'Vegan'), (
                                                               b'insects',
                                                               b'Only Insects'), (
                                                               b'fruit',
                                                               b'Fruitarian')])),
                ('curriculum_vitae',
                 models.FileField(null=True, upload_to=b'cvs', blank=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now,
                                                     verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, verbose_name='active')),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
