# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0005_auto_20150825_2002'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AffectationSiteSentinelle',
        ),
        migrations.AlterField(
            model_name='personnecontact',
            name='telephoneBureau',
            field=models.CharField(max_length=45, blank=True),
        ),
        migrations.AlterField(
            model_name='sitesentinelle',
            name='hauteur',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sitesentinelle',
            name='latitude',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sitesentinelle',
            name='longitude',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
    ]
