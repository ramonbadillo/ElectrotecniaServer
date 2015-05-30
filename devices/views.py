from django.shortcuts import render

from .models import Device
from rest_framework import viewsets
from .serializers import DeviceSerializer

<<<<<<< HEAD

class DeviceViewSet(viewsets.ModelViewSet):
    model = Device
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
=======
class DeviceViewSet(viewsets.ModelViewSet):
    model = Device
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
