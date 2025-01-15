from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from .models import *
from django.utils.text import slugify


class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields=['name']

    def create(self,validated_data):
        if not validated_data.get('slug'):
            validated_data['slug']=slugify(validated_data['name'])
        return super().create(validated_data)
    
    def update(self,instance,validated_data):
        if 'slug' in validated_data:
            if not validated_data['slug']:
                validated_data['slug']=slugify(validated_data.get('name',instance.name))
        return super().update(instance,validated_data)
class RenkSerializer(ModelSerializer):
    class Meta:
        model=Renk
        fields='__all__'
class BedenSerializer(ModelSerializer):
    class Meta:
        model=Beden
        fields='__all__'
class UrunlerSerializer(ModelSerializer):
    class Meta:
        model=Urunler
        exclude=['olusturulma_zamani','guncelleme_zamani','slug']
    def create(self,validated_data):
        if not validated_data.get('slug'):
            validated_data['slug']=slugify(validated_data['name'])
        return super().create(validated_data)
    def update(self,instance,validated_data):
        if 'slug' in validated_data:
            if not validated_data['slug']:
                validated_data['slug']=slugify(validated_data.get('name',instance.name))
        
        return super().update(instance,validated_data)

class CommentSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'

class UPuanSerializer(ModelSerializer):
    class Meta:
        model=UPuan
        fields='__all__'
    
    def create(self, validated_data):
        user=self.context['request'].user
        urun=validated_data['urun']
        puan=validated_data['uPuan']

        puanlama,created=UPuan.objects.update_or_create(
            owner=user,
            urun=urun,
            defaults={'uPuan':puan}
        )
        return puanlama
class SepetUrunleriSerializer(ModelSerializer):
    urun=UrunlerSerializer(read_only=True)
    urun_id=PrimaryKeyRelatedField(queryset=Urunler.objects.all(),source='sepet',write_only=True)
    class Meta:
        model=SepetUrunleri
        fields='__all__'

class SepetSerializer(ModelSerializer):
    sepetUrunleri=SepetUrunleriSerializer(many=True)
    class Meta:
        model=Sepet
        fields='__all__'
    
    def create(self, validated_data):
        urunler_bilgisi=validated_data.pop('urun')
        sepet=Sepet.objects.create(**validated_data)
        for urun_bilgisi in urunler_bilgisi:
            SepetUrunleri.objects.create(sepet=sepet,**urun_bilgisi)
        return sepet
    def update(self, instance, validated_data):
        
        urunler_bilgisi=validated_data.pop('sepet',None)
        instance=super().update(instance,validated_data)

        if urunler_bilgisi:
            for urun_bilgisi in urunler_bilgisi:
                urun=urun_bilgisi.get('urun')
                adet=urun_bilgisi.get('adet',1)

                sepet_urunu,created=SepetUrunleri.objects.get_or_create(
                    sepet=instance,
                    urun=urun,
                    defaults={'adet',adet}
                )
                if not created:
                    urun_bilgisi.adet=adet
                    urun_bilgisi.save()
        return instance