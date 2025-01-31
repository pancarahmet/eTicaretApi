from rest_framework.permissions import BasePermission
from .models import *


class IsMagzaUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in ('GET','HEAD','OPTIONS'):
            return True
        if request.method in ('POST'):
            if request.user.is_magza:
                return True
            
        return obj.owner==request.user
class IsMagzaOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner.owner==request.user