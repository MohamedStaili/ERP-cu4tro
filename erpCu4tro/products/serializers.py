from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['label', 'description', 'base_price', 'type', 'infos_dynamique']

        