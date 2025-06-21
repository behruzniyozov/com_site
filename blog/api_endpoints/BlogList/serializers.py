from rest_framework import serializers
from blog.models import Blog

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'content' , 'created_at']
        read_only_fields = ['id', 'user', 'created_at']  # Make 'id', 'user', 'author', and 'created_at' read-only

    def validate(self, attrs):
        request = self.context.get('request')
        if request and request.user != attrs.get('user'):
            raise serializers.ValidationError("You do not have permission to view this blog.")
        return attrs