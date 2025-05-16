from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import ProductVariant


class ProductOptionDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            product_variant = ProductVariant.objects.get(pk=pk)
            product_variant.delete()
            return Response({"message": "Product variant deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except ProductVariant.DoesNotExist:
            return Response({"error": "Product variant not found"}, status=status.HTTP_404_NOT_FOUND)