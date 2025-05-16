from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import ProductVariant, Brand

from .serializers import BrandListSerializer    

class BrandListView(APIView):
    permission_classes = []

    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandListSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)