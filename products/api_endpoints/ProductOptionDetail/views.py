from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import ProductVariant
from .serializers import ProductOptionDetailSerializer


class ProductOptionDetailView(APIView):
    permission_classes = []

    def get(self, request, pk):
        try:
            product_variant = ProductVariant.objects.get(pk=pk)
            serializer = ProductOptionDetailSerializer(product_variant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProductVariant.DoesNotExist:
            return Response({"error": "Product variant not found"}, status=status.HTTP_404_NOT_FOUND)