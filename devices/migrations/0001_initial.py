# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
<<<<<<< HEAD
from django.conf import settings
=======
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
<<<<<<< HEAD
                ('nSerial', models.CharField(max_length=17)),
                ('nKill', models.PositiveIntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
=======
                ('name', models.CharField(max_length=255)),
                ('avarage', models.PositiveIntegerField()),
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
            ],
        ),
    ]
