from rest_framework.serializers import ModelSerializer
from products.models import Product


class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category', 'image', 'slug']
        read_only_fields = ['id']