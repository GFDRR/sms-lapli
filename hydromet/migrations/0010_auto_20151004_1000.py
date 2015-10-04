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
            name='dateDebut',
            field=models.DateField(verbose_name='Date de debut'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='dateFin',
            field=models.DateField(verbose_name='Date de fin'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='quantitePluie',
            field=models.DecimalField(blank=True, decimal_places=2, verbose_name='Quantite de Pluie', max_digits=15),
        ),
        migrations.AlterField(
            model_name='station',
            name='idSiteSeninnelle',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Site Sentinelle', to='base.SiteSentinelle'),
        ),
        migrations.AlterField(
            model_name='station',
            name='nomStation',
            field=models.CharField(verbose_name='Nom de la Station', max_length=45),
        ),
        migrations.AlterField(
            model_name='station',
            name='typeStation',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Type de la Station', to='hydromet.TypeStation'),
        ),
        migrations.AlterField(
            model_name='station',
            name='uniteMesure',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Unite de mesure', to='hydromet.UniteDeMesure'),
        ),
        migrations.AlterField(
            model_name='unitedemesure',
            name='uniteMesure',
            field=models.CharField(unique=True, max_length=7, verbose_name='Unite de mesure'),
        ),
    ]
