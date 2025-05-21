from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Cart, CartItem
from .serializers import CartCreateSerializer

class CartCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CartCreateSerializer(data=request.data)
        if serializer.is_valid():
            cart = serializer.save()
            return Response(CartCreateSerializer(cart).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
