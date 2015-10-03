# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0004_auto_20151003_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationpluviometrique',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stationpluviometrique',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
