from rest_framework import viewsets, permissions
from .models import Result
from .serializers import AdminResultSerializer

class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class ResultAdminViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = AdminResultSerializer
    permission_classes = [AdminOnly]
