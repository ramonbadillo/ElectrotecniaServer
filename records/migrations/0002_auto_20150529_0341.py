# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='date',
        ),
        migrations.AddField(
            model_name='record',
            name='idKill',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='timeStampClient',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='timestampServer',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
