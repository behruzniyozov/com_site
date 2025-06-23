from rest_framework import serializers
from orders.choices import CheckoutSourceChoices
from orders.api_endpoints.Checkout.services import create_order

class CheckoutSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True),
    source=serializers.ChoiceField(choices=CheckoutSourceChoices.choices, required=True, write_only=True)
    product=serializers.IntegerField(required=False, write_only=True)
    quantity=serializers.IntegerField(required=False, write_only=True)

    def create(self, validated_data):
        create_order=create_order(**validated_data)
        if not create_order:
            raise serializers.ValidationError("Order creation failed")
        return create_order