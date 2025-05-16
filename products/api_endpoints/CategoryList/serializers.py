from rest_framework.serializers import ModelSerializer
from products.models import Product, Category


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image']