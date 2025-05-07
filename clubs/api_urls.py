from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_admin import ClubAdminViewSet

router = DefaultRouter()
router.register(r'admin/clubs', ClubAdminViewSet, basename='admin-clubs')

urlpatterns = [
    path('', include(router.urls)),
]
