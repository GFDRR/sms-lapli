# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commune',
            name='id_code',
            field=models.CharField(max_length=7, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='departement',
            name='id_code',
            field=models.CharField(max_length=7, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='sectioncommunale',
            name='id_code',
            field=models.CharField(max_length=7, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='sectioncommunale',
            name='nomOfficiel',
            field=models.CharField(max_length=45, verbose_name='Nom officiel', blank=True),
        ),
    ]
