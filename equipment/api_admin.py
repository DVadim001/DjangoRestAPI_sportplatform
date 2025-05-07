from rest_framework import viewsets, permissions
from .models import Equipment
from .serializers import AdminEquipmentSerializer

class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class EquipmentAdminViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = AdminEquipmentSerializer
    permission_classes = [AdminOnly]
