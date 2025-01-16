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
class MCommentViewSet(viewsets.ModelViewSet):
    queryset=MCommet.objects.all()
    serializer_class=MCommentSerializer

class MPuanViewSet(viewsets.ModelViewSet):
    queryset=MPuan.objects.all()
    serializer_class=MPuanSerializer

class SistemBakiyeViewSet(viewsets.ModelViewSet):
    queryset=SistemBakiye.objects.all()
    serializer_class=SistemBakiyeSerializer



    

    
