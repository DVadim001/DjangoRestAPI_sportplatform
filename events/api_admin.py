from rest_framework import viewsets, permissions
from .models import Event
from .serializers import AdminEventSerializer

class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class EventAdminViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = AdminEventSerializer
    permission_classes = [AdminOnly]
