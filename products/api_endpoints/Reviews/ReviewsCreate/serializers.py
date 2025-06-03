from rest_framework import serializers
from com_site.products.models import Review

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'comment']
        read_only_fields = ['user']  # Assuming the user is set automatically in the view

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user  # Set the user from the request
        return super().create(validated_data)