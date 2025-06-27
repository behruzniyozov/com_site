from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from .serializers import ProductCreateSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

