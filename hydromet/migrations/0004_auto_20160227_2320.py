# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0003_auto_20160227_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'verbose_name': 'Log', 'verbose_name_plural': 'Log'},
        ),
        migrations.AlterModelOptions(
            name='observateurhydromet',
            options={'verbose_name': 'Observateur (Pluviométrique)', 'verbose_name_plural': 'Observateurs (Pluviométrique)'},
        ),
        migrations.AlterModelOptions(
            name='typeobservation',
            options={'verbose_name': "Type d'Observation (Pluviométrique)", 'verbose_name_plural': "Types d'Observation"},
        ),
        migrations.AlterModelOptions(
            name='typestation',
            options={'verbose_name': 'Type de Station', 'verbose_name_plural': 'Types de Station'},
        ),
        migrations.AlterField(
            model_name='typeobservation',
            name='unitemesure',
            field=models.ForeignKey(verbose_name='Unite de mesure par défaut', blank=True, to='base.UniteMesure', null=True),
        ),
        migrations.AlterField(
            model_name='typestationtypeobservation',
            name='unitemesure',
            field=models.ForeignKey(verbose_name='Unite de mesure pour cette station', blank=True, to='base.UniteMesure', null=True),
        ),
        migrations.DeleteModel(
            name='UniteMesure',
        ),
    ]
