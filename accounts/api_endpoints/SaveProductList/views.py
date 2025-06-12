from rest_framework.views import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from com_site.accounts.api_endpoints.SaveProductList.serializers import SaveProductListSerializer

from products.models import Product


class SaveProductListView(ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SaveProductListSerializer

    def get(self, request):
        saved_products = request.user.saved_products.all()
        serializer = self.get_serializer(saved_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)