# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('modelo', models.CharField(max_length=40)),
                ('topValue', models.FloatField()),
                ('botValue', models.FloatField()),
                ('avgValue', models.FloatField()),
            ],
        ),
    ]
