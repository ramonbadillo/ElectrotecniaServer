from rest_framework import serializers
from .models import Registry
from gadgets.serializers import GadgetSerializerReg




class RegistrySerializer(serializers.HyperlinkedModelSerializer):
    
    idGadget = GadgetSerializerReg()
    
    class Meta:
        model = Registry
        fields = ('watts','amp','volts','date','idGadget','idDev')