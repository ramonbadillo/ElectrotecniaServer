from django.db import models

class Device(models.Model):
    name = models.CharField(max_length = 255)
    avarage = models.PositiveIntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name