from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from products.models import Brand
from .serializers import BrandDetailSerializer
from rest_framework.response import Response


class BrandDetailView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer
    permission_classes = []
    lookup_field = 'id'
    
    