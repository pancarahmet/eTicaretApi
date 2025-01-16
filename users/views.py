from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.


class UserViewSets(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class AdresViewSet(viewsets.ModelViewSet):
    queryset=Adress.objects.all()
    serializer_class=AdresSerializer

class FavoriUrunViewSet(viewsets.ModelViewSet):
    queryset=FavoriUrun.objects.all()
    serializer_class=FavoriUrunSerializer
class RegisterViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer



