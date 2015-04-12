from django.shortcuts import render

from .models import Registry
from devices.models import Device
from gadgets.models import Gadget
from .serializers import RegistrySerializer
from rest_framework import viewsets

class RegistryViewSet(viewsets.ModelViewSet):
    model = Registry
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer