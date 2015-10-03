# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0003_auto_20151003_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationpluviometrique',
            name='latitude',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=15),
        ),
        migrations.AlterField(
            model_name='stationpluviometrique',
            name='longitude',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=15),
        ),
    ]
