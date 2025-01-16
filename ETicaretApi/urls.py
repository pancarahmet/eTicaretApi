"""ETicaretApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from magza.views import *
from users.views import *
from urunmodelleri.views import *

router=DefaultRouter()
############ MAĞZA #########
router.register(r'magza',MagzaViewSet,basename='magzaViewSet')
router.register(r'banka',BankaViewSet,basename='bankaViewSet')
router.register(r'mpuan',MPuanViewSet,basename='mPuanViewSet')
router.register(r'mcomment',MCommentViewSet,basename='mCommentViewSet')
router.register(r'sistem',SistemBakiyeViewSet,basename='sistemBakiyeViewSet')
########### Urunler #########
router.register(r'sepet',SepetViewSet,basename='sepetViewSet')
router.register(r'category',CategoryViewSet,basename="categoryViewSet")
router.register(r'beden',BedenViewSet,basename="bedenViewSet")
router.register(r'renk',RenkViewSet,basename="RenkViewSet")
router.register(r'urunler',UrunlerViewSet,basename="urunlerViewSet")
router.register(r'ucomment',UCommentViewSet,basename="uCommentViewSet")
router.register(r'upuan',UPuanViewSet,basename="uPuanViewSet")
router.register(r'kargotakip',KargoTakipViewSet,basename="kargoTakipViewSet")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
