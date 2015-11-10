# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0006_auto_20151107_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='limite',
            field=models.ForeignKey(blank=True, to='base.Limite', null=True),
        ),
    ]
