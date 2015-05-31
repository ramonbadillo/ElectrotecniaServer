from django.db import models
from devices.models import Device
from django.contrib.auth.models import User

class Record(models.Model):
    watts = models.FloatField()
    kwh = models.FloatField(null=True)
    amp = models.FloatField()
    volts = models.FloatField()
    idKill = models.PositiveIntegerField(null=True)
    timeStampClient = models.DateTimeField(null=True)
    timestampServer = models.DateTimeField(auto_now=True,null=True)
    idDev = models.ForeignKey(Device)
    user = models.ForeignKey(User)

    def __unicode__(self):
            return str(self.id)
