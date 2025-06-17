from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from accounts.api_endpoints.SaveProduct.serializers import SaveProductSerializer

from products.models import Product
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SaveProductView(APIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SaveProductSerializer

    @swagger_auto_schema(
        request_body=SaveProductSerializer,
    )
    def post(self, request):
        if request.data.get('id'):
            product= get_object_or_404(Product, id=request.data['id'])

            if product in request.user.saved_products.all():
                self.request.user.saved_products.remove(product)
            
            else:
                self.request.user.saved_products.add(product)

            return Response(
                {"message": "Product saved successfully."},
                status=status.HTTP_200_OK
            )
        return Response(
            {"error": "Product ID is required."},
            status=status.HTTP_400_BAD_REQUEST
        )