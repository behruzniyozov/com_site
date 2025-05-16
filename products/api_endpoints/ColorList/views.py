from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Color
from .serializers import ColorListSerializer

class ColorListView(APIView):
    permission_classes = []

    def get(self, request):
        colors = Color.objects.all()
        serializer = ColorListSerializer(colors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)