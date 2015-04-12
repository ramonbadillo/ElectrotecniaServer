from django.shortcuts import render

from .models import Gadget
from rest_framework import viewsets
from .serializers import GadgetSerializer

class GadgetViewSet(viewsets.ModelViewSet):
    model = Gadget
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer