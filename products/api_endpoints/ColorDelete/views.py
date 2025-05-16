from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Color


class ColorDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            color = Color.objects.get(pk=pk)
        except Color.DoesNotExist:
            return Response({"error": "Color not found."}, status=status.HTTP_404_NOT_FOUND)

        color.delete()
        return Response({"message": "Color deleted successfully."}, status=status.HTTP_204_NO_CONTENT)