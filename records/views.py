from django.shortcuts import render

from .models import Record
from devices.models import Device
from .serializers import RecordSerializer
from rest_framework import viewsets

class RecordViewSet(viewsets.ModelViewSet):
    model = Record
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
