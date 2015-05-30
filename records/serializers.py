from rest_framework import serializers
from .models import Record
#from gadgets.serializers import GadgetSerializerReg




class RecordSerializer(serializers.HyperlinkedModelSerializer):

#    idGadget = GadgetSerializerReg()

    class Meta:
        model = Record
        fields = ('watts','amp','volts','idKill','timeStampClient','timestampServer','idDev','user')
