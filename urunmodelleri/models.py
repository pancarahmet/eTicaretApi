from django.db import models
from users.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Renk(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Beden(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Urunler(models.Model):
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING,related_name="urunler")
    name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    aciklama=models.TextField(blank=True,null=True)
    fiyat=models.DecimalField(max_digits=10,decimal_places=2)
    stok=models.PositiveIntegerField(default=0)
    olusturulma_zamani=models.DateTimeField(auto_now_add=True)
    guncelleme_zamani=models.DateTimeField(auto_now=True)
    ebat=models.ManyToManyField(Beden)
    renk=models.ManyToManyField(Renk)

    def __str__(self):
        return self.name
    
class Sepet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sepet")
    olusturulma_zamani=models.DateTimeField(auto_now_add=True)
    guncelleme_zamani=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sepet: {self.id} - {self.user.username}"
    
class SepetUrunleri(models.Model):
    sepet=models.ForeignKey(Sepet,on_delete=models.CASCADE,related_name="sepetUrunleri")
    urun=models.ForeignKey(Urunler,on_delete=models.CASCADE)
    adet=models.PositiveIntegerField(default=1)
    ekleme_zamani=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.urun.name} x {self.adet}"