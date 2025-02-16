from django.contrib import admin
from .models import Customer, Cookie, Order  # Import all models

# Register models so they appear in the Admin Panel
admin.site.register(Customer)
admin.site.register(Cookie)
admin.site.register(Order)
