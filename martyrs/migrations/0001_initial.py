# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Martyr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField()),
                ('cause_of_death', models.TextField(max_length=500)),
                ('officer_name', models.CharField(max_length=200)),
                ('governorate', models.CharField(max_length=100)),
            ],
        ),
    ]
