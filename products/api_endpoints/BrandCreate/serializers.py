from rest_framework import serializers
from products.models import ProductVariant, Brand

class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'logo', 'slug']
        read_only_fields = ['id']