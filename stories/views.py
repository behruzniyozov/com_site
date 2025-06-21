# stories/views.py
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .models import Story
from .serializers import StorySerializer

class StoryAPIView(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        story = serializer.save(user=self.request.user)
        from .tasks import delete_story_later
        delete_story_later.delay(story.id)
        
