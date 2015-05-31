from rest_framework import serializers
from .models import Record
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('user','email')


class RecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Record
        fields = ('watts','kwh','amp','volts','idKill','timeStampClient','timestampServer','idDev','user')
