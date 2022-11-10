from dataclasses import fields
from rest_framework import serializers
from .models import *



class MCserializers(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = MC  