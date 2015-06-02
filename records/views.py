from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Record
from devices.models import Device
from records.models import Record
from .serializers import RecordSerializer
from .serializers import UserSerializer
from rest_framework import viewsets
from django.db.models import Sum
from pprint import pprint
import datetime
from datetime import date
from calendar import monthrange

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
    currentWatts = 0
    totalKwh = 0
    totalCurrentW = 0
    deviceName = {}
    lastUpdate = {}
    #the max and the min Values for the gauges
    maxVal = 0
    minVal = 0

    #
    monthFormated = 0
    yearFormated = 0
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



    print "rango"

    monthFormated = int(month)
    yearFormated = int(year)
    week , days = monthrange( yearFormated , monthFormated)
    print days


    if request.user.is_authenticated():
        result = Record.objects.filter(user = request.user.id,timeStampClient__year=year,
        timeStampClient__month=month)

        devices = result.values('idKill').distinct()

        #For each device in the list make a dictionary with the necesary info to make the gauge
        for device in devices:

            daysData = result.filter(idKill=device['idKill'])
            idDev = daysData.values('idDev').latest('timeStampClient')
            lastUpdate = daysData.values('timestampServer').latest('timeStampClient')


            currentWatts = daysData.values('watts').latest('timeStampClient')

            totalKwh += daysData.aggregate(Sum('kwh'))['kwh__sum']
            totalCurrentW += currentWatts['watts']

            deviceName = Device.objects.filter(pk = idDev['idDev']).values('name','avarage')
            #for day in range(0,days[1])
            #    print day

            deviceData = {
                "idKill" : device['idKill'],
                "currentWatts" : currentWatts['watts'],
                "data" : daysData.aggregate(Sum('kwh'))['kwh__sum']/1000,
                "deviceName" : deviceName[0],
                "lastUpdate" : lastUpdate['timestampServer'],
                "maxVal" : deviceName[0]['avarage']*1.5,
                "minVal" : deviceName[0]['avarage']/2,
            }

            dataGraph.append(deviceData)
            #print deviceData
        context = {
            "queryset" : dataGraph,
            "total" : totalKwh/1000,
            "totalCurrentW" : totalCurrentW,
            "fecha" : str(month) + "/" + str(year)
            #"devices" : result.values('idKill').distinct()
        }

    return render(request, "home.html", context)
