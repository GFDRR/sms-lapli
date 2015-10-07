# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_personnecontact_cfatachstation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnecontact',
            name='isactif',
            field=models.BooleanField(verbose_name='Active'),
        ),
    ]
