# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0005_auto_20141117_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eestecer',
            name='food_preferences',
            field=models.CharField(default=b'none', max_length=15,
                                   choices=[(b'none', b'None'), (b'kosher', b'Kosher'),
                                            (b'halal', b'Halal'),
                                            (b'nopork', b'No Pork'),
                                            (b'nofish', b'Pescarian'),
                                            (b'veggie', b'Vegetarian'),
                                            (b'vegan', b'Vegan')]),
        ),
    ]
