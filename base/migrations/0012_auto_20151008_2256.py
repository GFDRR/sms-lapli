# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commune',
            name='id_code',
            field=models.CharField(unique=True, verbose_name='Code', max_length=7),
        ),
        migrations.AlterField(
            model_name='departement',
            name='id_code',
            field=models.CharField(unique=True, verbose_name='Code', max_length=7),
        ),
        migrations.AlterField(
            model_name='sectioncommunale',
            name='id_code',
            field=models.CharField(unique=True, verbose_name='Code', max_length=7),
        ),
        migrations.AlterField(
            model_name='sectioncommunale',
            name='nomOfficiel',
            field=models.CharField(blank=True, verbose_name='Nom officiel', max_length=45),
        ),
    ]
