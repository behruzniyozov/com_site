from rest_framework import serializers
from com_site.products.models import ProductReview, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']
        read_only_fields = ['id'] 

class ReviewCreateSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  
    class Meta:
        model = ProductReview
        fields = ['product', 'rating', 'comment']
        read_only_fields = ['user']  

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user  
        return super().create(validated_data)