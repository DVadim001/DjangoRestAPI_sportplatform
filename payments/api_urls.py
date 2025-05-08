from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, ServiceTypeViewSet

router = DefaultRouter()
router.register(r'admin/payments', PaymentViewSet, basename='admin-payments')
router.register(r'admin/services', ServiceTypeViewSet, basename='admin-services')  # исправлено имя

urlpatterns = [
    path('', include(router.urls)),
]
