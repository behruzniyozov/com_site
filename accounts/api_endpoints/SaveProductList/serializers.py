from rest_framework import serializers
from products.models import Product, ProductVariant

class SaveProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ['id', 'name', 'brand', 'price', 'category']
