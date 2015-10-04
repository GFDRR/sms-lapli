# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0009_auto_20151004_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='temperatureMax',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='temperatureMin',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=3, blank=True),
        ),
    ]
