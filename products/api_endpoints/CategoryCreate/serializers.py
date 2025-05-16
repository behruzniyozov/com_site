from rest_framework.serializers import ModelSerializer
from products.models import Category

class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'image']
        read_only_fields = ['id']
        