# serializers.py

from rest_framework import serializers
from accounts.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CartCreateSerializer(serializers.ModelSerializer):
    product = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']



