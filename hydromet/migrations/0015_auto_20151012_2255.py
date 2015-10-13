# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20151012_2255'),
        ('hydromet', '0014_auto_20151007_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperatureMax', models.DecimalField(null=True, max_digits=5, blank=True, verbose_name='Temperature max', decimal_places=3)),
                ('temperatureMin', models.DecimalField(null=True, max_digits=5, blank=True, verbose_name='Temperature min', decimal_places=3)),
                ('quantitePluie', models.DecimalField(decimal_places=2, max_digits=15, blank=True, verbose_name='Quantite de Pluie')),
            ],
        ),
        migrations.AlterField(
            model_name='observation',
            name='valider',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='log',
            name='observation',
            field=models.ForeignKey(null=True, to='hydromet.Observation', blank=True, default=None),
        ),
        migrations.AddField(
            model_name='log',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact'),
        ),
    ]
