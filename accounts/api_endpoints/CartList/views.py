from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from accounts.models import Cart, CartItem
from .serializers import CartListSerializer

class CartListView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=request.user)
            serializer = CartListSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)