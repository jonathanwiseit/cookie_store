from rest_framework import serializers
from .models import Customer, Cookie, Order, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone_number', 'address']

class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie
        fields = ['id', 'name', 'price', 'image']

class OrderItemSerializer(serializers.ModelSerializer):
    cookie = CookieSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'cookie', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'created_at', 'items']
