from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Color
from .serializers import ColorUpdateSerializer


class ColorUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            color = Color.objects.get(pk=pk)
        except Color.DoesNotExist:
            return Response({"error": "Color not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ColorUpdateSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)