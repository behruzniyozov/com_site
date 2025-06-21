from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogDetailSerializer
from blog.models import Blog

class BlogDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogDetailSerializer
    queryset = Blog.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            blog = self.get_object()
            serializer = self.get_serializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({"detail": "Blog not found."}, status=status.HTTP_404_NOT_FOUND)