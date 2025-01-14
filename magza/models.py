from django.db import models
from users.models import User

# Create your models here.

class MCommet(models.Model):
    owner=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    mYorum=models.TextField()

    def __str__(self):
        return self.owner.ad
class MPuan(models.Model):
    owner=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    mPuan=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.owner.ad} - {self.mPuan}"


class Magzalar(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userMagza")
    mAdi=models.CharField(max_length=255)
    mTelefon=models.CharField(max_length=15)
    mAdresIl=models.CharField(max_length=30)
    mAdresIlce=models.CharField(max_length=50)
    mAdres=models.TextField()
    mEmail=models.EmailField(max_length=255,unique=True)
    mLogo=models.FileField(upload_to="magzaLogo",null=True,blank=True)
    mWebAdres=models.CharField(max_length=255)
    mVn=models.CharField(max_length=15)
    mVd=models.CharField(max_length=250)
    mBakiye=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    puan=models.ForeignKey()


    def __str__(self):
        return self.mAdi


    # mbakiye-sepet bakiyesi(100TL)
    # mbakiye + (sepet bakiyesi * 0.85)(85TL)
    # sistem bakiyesi + (sepet bakiyesi * 0.15)(15TL)
class Bankalar(models.Model):
    owner=models.ForeignKey(Magzalar,on_delete=models.CASCADE)
    bankaAdi=models.CharField(max_length=255)
    iban=models.CharField(max_length=50)
    
    def __str__(self):
        return self.bankaAdi


    
class SistemBakiye(models.Model):
    sBakiye=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    gelenMagza=models.ForeignKey(Magzalar,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Magza: {self.gelenMagza.mAdi} - Bakiye: {self.sBakiye}"

