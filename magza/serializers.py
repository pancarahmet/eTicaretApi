from rest_framework import serializers
from .models import *

class MagzaSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Magzalar
        fields='__all__'