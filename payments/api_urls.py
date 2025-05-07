from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_admin import PaymentAdminViewSet

router = DefaultRouter()
router.register(r'admin/payments', PaymentAdminViewSet, basename='admin-payments')

urlpatterns = [
    path('', include(router.urls)),
]
