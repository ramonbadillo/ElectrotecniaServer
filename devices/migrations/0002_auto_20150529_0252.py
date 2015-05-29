# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='nKill',
            new_name='avarage',
        ),
        migrations.RemoveField(
            model_name='device',
            name='nSerial',
        ),
        migrations.RemoveField(
            model_name='device',
            name='user',
        ),
        migrations.AddField(
            model_name='device',
            name='modelo',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='name',
            field=models.CharField(default='default', max_length=60),
            preserve_default=False,
        ),
    ]
