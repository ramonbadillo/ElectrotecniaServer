from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    name = models.CharField(max_length=60,default='')
    modelo = models.CharField(max_length=40)

    topValue = models.FloatField()
    botValue = models.FloatField()
    avgValue = models.FloatField()
    #nSerial = models.CharField(max_length=17)
    #nKill = models.PositiveIntegerField()
    #user = models.ForeignKey(User)

    def __unicode__(self):
            return self.name
