# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prix_marche', '0004_auto_20160315_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marche',
            name='position',
        ),
        migrations.AddField(
            model_name='marche',
            name='coordonnees_x_y',
            field=geoposition.fields.GeopositionField(null=True, max_length=42, verbose_name='Position', blank=True),
        ),
    ]
