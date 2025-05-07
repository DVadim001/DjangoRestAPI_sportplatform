from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_admin import EquipmentAdminViewSet

router = DefaultRouter()
router.register(r'admin/equipment', EquipmentAdminViewSet, basename='admin-equipment')

urlpatterns = [
    path('', include(router.urls)),
]
