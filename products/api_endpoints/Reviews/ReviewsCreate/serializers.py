from rest_framework import serializers
from products.models import ProductReview, Product


class ReviewCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductReview
        fields = ['product', 'rating', 'review']
        read_only_fields = ['user']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return ProductReview.objects.create(**validated_data)
