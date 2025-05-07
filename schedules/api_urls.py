from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_admin import ScheduleAdminViewSet

router = DefaultRouter()
router.register(r'admin/schedules', ScheduleAdminViewSet, basename='admin-schedules')

urlpatterns = [
    path('', include(router.urls)),
]
