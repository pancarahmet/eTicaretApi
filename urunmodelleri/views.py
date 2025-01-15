from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,status
from .serializers import *
from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class SepetViewSet(viewsets.ModelViewSet):
    queryset=Sepet.objects.all()
    serializer_class=SepetSerializer

    def get_queryset(self):
        return Sepet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
       serializer.save(user=self.request.user)
    
    @action(detail=False,methods=['get'])
    def active(self,request):
        sepet=Sepet.objects.filter(user=request.user,is_complated=False)
        if not sepet:
            sepet=Sepet.objects.create(user=request.user)
        serializer=self.get_serializer(sepet)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=True,methods=['post'])
    def complate(self,request,pk=None):
        sepet=get_object_or_404(Sepet,pk=pk,user=request.user)

        if sepet.is_complated:
            return Response({"detail":"Bu sepet tamamlanmış"})
        
        sepet.is_complated=True
        sepet.save()
        yeni_sepet=Sepet.objects.create(user=request.user)
        return Response(
            {
                "eski_sepet":self.get_serializer(sepet).data,
                "yeni_sepet":self.get_serializer(yeni_sepet).data
            },
            status=status.HTTP_200_OK
        )