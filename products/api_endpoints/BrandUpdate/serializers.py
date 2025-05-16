from rest_framework import serializers
from products.models import ProductVariant, Brand

class BrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'logo', 'slug']
        read_only_fields = ['id']
