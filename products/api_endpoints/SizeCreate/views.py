from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Size
from .serializers import SizeCreateSerializer

class SizeCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SizeCreateSerializer(data=request.data)
        if serializer.is_valid():
            size = serializer.save()
            return Response({"message": "Size created successfully.", "size_id": size.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)