from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Record
from devices.models import Device
from records.models import Record
from .serializers import RecordSerializer
from .serializers import UserSerializer
from rest_framework import viewsets

class RecordViewSet(viewsets.ModelViewSet):
    model = Record
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

def home(request):
    context = {}
    if request.user.is_authenticated():

        context = {
            "queryset" : Record.objects.filter(user = request.user.id).values('idKill').distinct()

        }

    return render(request, "home.html", context)
