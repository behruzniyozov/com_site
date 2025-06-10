from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from accounts.models import Cart
from accounts.api_endpoints.Profile.UserRegister.tokens import generate_user_register_token

from accounts.api_endpoints.Profile.UserRegister.serializers import (
    UserRegisterRequestSerializer,
    UserRegisterVerifySerializer,
)
from accounts.api_endpoints.Profile.UserRegister.email_send import send_user_register_email


class UserRegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=UserRegisterRequestSerializer,
        responses={201: openapi.Response("User registered successfully.")}
    )
    def post(self, request):
        serializer = UserRegisterRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Send token via email, not response
        token = generate_user_register_token(user)
        user.cart = Cart.objects.create(user=user) 
        user.save()  
        send_user_register_email(user.email, token)

        return Response({
            "detail": "User registered successfully. Please check your email to confirm your account."
        }, status=201)


class UserRegisterVerifyAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=UserRegisterVerifySerializer,
        responses={200: openapi.Response("User email confirmed successfully.")}
    )
    def post(self, request):
        serializer = UserRegisterVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "detail": "User email confirmed successfully."
        }, status=200)
