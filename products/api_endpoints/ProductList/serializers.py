from rest_framework.serializers import ModelSerializer
from products.models import Product

class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'image', 'slug']