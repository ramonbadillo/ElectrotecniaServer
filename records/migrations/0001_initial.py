# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devices', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('watts', models.FloatField()),
                ('kwh', models.FloatField()),
                ('amp', models.FloatField()),
                ('volts', models.FloatField()),
                ('idKill', models.PositiveIntegerField()),
                ('timeStampClient', models.DateTimeField()),
                ('timestampServer', models.DateTimeField(auto_now=True)),
                ('idDev', models.ForeignKey(blank=True, to='devices.Device', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
