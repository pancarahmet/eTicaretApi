from rest_framework import serializers
from .models import *

class MagzaSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model=Magzalar
        
        exclude=['id','owner','olusturma_zamani','guncelleme_zamani','puan']

    
    def create(self,validated_data):
        user = self.context['request'].user
        return Magzalar.objects.create(owner=user,**validated_data)
        
class BankaSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Bankalar
        exclude=['id']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        request=self.context.get('request')
        if request and hasattr(request,'user'):
            self.fields['owner'].queryset=Magzalar.objects.filter(owner=request.user)
    

        