# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_personnecontact_cfatachstation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commune',
            name='id_code',
            field=models.CharField(unique=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='departement',
            name='departement',
            field=models.CharField(verbose_name='Departement', max_length=40),
        ),
        migrations.AlterField(
            model_name='departement',
            name='id_code',
            field=models.CharField(unique=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='personnecontact',
            name='isactif',
            field=models.BooleanField(verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='sectioncommunale',
            name='id_code',
            field=models.CharField(unique=True, max_length=7),
        ),
    ]
