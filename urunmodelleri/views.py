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
        sepet=sepet.first()
        if not sepet:
            sepet=Sepet.objects.create(user=request.user)
        serializer=self.get_serializer(sepet)
       
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=False,methods=['post'])
    def complate(self,request):
        sepet=Sepet.objects.filter(user=request.user,is_complated=False).first()

        if not sepet:
            return Response({'detail':'Aktif sepet yok'},status=400)
        
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
    @action(detail=True,methods=['get','post'])
    def add_urun(self,request,pk=None):
        sepet,created= Sepet.objects.get_or_create(user=request.user,is_complated=False,pk=pk)

        if request.method=='POST':
            serializer=SepetUrunleriSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            urun=serializer.validated_data['urun']
            adet=serializer.validated_data.get('adet',1)
            sepet_urunu,is_new=SepetUrunleri.objects.update_or_create(
                sepet=sepet,
                urun=urun,
                defaults={'adet':adet}
            )
            return Response({'detail':'ürün eklendi'},status=status.HTTP_201_CREATED)
        
        sepet_serializer=self.get_serializer(sepet)
        return Response(sepet_serializer.data,status=status.HTTP_200_OK)
        
class RenkViewSet(viewsets.ModelViewSet):
    queryset=Renk.objects.all()
    serializer_class=RenkSerializer

class BedenViewSet(viewsets.ModelViewSet):
    queryset=Beden.objects.all()
    serializer_class=BedenSerializer
class UCommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
class UPuanViewSet(viewsets.ModelViewSet):
    queryset=UPuan.objects.all()
    serializer_class=UPuanSerializer
class UrunlerViewSet(viewsets.ModelViewSet):
    queryset=Urunler.objects.all()
    serializer_class=UrunlerSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
class KargoTakipViewSet(viewsets.ModelViewSet):
    queryset=KargoTakip.objects.all()
    serializer_class=KargoTakipSerializer