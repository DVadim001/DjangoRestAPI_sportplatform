from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_admin import EventAdminViewSet

router = DefaultRouter()
router.register(r'admin/events', EventAdminViewSet, basename='admin-events')

urlpatterns = [
    path('', include(router.urls)),
]
