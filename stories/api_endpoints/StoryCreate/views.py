from rest_framework.views import APIView
from rest_framework import permissions, parsers
from stories.models import Story
from .serializers import StoryCreateSerializer
from rest_framework.response import Response

class StoryCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.JSONParser]

    def post(self, request, *args, **kwargs):
        serializer = StoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            story = serializer.save(user=request.user)
            return Response(StoryCreateSerializer(story).data, status=201)
        return Response(serializer.errors, status=400)