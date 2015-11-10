# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='observation',
            name='time_end',
            field=models.DateTimeField(verbose_name='Heure de Fin'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='time_result',
            field=models.DateTimeField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='time_start',
            field=models.DateTimeField(verbose_name='Heure de Début'),
        ),
        migrations.AlterField(
            model_name='station',
            name='limite',
            field=models.ForeignKey(verbose_name='Zone', blank=True, null=True, to='base.Limite'),
        ),
    ]
