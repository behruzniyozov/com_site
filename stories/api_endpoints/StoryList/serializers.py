from rest_framework import serializers
from stories.models import Story

class StoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'story', 'content', 'is_active']
        read_only_fields = ['id', 'is_active']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.user.username if instance.user else None
        return representation