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
    valuesStacked = []
    #
    monthFormated = 0
    yearFormated = 0
    deviceStacked = ""
    listOfDevices = ""
    dataOfDay = 0
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





    monthFormated = int(month)
    yearFormated = int(year)
    week , days = monthrange( yearFormated , monthFormated)




    if request.user.is_authenticated():

        axisX = "[ \'x\',"
        for day in range(1,days+1):
            axisX +=  str(day) + ","
        axisX += "],"

        listOfDevices += "[" #['Refrigerador','Television','Computadora','Caminadora']



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

            deviceName = Device.objects.filter(pk = idDev['idDev']).values('name','avgValue')





#['x', 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,],
#	['lavadora', 30, 200, 200, 400, 150, 250,100,20,100,100,100, 30, 200, 200, 400, 150, 250,100,20,100,100,100, 30, 200, 200, 400, 150, 250,100,20,],
#    ['television', 130, 100, 100, 200, 150, 50,10,20,200,200,200, 30, 200, 200, 400, 150, 250,100,20,100,100,100, 30, 200, 200, 400, 150, 250,100,100,],
#    ['computadora', 230, 200, 200, 0, 250, 250,200,200,200,200, 30, 200, 200, 400, 150, 250,100,20,100,100,100, 30, 200, 200, 400, 150, 250,100,20,100.],
            deviceData = {
                "idKill" : device['idKill'],
                "currentWatts" : currentWatts['watts'],
                "data" : daysData.aggregate(Sum('kwh'))['kwh__sum'],
                "deviceName" : deviceName[0],
                "lastUpdate" : lastUpdate['timestampServer'],
                "maxVal" : deviceName[0]['avgValue']*1.5,
                "minVal" : deviceName[0]['avgValue']/2,
            }


            deviceStacked = "[ \'"

            deviceStacked += deviceName[0]['name']
            deviceStacked += "\',"
            for day in range(1,days+1):
                dataOfDay = daysData.filter(timeStampClient__day=day).aggregate(Sum('kwh'))['kwh__sum']

                if dataOfDay is None:
                    dataOfDay = "0"
                deviceStacked +=  str(dataOfDay) + ","
            deviceStacked +=  "],"
            #print deviceStacked

            valuesStacked.append(deviceStacked)
            #print valuesStacked[0]
            listOfDevices +="\'"
            listOfDevices += deviceName[0]['name']
            listOfDevices +="\',"

            dataGraph.append(deviceData)
        listOfDevices += "]"
            #print deviceData
        context = {
            "queryset" : dataGraph,
            "total" : totalKwh/1000,
            "totalCurrentW" : totalCurrentW,
            "fecha" : datetime.datetime.strptime( "01"+ ""+str(month) + "" + str(year), "%d%m%Y").date(),
            "axisX" : axisX,
            "valuesStacked": valuesStacked,
            "listOfDevices" : listOfDevices
            #"devices" : result.values('idKill').distinct()
        }

    return render(request, "home.html", context)
