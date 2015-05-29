from django.db import models
from devices.models import Device

class Record(models.Model):
    watts = models.FloatField()
    amp = models.FloatField()
    volts = models.FloatField()
    idKill = models.PositiveIntegerField(null=True)
    timeStampClient = models.DateTimeField(null=True)
    timestampServer = models.DateTimeField(auto_now=True,null=True)
    idDev = models.ForeignKey(Device)

    def __unicode__(self):
            return str(self.id)
