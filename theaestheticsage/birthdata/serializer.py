from rest_framework import serializers
from . models import *
class Birthserializer(serializers.ModelSerializer):
    class Meta:
        model=Birthdata
        fields=['latitude','longitude','date','month','year','hour','minutes']
        