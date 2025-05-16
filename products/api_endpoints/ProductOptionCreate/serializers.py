from rest_framework import serializers
from products.models import ProductVariant, Product

class ProductOptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['name', 'price', 'product', 'images', 'stock', 'color', 'size', 'is_active']
        read_only_fields = ['id']

    