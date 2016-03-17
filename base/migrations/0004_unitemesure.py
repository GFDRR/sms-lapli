# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151112_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniteMesure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=45)),
                ('unite', models.CharField(max_length=7, unique=True)),
                ('description', models.TextField(blank=True)),
                ('formule', models.DecimalField(verbose_name='Formule', null=True, blank=True, decimal_places=3, max_digits=5)),
            ],
            options={
                'verbose_name': 'Unité de Mesure',
                'verbose_name_plural': 'Unités de Mesure',
            },
        ),
    ]
