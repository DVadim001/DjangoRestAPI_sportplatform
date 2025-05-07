from rest_framework import viewsets, permissions
from .models import Schedule
from .serializers import ScheduleSerializer

class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class ScheduleAdminViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [AdminOnly]
