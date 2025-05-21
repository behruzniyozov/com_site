from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import Cart, CartItem
from .serializers import CartItemDetailSerializer

class CartItemDetailView(RetrieveAPIView):
    permission_classes = []
    queryset = CartItem.objects.all()
    serializer_class = CartItemDetailSerializer
    lookup_field = 'id'