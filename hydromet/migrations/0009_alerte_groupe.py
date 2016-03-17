# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('hydromet', '0008_alerte'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerte',
            name='groupe',
            field=models.ForeignKey(null=True, verbose_name='Groupe Concerné', to='auth.Group', blank=True),
        ),
    ]
