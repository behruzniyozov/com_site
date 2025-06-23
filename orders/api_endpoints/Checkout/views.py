from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from orders.api_endpoints.Checkout.serializers import CheckoutSerializer


class CheckoutAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CheckoutSerializer

    def create(self,request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)