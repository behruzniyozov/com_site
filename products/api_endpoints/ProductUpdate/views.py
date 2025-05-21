from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from .serializers import ProductUpdateSerializer

class ProductUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        serializer = ProductUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
