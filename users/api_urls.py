from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api_admin import UserAdminViewSet

router = DefaultRouter()
router.register(r'admin/users', UserAdminViewSet, basename='admin-users')

urlpatterns = [
    path('', include(router.urls)),
]
