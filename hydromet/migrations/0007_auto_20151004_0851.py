# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0006_auto_20151003_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationpluviometrique',
            name='uniteMesure',
            field=models.ForeignKey(verbose_name=b'Unite de mesure', blank=True, to='hydromet.UniteDeMesure', null=True),
        ),
        migrations.AlterField(
            model_name='unitedemesure',
            name='uniteMesure',
            field=models.CharField(unique=True, max_length=7, verbose_name=b'Unite de mesure'),
        ),
    ]
