from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets,permissions
from .permissions import *

# Create your views here.


class UserViewSets(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsSystemUser]

class AdresViewSet(viewsets.ModelViewSet):
    queryset=Adress.objects.all()
    serializer_class=AdresSerializer
    permission_classes=[permissions.IsAuthenticated]

class FavoriUrunViewSet(viewsets.ModelViewSet):
    queryset=FavoriUrun.objects.all()
    serializer_class=FavoriUrunSerializer
    permission_classes=[permissions.IsAuthenticated]

class RegisterViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer



