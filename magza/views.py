from django.shortcuts import render
from .serializers import *
from rest_framework import generics,viewsets,permissions
from .models import *
from .permissions import *
from users.permissions import *



# Create your views here.


class MagzaViewSet(viewsets.ModelViewSet):
    queryset = Magzalar.objects.all()
    serializer_class= MagzaSerialzer
    permission_classes=[IsMagzaUser]

class BankaViewSet(viewsets.ModelViewSet):
    queryset=Bankalar.objects.all()
    serializer_class=BankaSerialzer
    permission_classes=[permissions.IsAuthenticated,IsMagzaOwner]

class MCommentViewSet(viewsets.ModelViewSet):
    queryset=MCommet.objects.all()
    serializer_class=MCommentSerializer
    permission_classes=[permissions.IsAuthenticated]

class MPuanViewSet(viewsets.ModelViewSet):
    queryset=MPuan.objects.all()
    serializer_class=MPuanSerializer
    permission_classes=[permissions.IsAuthenticated]

class SistemBakiyeViewSet(viewsets.ModelViewSet):
    queryset=SistemBakiye.objects.all()
    serializer_class=SistemBakiyeSerializer
    permission_classes=[IsSystemUser]




    

    
