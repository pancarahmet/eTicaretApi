from rest_framework.permissions import BasePermission
from magza.models import *


class IsMagzaUsers(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET','HEAD','OPTIONS'):
            return True
        
        magza=Magzalar.objects.filter(owner=request.user)
        
        if request.user in magza.owner:
            return True