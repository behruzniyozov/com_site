from rest_framework import serializers
from products.models import Product

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'brand', 'price', 'stock', 'category']
        read_only_fields = ['id']


