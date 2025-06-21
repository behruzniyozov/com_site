from rest_framework import serializers
from products.models import ProductReview, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']
        read_only_fields = ['id']  # Make 'id' read-only to prevent it from being set during creation
    

class ReviewListSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Use the ProductSerializer to represent the product

    class Meta:
        model = ProductReview
        fields = ['id', 'product', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']  # Make 'id' and 'created_at' read-only
