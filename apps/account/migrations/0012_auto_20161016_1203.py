# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={},
        ),
        migrations.AlterModelOptions(
            name='eestecer',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={},
        ),
        migrations.AlterField(
            model_name='eestecer',
            name='curriculum_vitae',
            field=models.FileField(null=True, upload_to=b'cvs', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eestecer',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'users', blank=True),
            preserve_default=True,
        ),
    ]
