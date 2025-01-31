from rest_framework import permissions

class IsSystemUser(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.user.is_systemuser:
            return True
        