from django.db import models
from django.contrib.auth.models import User

class Gadget(models.Model):
    maca = models.CharField(max_length=17)
    nKill = models.PositiveIntegerField()
    user = models.ForeignKey(User)