from django.shortcuts import render, get_object_or_404

from .models import Gadget
from django.http import HttpResponse, Http404

from rest_framework import viewsets
from .serializers import GadgetSerializer

class GadgetViewSet(viewsets.ModelViewSet):
    model = Gadget
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer
    
def gadgetDashboard(request,maca):
    gadget = get_object_or_404(Gadget,user=maca)
    return render(request,'dashboard.html',{'gadget':gadget})