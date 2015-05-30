from django.shortcuts import render

from .models import Device
from rest_framework import viewsets
from .serializers import DeviceSerializer



class DeviceViewSet(viewsets.ModelViewSet):
    model = Device
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
