from django.contrib import admin
from django.urls import path
from store.views import customer_list, cookie_list, order_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer_list/', customer_list, name='customer_list'),
    path('cookie_list/', cookie_list, name='cookie_list'),
    path('order_list/', order_list, name='order_list'),
]
