from dataclasses import fields
from rest_framework import serializers
from .models import *



class MCserializers(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = MC  

class FQserializers(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = FQ  
class Eventserializers(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = Event

class MCTEAMser(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = MCTEAM

class FQserializers(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = FQ


class FormsSerializers(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = Forms