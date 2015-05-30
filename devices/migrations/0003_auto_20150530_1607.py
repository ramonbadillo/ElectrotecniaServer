# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20150529_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='avarage',
            field=models.FloatField(),
        ),
    ]
