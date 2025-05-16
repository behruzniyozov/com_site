from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import ProductVariant
from .serializers import ProductOptionUpdateSerializer


class ProductOptionUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            product_variant = ProductVariant.objects.get(pk=pk)
            serializer = ProductOptionUpdateSerializer(product_variant, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ProductVariant.DoesNotExist:
            return Response({"error": "Product variant not found"}, status=status.HTTP_404_NOT_FOUND)