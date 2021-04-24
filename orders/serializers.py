from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'products', 'quantity', 'amount', 'seller', 'buyer', 'payment_method', 'delivery_location', 'status', 'timestamp']
        read_only_fields = ['id', 'order_number']
