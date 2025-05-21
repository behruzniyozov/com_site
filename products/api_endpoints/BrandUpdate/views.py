from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import ProductVariant, Brand
from .serializers import BrandUpdateSerializer

class BrandUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            brand = Brand.objects.get(id=id)
        except Brand.DoesNotExist:
            return Response({"error": "Brand not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BrandUpdateSerializer(brand, data=request.data)
        if serializer.is_valid():
            brand = serializer.save()
            return Response(BrandUpdateSerializer(brand).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)