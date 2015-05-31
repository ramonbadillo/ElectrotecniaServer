from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Record
from devices.models import Device
from records.models import Record
from .serializers import RecordSerializer
from .serializers import UserSerializer
from rest_framework import viewsets
from django.db.models import Sum
import datetime

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

    dataGraph = []
    deviceData = {}
    daysData = {}
    idDev = {}
    #manejar excepcion de que no este la fecha
    #date = request.GET['date']
    #print date
    if request.method == 'GET' and 'month' in request.GET:
        month = request.GET['month']
        year = request.GET['year']
    else:
        d = datetime.date.today()
        month = '%02d' % d.month
        year = '%04d' % d.year




    if request.user.is_authenticated():
        result = Record.objects.filter(user = request.user.id,timeStampClient__year=year,
        timeStampClient__month=month)#.values('idKill').distinct()
        devices = result.values('idKill').distinct()
        for device in devices:
            #print device['idKill']
            daysData = result.filter(idKill=device['idKill'])
            idDev = daysData.values('idDev').latest('timeStampClient')#.latest('timeStampClient')
            #print idDev['idDev']
            print daysData.aggregate(Sum('watts'))
            deviceData = {
                "idKill" : device['idKill'],
                "data" : daysData.aggregate(Sum('watts'))['watts__sum'],
                "device" : idDev['idDev']
            }

            dataGraph.append(deviceData)
            #print deviceData
        context = {
            "queryset" : dataGraph
            #"devices" : result.values('idKill').distinct()
        }

    return render(request, "home.html", context)
