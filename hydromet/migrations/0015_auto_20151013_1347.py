# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20151013_1347'),
        ('hydromet', '0014_auto_20151007_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperatureMax', models.DecimalField(max_digits=5, null=True, decimal_places=3, blank=True, verbose_name='Temperature max')),
                ('temperatureMin', models.DecimalField(max_digits=5, null=True, decimal_places=3, blank=True, verbose_name='Temperature min')),
                ('quantitePluie', models.DecimalField(max_digits=15, decimal_places=2, blank=True, verbose_name='Quantite de Pluie')),
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
            field=models.ForeignKey(to='hydromet.Observation', default=None, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact'),
        ),
    ]
