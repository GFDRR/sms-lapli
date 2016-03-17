# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0005_auto_20160315_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='station',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='station',
            name='coordonnees_x_y',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, blank=True, verbose_name='Position'),
        ),
    ]
