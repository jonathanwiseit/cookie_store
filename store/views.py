from rest_framework import viewsets
from .models import Customer, Cookie, Order
from .serializers import CustomerSerializer, CookieSerializer, OrderSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CookieViewSet(viewsets.ModelViewSet):
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
