from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_admin import ResultAdminViewSet

router = DefaultRouter()
router.register(r'admin/results', ResultAdminViewSet, basename='admin-results')

urlpatterns = [
    path('', include(router.urls)),
]
