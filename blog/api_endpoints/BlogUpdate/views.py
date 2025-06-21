from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogUpdateSerializer
from blog.models import Blog

class BlogUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk, user=request.user)
        except Blog.DoesNotExist:
            return Response({"detail": "Blog not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogUpdateSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)