# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_record_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='kwh',
            field=models.FloatField(null=True),
        ),
    ]
