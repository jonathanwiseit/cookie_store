from django.contrib import admin  # ✅ Add this line
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views import CustomerViewSet, CookieViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'cookies', CookieViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Fix: Now admin is imported
    path('', include(router.urls)),   # Use REST API router
]
