# stories/serializers.py
from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'user', 'content', 'story', 'created_at', 'is_active']
        read_only_fields = ['id', 'user', 'created_at']
