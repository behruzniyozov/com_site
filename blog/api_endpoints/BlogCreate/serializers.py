from rest_framework import serializers

from blog.models import Blog

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']  # Make 'id', 'author', and 'created_at' read-only

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)