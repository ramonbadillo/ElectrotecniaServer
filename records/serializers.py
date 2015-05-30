from rest_framework import serializers
from .models import Record
from django.contrib.auth.models import User
#from gadgets.serializers import GadgetSerializerReg


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)



class RecordSerializer(serializers.HyperlinkedModelSerializer):

#    idGadget = GadgetSerializerReg()
    user = UserSerializer()
    class Meta:
        model = Record
        fields = ('watts','amp','volts','idKill','timeStampClient','timestampServer','idDev','user')
