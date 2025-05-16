from rest_framework import serializers
from products.models import ProductVariant, Brand

class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'logo', 'slug']
        read_only_fields = ['id']
        
