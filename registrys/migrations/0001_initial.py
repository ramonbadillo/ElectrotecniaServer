# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
        ('gadgets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('watts', models.IntegerField()),
                ('amp', models.IntegerField()),
                ('volts', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('idDev', models.ForeignKey(to='devices.Device')),
                ('idGadget', models.ForeignKey(to='gadgets.Gadget')),
            ],
        ),
    ]
