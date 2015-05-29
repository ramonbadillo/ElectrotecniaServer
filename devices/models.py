from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    name = models.CharField(max_length=60)
    modelo = models.CharField(max_length=40)
    avarage = models.PositiveIntegerField()
    #nSerial = models.CharField(max_length=17)
    #nKill = models.PositiveIntegerField()
    #user = models.ForeignKey(User)

    def __unicode__(self):
            return str(self.id)
