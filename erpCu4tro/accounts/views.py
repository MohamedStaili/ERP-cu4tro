from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer
from core import roles
class CreateUserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all().order_by('-date_joined')
    serializer_class= UserSerializer
    permission_classes = [roles.IsAdmin]
    #pas de delete , faire desactiver le compte
    http_method_names=['get', 'post', 'put', 'patch']

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        if 'password' in serializer.validated_data:
            instance.set_password(instance.password)
            instance.save()
    
    def perform_destroy(self, instance):
        instance.is_active= False
        instance.save()