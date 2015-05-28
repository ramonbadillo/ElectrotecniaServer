from django.db import models
from devices.models import Device

class Record(models.Model):
    watts = models.FloatField()
    amp = models.FloatField()
    volts = models.FloatField()
    date = models.DateTimeField()

    idDev = models.ForeignKey(Device)

    def __unicode__(self):
            return str(self.id)
