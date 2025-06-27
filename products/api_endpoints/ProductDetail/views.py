from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from .serializers import ProductDetailSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = []
    lookup_field = 'slug'