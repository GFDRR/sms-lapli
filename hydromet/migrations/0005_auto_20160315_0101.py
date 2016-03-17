# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0004_auto_20160227_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observation',
            old_name='note',
            new_name='remarque',
        ),
        migrations.RemoveField(
            model_name='station',
            name='position',
        ),
        migrations.AddField(
            model_name='station',
            name='coordonnees_x_y',
            field=geoposition.fields.GeopositionField(null=True, max_length=42, blank=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='observateurhydromet',
            field=models.ForeignKey(null=True, to='base.Personne', blank=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='time_end',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Heure de Fin'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='time_start',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Heure de Début'),
        ),
    ]
