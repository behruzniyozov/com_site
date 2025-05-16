from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Color
from .serializers import ColorCreateSerializer

class ColorCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ColorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)