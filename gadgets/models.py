from django.db import models
from django.contrib.auth.models import User
from devices.models import Device

class Gadget(models.Model):
    name = models.CharField(max_length=60)
    idKill = models.PositiveIntegerField( unique= True)
    user = models.ForeignKey(User)
    idDev = models.ForeignKey(Device)


    def __unicode__(self):
            return self.name
