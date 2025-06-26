from rest_framework import serializers
from stories.models import Story


class StoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'story', 'content', 'created_at', 'is_active']
        read_only_fields = ['id', 'is_active', 'created_at']

    def create(self, validated_data):
        story = Story.objects.create(**validated_data)
        return story