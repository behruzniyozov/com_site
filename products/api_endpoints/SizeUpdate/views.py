from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Size
from .serializers import SizeUpdateSerializer


class SizeUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            size = Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            return Response({"error": "Size not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SizeUpdateSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Size updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
