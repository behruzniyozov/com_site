from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import ProductVariant
from .serializers import ProductOptionsListSerializer


class ProductOptionsListView(APIView):
    permission_classes = []

    def get(self, request):
        product= ProductVariant.objects.all()
        serializer = ProductOptionsListSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        