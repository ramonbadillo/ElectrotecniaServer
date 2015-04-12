from rest_framework import serializers
from .models import Gadget
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class GadgetSerializer(serializers.HyperlinkedModelSerializer):
    
    user = UserSerializer()
    class Meta:
        model = Gadget
        fields = ('maca','nKill','user')
        
class GadgetSerializerReg(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Gadget
        fields = ('id','maca')