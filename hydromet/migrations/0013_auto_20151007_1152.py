# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0012_unitedemesure_formule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='dateDebut',
            field=models.DateField(verbose_name='Debut'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='dateFin',
            field=models.DateField(verbose_name='Fin'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='temperatureMax',
            field=models.DecimalField(decimal_places=3, verbose_name='Temperature max', blank=True, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='observation',
            name='temperatureMin',
            field=models.DecimalField(decimal_places=3, verbose_name='Temperature min', blank=True, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='unitedemesure',
            name='formule',
            field=models.TextField(verbose_name='Formule', blank='True'),
        ),
    ]
