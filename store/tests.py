from django.test import TestCase
from .models import Customer, Cookie, Order, OrderItem

class ModelTests(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Test Customer", email="test@example.com")
        self.cookie = Cookie.objects.create(name="Chocolate Chip", price=2.99)
        self.order = Order.objects.create(customer=self.customer)
        self.order_item = OrderItem.objects.create(order=self.order, cookie=self.cookie, quantity=3)

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "Test Customer")

    def test_cookie_creation(self):
        self.assertEqual(self.cookie.name, "Chocolate Chip")

    def test_order_creation(self):
        self.assertEqual(self.order.customer.name, "Test Customer")

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.quantity, 3)
