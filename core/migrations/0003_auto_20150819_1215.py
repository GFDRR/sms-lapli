# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150819_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonneContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nomPersonne', models.CharField(max_length=45)),
                ('prenomPersonne', models.CharField(max_length=45)),
                ('telephoneBureau', models.CharField(blank=True, max_length=45)),
                ('telephonePersonnelle', models.CharField(max_length=45)),
                ('emailBureau', models.CharField(blank=True, max_length=45)),
                ('emailPersonnelle', models.CharField(blank=True, max_length=45)),
                ('adressePersonnelle', models.CharField(max_length=45)),
                ('nif', models.CharField(blank=True, max_length=45)),
                ('cin', models.CharField(blank=True, max_length=45)),
                ('nomPoste', models.CharField(blank=True, max_length=45)),
                ('dateEmbauche', models.DateField()),
                ('sectionCommunale', models.ForeignKey(to='core.SectionCommunale')),
            ],
        ),
        migrations.AlterField(
            model_name='departement',
            name='description',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
