from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import Cart
from .serializers import CartDetailSerializer

class CartDetailView(RetrieveAPIView):
    permission_classes = []
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer
    lookup_field = 'id'