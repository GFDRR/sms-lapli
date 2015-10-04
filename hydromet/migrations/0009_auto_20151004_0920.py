# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0008_auto_20151004_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='observer',
            field=models.ForeignKey(to='base.PersonneContact'),
        ),
    ]
