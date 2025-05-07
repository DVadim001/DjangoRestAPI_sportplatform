from rest_framework import viewsets, permissions
from .models import Club
from .serializers import AdminClubSerializer

class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class ClubAdminViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = AdminClubSerializer
    permission_classes = [AdminOnly]
