from rest_framework import serializers
from .models import Record
from django.contrib.auth.models import User
#from .serializers import UserSerializer
#from gadgets.serializers import GadgetSerializerReg


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('user','email')
    #username = serializers.CharField(max_length=100)

'''
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
'''

class RecordSerializer(serializers.HyperlinkedModelSerializer):

#    idGadget = GadgetSerializerReg()
    #user = UserSerializer()
    class Meta:
        model = Record
        fields = ('watts','amp','volts','idKill','timeStampClient','timestampServer','idDev','user')
