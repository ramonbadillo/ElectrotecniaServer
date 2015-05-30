from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
<<<<<<< HEAD

    class Meta:
        model = Device
        fields = ('name','avarage','modelo')
=======
    
    class Meta:
        model = Device
        fields = ('name','avarage')
>>>>>>> 0339671924fedaf831644945f347abc8f42e3d81
