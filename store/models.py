from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, default="000-000-0000")  # Default value added
    address = models.TextField(blank=True, null=True)  # Optional

    def __str__(self):
        return self.name

class Cookie(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Stores price in SEK (Swedish kronor)
    image = models.ImageField(upload_to='cookie_images/', blank=True, null=True)  # Optional image

    def __str__(self):
        return f"{self.name} - {self.price} SEK"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.cookie.name} in Order {self.order.id}"
