from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from stories.models import Story

class StoryDeleteAPIView(DestroyAPIView):
    queryset = Story.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def perform_destroy(self, instance):
        # Custom logic before deleting the story, if needed
        instance.delete()