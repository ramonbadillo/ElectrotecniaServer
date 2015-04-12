from django.db import models
from gadgets.models import Gadget
from devices.models import Device

class Registry(models.Model):
    watts = models.IntegerField()
    amp = models.IntegerField()
    volts = models.IntegerField()
    date = models.DateTimeField()
    idGadget = models.ForeignKey(Gadget)
    idDev = models.ForeignKey(Device)
    
    def __unicode__(self):
            return str(self.id)
