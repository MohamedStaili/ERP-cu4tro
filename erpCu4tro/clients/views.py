from rest_framework import viewsets
from accounts.permissions import IsAdmin
from .models import Client, ClientProduct
from .serializers import ClientSerializer, ClientProductSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by("-id")
    serializer_class = ClientSerializer
    permission_classes = [IsAdmin]

class ClientProductsViewSet(viewsets.ModelViewSet):
    queryset =ClientProduct.objects.all().order_by("-id")
    serializer_class = ClientProductSerializer
    permission_classes = [IsAdmin]