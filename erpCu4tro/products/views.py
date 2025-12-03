from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from accounts.permissions import IsAdmin

# Create your views here.

class ProductViews(viewsets.ModelViewSet):
    queryset=Product.objects.all().order_by('-id')
    permission_classes=[IsAdmin]
    serializer_class=ProductSerializer
