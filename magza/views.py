from django.shortcuts import render
from .serializers import *
from rest_framework import generics,viewsets,permissions
from .models import *



# Create your views here.


class MagzaViewSet(viewsets.ModelViewSet):
    queryset = Magzalar.objects.all()
    serializer_class= MagzaSerialzer

class BankaViewSet(viewsets.ModelViewSet):
    queryset=Bankalar.objects.all()
    serializer_class=BankaSerialzer

    


    

    
