# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prix_marche', '0003_auto_20160227_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observationdeprix',
            old_name='description',
            new_name='remarque',
        ),
        migrations.AlterField(
            model_name='marche',
            name='hauteur',
            field=models.DecimalField(verbose_name='Hauteur', default=0, max_digits=8, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='marche',
            name='latitude',
            field=models.DecimalField(verbose_name='Latitude', default=0, max_digits=10, decimal_places=7),
        ),
        migrations.AlterField(
            model_name='marche',
            name='limite',
            field=models.ForeignKey(verbose_name='Limite Administrative', to='base.Limite', null=True),
        ),
        migrations.AlterField(
            model_name='marche',
            name='longitude',
            field=models.DecimalField(verbose_name='Longitude', default=0, max_digits=10, decimal_places=7),
        ),
    ]
