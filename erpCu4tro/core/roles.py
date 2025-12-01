from django.contrib.auth.models import Group
from rest_framework import permissions
def _in_group(user, groupe_name:str) -> bool:
    return user.is_authenticated and user.groups.filter(name=groupe_name).exists()

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return _in_group(request.user, 'Admin')

class IsSupervisor(permissions.BasePermission):
    def has_permission(self, request, view):
        return _in_group(request.user, 'Supervisor')

class IsOperator(permissions.BasePermission):
    def has_permission(self, request, view):
        return _in_group(request.user, 'Operator')

class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return _in_group(request.user, 'Client')
