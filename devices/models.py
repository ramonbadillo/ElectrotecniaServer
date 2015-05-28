from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    nSerial = models.CharField(max_length=17)
    nKill = models.PositiveIntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
            return self.nSerial
