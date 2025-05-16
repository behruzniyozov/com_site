from rest_framework import serializers
from products.models import ProductVariant

class ProductOptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['name', 'price', 'product', 'images', 'stock', 'color', 'size', 'is_active']
        read_only_fields = ['id']