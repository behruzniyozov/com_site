from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Size

class SizeDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            size = Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            return Response({"error": "Size not found."}, status=status.HTTP_404_NOT_FOUND)

        size.delete()
        return Response({"message": "Size deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
