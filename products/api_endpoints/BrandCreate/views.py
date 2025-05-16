from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import ProductVariant, Brand
from .serializers import BrandCreateSerializer

class BrandCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = BrandCreateSerializer(data=request.data)
        if serializer.is_valid():
            brand = serializer.save()
            return Response(BrandCreateSerializer(brand).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
