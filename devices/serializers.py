from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Device
        fields = ('name','avarage','modelo')
