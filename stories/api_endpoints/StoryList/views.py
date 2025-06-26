from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from stories.models import Story
from .serializers import StoryListSerializer
from rest_framework.response import Response

class StoryListAPIView(APIView):
    queryset = Story.objects.all()
    serializer_class = StoryListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)