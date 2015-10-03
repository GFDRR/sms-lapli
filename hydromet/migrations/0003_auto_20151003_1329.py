# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0002_auto_20151003_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationpluviometrique',
            name='idStation',
            field=models.CharField(max_length=5, blank=True),
        ),
        migrations.AlterField(
            model_name='stationpluviometrique',
            name='idSiteSeninnelle',
            field=models.ForeignKey(verbose_name=b'Site Sentinelle', blank=True, to='base.SiteSentinelle', null=True),
        ),
        migrations.AlterField(
            model_name='stationpluviometrique',
            name='typeStation',
            field=models.ForeignKey(verbose_name=b'Type de la Station', blank=True, to='hydromet.TypeStationPluviometrique', null=True),
        ),
    ]
