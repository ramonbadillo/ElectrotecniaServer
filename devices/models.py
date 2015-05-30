from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User


class Device(models.Model):
    name = models.CharField(max_length=60)
    modelo = models.CharField(max_length=40)
    avarage = models.FloatField()
    #nSerial = models.CharField(max_length=17)
    #nKill = models.PositiveIntegerField()
    #user = models.ForeignKey(User)

    def __unicode__(self):
            return str(self.id)
=======

class Device(models.Model):
    name = models.CharField(max_length = 255)
    avarage = models.PositiveIntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
