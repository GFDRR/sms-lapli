# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prix_marche', '0002_auto_20160227_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='unitemesure',
            field=models.ForeignKey(to='base.UniteMesure', verbose_name='Unite de mesure'),
        ),
        migrations.AlterField(
            model_name='observationdeprix',
            name='unitemesure',
            field=models.ForeignKey(to='base.UniteMesure', verbose_name='Unite de mesure'),
        ),
        migrations.DeleteModel(
            name='UniteMesure',
        ),
    ]
