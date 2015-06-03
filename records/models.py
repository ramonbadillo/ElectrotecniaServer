import os
from django.db import models
from devices.models import Device
from django.contrib.auth.models import User
from gadgets.models import Gadget

class Record(models.Model):
    watts = models.FloatField()
    kwh = models.FloatField()
    amp = models.FloatField()
    volts = models.FloatField()
    idKill = models.PositiveIntegerField()
    timeStampClient = models.DateTimeField()
    timestampServer = models.DateTimeField(auto_now=True)
    idDev = models.ForeignKey(Device, null=True,blank = True)
    #idGad = models.ForeignKey(Gadget, blank=True, null=True, default=0)
    user = models.ForeignKey(User)

    def __unicode__(self):
            return str(self.id)

    def create_hash(self):
        return os.urandom(32).encode('hex')



    #Overriding
    def save(self, *args, **kwargs):
        #check if the row with this hash already exists.
        if not self.pk:
            self.hash = self.create_hash()
        #self.my_stuff = 'something I want to save in that field'

        ##self.idDev = Gadget.objects.filter(idKill = self.idKill)
        #checar excepcion para cuando no exista ningun gadget
        #idDevNew = Gadget.objects.filter(idKill = self.idKill).values('idDev')[0]['idDev']
        #self.idDev = Device.objects.get(pk=idDevNew)
        super(Record, self).save(*args, **kwargs)
