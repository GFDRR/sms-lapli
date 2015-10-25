# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departement',
            name='departement',
            field=models.CharField(max_length=40, verbose_name='Departement'),
        ),
    ]
