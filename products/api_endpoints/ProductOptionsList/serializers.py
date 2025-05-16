from rest_framework import serializers
from products.models import ProductVariant

class ProductOptionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'product', 'option', 'value']
        read_only_fields = ['id']