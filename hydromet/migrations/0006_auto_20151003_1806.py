# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0005_auto_20151003_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniteDeMesure',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('uniteMesure', models.CharField(max_length=7, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='observationpluviometrique',
            name='personne',
            field=models.CharField(max_length=45, default='', verbose_name='Telephone (Personne)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='observationpluviometrique',
            name='valider',
            field=models.BooleanField(verbose_name='Validation'),
        ),
        migrations.AlterField(
            model_name='stationpluviometrique',
            name='idSiteSeninnelle',
            field=models.ForeignKey(to='base.SiteSentinelle', verbose_name='Site Sentinelle', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stationpluviometrique',
            name='typeStation',
            field=models.ForeignKey(to='hydromet.TypeStationPluviometrique', verbose_name='Type de la Station', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='stationpluviometrique',
            name='uniteMesure',
            field=models.ForeignKey(default='', to='hydromet.UniteDeMesure'),
            preserve_default=False,
        ),
    ]
