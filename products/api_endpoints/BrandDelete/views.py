from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import ProductVariant, Brand


class BrandDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            brand = Brand.objects.get(pk=pk)
            brand.delete()
            return Response({"message": "Brand deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Brand.DoesNotExist:
            return Response({"error": "Brand not found"}, status=status.HTTP_404_NOT_FOUND)