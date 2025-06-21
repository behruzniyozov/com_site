# stories/views.py
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .models import Story
from .serializers import StorySerializer
from .tasks import deactivate_story_later

class StoryAPIView(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        story = serializer.save(user=self.request.user)
        deactivate_story_later.apply_async(args=[story.id], countdown=60 * 60 * 24)
        
        
